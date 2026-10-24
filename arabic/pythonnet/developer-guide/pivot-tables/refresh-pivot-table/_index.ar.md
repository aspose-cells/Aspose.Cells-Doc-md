---
title: تحديث الجداول المحورية وذواكر التخزين المؤقت في Aspose.Cells for Python via .NET
linktitle: تحديث الجداول المحورية وذواكر التخزين المؤقت في Aspose.Cells for Python via .NET
description: تعرف على كيفية تحديث الجداول المحورية في Aspose.Cells for Python via .NET باستخدام واجهة API للتحديث المسماة pivot-refresh في الإصدار v26.7+. تغطي هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة برمجية عملية.
keywords: Aspose.Cells, Python via .NET, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة API للتحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجداول المحورية عبر أربعة نطاقات مختلفة — من المصنف بالكامل وصولًا إلى جدول محوري واحد. اعتبارًا من **Aspose.Cells for Python via .NET v26.7**، أصبحت الطريقة القديمة `PivotTable.refresh_data()` مهجورة، وينبغي استبدالها بواجهات API أكثر كفاءة تعتمد على ذاكرة التخزين المؤقت، كما هو موضح في هذه المقالة.
{{% /alert %}}

## Introduction
لا يقتصر تحديث الجدول المحوري عادةً على عملية واحدة. في الخلفية، يحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة في ورقة العمل. ويُعد فهم هذه السلسلة مفتاح اختيار واجهة API المناسبة للتحديث في كل حالة.
سلسلة البيانات ذات الطبقات الأربع هي:
1. **مصدر البيانات** — نطاقات أوراق العمل المصدرية أو استعلام قاعدة البيانات أو نطاق التوحيد الذي توجد فيه القيم الخام.
2. **`PivotCache`** — لقطة في الذاكرة لبيانات المصدر. تُبنى جميع الجداول المحورية على `PivotCache`، حيث تُجمع البيانات وتُجمَّع.
3. **`PivotTable`** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم وعوامل التصفية. ويقرأ `PivotTable` من `PivotCache` *فقط*، ولا يقرأ من مصدر البيانات مباشرةً.
4. **`Cells`** — مجموعة `Cells` الخاصة بورقة العمل، والتي يُدرج فيها `PivotTable` قيمه المحسوبة وأنماطه.

{{% alert color="primary" %}}
يوضح `PivotCache.source_type` (التعداد `PivotTableSourceType`) مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من v26.7، لا يدعم `PivotCache.refresh()` سوى نوعَي المصدر **`Sheet`** و**`Consolidation`** — أي البيانات الموجودة في نطاقات أوراق العمل. أما المصادر الخارجية (قواعد البيانات والاتصالات الخارجية وما شابهها)، فليست قابلة للتحديث حتى الآن عبر واجهة API الخاصة بذاكرة التخزين المؤقت.
ونتيجةً لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.calculate_data()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، من دون انتقال ذهابًا وإيابًا إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات خلايا ورقة العمل كمصدر، لذا يكون نوع المصدر `Sheet` وتتخذ عمليات التحديث السلوك الموضح.
{{% /alert %}}

## Quick Start
إذا كنت تحتاج فقط إلى أقصر شيفرة ممكنة لتحديث جميع الجداول المحورية في المصنف، فتكفي استدعاءً واحدًا:

```python
import aspose.cells as ac

workbook = ac.Workbook("input.xlsx")
workbook.refresh_all()
workbook.save("output.xlsx")
```

يوضح الجزء المتبقي من هذه المقالة متى ينبغي اختيار واجهة API ذات نطاق أضيق.

