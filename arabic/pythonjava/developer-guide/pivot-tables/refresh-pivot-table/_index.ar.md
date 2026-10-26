---
title: تحديث الجداول المحورية وذاكرات التخزين المؤقت في Aspose.Cells for Python via Java
linktitle: تحديث الجداول المحورية وذاكرات التخزين المؤقت في Aspose.Cells for Python via Java
description: تعلم كيفية تحديث الجداول المحورية في Aspose.Cells for Python via Java باستخدام واجهة برمجة التطبيقات لتحديث المحاور في الإصدار v26.7+. تتناول هذه المقالة واجهات refreshAll و refreshPivotTables و PivotCache.refresh و calculateData و getPivotTables مع أمثلة عملية على الكود.
keywords: Aspose.Cells, Python via Java, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة برمجة تطبيقات تحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات المحاور بأربعة نطاقات مختلفة — من المصنف بأكمله إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Python via Java v26.7**، تم وضع علامة على الطريقة التقليدية `PivotTable.refreshData()` باعتبارها قديمة ويجب استبدالها بواجهات البرمجة الأكثر كفاءة والمراعية لذاكرة التخزين المؤقت الموضحة في هذه المقالة.
{{% /alert %}}

## Introduction
نادرًا ما يكون تحديث جدول محوري عملية واحدة. وراء الكواليس، يحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو مفتاح اختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.
سلسلة البيانات المكونة من أربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. كل جدول محوري مبني فوق `PivotCache`؛ حيث يتم جمع جميع البيانات وتجميعها.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرةً من مصدر البيانات.
4. **الخلايا (Cells)** — `Cells` ورقة العمل التي يقوم `PivotTable` بعرض القيم والأنماط المحسوبة فيها.

{{% alert color="primary" %}}
يشير `PivotCache.getSourceType()` (التعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، يدعم `PivotCache.refresh()` أنواع المصادر **`SHEET`** و **`CONSOLIDATION`** فقط — أي البيانات التي تعيش في نطاقات أوراق العمل. المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) لا يمكن تحديثها بعد من خلال واجهة برمجة التطبيقات لذاكرة التخزين المؤقت.
بسبب هذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.calculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون رحلة ذهاب وإياب إلى مصدر البيانات.
جميع السيناريوهات في هذه المقالة تستخدم بيانات مصدر خلايا ورقة العمل، لذا فإن نوع المصدر هو `SHEET` وتعمل عمليات التحديث كما هو موضح.
{{% /alert %}}

## Quick Start
إذا كنت تحتاج فقط إلى أقصر كود ممكن لتحديث كل محور في المصنف، فإن استدعاءً واحدًا كافٍ:

```python
import jpype
from asposecells.api import Workbook

workbook = Workbook("input.xlsx")
workbook.refreshAll()
workbook.save("output.xlsx")
```

كل شيء آخر في هذه المقالة يشرح متى تختار واجهة برمجة تطبيقات أضيق بدلاً من ذلك.

## Required Imports
تعتمد جميع أمثلة Python في هذه المقالة على الواردات التالية لأن أنواع المحاور تعيش في مساحة الاسم `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
تُستخدم وحدة `jpype` لتشغيل JVM، بينما تكشف `aspose.cells` عن أنواع المصنف/ورقة العمل/الخلية/المحور المستخدمة في جميع الأمثلة.

## Refresh All Pivot Tables in the Workbook
عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت للمحاور وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط واجهة برمجة تطبيقات وأكثرها شمولاً هي `Workbook.refreshAll()`. استدعاء واحد يجتاز المصنف بأكمله — يحدّث كل `PivotCache` من مصدره ثم يعيد حساب كل `PivotTable` تابع. هذا هو الأسلوب الموصى به للتحديثات العامة للمستند بالكامل حيث لا يكون الأداء موضع قلق.
يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويُعدّل بعض قيم المصدر، ثم يستخدم `refreshAll()` لجلب كل شيء حتى تاريخه باستدعاء واحد.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# Add a pivot table: source range "A1:C9", destination cell "E3"
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll()
# Save the workbook
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh All Pivot Tables on a Single Worksheet
في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية التي تعيش في ورقة عمل واحدة محددة — على سبيل المثال، عندما يكون من المعروف أن الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.refreshPivotTables()`، الذي يتم تحديد نطاقه لمثيل `Worksheet` واحد.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh a Single Pivot Table
عندما تريد تحكمًا دقيقًا في جدول محوري واحد، تمنحك واجهة البرمجة المستندة إلى ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه.

