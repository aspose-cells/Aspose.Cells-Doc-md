---
title: تحديث الجداول المحورية في Aspose.Cells for .NET
linktitle: تحديث الجداول المحورية في Aspose.Cells for .NET
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for .NET باستخدام واجهة برمجة التطبيقات للتحديث v26.7+. يغطي هذا المقال RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على الكود.
keywords: Aspose.Cells, .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يوفر Aspose.Cells واجهة برمجة تطبيقات (API) للتحديث ذات طبقات تتيح لك إعادة تحميل بيانات الجدول المحوري على أربعة نطاقات مختلفة — من المصنف بالكامل وصولاً إلى جدول محوري واحد. بدءًا من إصدار **Aspose.Cells for .NET v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` باعتبارها قديمة (obsolete) ويجب استبدالها بواجهات البرمجة الأكثر كفاءة والمبنية على مفهوم التخزين المؤقت (cache-aware) الموضحة في هذا المقال.

{{% /alert %}}

## مقدمة

نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. في الخلفية، يحتفظ Aspose.Cells بسلسلة بيانات ذات طبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.

سلسلة البيانات المكوّنة من أربع طبقات هي:

1. **مصدر البيانات (Data Source)** — نطاقات أوراق العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق التجميع حيث توجد القيم الخام.
2. **PivotCache** — اللقطة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ حيث يتم هنا جمع وتجميع جميع البيانات.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والفلاتر. يقرأ `PivotTable` من `PivotCache` الخاص به *فقط*، وليس مباشرةً من مصدر البيانات.
4. **الخلايا (Cells)** — كائن `Cells` الخاص بورقة العمل الذي يقوم `PivotTable` بعرض القيم والأنماط المحسوبة فيه.

من المفاهيم المهمة بشكل خاص مفهوم **التخزين المؤقت المشترك (shared cache)**. عندما تشير عدة جداول محورية في مصنف إلى نفس نطاق المصدر، فإنها تتشارك *مثيلًا واحدًا* من `PivotCache`. يمكن الإشارة إلى `PivotCache` واحد من قِبل العديد من الجداول المحورية، وتحديث هذا التخزين المؤقت يؤدي إلى تحديث كل `PivotTable` التابع له في وقت واحد.

{{% alert color="primary" %}}

يشير `PivotCache.SourceType` (وهو من النوع `PivotTableSourceType`) إلى مصدر بيانات التخزين المؤقت. اعتبارًا من الإصدار v26.7، تدعم `PivotCache.Refresh()` أنواع المصادر **`Sheet`** و **`Consolidation`** فقط — أي البيانات الموجودة في نطاقات أوراق العمل. لا يمكن بعدُ تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، وما إلى ذلك) من خلال واجهة برمجة التطبيقات الخاصة بالتخزين المؤقت.

{{% /alert %}}

نظرًا لهذه السلسلة، توجد مساران أساسيان للتحديث في Aspose.Cells:

- **`PivotCache.Refresh()`** — يعيد تحميل البيانات من المصدر إلى التخزين المؤقت (cache) **و** يعيد حساب جميع كائنات `PivotTable` التابعة في عملية واحدة.
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون أي رحلة ذهاب وإياب إلى مصدر البيانات.

تستخدم جميع السيناريوهات في هذا المقال بيانات مصدر موجودة في خلايا ورقة العمل، لذلك يكون نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.

## توجيهات Using المطلوبة

تبدأ جميع أمثلة C# في هذا المقال بتوجيهات using الثلاثة التالية لأن أنواع الجداول المحورية توجد في مساحة الأسماء `Aspose.Cells.Pivot`:

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## تحديث جميع الجداول المحورية في المصنف

عندما تحتاج إلى ضمان أن يعكس كل تخزين مؤقت وكل جدول محوري في المصنف أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.RefreshAll()`. تتجاوز هذه المكالمة الواحدة المصنف بالكامل — حيث تحدّث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` تابع. يُعد هذا الأسلوب الموصى به للتحديثات العامة والشاملة للمستند حيث لا يكون الأداء موضع قلق.

يُنشئ المثال التالي مصنفًا يحتوي على نطاق مصدر Fruit/Year/Amount، ويُنشئ جدولًا محوريًا واحدًا، ويُعدّل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لتحديث كل شيء في مكالمة واحدة.

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

// كتابة صفوف البيانات في الخلايا من A2 إلى C9 (8 صفوف من بيانات الفواكه عبر عامي 2020 و2021)
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

// تعديل عدة قيم في عمود Amount في بيانات المصدر لمحاكاة التغييرات
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// تحديث جميع الجداول المحورية / ذاكرة التخزين المؤقت للجدول المحوري في المصنف
workbook.RefreshAll();

// حفظ المصنف
workbook.Save("output.xlsx");
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة

في بعض الأحيان، تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما تعلم أن الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا ينبغي المساس بها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.RefreshPivotTables()`، وهو مقيّد بمثيل `Worksheet` واحد.

