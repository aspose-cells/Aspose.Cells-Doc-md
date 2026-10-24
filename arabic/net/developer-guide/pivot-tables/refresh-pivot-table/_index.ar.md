---
title: تحديث الجداول المحورية وذاكر التخزين المؤقت في Aspose.Cells for .Net
linktitle: تحديث الجداول المحورية وذاكر التخزين المؤقت في Aspose.Cells for .Net
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for .Net باستخدام واجهة API لتحديث الجداول المحورية المتاحة في v26.7+. تغطي هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة برمجية عملية.
keywords: Aspose.Cells, .NET, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells واجهة API متدرجة للتحديث تتيح لك إعادة تحميل بيانات الجداول المحورية ضمن أربعة نطاقات مختلفة — من المصنف بأكمله وصولًا إلى جدول محوري واحد. بدءًا من **Aspose.Cells for .Net v26.7**، أصبحت الطريقة القديمة `PivotTable.RefreshData()` **مهجورة**، ويجب استبدالها بواجهات API أكثر كفاءة تستند إلى ذاكرة التخزين المؤقت، كما هو موضح في هذه المقالة.
{{% /alert %}}

## مقدمة
لا يقتصر تحديث جدول محوري عادةً على عملية واحدة. في الخلفية، يحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة في ورقة العمل. يعد فهم هذه السلسلة مفتاح اختيار واجهة API المناسبة للتحديث في كل حالة.
تتمثل سلسلة البيانات ذات الطبقات الأربع في:
1. **مصدر البيانات** — نطاقات أوراق العمل الأصلية أو استعلام قاعدة البيانات أو نطاق التوحيد حيث توجد القيم الخام.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري اعتمادًا على `PivotCache`؛ وتُجمع البيانات وتُجرى عمليات التجميع فيه.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache`، ولا يقرأ من مصدر البيانات مباشرة.
4. **Cells** — مجموعة `Cells` الخاصة بورقة العمل، والتي يكتب `PivotTable` فيها قيمه المحسوبة وأنماطه.

{{% alert color="primary" %}}
تشير `PivotCache.SourceType` (التعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من v26.7، لا تدعم `PivotCache.Refresh()` سوى نوعَي المصدر **`Sheet`** و**`Consolidation`** — أي البيانات الموجودة في نطاقات أوراق العمل. ولا يمكن حتى الآن تحديث المصادر الخارجية (قواعد البيانات والاتصالات الخارجية وما إلى ذلك) عبر واجهة API الخاصة بذاكرة التخزين المؤقت.
نتيجة لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد انطلاقًا من البيانات المخزنة مؤقتًا بالفعل، من دون الانتقال إلى مصدر البيانات والعودة منه.
تستخدم جميع السيناريوهات في هذه المقالة خلايا ورقة العمل بوصفها مصدر البيانات، لذا يكون نوع المصدر `Sheet` وتعمل عمليات التحديث وفقًا لما هو موضح.
{{% /alert %}}

## بدء الاستخدام السريع
إذا كنت لا تحتاج سوى أقصر شيفرة ممكنة لتحديث كل جدول محوري في المصنف، فإن مكالمة واحدة تكفي:

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

تشرح بقية هذه المقالة متى ينبغي اختيار واجهة API أكثر تحديدًا.

## توجيهات `using` المطلوبة
تبدأ جميع أمثلة C# في هذه المقالة بتوجيهات `using` الثلاثة التالية، لأن أنواع الجداول المحورية موجودة في namespace `Aspose.Cells.Pivot`:
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى ضمان أن تعكس كل ذاكرة تخزين مؤقت وكل جدول محوري في المصنف أحدث بيانات المصدر، تكون واجهة API الأبسط والأكثر شمولاً هي `Workbook.RefreshAll()`. تنتقل هذه المكالمة عبر المصنف بأكمله — فتحدّث كل `PivotCache` من مصدره، ثم تعيد حساب كل `PivotTable` تعتمد عليه. هذا هو الأسلوب الموصى به للتحديثات العامة الكاملة للمستند عندما لا يمثل الأداء اعتبارًا مهمًا.
ينشئ المثال التالي مصنفًا يحتوي على نطاق مصدر Fruit/Year/Amount، وينشئ جدولاً محوريًا واحدًا، ويعدّل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لتحديث كل شيء في مكالمة واحدة.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// إنشاء مصنف جديد
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// كتابة صف العناوين في الخلايا A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر عامي 2020 و2021)
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
// تعيين حقول الجدول المحوري: Fruit إلى الصفوف، Year إلى الأعمدة، Amount إلى البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// تعديل عدة قيم Amount في بيانات المصدر لمحاكاة التغييرات
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// تحديث جميع الجداول المحورية / ذاكرات التخزين المؤقت للجداول المحورية في المصنف
workbook.RefreshAll();
// حفظ المصنف
workbook.Save("output.xlsx");
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان، لا تحتاج إلا إلى تحديث الجداول المحورية الموجودة في ورقة عمل محددة — على سبيل المثال، عندما يكون من المعروف أن جداول pivot في أوراق عمل أخرى غير مرتبطة ولا ينبغي المساس بها. في هذه الحالة، توفر Aspose.Cells `Worksheet.RefreshPivotTables()`، وهي مقصورة على مثيل `Worksheet` واحد.

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
عند الرغبة في التحكم الدقيق في جدول محوري واحد، توفر واجهة API القائمة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أم إعدادات العرض أو التخطيط الخاصة بالجدول المحوري نفسه.

### تغيرت بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيرت بيانات المصدر الأساسية، ف نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت، ثم تعيد حساب كل `PivotTable` يعتمد عليها.

### تغيرت إعدادات العرض أو التخطيط فقط — استخدم `CalculateData()`
إذا *لم* تتغير بيانات المصدر، ولكن عُدّلت إعدادات عرض الجدول المحوري أو تخطيطه فقط (على سبيل المثال، عند نقل حقل إلى منطقة مختلفة أو تبديل إعداد التحديث عند الفتح)، فلا حاجة إلى الانتقال إلى مصدر البيانات والعودة منه. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة، ولا يلزم سوى إعادة حساب `PivotTable` المعروض. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار المناسب.
يعدّل المثال التالي خاصية لا تتعلق بالمصدر في الجدول المحوري، ثم يستدعي `CalculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الحالية.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// كتابة صف رؤوس Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// كتابة 8 صفوف بيانات (الصفوف 2-9، بما يناسب نطاق المصدر A1:C9)
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
// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، مع مصدره A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// تعيين الحقول: Fruit إلى Row، وYear إلى Column، وAmount إلى Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// تعديل خاصية العرض/التخطيط — وهذا تغيير للعرض فقط،
// لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() يعيد رسم عرض جدول المحوري هذا (البيانات + النمط) من
// البيانات الموجودة بالفعل في PivotCache. ولأن بيانات المصدر لم تتغير،
// فلا يتم تنفيذ رحلة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتًا
// داخل خلايا ورقة العمل.
pivotTable.CalculateData();
// حفظ المصنف على القرص
workbook.Save("output.xlsx");
```

يحتوي المصنف عادةً على جداول محورية كثيرة تشترك جميعها في ذاكرة تخزين مؤقت واحدة. لتعدادها — على سبيل المثال، قبل تنفيذ تحديث جماعي أو لتشخيص أثر ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المحددة.

## الترحيل من الطريقة المهجورة `PivotTable.RefreshData()`
قبل Aspose.Cells for .Net v26.7، كانت الطريقة المعيارية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من v26.7، أصبحت هذه الطريقة **مهجورة**، ويجب استبدالها بواجهات API المعتمدة على ذاكرة التخزين المؤقت والموضحة أعلاه.
هناك سببان يجعل أسلوب `RefreshData()` لكل جدول مشكلة في المصنفات المستخدمة في العالم الحقيقي:
- يعيد جلب بيانات المصدر *في كل مرة* تُستدعى فيها، حتى عندما لا يكون المصدر قد تغير.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الجديد الأكثر كفاءة للمصنفات التي تحتوي على جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت واحدة.

## أي واجهة API للتحديث ينبغي استخدامها؟
يلخص الجدول التالي واجهات API المتاحة للتحديث ومتى ينبغي اختيار كل منها.
| الهدف | واجهة API الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي كل ذاكر التخزين المؤقت والجداول المحورية. |
| تحديث الجداول المحورية في ورقة عمل واحدة فقط | `Worksheet.RefreshPivotTables()` | مقصورة على ورقة عمل واحدة. |
| تغيرت بيانات المصدر الخاصة بذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.Refresh()` | تحدّث جميع الجداول المحورية الموجودة على ذاكرة التخزين المؤقت المشتركة. |
| تغيرت إعدادات العرض أو التخطيط فقط | `pivotTable.CalculateData()` | تتجنب الانتقال غير الضروري إلى المصدر والعودة منه. |
| حصر جميع الجداول المحورية الموجودة في ذاكرة تخزين مؤقت مشتركة | `pivotCache.GetPivotTables()` | استخدمها للتعداد قبل تنفيذ تحديث مجمّع. |
في الواقع، يُفضّل استخدام واجهات API المستندة إلى ذاكرة التخزين المؤقت بدلًا من `RefreshData()` المهجورة الخاصة بكل جدول. فهذه الواجهات تراعي ذاكر التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر المتكررة، وتتيح لك اختيار أضيق نطاق يحقق متطلبات التحديث.