### Source Data Changed — Use `PivotCache.refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.getPivotCache().refresh()`. يعيد هذا الاستدعاء قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم يعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة المؤقتة.

### Only View/Layout Changed — Use `calculateData()`
إذا لم تتغير بيانات المصدر ولكن تم تعديل إعدادات عرض أو تخطيط الجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للذهاب والإياب إلى مصدر البيانات. تحتفظ ذاكرة التخزين المؤقت بالفعل بالبيانات الصحيحة؛ فقط `PivotTable` المعروض يحتاج إلى إعادة حساب. في هذه الحالة، `pivotTable.calculateData()` هو الاختيار الصحيح.
يعدّل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# Add a pivot table placed at destination cell E3, sourcing from A1:C9
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivotTable.calculateData()
# Save the workbook to disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس جميعها فوق ذاكرة تخزين مؤقت واحدة مشتركة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.getPivotTables()`. ترجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المحددة.

## Migrating from the Obsolete `PivotTable.refreshData()`
قبل Aspose.Cells for Python via Java v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.refreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة باعتبارها **قديمة** ويجب استبدالها بواجهات البرمجة المراعية لذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان يجعل نهج `refreshData()` لكل جدول مشكلة في المصنفات الواقعية:
- يقوم بإعادة جلب البيانات من المصدر *في كل مرة* يتم استدعاؤه فيها، حتى عندما لا يتغير المصدر.
البدائل الموصى بها:
يوضح المثال التالي النمط الجديد والفعال للمصنفات ذات الجداول المحورية المتعددة التي تشترك في ذاكرة تخزين مؤقت واحدة.

## Which Refresh API Should I Use?
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة.
| الهدف | واجهة البرمجة الموصى بها | ملاحظات |
|------|--------------------------|---------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | استدعاء واحد؛ يغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية فقط على ورقة واحدة | `Worksheet.refreshPivotTables()` | محدد النطاق بورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.getPivotCache().refresh()` | يحدّث جميع الجداول المحورية على تلك الذاكرة المؤقتة المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.calculateData()` | يتخطى رحلة المصدر غير الضرورية. |
| يسرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | يُستخدم للتعداد قبل التحديث المجمّع. |
عمليًا، فضّل واجهات البرمجة المستندة إلى ذاكرة التخزين المؤقت على `refreshData()` القديمة لكل جدول. إنها على دراية بذاكرة التخزين المؤقت المشتركة، وتتجنب جلب المصدر بشكل مكرر، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث.

## Common Pitfalls
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة البيانات الخاصة به. إذا قمت بتعديل خلايا المصدر، فاستدعِ `PivotCache.refresh()` (أو `Workbook.refreshAll()`) قبل `Workbook.save()`، وإلا فإن الملف المحفوظ سيظل يحتوي على القيم المجمّعة القديمة.
- **استدعاء `RefreshData()` القديمة لكل جدول.** في الإصدار v26.7، تم وضع علامة `PivotTable.RefreshData()` على أنها قديمة وتعيد جلب المصدر لكل استدعاء. مع جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت يعني هذا وجود عدد N من جلبات المصدر المكررة. استبدل بـ `PivotCache.refresh()` واحد متبوعًا بـ `calculateData()` لكل جدول.
- **التحديث عندما يتغير التخطيط فقط.** إذا قمت فقط بتغيير عرض الجدول المحوري (ترتيب الأعمدة، `ConsolidationFunction`، إلخ) دون لمس بيانات المصدر، فإن `PivotCache.refresh()` غير ضروري وبطيء. استدعِ `pivotTable.calculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة.
- **المصدر الخارجي غير مدعوم من قبل `PivotCache.refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، إلخ)، فإن `PivotCache.refresh()` لا يمكنه تحديثه في الإصدار v26.7 — فهو يدعم حاليًا أنواع مصادر `Sheet` و `Consolidation` فقط. بالنسبة للمصادر الخارجية، أعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="python" >}}