هذا أكثر انتقائية من `Workbook.RefreshAll()`: حيث يتم تحديث الجداول المحورية الموجودة في ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية في أوراق العمل الأخرى دون مساس.

يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويُضيف جدولًا محوريًا على ورقة العمل الأولى، ويُعدّل بعض قيم المصدر، ثم يحدّث الجداول المحورية الموجودة في تلك الورقة فقط.

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

عندما تريد تحكمًا دقيقًا في جدول محوري واحد، توفر لك واجهة البرمجة القائمة على التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو مجرد إعدادات العرض/التخطيط (view/layout) للجدول المحوري نفسه.

### عند تغيير بيانات المصدر — استخدم `PivotCache.Refresh()`

إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر في التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على هذا التخزين المؤقت.

{{% alert color="primary" %}}

نظرًا لأن الجداول المحورية تتشارك مثيلًا واحدًا من `PivotCache`، فإن استدعاء `PivotCache.Refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على نفس التخزين المؤقت — وليس فقط الذي تشير إليه. إذا كان هناك جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث تخزين مؤقت واحد يحدّث كليهما.

{{% /alert %}}

يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لتوضيح سلوك التخزين المؤقت المشترك هذا، ويُعدّل بعض قيم المصدر، ثم يحدّث من خلال مرجع تخزين مؤقت واحد.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// كتابة صف الرأس: الفاكهة / السنة / المبلغ
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// كتابة حوالي 9 صفوف من البيانات (عنب / توت أزرق / كيوي / كرز عبر 2020-2021)
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
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// إضافة جدول محوري أول "Pivot1" مثبت عند الخلية E3، نطاق المصدر A1:C9
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// تعيين الحقول لـ Pivot1
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// إضافة جدول محوري ثاني "Pivot2" مثبت عند E15 باستخدام نفس نطاق المصدر A1:C9
// يتشارك كل من Pivot1 و Pivot2 في ذاكرة تخزين مؤقتة واحدة للجدول المحوري لأن نطاق المصدر متطابق.
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// تعيين نفس الحقول لـ Pivot2
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// تعديل قيم خلايا المبلغ في البيانات المصدر لمحاكاة تغيير البيانات
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// تحديث ذاكرة التخزين المؤقتة المشتركة للجدول المحوري.
// لأن Pivot1 و Pivot2 يتشاركان نفس ذاكرة التخزين المؤقتة للجدول المحوري، فإن هذه المكالمة الواحدة
// تُحدّث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المُحدّث.
pivotTable1.PivotCache.Refresh();

// حفظ المصنف
workbook.Save("output.xlsx");
```

### عند تغيير العرض/التخطيط فقط — استخدم `CalculateData()`

إذا *لم* تتغير بيانات المصدر ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا حاجة للقيام برحلة ذهاب وإياب إلى مصدر البيانات. يحتفظ التخزين المؤقت بالفعل بالبيانات الصحيحة؛ فقط يحتاج `PivotTable` المعروض إلى إعادة الحساب. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار الصحيح.

هذا يتجنب عملية جلب المصدر غير الضرورية وأسرع بكثير عندما تتشارك العديد من الجداول المحورية نفس التخزين المؤقت.