## Required Imports
تبدأ جميع أمثلة Python في هذه المقالة بعبارات الاستيراد الثلاث التالية، لأن أنواع الجداول المحورية موجودة في namespace `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Refresh All Pivot Tables in the Workbook
عند الحاجة إلى ضمان أن تعكس جميع ذواكر التخزين المؤقت وجميع الجداول المحورية في المصنف أحدث بيانات المصدر، تُعد `Workbook.refresh_all()` أبسط واجهة API وأكثرها شمولًا. يمر الاستدعاء الواحد على المصنف بأكمله، فيحدّث كل `PivotCache` من مصدره ثم يعيد حساب كل `PivotTable` يعتمد عليه. وهذا هو النهج الموصى به لتحديث المستند بالكامل في مهام التحديث العامة، عندما لا يكون الأداء مصدر قلق.
ينشئ المثال التالي مصنفًا يتضمن نطاق مصدر Fruit/Year/Amount، ويضيف جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `refresh_all()` لتحديث كل شيء باستدعاء واحد.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write header row into cells A1:C1
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(50)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(60)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(70)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(80)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(90)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(100)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(110)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(120)
# Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.cells.get("C2").put_value(55)
worksheet.cells.get("C5").put_value(85)
worksheet.cells.get("C9").put_value(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refresh_all()
# Save the workbook
workbook.save("output.xlsx")
```

## Refresh All Pivot Tables on a Single Worksheet
أحيانًا، لا يلزم سوى تحديث الجداول المحورية الموجودة في ورقة عمل محددة — على سبيل المثال، عندما يكون من المعروف أن الجداول المحورية في أوراق العمل الأخرى غير مرتبطة ولا ينبغي المساس بها. في هذه الحالة، توفر Aspose.Cells `Worksheet.refresh_pivot_tables()`، وهي مقصورة على مثيل واحد من `Worksheet`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2021)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2021)
worksheet.cells.get("C5").put_value(120)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(180)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2020)
worksheet.cells.get("C7").put_value(130)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(220)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2020)
worksheet.cells.get("C9").put_value(140)
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
worksheet.cells.get("C2").put_value(300)
worksheet.cells.get("C5").put_value(250)
worksheet.cells.get("C9").put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Refresh a Single Pivot Table
عند الحاجة إلى التحكم الدقيق في جدول محوري واحد، تتيح واجهة API المعتمدة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغيّر فعليًا: بيانات المصدر الأساسية، أم إعدادات العرض أو التخطيط للجدول المحوري نفسه فقط.

### Source Data Changed — Use `PivotCache.refresh()`
إذا كانت بيانات المصدر الأساسية قد تغيرت، تكون نقطة الدخول الصحيحة هي `pivot_table.pivot_cache.refresh()`. يعيد هذا الاستدعاء قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت، ثم يعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة.