## المزالق الشائعة
- **النسيان إجراء التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة البيانات المرتبطة به. إذا عدلت خلايا المصدر، فاستدعِ `PivotCache.Refresh()` (أو `Workbook.RefreshAll()`) قبل `Workbook.Save()`، وإلا فسيظل الملف المحفوظ يحتوي على القيم المجمعة القديمة.
- **استدعاء `RefreshData()` المهجورة لكل جدول.** في v26.7، أصبحت `PivotTable.RefreshData()` مهجورة وتعيد جلب المصدر في كل استدعاء. ومع تعدد الجداول المحورية التي تشترك في ذاكرة تخزين مؤقت واحدة، يعني ذلك N عمليات جلب زائدة للمصدر. استبدل ذلك بمكالمة واحدة إلى `PivotCache.Refresh()` تليها `CalculateData()` لكل جدول.
- **إجراء التحديث عندما يكون التخطيط وحده قد تغير.** إذا غيّرت عرض الجدول المحوري فقط (ترتيب الأعمدة، `ConsolidationFunction`، وما إلى ذلك) دون تعديل بيانات المصدر، فإن `PivotCache.Refresh()` غير ضروري وبطيء. استدعِ `pivotTable.CalculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الحالية.
- **مصدر خارجي غير مدعوم من `PivotCache.Refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، وما إلى ذلك)، فلا يمكن لـ `PivotCache.Refresh()` تحديثه في v26.7 — فهو يدعم حاليًا نوعَي المصدر `Sheet` و`Consolidation` فقط. أما المصادر الخارجية، فأعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="csharp" >}}