يُعدّل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من التخزين المؤقت الموجود.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// كتابة صف العنوان Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// كتابة 8 صفوف بيانات (الصفوف من 2 إلى 9، تناسب نطاق المصدر A1:C9)
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

// إضافة جدول محوري اسمه "Pivot1" موضوع في خلية الوجهة E3، مصدره من A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// تعيين الحقول: Fruit إلى الصف، Year إلى العمود، Amount إلى البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// تعديل خاصية عرض/تخطيط — هذا تغيير للعرض فقط،
// لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;

// تقوم CalculateData() بإعادة عرض هذا الجدول المحوري (البيانات + النمط) من
// البيانات الموجودة بالفعل في PivotCache. نظراً لأن بيانات المصدر لم تتغير،
// لا يتم تنفيذ رحلة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتاً
// إلى خلايا ورقة العمل.
pivotTable.CalculateData();

// حفظ المصنف على القرص
workbook.Save("output.xlsx");
```

## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تقع جميعها فوق تخزين مؤقت مشترك واحد. لتعدادها — على سبيل المثال، قبل إجراء تحديث مجمع، أو لتشخيص تأثير التخزين المؤقت المشترك — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على التخزين المؤقت المعطى.

هذه أيضًا هي الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان بالفعل نفس مثيل `PivotCache`: يمكنك مقارنة مراجع التخزين المؤقت، أو ببساطة تكرار المجموعة التي تُرجعها `GetPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.

يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان نفس مثيل التخزين المؤقت، ثم يعدّد جداول التخزين المؤقت المحورية.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Sheet1";

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

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
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

int pivot1Index = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivot1Index];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivot2Index];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

