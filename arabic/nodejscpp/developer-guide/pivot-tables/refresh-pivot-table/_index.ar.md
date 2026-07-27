---
title: تحديث الجداول المحورية في Aspose.Cells for Node.js via C++
linktitle: تحديث الجداول المحورية في Aspose.Cells for Node.js via C++
description: تعلم كيفية تحديث الجداول المحورية في Aspose.Cells for Node.js via C++ باستخدام واجهة برمجة التطبيقات الخاصة بالتحديث v26.7+، تتناول هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, Node.js via C++, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة برمجة تطبيقات متعددة الطبقات للتحديث تتيح لك إعادة تحميل بيانات الجدول المحوري بأربعة نطاقات مختلفة، بدءًا من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Node.js via C++ v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` باعتبارها مهملة، ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمبنية على أساس ذاكرة التخزين المؤقت الموضحة في هذه المقالة.
{{% /alert %}}
## المقدمة
نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. وراء الكواليس، يحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.
سلسلة البيانات ذات الطبقات الأربع هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. يتم بناء كل جدول محوري فوق `PivotCache`؛ هذا هو المكان الذي يتم فيه جمع وتجميع جميع البيانات.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، ولا يقرأ أبدًا مباشرةً من مصدر البيانات.
4. **Cells** — ورقة العمل `Cells` التي يقوم `PivotTable` بعرض القيم والأنماط المحسوبة فيها.
من المفاهيم المهمة بشكل خاص: **ذاكرة التخزين المؤقت المشتركة**. عندما تشير جداول محورية متعددة في مصنف إلى نفس نطاق المصدر، فإنها تشارك *مثيلًا واحدًا* من `PivotCache`. يمكن الإشارة إلى `PivotCache` واحد بواسطة العديد من الجداول المحورية، ويؤدي تحديث ذاكرة التخزين المؤقت تلك إلى تحديث كل `PivotTable` تابع لها في وقت واحد.
{{% alert color="primary" %}}
يشير `PivotCache.SourceType` (التعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، يدعم `PivotCache.Refresh()` أنواع المصادر **`Sheet`** و**`Consolidation`** فقط، أي البيانات الموجودة في نطاقات أوراق العمل. لا يمكن تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، وما إلى ذلك) من خلال واجهة برمجة التطبيقات الخاصة بذاكرة التخزين المؤقت بعدُ.
{{% /alert %}}
نظرًا لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotCache.Refresh()`** — يعيد تحميل المصدر إلى ذاكرة التخزين المؤقت ويعيد حساب جميع `PivotTable` التابعة في عملية واحدة.
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون الحاجة إلى العودة إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات خلايا ورقة العمل كمصدر، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.
## الواردات المطلوبة
تفترض جميع أمثلة JavaScript في هذه المقالة أنه تم تحميل الوحدة Aspose.Cells for Node.js via C++، وأن أنواع الجدول المحوري موجودة في مساحة الأسماء `Aspose.Cells.Pivot`. الإعداد النموذجي هو:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (أو الوصول عبر `AsposeCells.Pivot.PivotFieldType`)
## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت للجداول المحورية وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط واجهة برمجة تطبيقات وأكثرها شمولاً هي `Workbook.RefreshAll()`. تتجاوز هذه المكالمة المصنف بأكمله، حيث تقوم بتحديث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` تابع له. هذا هو الأسلوب الموصى به للتحديثات العامة والشاملة للمستندات حيث لا يكون الأداء مصدر قلق.
يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لتحديث كل شيء في مكالمة واحدة.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// اكتب صف الرأس في الخلايا A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// اكتب صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر عامي 2020 و2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);

// أضف جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// خصص حقول الجدول المحوري: Fruit إلى Rows، Year إلى Columns، Amount إلى Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// عدّل عدة قيم Amount في بيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// حدّث كل جدول محوري / ذاكرة التخزين المؤقتة للجدول المحوري في المصنف
workbook.refreshAll();

// احفظ المصنف
workbook.save("output.xlsx");
```
## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة، على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى معروفة بأنها غير ذات صلة ولا يجب لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.RefreshPivotTables()`، وهو مخصص لمثيل `Worksheet` واحد.
هذا أكثر تحديدًا من `Workbook.RefreshAll()`: لا يتم تحديث سوى الجداول المحورية الموجودة في ورقة العمل المستهدفة، مع ترك أي جداول محورية في أوراق العمل الأخرى دون تغيير.
يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويضيف جدولًا محوريًا في ورقة العمل الأولى، ويعدل بعض قيم المصدر، ثم يقوم بتحديث الجداول المحورية في تلك الورقة فقط.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);

