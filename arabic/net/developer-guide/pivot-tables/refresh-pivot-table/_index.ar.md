---
title: تحديث الجداول المحورية في Aspose.Cells for .NET
linktitle: تحديث الجداول المحورية في Aspose.Cells for .NET
description: تعلم كيفية تحديث الجداول المحورية في Aspose.Cells for .NET باستخدام واجهة برمجة التطبيقات v26.7+ لتحديث الجداول المحورية. يتناول هذا المقال RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على الكود.
keywords: Aspose.Cells, .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة برمجة تطبيقات للتحديث على شكل طبقات تتيح لك إعادة تحميل بيانات الجدول المحوري على أربعة نطاقات مختلفة، من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءًا من **Aspose.Cells for .NET v26.7**، تم وضع علامة "مهجور" على الطريقة القديمة `PivotTable.RefreshData()`، ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمدرِكة لذاكرة التخزين المؤقت الموضحة في هذا المقال.
{{% /alert %}}
## المقدمة
نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. خلف الكواليس، يحافظ Aspose.Cells على سلسلة بيانات متعدد الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.
سلسلة البيانات المكونة من أربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ حيث يتم هنا جمع وتجميع جميع البيانات.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، ولا يقرأ مباشرةً من مصدر البيانات.
4. **Cells** — عناصر `Cells` في ورقة العمل التي يُصيّر فيها `PivotTable` القيم المحسوبة والأنماط.
من المفاهيم المهمة بشكل خاص **ذاكرة التخزين المؤقت المشتركة**. عندما تشير جداول محورية متعددة في المصنف إلى نفس نطاق المصدر، فإنها تتشارك *نفس* مثيل `PivotCache`. يمكن أن يشير `PivotCache` واحد إلى عدة جداول محورية، ويؤدي تحديث ذاكرة التخزين المؤقت تلك إلى تحديث كل `PivotTable` تابع لها في وقت واحد.
{{% alert color="primary" %}}
يوضح `PivotCache.SourceType` (التعداد `PivotTableSourceType`) مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، يدعم `PivotCache.Refresh()` فقط نوعي المصدر **`Sheet`** و **`Consolidation`** — أي البيانات الموجودة في نطاقات أوراق العمل. لا يمكن تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، وما إلى ذلك) من خلال واجهة برمجة التطبيقات الخاصة بذاكرة التخزين المؤقت حتى الآن.
{{% /alert %}}
بسبب هذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotCache.Refresh()`** — يُعيد تحميل البيانات من المصدر إلى ذاكرة التخزين المؤقت ويُعيد حساب جميع `PivotTable` التابعة في عملية واحدة.
- **`PivotTable.CalculateData()`** — يُعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون أي رحلة ذهاب وإياب إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذا المقال بيانات مصدر من خلايا ورقة العمل، لذلك فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.
## توجيهات الاستخدام المطلوبة
تبدأ جميع أمثلة C# في هذا المقال بتوجيهات الاستخدام الثلاثة التالية لأن أنواع الجداول المحورية توجد في مساحة الأسماء `Aspose.Cells.Pivot`:
## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.RefreshAll()`. تتجاوز مكالمة واحدة المصنف بأكمله — حيث تُحدِّث كل `PivotCache` من مصدره ثم تُعيد حساب كل `PivotTable` تابع. هذه هي الطريقة الموصى بها للتحديثات العامة والشاملة للمستندات عندما لا يكون الأداء مصدر قلق.
يُنشئ المثال التالي مصنفًا يحتوي على نطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويُعدِّل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لجلب كل شيء حتى تاريخه في مكالمة واحدة.
```csharp
using Aspose.Cells;

Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```
## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما يكون من المعروف أن الجداول المحورية في أوراق العمل الأخرى غير مرتبطة بها ولا ينبغي لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.RefreshPivotTables()`، التي يتم تحديد نطاقها لمثيل `Worksheet` واحد.
هذا أكثر انتقائية من `Workbook.RefreshAll()`: يتم تحديث الجداول المحورية الموجودة فقط على ورقة العمل المستهدفة، مع ترك أي جداول محورية على أوراق العمل الأخرى دون تغيير.
يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويُضيف جدولاً محوريًا في ورقة العمل الأولى، ويُعدِّل بعض قيم المصدر، ثم يُحدِّث الجداول المحورية الموجودة في ورقة العمل تلك فقط.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// إنشاء مصنف جديد
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// كتابة صف الرأس في الخلايا A1:C1
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
## تحديث جدول محوري واحد
عندما تريد التحكم الدقيق في جدول محوري واحد، توفر لك واجهة برمجة التطبيقات المستندة إلى ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو مجرد إعدادات العرض/التخطيط للجدول المحوري نفسه.
### تغيرت بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. تُعيد هذه المكالمة قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت ثم تُعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت تلك.
{{% alert color="primary" %}}
نظرًا لأن الجداول المحورية تتشارك مثيل `PivotCache` واحد، فإن استدعاء `PivotCache.Refresh()` يُعيد حساب **جميع** الجداول المحورية المبنية على نفس ذاكرة التخزين المؤقت — وليس فقط الجدول الذي تشير إليه. إذا كان هناك جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث ذاكرة تخزين مؤقت واحدة يُحدِّث كليهما.
{{% /alert %}}
يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لتوضيح سلوك ذاكرة التخزين المؤقت المشتركة، ويُعدِّل بعض قيم المصدر، ثم يُحدِّث من خلال مرجع ذاكرة تخزين مؤقت واحد.
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
### تغير العرض/التخطيط فقط — استخدم `CalculateData()`
إذا *لم* تتغير بيانات المصدر ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتفظ ذاكرة التخزين المؤقت بالفعل بالبيانات الصحيحة؛ فقط يحتاج `PivotTable` المعروض إلى إعادة الحساب. في هذه الحالة، `pivotTable.CalculateData()` هو الخيار الصحيح.
هذا يتجنب جلب المصدر غير الضروري وهو أسرع بكثير عندما تتشارك عدة جداول محورية نفس ذاكرة التخزين المؤقت.
يُعدِّل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// إنشاء مصنف جديد والوصول إلى أول ورقة عمل
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// كتابة صف العناوين: الفاكهة / السنة / المبلغ
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

