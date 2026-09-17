---
title: تحديث الجداول المحورية وذاكرة التخزين المؤقت في Aspose.Cells for .NET
linktitle: تحديث الجداول المحورية وذاكرة التخزين المؤقت في Aspose.Cells for .NET
description: تعرّف على كيفية تحديث الجداول المحورية في Aspose.Cells for .NET باستخدام واجهة برمجة التطبيقات للتحديث في الإصدار v26.7+. تتناول هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة برمجة تطبيقات للتحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري بأربعة نطاقات مختلفة، بدءًا من المصنف بالكامل وحتى جدول محوري واحد. بدءًا من **Aspose.Cells for .NET v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` على أنها قديمة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمدركة لذاكرة التخزين المؤقت الموضحة في هذه المقالة.
{{% /alert %}}

## مقدمة
نادرًا ما تكون عملية تحديث الجدول المحوري عملية واحدة. في الخلفية، يحتفظ Aspose.Cells بسلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.
سلسلة البيانات ذات الأربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق التجميع حيث توجد القيم الأولية.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. كل جدول محوري مبني فوق `PivotCache`؛ حيث يتم جمع جميع البيانات وتجميعها هنا.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` من `PivotCache` الخاص به *فقط*، وليس مباشرة من مصدر البيانات.
4. **Cells** — العناصر `Cells` في ورقة العمل التي يعرض فيها `PivotTable` القيم والأنماط المحسوبة.

{{% alert color="primary" %}}
تشير `PivotCache.SourceType` (تعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، تدعم `PivotCache.Refresh()` أنواع المصادر **`Sheet`** و**`Consolidation`** فقط، أي البيانات الموجودة في نطاقات ورقة العمل. لا يمكن تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) من خلال واجهة برمجة تطبيقات ذاكرة التخزين المؤقت حتى الآن.
{{% /alert %}}

نظرًا لهذه السلسلة، هناك مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون العودة إلى مصدر البيانات.
تعتمد جميع السيناريوهات في هذه المقالة على بيانات المصدر الموجودة في خلايا ورقة العمل، لذا يكون نوع المصدر `Sheet` وتعمل عمليات التحديث كما هو موضح.

## بدء سريع
إذا كنت تحتاج فقط إلى أقصر كود ممكن لتحديث كل جدول محوري في المصنف، فإن استدعاءً واحدًا يكفي:

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

كل شيء آخر في هذه المقالة يوضح متى تختار واجهة برمجة تطبيقات أضيق نطاقًا بدلاً من ذلك.

## توجيهات Using المطلوبة
تبدأ جميع أمثلة C# في هذه المقالة بتوجيهات using الثلاثة التالية لأن أنواع الجداول المحورية موجودة في مساحة الاسم `Aspose.Cells.Pivot`:
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت للجدول المحوري وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط واجهة برمجة تطبيقات وأكثرها شمولًا هي `Workbook.RefreshAll()`. يتجاوز هذا الاستدعاء المصنف بالكامل، حيث يقوم بتحديث كل `PivotCache` من مصدره ثم يعيد حساب كل `PivotTable` تابع. هذه هي الطريقة الموصى بها للتحديثات العامة والشاملة للمستندات عندما لا يكون الأداء موضع قلق.
يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لإحضار كل شيء إلى أحدث حالة في استدعاء واحد.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// إنشاء مصنف جديد
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// كتابة صف الرأس في الخلايا من A1 إلى C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// كتابة صفوف البيانات في الخلايا من A2 إلى C9 (8 صفوف من بيانات الفاكهة عبر عامي 2020 و 2021)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);
// إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// تعيين حقول الجدول المحوري: الفاكهة إلى الصفوف، السنة إلى الأعمدة، المبلغ إلى البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// تعديل عدة قيم للمبلغ في بيانات المصدر لمحاكاة التغييرات
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// تحديث كل جدول محوري / ذاكرة تخزين مؤقت للجدول المحوري في المصنف
workbook.RefreshAll();
// حفظ المصنف
workbook.Save("output.xlsx");
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة، على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.RefreshPivotTables()`، والذي يكون نطاقه محصورًا في مثيل `Worksheet` واحد.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);
worksheet.RefreshPivotTables();
workbook.Save("output.xlsx");
```

## تحديث جدول محوري واحد
عندما تريد تحكمًا دقيقًا في جدول محوري واحد، تمنحك واجهة برمجة التطبيقات المعتمدة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه فقط.