let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```
## تحديث جدول محوري واحد
عندما تريد التحكم الدقيق في جدول محوري واحد، تمنحك واجهة برمجة التطبيقات المبنية على أساس ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو مجرد إعدادات العرض/التخطيط للجدول المحوري نفسه.
### تغيرت بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت هذه.
{{% alert color="primary" %}}
نظرًا لأن الجداول المحورية تشترك في مثيل `PivotCache` واحد، فإن استدعاء `PivotCache.Refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على نفس ذاكرة التخزين المؤقت، وليس فقط الجدول الذي تشير إليه. إذا شارك جدولان محوريان نفس نطاق المصدر، فإن تحديثَ ذاكرة تخزين مؤقت واحدة يُحدِّث كليهما.
{{% /alert %}}
ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لإثبات سلوك ذاكرة التخزين المؤقت المشتركة، ويعدل بعض قيم المصدر، ثم يقوم بالتحديث من خلال مرجع ذاكرة تخزين مؤقت واحد.
```javascript
const AsposeCells = require("aspose.cells");

// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// كتابة صف الرأس: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// كتابة حوالي 9 صفوف بيانات (عنب / توت أزرق / كيوي / كرز عبر 2020-2021)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// إضافة الجدول المحوري الأول "Pivot1" مثبتًا عند الخلية E3، نطاق المصدر A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// تعيين الحقول لـ Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// إضافة جدول محوري ثانٍ "Pivot2" مثبتًا عند E15 باستخدام نفس نطاق المصدر A1:C9
// كل من Pivot1 و Pivot2 يتشاركان PivotCache واحد لأن نطاق المصدر متطابق.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// تعيين نفس الحقول لـ Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تعديل عدة قيم خلايا المبلغ في بيانات المصدر لمحاكاة تغيير البيانات
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// تحديث PivotCache المشترك.
// نظرًا لأن Pivot1 و Pivot2 يتشاركان نفس PivotCache، فإن هذه المكالمة الواحدة
// تقوم بتحديث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المحدّث.
pivotTable1.getPivotCache().refresh();

// حفظ المصنف
workbook.save("output.xlsx");
```
### تغير العرض/التخطيط فقط — استخدم `CalculateData()`
إذا لم تتغير بيانات المصدر ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتفظ ذاكرة التخزين المؤقت بالفعل بالبيانات الصحيحة؛ فقط يحتاج `PivotTable` المعروض إلى إعادة حساب. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار الصحيح.
هذا يتجنب جلب المصدر غير الضروري، وهو أسرع بكثير عندما تشترك العديد من الجداول المحورية في نفس ذاكرة التخزين المؤقت.
يعدل المثال التالي خاصية غير متعلقة بالمصدر للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.
```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// كتابة 8 صفوف بيانات (الصفوف من 2 إلى 9، مطابقة لنطاق المصدر A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);

// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، مصدره A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين الحقول: الفاكهة في الصفوف، السنة في الأعمدة، المبلغ في البيانات
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// تعديل خاصية عرض/تخطيط — هذا تغيير خاص بالعرض فقط،
// لذلك لا يتطلب إعادة قراءة البيانات المصدر عبر PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() يعيد عرض هذا الجدول المحوري (البيانات + النمط) من
// البيانات الموجودة بالفعل في PivotCache. نظرًا لأن البيانات المصدر لم تتغير،
// لا يتم إجراء أي رحلة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتًا
// في خلايا ورقة العمل.
pivotTable.calculateData();

// حفظ المصنف على القرص
workbook.save("output.xlsx");
```
## الحصول على جميع الجداول المحورية التي تشترك في نفس PivotCache
غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تقع جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها، على سبيل المثال، قبل تنفيذ تحديث دفعة واحدة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة، استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.
هذه أيضًا الطريقة الأكثر directe للتأكد من أن جدولين محوريين يتشاركان بالفعل في نفس مثيل `PivotCache`: يمكنك مقارنة مراجع ذاكرة التخزين المؤقت، أو ببساطة تكرار المجموعة التي تم إرجاعها بواسطة `GetPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.
ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يشتركان في نفس مثيل ذاكرة التخزين المؤقت، ثم يعدد جداول ذاكرة التخزين المؤقت.

## الانتقال من `PivotTable.RefreshData()` المهمل
قبل Aspose.Cells for Node.js via C++ v26.7، كانت الطريقة القياسية لتحديث الجدول المحوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة باعتبارها **مهملة** ويجب استبدالها بواجهات برمجة التطبيقات المبنية على أساس ذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان يجعلان نهج `RefreshData()` لكل جدول يمثل مشكلة في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤه، حتى عندما لا يتغير المصدر.
- تُحدِّث كل مكالمة ذاكرة التخزين المؤقت المشتركة بأكملها. عندما تشترك العديد من الجداول المحورية في ذاكرة تخزين مؤقت واحدة، فإن استدعاء `RefreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس ذاكرة التخزين المؤقت مرارًا وتكرارًا، وهو بطيء جدًا.
البدائل الموصى بها هي:
- **تحديث جميع الجداول المحورية في المصنف** → استخدم `workbook.refreshAll();`
- **تحديث بعضها** → استخدم `pivotTable.PivotCache.Refresh();` لذاكرة تخزين مؤقت واحدة. نظرًا لأن ذاكرة التخزين المؤقت مشتركة، فإن هذه المكالمة الواحدة تحدّث كل جدول محوري مبني فوق ذاكرة التخزين المؤقت تلك. يمكن تخطي الجداول المحورية الأخرى التي تعتمد على ذاكرة تخزين مؤقت تم تحديثها بالفعل بأمان.
- **تغير عرض/تخطيط الجدول المحوري فقط** → استخدم `pivotTable.CalculateData();` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة دون أي رحلة ذهاب وإياب إلى المصدر.
يوضح المثال التالي النمط الجديد الفعال للمصنفات التي تحتوي على جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت واحدة.
```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- بناء بيانات المصدر: الفاكهة / السنة / المبلغ (رأس + 9 صفوف) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- إضافة أول جدول محوري (Pivot1) في خلية الوجهة E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- إضافة الجدول المحوري الثاني (Pivot2) على نفس نطاق المصدر ---
// يتشارك كل من Pivot1 و Pivot2 في ذاكرة تخزين مؤقت محورية أساسية واحدة.
// هذا هو بالضبط السيناريو الذي تصبح فيه الطريقة القديمة RefreshData() لكل جدول
// غير فعالة: تحديث جدول واحد يجلب مرة أخرى كامل
// ذاكرة التخزين المؤقت المشتركة، لذا فإن تحديث N جداول يقوم بنفس الجلب المكلف N مرات.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- تعديل عدة قيم للمبلغ في بيانات المصدر ---
sheet.getCells().get("C2").putValue(5000);   // عنب 2020
sheet.getCells().get("C5").putValue(7500);   // كرز 2020
sheet.getCells().get("C9").putValue(9500);   // كرز 2021

// --- نمط قديم (قبل 26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // يجلب مرة أخرى من المصدر، يحدث ذاكرة التخزين المؤقت بالكامل
// pivotTable2.RefreshData();  // يجلب مرة أخرى — ذاكرة التخزين المؤقت طازجة بالفعل!
// كل استدعاء يعيد بناء ذاكرة التخزين المؤقت المشتركة، لذا N جداول = N جلب متكرر.

// --- نمط v26.7+ الجديد: حدث ذاكرة التخزين المؤقت مرة واحدة، ثم أعد العرض حسب الحاجة ---
// استدعاء واحد لـ PivotCache.Refresh() يسحب القيم المعدلة إلى المشتركة
// ذاكرة التخزين المؤقت ويعيد حساب عرض كل جدول محوري يشير إليها.
// لأن Pivot1 و Pivot2 يتشاركان في ذاكرة تخزين مؤقت محورية واحدة، فإن هذا الاستدعاء الواحد يحدث
// كلا الجدولين — لا حاجة إلى رحلة ثانية للمصدر.
pivotTable1.getPivotCache().refresh();

// CalculateData() يعيد عرض الجدول المحوري فقط (البيانات + النمط)
// من البيانات الموجودة بالفعل في ذاكرة التخزين المؤقت — فهو لا يلمس المصدر.
// نستدعيه على Pivot2 هنا فقط لتوضيح واجهة برمجة التطبيقات: بعد ذاكرة التخزين المؤقت
// تم تحديثها مرة واحدة، يمكن إعادة عرض أي جدول تابع دون
// العودة إلى المصدر. استخدم CalculateData() بمفردها عندما تكون فقط
// إعدادات عرض/تخطيط الجدول المحوري قد تغيرت وذاكرة التخزين المؤقت حالية.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل منها.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة، تغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.RefreshPivotTables()` | مخصصة لورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.Refresh()` | يحدّث **جميع** الجداول المحورية على تلك ذاكرة التخزين المؤقت المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | يتجنب رحلة غير ضرورية إلى المصدر. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.GetPivotTables()` | استخدم للتعداد قبل التحديث المجمّع. |
عمليًا، يُفضل استخدام واجهات برمجة التطبيقات المبنية على أساس ذاكرة التخزين المؤقت على `RefreshData()` المهمل لكل جدول. إنها على دراية بذاكرات التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر الزائدة عن الحاجة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث لديك.
## المقالات ذات الصلة
- [إدراج صورة في خلية](/cells/ar/nodejs-cpp/inserting-an-image-into-a-cell/)
- [قراءة وكتابة ملفات DBF](/cells/ar/nodejs-cpp/dbf/)
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [الرسوم البيانية المصغرة في Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/sparkline/)
{{< app/cells/assistant language="javascript" >}}