### Only View/Layout Changed — Use `calculate_data()`
إذا لم تتغير بيانات المصدر، بل تغيّرت إعدادات عرض الجدول المحوري أو تخطيطه فقط (على سبيل المثال، نقل حقل إلى منطقة أخرى أو تبديل إعداد التحديث عند الفتح)، فلا حاجة إلى الانتقال ذهابًا وإيابًا إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة، ولا يلزم سوى إعادة حساب `PivotTable` المعروض. في هذه الحالة، يكون `pivot_table.calculate_data()` هو الخيار المناسب.
يعدل المثال التالي خاصية غير مرتبطة بالمصدر في الجدول المحوري، ثم يستدعي `calculate_data()` لإعادة عرضه من ذاكرة التخزين المؤقت الحالية.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write Fruit / Year / Amount header row
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(150)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(250)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(350)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(450)
# Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivot_table.refresh_data_on_opening_file = False
# calculate_data() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivot_table.calculate_data()
# Save the workbook to disk
workbook.save("output.xlsx")
```

يحتوي المصنف عادةً على عدة جداول محورية تستند جميعها إلى ذاكرة تخزين مؤقتة مشتركة. لتعدادها — على سبيل المثال، قبل تنفيذ تحديث جماعي أو لتشخيص أثر ذاكرة التخزين المؤقتة المشتركة — استخدم `PivotCache.get_pivot_tables()`. تعيد هذه الطريقة مجموعة تضم جميع `PivotTable` التي تعتمد على ذاكرة التخزين المؤقت المحددة.

## Migrating from the Obsolete `PivotTable.refresh_data()`
قبل إصدار Aspose.Cells for Python via .NET v26.7، كانت الطريقة المعيارية لتحديث الجدول المحوري هي استدعاء `PivotTable.refresh_data()` لكل جدول محوري على حدة. اعتبارًا من v26.7، أصبحت هذه الطريقة **مهجورة**، وينبغي استبدالها بواجهات API المعتمدة على ذاكرة التخزين المؤقت والموضحة أعلاه.
هناك سببان يجعلان أسلوب `refresh_data()` لكل جدول مشكلة في مصنفات العالم الحقيقي:
- يعيد جلب البيانات من المصدر *في كل مرة* يتم فيها استدعاؤه، حتى عندما لا تكون بيانات المصدر قد تغيرت.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الجديد الفعال في المصنفات التي تحتوي على عدة جداول محورية تتشارك ذاكرة تخزين مؤقتة واحدة.

## Which Refresh API Should I Use?
يلخص الجدول التالي واجهات API المتاحة للتحديث ومتى تختار كل منها.
| الهدف | واجهة API الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refresh_all()` | استدعاء واحد؛ يغطي جميع ذواكر التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة عمل واحدة فقط | `Worksheet.refresh_pivot_tables()` | محدودة بنطاق ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقتة واحدة | `pivot_table.pivot_cache.refresh()` | يحدّث جميع الجداول المحورية التي تشترك في ذاكرة التخزين المؤقت. |
| تغيرت إعدادات العرض أو التخطيط فقط | `pivot_table.calculate_data()` | تتخطى رحلة غير ضرورية إلى المصدر. |
| حصر جميع الجداول المحورية في ذاكرة تخزين مؤقتة مشتركة | `pivot_cache.get_pivot_tables()` | استخدمه لحصر الجداول قبل التحديث الجماعي. |
في التطبيق العملي، تفضّل واجهات API المعتمدة على ذاكرة التخزين المؤقت على أسلوب `refresh_data()` القديم لكل جدول. فهي تراعي ذواكر التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر المتكررة، وتتيح لك اختيار أصغر نطاق يحقق متطلب التحديث.

## Common Pitfalls
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة بياناته. إذا عدلت خلايا المصدر، استدعِ `PivotCache.refresh()` (أو `Workbook.refresh_all()`) قبل `Workbook.save()`، وإلا فسيظل الملف المحفوظ يحتوي على القيم المجمَّعة القديمة.
- **استدعاء `refresh_data()` القديم لكل جدول.** في v26.7، وضعت علامة «مهجور» على `PivotTable.refresh_data()`، وهو يعيد جلب المصدر في كل استدعاء. وعند وجود عدة جداول محورية تتشارك ذاكرة تخزين مؤقتة، يعني ذلك N عمليات جلب مكررة من المصدر. استبدل ذلك باستدعاء `PivotCache.refresh()` واحد يليه `calculate_data()` لكل جدول.
- **التحديث عندما يكون التخطيط فقط قد تغير.** إذا غيّرت طريقة عرض الجدول المحوري فقط (ترتيب الأعمدة، `ConsolidationFunction`، إلخ) دون المساس ببيانات المصدر، فلا حاجة إلى استدعاء `PivotCache.refresh()` لأنه غير ضروري وبطيء. استدعِ `pivotTable.calculate_data()` لإعادة العرض من ذاكرة التخزين المؤقت الحالية.
- **مصدر خارجي غير مدعوم من `PivotCache.refresh()`.** إذا كان الجدول المحوري يستخدم مصدرًا خارجيًا متصلًا (قاعدة بيانات، مكعب OLAP، إلخ)، فلا يمكن لـ `PivotCache.refresh()` تحديثه في v26.7 — فهو يدعم حاليًا نوعَي المصدر `Sheet` و`Consolidation` فقط. أما المصادر الخارجية، فأعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="python-net" >}}