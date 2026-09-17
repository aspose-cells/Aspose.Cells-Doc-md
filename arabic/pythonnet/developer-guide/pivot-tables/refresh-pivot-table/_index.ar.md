---
title: تحديث الجداول المحورية وذاكرة التخزين المؤقتة في Aspose.Cells for Python via .NET
linktitle: تحديث الجداول المحورية وذاكرة التخزين المؤقتة في Aspose.Cells for Python via .NET
description: تعرف على كيفية تحديث الجداول المحورية في Aspose.Cells for Python via .NET باستخدام واجهة برمجة التطبيقات للتحديث v26.7+. تتناول هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية.
keywords: Aspose.Cells, Python via .NET, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells واجهة برمجة تطبيقات تحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري في أربعة نطاقات مختلفة — من المصنف بأكمله إلى جدول محوري واحد. بدءًا من Aspose.Cells for Python via .NET v26.7، تم وضع علامة على الطريقة القديمة `PivotTable.refresh_data()` باعتبارها قديمة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمبنية على ذاكرة التخزين المؤقت الموضحة في هذه المقالة.
{{% /alert %}}

## مقدمة
نادرًا ما تكون عملية تحديث الجدول المحوري عملية واحدة. في الخلفية، تحتفظ Aspose.Cells بسلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو مفتاح اختيار واجهة برمجة التطبيقات الصحيحة للتحديث في أي موقف.
سلسلة البيانات المكونة من أربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الأولية.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. كل جدول محوري مبني فوق `PivotCache`؛ هذا هو المكان الذي يتم فيه جمع وتجميع جميع البيانات.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والفلاتر. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرةً من مصدر البيانات.
4. **Cells** — `Cells` الخاصة بورقة العمل التي يقوم `PivotTable` بعرض القيم والأنماط المحسوبة فيها.

{{% alert color="primary" %}}
`PivotCache.source_type` (التعداد `PivotTableSourceType`) يوضح من أين جاءت بيانات ذاكرة التخزين المؤقت. اعتبارًا من v26.7، يدعم `PivotCache.refresh()` فقط أنواع المصادر **`Sheet`** و**`Consolidation`** — أي البيانات الموجودة في نطاقات ورقة العمل. المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) ليست قابلة للتحديث بعد من خلال واجهة برمجة تطبيقات ذاكرة التخزين المؤقت.
{{% /alert %}}

بسبب هذه السلسلة، يوجد مسارا تحديث أساسيان في Aspose.Cells:
- **`PivotTable.calculate_data()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون الرجوع إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر خلايا ورقة العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.

## بداية سريعة
إذا كنت تحتاج فقط إلى أقصر كود ممكن يحدّث كل محور في المصنف، فإن استدعاءً واحدًا كافٍ:

```python
import aspose.cells as ac
# إنشاء مصنف جديد
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# كتابة صف الرأس في الخلايا A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفواكه عبر عامي 2020 و2021)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)
worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)
worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)
worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)
worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)
worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)
worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)
worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)
# إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# تعيين حقول الجدول المحوري: Fruit إلى الصفوف، Year إلى الأعمدة، Amount إلى البيانات
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# تعديل عدة قيم Amount في بيانات المصدر لمحاكاة التغييرات
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)
# تحديث كل جدول محوري / ذاكرة تخزين مؤقت للجدول المحوري في المصنف
workbook.refresh_all()
# حفظ المصنف
workbook.save("output.xlsx")
```

كل شيء آخر في هذه المقالة يشرح متى تختار واجهة برمجة تطبيقات أضيق بدلاً من ذلك.

## الاستيرادات المطلوبة
تبدأ جميع أمثلة Python في هذه المقالة بعبارات الاستيراد الثلاث التالية لأن أنواع الجداول المحورية موجودة في namespace `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقتة للجدول المحوري وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.refresh_all()`. يتنقل استدعاء واحد عبر المصنف بأكمله — يحدّث كل `PivotCache` من مصدره ثم يعيد حساب كل `PivotTable` تابع. هذا هو الأسلوب الموصى به لتحديثات المستند الكاملة العامة حيث لا تشكل الأداء مصدر قلق.
يبني المثال التالي مصنفًا بنطاق مصدر فاكهة/سنة/مبلغ، وينشئ جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `refresh_all()` لجلب كل شيء حتى تاريخه في استدعاء واحد.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)
worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)
worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)
worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)
worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)
worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)
worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية التي تعيش في ورقة عمل محددة واحدة — على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى معروفة بأنها غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، توفر Aspose.Cells `Worksheet.refresh_pivot_tables()`، والتي تكون محصورة في نسخة `Worksheet` واحدة.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# كتابة صف العناوين Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# كتابة 8 صفوف بيانات (الصفوف 2-9، المناسبة لنطاق المصدر A1:C9)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)
# إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، يستمد بياناته من A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# تعيين الحقول: Fruit إلى Row، Year إلى Column، Amount إلى Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# تعديل خاصية عرض/تخطيط — هذا تغيير على العرض فقط،
# لذلك لا يتطلب إعادة قراءة بيانات المصدر من خلال PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False
# CalculateData() يعيد عرض هذا الجدول المحوري (البيانات + النمط) من
# البيانات الموجودة بالفعل في PivotCache. نظرًا لعدم تغير بيانات المصدر،
# لن يتم تنفيذ أي رحلة ذهاب وإياب إلى المصدر — سيتم فقط إعادة حساب
# القيم المخزنة مؤقتًا في خلايا ورقة العمل.
pivot_table.calculate_data()
# حفظ المصنف على القرص
workbook.save("output.xlsx")
```