### تغيير بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. يعيد هذا الاستدعاء قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم يعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت هذه.

### تغيير العرض/التخطيط فقط — استخدم `CalculateData()`
إذا لم تتغير بيانات المصدر *ولكن* تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا داعي للعودة إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة؛ فقط يحتاج `PivotTable` المعروض إلى إعادة حساب. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار الصحيح.
يعدل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// كتابة صف رأس Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// كتابة 8 صفوف من البيانات (الصفوف 2-9، بما يتناسب مع نطاق المصدر A1:C9)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);
// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، ومصدره A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// تعيين الحقول: Fruit إلى Row، وYear إلى Column، وAmount إلى Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// تعديل خاصية عرض/تخطيط — هذا تغيير للعرض فقط،
// لذلك لا يتطلب إعادة قراءة بيانات المصدر من خلال PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() يعيد عرض الجدول المحوري هذا (البيانات + النمط) من
// البيانات المحفوظة بالفعل في PivotCache. نظرًا لأن بيانات المصدر لم تتغير،
// لن يتم إجراء أي جولة ذهاب وإياب إلى المصدر — فقط يتم إعادة حساب القيم المخزنة مؤقتًا
// في خلايا ورقة العمل.
pivotTable.CalculateData();
// حفظ المصنف على القرص
workbook.Save("output.xlsx");
```

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.

## الانتقال من `PivotTable.RefreshData()` القديمة
قبل Aspose.Cells for .NET v26.7، كانت الطريقة القياسية لتحديث الجدول المحوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة على أنها **قديمة** ويجب استبدالها بواجهات برمجة التطبيقات المدركة لذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان يجعلان نهج `RefreshData()` لكل جدول يمثل مشكلة في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر في *كل* مرة يتم استدعاؤها، حتى عندما لا يتغير المصدر.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الفعّال الجديد للمصنفات ذات الجداول المحورية المتعددة التي تتشارك ذاكرة تخزين مؤقت واحدة.

## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل منها.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | استدعاء واحد؛ يغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.RefreshPivotTables()` | محصور في ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.Refresh()` | يحدث جميع الجداول المحورية على ذاكرة التخزين المؤقت المشتركة هذه. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | يتجاوز جلب المصدر غير الضروري. |
| إدراج جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.GetPivotTables()` | استخدم للتعداد قبل التحديث المجمع. |
عمليًا، يُفضل استخدام واجهات برمجة التطبيقات المعتمدة على ذاكرة التخزين المؤقت بدلاً من `RefreshData()` القديمة لكل جدول. إنها تدرك ذاكرات التخزين المؤقت المشتركة، وتتجنب جلب المصدر المتكرر، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث لديك.

## المزالق الشائعة
- **نسيان التحديث قبل الحفظ.** يكتب الجدول المحوري قيمه المعروضة في ورقة العمل فقط عند تحديث سلسلة البيانات الخاصة به. إذا قمت بتعديل خلايا المصدر، فاستدعِ `PivotCache.Refresh()` (أو `Workbook.RefreshAll()`) قبل `Workbook.Save()`، وإلا فإن الملف المحفوظ لا يزال يحتوي على القيم المجمعة القديمة.
- **استدعاء `RefreshData()` القديمة لكل جدول.** في الإصدار v26.7، تم وضع علامة على `PivotTable.RefreshData()` على أنها قديمة وتعيد جلب المصدر لكل استدعاء. مع الجداول المحورية المتعددة التي تتشارك ذاكرة تخزين مؤقت، يعني هذا إجراء جلب مصدر متكرر بمقدار N مرة. استبدلها باستدعاء واحد لـ `PivotCache.Refresh()` متبوعًا بـ `CalculateData()` لكل جدول.
- **التحديث عند تغير التخطيط فقط.** إذا قمت بتغيير عرض الجدول المحوري فقط (ترتيب الأعمدة، `ConsolidationFunction`، إلخ) دون لمس بيانات المصدر، فإن `PivotCache.Refresh()` غير ضروري وبطيء. استدعِ `pivotTable.CalculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة.
- **المصدر الخارجي غير مدعوم من قبل `PivotCache.Refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، إلخ)، فلا يمكن لـ `PivotCache.Refresh()` تحديثه في الإصدار v26.7 — فهو يدعم حاليًا أنواع المصادر `Sheet` و`Consolidation` فقط. بالنسبة للمصادر الخارجية، أعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="csharp" >}}