// إضافة الجدول المحوري الأول "Pivot1" مثبتًا في الخلية E3، نطاق المصدر A1:C9
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// تعيين الحقول لـ Pivot1
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// إضافة جدول محوري ثانٍ "Pivot2" مثبتًا في E15 باستخدام نفس نطاق المصدر A1:C9
// يتشارك كل من Pivot1 و Pivot2 ذاكرة تخزين مؤقت واحدة لأن نطاق المصدر متطابق.
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// تعيين نفس الحقول لـ Pivot2
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// تعديل عدة قيم خلايا للمبلغ في البيانات المصدر لمحاكاة تغيير في البيانات
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// تحديث ذاكرة التخزين المؤقت للمحور المشتركة.
// لأن Pivot1 و Pivot2 يتشاركان نفس ذاكرة التخزين المؤقت للمحور، هذا الاستدعاء الوحيد
// يحدث كلاً من الجدولين المحوريين (البيانات + النمط) من المصدر المحدّث.
pivotTable1.PivotCache.Refresh();

// حفظ المصنف
workbook.Save("output.xlsx");
```
## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache
غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل تنفيذ تحديث مجمع، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.
هذه هي أيضًا الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان بالفعل نفس مثيل `PivotCache`: يمكنك مقارنة مراجع ذاكرة التخزين المؤقت، أو ببساطة تكرار المجموعة التي تُرجعها `GetPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.
يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان نفس مثيل ذاكرة التخزين المؤقت، ثم يعدد جداول ذاكرة التخزين المؤقت.
```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// كتابة 8 صفوف من البيانات (الصفوف 2-9، لتطابق نطاق المصدر A1:C9)
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

// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، ويستمد بياناته من A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// تعيين الحقول: Fruit إلى الصف، Year إلى العمود، Amount إلى البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// تعديل خاصية عرض/تخطيط — هذا تغيير يخص العرض فقط،
// لذلك فهو لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;

// تعمل CalculateData() على إعادة عرض جدول المحوري هذا (البيانات + النمط) من
// البيانات المحفوظة بالفعل في PivotCache. نظرًا لأن بيانات المصدر لم تتغير،
// لا يتم تنفيذ أي رحلة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتًا
// في خلايا ورقة العمل.
pivotTable.CalculateData();

// حفظ المصنف على القرص
workbook.Save("output.xlsx");
```
## الانتقال من `PivotTable.RefreshData()` المهجور
قبل Aspose.Cells for .NET v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة "مهجور" على هذه الطريقة ويجب استبدالها بواجهات برمجة التطبيقات المدرِكة لذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان يجعل نهج `RefreshData()` لكل جدول مشكلة في المصنفات الواقعية:
- إنه يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤها، حتى عندما لم يتغير المصدر.
- كل مكالمة تُحدِّث ذاكرة التخزين المؤقت المشتركة بالكامل. عندما تتشارك العديد من الجداول المحورية نفس ذاكرة التخزين المؤقت، فإن استدعاء `RefreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس ذاكرة التخزين المؤقت مرارًا وتكرارًا، وهو بطيء جدًا.
البدائل الموصى بها هي:
- **تحديث جميع الجداول المحورية في المصنف** ← استخدم `workbook.RefreshAll();`
- **تحديث بعضها** ← استخدم `pivotTable.PivotCache.Refresh();` لذاكرة تخزين مؤقت واحدة. نظرًا لأن ذاكرة التخزين المؤقت مشتركة، فإن هذه المكالمة الواحدة تُحدِّث كل جدول محوري مبني فوق ذاكرة التخزين المؤقت تلك. يمكن تخطي الجداول المحورية الأخرى التي تجلس فوق ذاكرة تخزين مؤقت تم تحديثها بالفعل بأمان.
- **تغير عرض/تخطيط الجدول المحوري فقط** ← استخدم `pivotTable.CalculateData();` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة دون أي رحلة ذهاب وإياب إلى المصدر.
يوضح المثال التالي النمط الفعّال الجديد للمصنفات ذات الجداول المحورية المتعددة التي تتشارك ذاكرة تخزين مؤقت واحدة.

## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة منها.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية فقط في ورقة واحدة | `Worksheet.RefreshPivotTables()` | مقيدة بورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.Refresh()` | تُحدِّث جميع الجداول المحورية على ذاكرة التخزين المؤقت المشتركة تلك. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | تتجنب رحلة غير ضرورية إلى المصدر. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.GetPivotTables()` | استخدم للتعداد قبل التحديث المجمع. |
عمليًا، يُفضل استخدام واجهات برمجة التطبيقات المستندة إلى ذاكرة التخزين المؤقت على `RefreshData()` المهجور لكل جدول. إنها مدرِكة لذاكرة التخزين المؤقت المشتركة، وتتجنب جلب المصدر الزائد عن الحاجة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث لديك.
## مقالات ذات صلة
- [إدراج صورة في خلية](/cells/ar/net/inserting-an-image-into-a-cell/)
- [قراءة وكتابة ملفات DBF](/cells/ar/net/dbf/)
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/net/splitting-excel-files-into-multiple-files/)
- [الرسوم البيانية المصغرة في Aspose.Cells for .NET](/cells/ar/net/sparkline/)
{{< app/cells/assistant language="csharp" >}}