bool sameCache = object.ReferenceEquals(pivotTable1.PivotCache, pivotTable2.PivotCache);
Console.WriteLine("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.PivotCache.GetPivotTables();
Console.WriteLine("Number of pivot tables sharing the cache: " + sharedPivotTables.Length);

foreach (PivotTable pt in sharedPivotTables)
{
    Console.WriteLine("Pivot table name: " + pt.Name);
}

workbook.Save("output.xlsx");
```

## الانتقال من الطريقة القديمة `PivotTable.RefreshData()`

قبل Aspose.Cells for .NET v26.7، كانت الطريقة المعيارية لتحديث الجدول المحوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من v26.7، تم وضع علامة على هذه الطريقة باعتبارها **قديمة (obsolete)** ويجب استبدالها بواجهات البرمجة المبنية على التخزين المؤقت الموضحة أعلاه.

هناك سببان يجعلان نهج `RefreshData()` لكل جدول يمثل مشكلة في المصنفات الواقعية:

- يعيد جلب البيانات من المصدر في *كل* مرة يتم استدعاؤها، حتى عندما لا يكون المصدر قد تغير.
- كل استدعاء يحدّث التخزين المؤقت المشترك بالكامل. عندما تتشارك العديد من الجداول المحورية تخزينًا مؤقتًا واحدًا، فإن استدعاء `RefreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس التخزين المؤقت مرارًا وتكرارًا، وهو بطيء جدًا.

البدائل الموصى بها هي:

- **لتحديث جميع الجداول المحورية في المصنف** → استخدم `workbook.RefreshAll();`
- **لتحديث بعضها** → استخدم `pivotTable.PivotCache.Refresh();` لتخزين مؤقت واحد. ولأن التخزين المؤقت مشترك، فإن هذه المكالمة الواحدة تحدّث كل جدول محوري مبني فوق هذا التخزين المؤقت. يمكن تخطي الجداول المحورية الأخرى التي تقع على تخزين مؤقت تم تحديثه بالفعل بأمان.
- **عند تغيير العرض/التخطيط فقط** → استخدم `pivotTable.CalculateData();` لإعادة العرض من التخزين المؤقت الموجود دون أي رحلة إلى المصدر.

يوضح المثال التالي النمط الجديد الفعال للمصنفات التي تحتوي على عدة جداول محورية تتشارك تخزينًا مؤقتًا واحدًا.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- بناء البيانات المصدر: الفاكهة / السنة / المبلغ (رأس + 9 صفوف) ---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- إضافة أول جدول محوري (Pivot1) عند خلية الوجهة E3 ---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- إضافة الجدول المحوري الثاني (Pivot2) على نفس نطاق المصدر ---
// يتشارك كل من Pivot1 و Pivot2 ذاكرة تخزين مؤقتة واحدة (PivotCache) أساسية.
// هذا هو بالضبط السيناريو الذي يصبح فيه نهج RefreshData() القديم
// لكل جدول غير فعال: حيث يؤدي تحديث جدول واحد إلى إعادة جلب كامل
// الذاكرة المشتركة، وبالتالي فإن تحديث N جدول يقوم بنفس الجلب المكلف N مرات.
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- تعديل عدة قيم للمبلغ في البيانات المصدر ---
sheet.Cells["C2"].PutValue(5000);   // Grape  2020
sheet.Cells["C5"].PutValue(7500);   // Cherry 2020
sheet.Cells["C9"].PutValue(9500);   // Cherry 2021

// --- النمط المهجور (قبل الإصدار 26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // يعيد الجلب من المصدر، ويحدّث كامل الذاكرة المؤقتة
// pivotTable2.RefreshData();  // يعيد الجلب مرة أخرى — الذاكرة المؤقتة بالفعل محدّثة!
// كل استدعاء يعيد بناء الذاكرة المشتركة، لذا N جدول = N جلب متكرر غير ضروري.

// --- النمط الجديد في الإصدار 26.7+: حدّث الذاكرة المؤقتة مرة واحدة، ثم أعد العرض حسب الحاجة ---
// استدعاء واحد لـ PivotCache.Refresh() يجلب القيم المعدلة إلى الذاكرة المشتركة
// ويعيد حساب العرض لكل جدول محوري يشير إليها.
// لأن Pivot1 و Pivot2 يتشاركان ذاكرة مؤقتة واحدة، فإن هذا الاستدعاء الوحيد يحدّث
// كلا الجدولين — دون الحاجة إلى رحلة ذهاب وإياب ثانية إلى المصدر.
pivotTable1.PivotCache.Refresh();

// CalculateData() يعيد فقط عرض الجدول المحوري (البيانات + النمط)
// من البيانات الموجودة بالفعل في الذاكرة المؤقتة — ولا يلمس المصدر.
// نستدعيها على Pivot2 هنا فقط لتوضيح الواجهة البرمجية: بعد تحديث الذاكرة المؤقتة
// مرة واحدة، يمكن إعادة عرض أي جدول تابع دون العودة إلى المصدر.
// استخدم CalculateData() بمفردها عندما تتغير إعدادات العرض/التخطيط فقط
// وتكون الذاكرة المؤقتة محدّثة.
pivotTable2.CalculateData();

workbook.Save("output.xlsx");
```

## أي واجهة برمجة تطبيقات (API) للتحديث يجب أن أستخدم؟

يلخص الجدول التالي واجهات التحديث المتاحة ومتى تختار كل منها.

| الهدف | واجهة البرمجة الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع التخزينات المؤقتة والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.RefreshPivotTables()` | مقيّد بورقة عمل واحدة. |
| تغيرت بيانات المصدر لتخزين مؤقت واحد | `pivotTable.PivotCache.Refresh()` | يحدّث **جميع** الجداول المحورية على ذلك التخزين المؤقت المشترك. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | يتجنب الرحلة غير الضرورية إلى المصدر. |
| سرد جميع الجداول المحورية على تخزين مؤقت مشترك | `pivotCache.GetPivotTables()` | استخدمه للتعداد قبل التحديث المجمع. |

عمليًا، يُفضّل استخدام واجهات البرمجة القائمة على التخزين المؤقت بدلاً من `RefreshData()` القديمة لكل جدول. إنها واعية بالتخزينات المؤقتة المشتركة، وتتجنب عمليات جلب المصدر المتكررة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث الخاصة بك.

{{< app/cells/assistant language="csharp" >}}