## تحديث جدول محوري واحد
عندما تريد تحكمًا دقيقًا في جدول محوري واحد، توفر لك واجهة برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو مجرد إعدادات العرض/التخطيط للجدول المحوري نفسه.

### تغيرت بيانات المصدر — استخدم `PivotCache.refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivot_table.pivot_cache.refresh()`. يعيد هذا الاستدعاء قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم يعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت تلك.

### تغير العرض/التخطيط فقط — استخدم `calculate_data()`
إذا لم تتغير بيانات المصدر *ولكن* تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة؛ فقط `PivotTable` المعروض يحتاج إلى إعادة حساب. في هذه الحالة، `pivot_table.calculate_data()` هو الخيار الصحيح.
يعدل المثال التالي خاصية غير مصدر للجدول المحوري ثم يستدعي `calculate_data()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.
غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس جميعها فوق ذاكرة تخزين مؤقتة مشتركة واحدة. لتعدادها — على سبيل المثال، قبل تنفيذ تحديث دفعة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.get_pivot_tables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.

## الترحيل من `PivotTable.refresh_data()` القديمة
قبل Aspose.Cells for Python via .NET v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.refresh_data()` على كل جدول محوري على حدة. اعتبارًا من v26.7، تم وضع علامة على هذه الطريقة باعتبارها **قديمة** ويجب استبدالها بواجهات برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان لكون نهج `refresh_data()` لكل جدول يمثل مشكلة في المصنفات في العالم الحقيقي:
- يعيد جلب البيانات من المصدر *في كل* مرة يتم استدعاؤها، حتى عندما لم يتغير المصدر.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الجديد الفعّال للمصنفات ذات الجداول المحورية المتعددة التي تتشارك ذاكرة تخزين مؤقتة واحدة.

## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل منها.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refresh_all()` | استدعاء واحد؛ يغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية فقط في ورقة واحدة | `Worksheet.refresh_pivot_tables()` | محصور في ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقتة واحدة | `pivot_table.pivot_cache.refresh()` | يحدّث جميع الجداول المحورية في ذاكرة التخزين المؤقت المشتركة تلك. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivot_table.calculate_data()` | يتخطى رحلة العودة غير الضرورية إلى المصدر. |
| سرد جميع الجداول المحورية في ذاكرة تخزين مؤقتة مشتركة | `pivot_cache.get_pivot_tables()` | استخدم للتعداد قبل التحديث المجمع. |
عمليًا، فضّل واجهات برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت على `refresh_data()` القديمة لكل جدول. إنها على دراية بذاكرات التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر المكررة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث الخاصة بك.

## الأخطاء الشائعة
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة البيانات الخاصة به. إذا قمت بتعديل خلايا المصدر، فاستدعِ `PivotCache.Refresh()` (أو `Workbook.RefreshAll()`) قبل `Workbook.save()`، وإلا فإن الملف المحفوظ لا يزال يحتوي على القيم المجمعة القديمة.
- **استدعاء `RefreshData()` القديمة لكل جدول.** في v26.7، تم وضع علامة على `PivotTable.RefreshData()` باعتبارها قديمة وتعيد جلب المصدر لكل استدعاء. مع وجود جداول محورية متعددة تتشارك ذاكرة تخزين مؤقتة، فهذا يعني N عملية جلب مصدر مكررة. استبدل بـ `PivotCache.Refresh()` واحدة متبوعة بـ `CalculateData()` لكل جدول.
- **التحديث عند تغير التخطيط فقط.** إذا قمت فقط بتغيير عرض الجدول المحوري (ترتيب الأعمدة، `ConsolidationFunction`، إلخ) دون لمس بيانات المصدر، فإن `PivotCache.Refresh()` غير ضروري وبطيء. استدعِ `pivotTable.CalculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة.
- **المصدر الخارجي غير مدعوم من `PivotCache.Refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، إلخ)، فلا يمكن لـ `PivotCache.Refresh()` تحديثه في v26.7 — فهو يدعم حاليًا فقط أنواع المصادر `Sheet` و`Consolidation`. بالنسبة للمصادر الخارجية، أعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python-net" >}}