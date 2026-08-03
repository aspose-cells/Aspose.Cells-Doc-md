---
title: تحديث الجداول المحورية في Aspose.Cells for Node.js via Java
linktitle: تحديث الجداول المحورية في Aspose.Cells for Node.js via Java
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Node.js via Java باستخدام واجهة برمجة التطبيقات لتحديث الجداول المحورية في الإصدار v26.7+. تتناول هذه المقالة RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية.
keywords: Aspose.Cells, Node.js, Java, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفّر Aspose.Cells واجهة برمجة تطبيقات تحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجداول المحورية بأربعة نطاقات مختلفة — من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Node.js via Java v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` على أنها قديمة، ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والواعية بالذاكرة المؤقتة الموضحة في هذه المقالة.
{{% /alert %}}
## مقدمة
نادرًا ما تكون عملية تحديث الجدول المحوري عملية واحدة. في الخلفية، تحتفظ Aspose.Cells بسلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة مفتاح اختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.
سلسلة البيانات المكوّنة من أربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ حيث يتم جمع جميع البيانات وتجميعها هنا.
3. **PivotTable** — كائن العرض الذي يعرّف حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` البيانات من `PivotCache` الخاص به *فقط*، وليس مباشرةً من مصدر البيانات.
4. **الخلايا (Cells)** — `Cells` الخاصة بورقة العمل التي يُرسِل إليها `PivotTable` قيمه وأنماطه المحسوبة.
من المفاهيم المهمة بشكل خاص مفهوم **الذاكرة المؤقتة المشتركة**. عندما تشير جداول محورية متعددة في مصنف ما إلى نفس نطاق المصدر، فإنها تتشارك *نسخة واحدة* من `PivotCache`. يمكن الإشارة إلى `PivotCache` واحد بواسطة جداول محورية عديدة، وتؤدي إعادة تحديث تلك الذاكرة المؤقتة إلى تحديث كل `PivotTable` تابع لها دفعةً واحدة.
{{% alert color="primary" %}}
يُشير `PivotCache.SourceType` (وهو من نوع التعداد `PivotTableSourceType`) إلى مصدر بيانات الذاكرة المؤقتة. اعتبارًا من الإصدار v26.7، تدعم `PivotCache.Refresh()` فقط نوعَي المصدر **`Sheet`** و **`Consolidation`** — أي البيانات الموجودة في نطاقات ورقة العمل. أما المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، وما إلى ذلك) فلا يمكن تحديثها بعد عبر واجهة برمجة تطبيقات الذاكرة المؤقتة.
{{% /alert %}}
نظرًا لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotCache.Refresh()`** — يُعيد تحميل البيانات من المصدر إلى الذاكرة المؤقتة، ويُعيد حساب جميع `PivotTable` التابعة في عملية واحدة.
- **`PivotTable.CalculateData()`** — يُعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون أي رحلة ذهاب وإياب إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر موجودة في خلايا ورقة العمل، لذا يكون نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موصوف.
## الاستيرادات المطلوبة
تتطلب جميع أمثلة JavaScript في هذه المقالة وحدة Aspose.Cells for Node.js via Java. توجد أنواع الجداول المحورية في مساحة الأسماء `Aspose.Cells.Pivot`، وهي جزء من نفس الوحدة:
- `const aspose = require('aspose.cells');`
- أو للاستيرادات المحددة: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`
## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى التأكد من أن كل ذاكرة مؤقتة وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط واجهة برمجة تطبيقات وأكثرها شمولًا هي `Workbook.RefreshAll()`. تتنقل هذه المكالمة الواحدة عبر المصنف بأكمله — حيث تُحدّث كل `PivotCache` من مصدرها ثم تُعيد حساب كل `PivotTable` تابع. يُعد هذا الأسلوب الموصى به لتحديثات المستندات الكاملة العامة في الحالات التي لا يكون فيها الأداء موضع قلق.
يُنشئ المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويُعدّل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لجلب كل شيء حتى تاريخه في مكالمة واحدة.
```javascript
const AsposeCells = require("aspose.cells");

// إنشاء مصنف جديد
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// كتابة صف الرأس في الخلايا A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر 2020 و 2021)
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

// إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين حقول الجدول المحوري: الفاكهة إلى الصفوف، السنة إلى الأعمدة، المبلغ إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تعديل عدة قيم للمبلغ في بيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// تحديث كل جدول محوري / ذاكرة التخزين المؤقت للجدول المحوري في المصنف
workbook.refreshAll();

// حفظ المصنف
workbook.save("output.xlsx");
```
## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان، تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى معروفة بأنها غير مرتبطة ولا ينبغي لمسها. لهذه الحالة، توفر Aspose.Cells واجهة `Worksheet.RefreshPivotTables()`، التي تكون محصورة بنسخة `Worksheet` واحدة.
تكون هذه الواجهة أكثر تحديدًا من `Workbook.RefreshAll()`: حيث يتم تحديث الجداول المحورية الموجودة في ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية في أوراق العمل الأخرى دون مساس.
يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويضيف جدولًا محوريًا في ورقة العمل الأولى، ويُعدّل بعض قيم المصدر، ثم يُحدّث الجداول المحورية في تلك الورقة فقط.
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
عندما ترغب في التحكم الدقيق في جدول محوري واحد، توفر لك واجهة برمجة التطبيقات القائمة على الذاكرة المؤقتة خيارين. يعتمد الاختيار بينهما على ما تغيّر فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه.
### تغيّرت بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيّرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. تُعيد هذه المكالمة قراءة بيانات المصدر إلى الذاكرة المؤقتة ثم تُعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة المؤقتة.
{{% alert color="primary" %}}
نظرًا لأن الجداول المحورية تتشارك نسخة `PivotCache` واحدة، فإن استدعاء `PivotCache.Refresh()` يُعيد حساب **جميع** الجداول المحورية المبنية على نفس الذاكرة المؤقتة — وليس فقط الجدول الذي تُشير إليه. إذا كان هناك جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث ذاكرة مؤقتة واحدة يُحدّث كليهما.
{{% /alert %}}
يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لتوضيح سلوك الذاكرة المؤقتة المشتركة، ويُعدّل بعض قيم المصدر، ثم يُحدّث من خلال مرجع ذاكرة مؤقتة واحدة.
```javascript
const AsposeCells = require("aspose.cells");

// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// كتابة صف العناوين: الفاكهة / السنة / المبلغ
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

// إضافة جدول محوري أول "Pivot1" مثبت عند الخلية E3، نطاق المصدر A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// تعيين الحقول لـ Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// إضافة جدول محوري ثانٍ "Pivot2" مثبت عند E15 باستخدام نفس نطاق المصدر A1:C9
// يتشارك كل من Pivot1 و Pivot2 ذاكرة تخزين مؤقت واحدة لأن نطاق المصدر متطابق.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// تعيين نفس الحقول لـ Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تعديل عدة قيم لخلايا المبلغ في بيانات المصدر لمحاكاة تغيير البيانات
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// تحديث ذاكرة التخزين المؤقت المشتركة للجدول المحوري.
// نظرًا لأن Pivot1 و Pivot2 يتشاركان نفس ذاكرة التخزين المؤقت، فإن هذه المكالمة الواحدة
// تُحدّث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المُحدّث.
pivotTable1.getPivotCache().refresh();

// حفظ المصنف
workbook.save("output.xlsx");
```
### تغيّر العرض/التخطيط فقط — استخدم `CalculateData()`
إذا *لم* تتغيّر بيانات المصدر ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتفظ الذاكرة المؤقتة بالفعل بالبيانات الصحيحة؛ فقط `PivotTable` المعروض يحتاج إلى إعادة حساب. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار الصحيح.
يتجنّب ذلك جلب المصدر غير الضروري، وهو أسرع بكثير عندما تتشارك عدة جداول محورية في نفس الذاكرة المؤقتة.
يُعدّل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من الذاكرة المؤقتة الموجودة.
```javascript
var workbook = new AsposeCells.Workbook();

var worksheet = workbook.getWorksheets().get(0);



// كتابة صف العناوين: الفاكهة / السنة / المبلغ

worksheet.getCells().get("A1").putValue("Fruit");

worksheet.getCells().get("B1").putValue("Year");

worksheet.getCells().get("C1").putValue("Amount");



// كتابة 8 صفوف من البيانات (الصفوف من 2 إلى 9، لتطابق نطاق المصدر A1:C9)

worksheet.getCells().get("A2").putValue("Grape");

worksheet.getCells().get("B2").putValue(2020); \nworksheet.getCells().get("C2").putValue(100);



worksheet.getCells().get("A3").putValue("Blueberry");

worksheet.getCells().get("B3").putValue(2020); \nworksheet.getCells().get("C3").putValue(200);



worksheet.getCells().get("A4").putValue("Kiwi");

worksheet.getCells().get("B4").putValue(2020); \nworksheet.getCells().get("C4").putValue(300);



worksheet.getCells().get("A5").putValue("Cherry");

worksheet.getCells().get("B5").putValue(2020); \nworksheet.getCells().get("C5").putValue(400);



worksheet.getCells().get("A6").putValue("Grape");

worksheet.getCells().get("B6").putValue(2021); \nworksheet.getCells().get("C6").putValue(150);



worksheet.getCells().get("A7").putValue("Blueberry");

worksheet.getCells().get("B7").putValue(2021); \nworksheet.getCells().get("C7").putValue(250);



worksheet.getCells().get("A8").putValue("Kiwi");

worksheet.getCells().get("B8").putValue(2021); \nworksheet.getCells().get("C8").putValue(350);



worksheet.getCells().get("A9").putValue("Cherry");

worksheet.getCells().get("B9").putValue(2021); \nworksheet.getCells().get("C9").putValue(450);



// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، يستقي بياناته من النطاق A1:C9\nvar pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");\nvar pivotTable = worksheet.getPivotTables().get(pivotIndex);\n\n// تعيين الحقول: الفاكهة إلى الصفوف، السنة إلى الأعمدة، المبلغ إلى البيانات\npivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");\npivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");\npivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");\n\n// تعديل خاصية عرض/تخطيط - هذا تغيير يتعلق بالعرض فقط،\n// لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().\npivotTable.setRefreshDataOnOpeningFile(false);\n\n// CalculateData() يعيد عرض هذا الجدول المحوري (البيانات + النمط) من\n// البيانات المخزنة بالفعل في PivotCache. ولأن بيانات المصدر لم تتغير،\n// لا يتم إجراء أي رحلة ذهاب وإياب إلى المصدر - يتم فقط إعادة حساب القيم المخزنة مؤقتًا\n// في خلايا ورقة العمل.\npivotTable.calculateData();\n\n// حفظ المصنف على القرص\nworkbook.save("output.xlsx");
```
## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache
غالبًا ما يحتوي المصنف على جداول محورية عديدة جميعها مبنية فوق ذاكرة مؤقتة مشتركة واحدة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعة، أو لتشخيص تأثير الذاكرة المؤقتة المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على الذاكرة المؤقتة المعطاة.
هذه أيضًا هي الطريقة المباشرة الأكثر تأكيدًا على أن جدولين محوريين يتشاركان فعلاً نفس نسخة `PivotCache`: يمكنك مقارنة مراجع الذاكرة المؤقتة، أو ببساطة تكرار المجموعة التي تُرجعها `GetPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.
يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان نفس نسخة الذاكرة المؤقتة، ثم يُعدّد جداول الذاكرة المؤقتة.

## الترحيل من `PivotTable.RefreshData()` القديمة
قبل Aspose.Cells for Node.js via Java v26.7، كانت الطريقة المعيارية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة على أنها **قديمة** ويجب استبدالها بواجهات برمجة التطبيقات الواعية بالذاكرة المؤقتة الموضحة أعلاه.
هناك سببان يجعل أسلوب `RefreshData()` لكل جدول يمثل مشكلة في المصنفات الواقعية:
- يُعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤها فيها، حتى عندما لا يكون المصدر قد تغيّر.
- يُحدّث كل استدعاء الذاكرة المؤقتة المشتركة بأكملها. عندما تتشارك عدة جداول محورية في ذاكرة مؤقتة واحدة، فإن استدعاء `RefreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس الذاكرة المؤقتة مرارًا وتكرارًا، وهو أمر بطيء جدًا.
البدائل الموصى بها هي:
- **تحديث جميع الجداول المحورية في المصنف** ← استخدم `workbook.refreshAll();`
- **تحديث بعضها فقط** ← استخدم `pivotTable.getPivotCache().refresh();` لذاكرة مؤقتة واحدة. نظرًا لأن الذاكرة المؤقتة مشتركة، فإن هذه المكالمة الواحدة تُحدّث كل جدول محوري مبني فوق تلك الذاكرة المؤقتة. يمكن بأمان تخطي الجداول المحورية الأخرى المبنية على ذاكرة مؤقتة تم تحديثها بالفعل.
- **تغيّر عرض/تخطيط الجدول المحوري فقط** ← استخدم `pivotTable.calculateData();` لإعادة العرض من الذاكرة المؤقتة الموجودة دون أي رحلة إلى المصدر.
يوضح المثال التالي النمط الجديد الفعّال للمصنفات التي تحتوي على جداول محورية متعددة تتشارك ذاكرة مؤقتة واحدة.
```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- بناء بيانات المصدر: الفاكهة / السنة / المبلغ (العنوان + 9 صفوف) ---
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

// --- إضافة الجدول المحوري الأول (Pivot1) في خلية الوجهة E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- إضافة الجدول المحوري الثاني (Pivot2) على نفس نطاق المصدر ---
// يشترك كل من Pivot1 و Pivot2 في ذاكرة تخزين مؤقت (PivotCache) واحدة أساسية.
// هذا هو بالضبط السيناريو الذي يصبح فيه النهج القديم القائم على RefreshData()
// لكل جدول غير فعّال: تحديث جدول واحد يعيد جلب كل الذاكرة المشتركة بالكامل،
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
// لذا فإن تحديث N من الجداول ينفذ عملية الجلب المكلفة نفسها N مرة.
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- تعديل عدة قيم للمبلغ في بيانات المصدر ---
sheet.getCells().get("C2").putValue(5000);   // عنب 2020
sheet.getCells().get("C5").putValue(7500);   // كرز 2020
sheet.getCells().get("C9").putValue(9500);   // كرز 2021

// --- النمط القديم (قبل الإصدار 26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // يعيد الجلب من المصدر، ويحدّث الذاكرة بالكامل
// pivotTable2.refreshData();  // يعيد الجلب مرة أخرى — الذاكرة محدّثة بالفعل!
// كل استدعاء يعيد بناء الذاكرة المشتركة، لذا فإن N جداول تعني N من عمليات الجلب المتكررة.

// --- النمط الجديد في الإصدار 26.7+: تحديث الذاكرة مرة واحدة، ثم إعادة العرض حسب الحاجة ---
// استدعاء واحد إلى PivotCache.Refresh() يسحب القيم المعدّلة إلى الذاكرة المشتركة
// ويعيد حساب العرض لكل جدول محوري يشير إليها.
// ولأن Pivot1 و Pivot2 يشتركان في PivotCache واحد، فإن هذا الاستدعاء الواحد
// يحدّث كلا الجدولين — ولا حاجة لذهاب ثانٍ إلى المصدر.
pivotTable1.getPivotCache().refresh();

// CalculateData() يعيد فقط عرض الجدول المحوري (البيانات + النمط)
// من البيانات الموجودة فعلاً في الذاكرة — ولا يلمس المصدر.
// نستدعيه هنا على Pivot2 فقط لتوضيح الواجهة البرمجية: بعد تحديث
// الذاكرة مرة واحدة، يمكن إعادة عرض أي جدول تابع دون العودة إلى المصدر.
// استخدم CalculateData() بمفردها عندما تتغير إعدادات العرض/التخطيط
// فقط للجدول المحوري وتكون الذاكرة محدّثة.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة منها.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع الذواكر المؤقتة والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.RefreshPivotTables()` | محصور بورقة عمل واحدة. |
| تغيّرت بيانات المصدر لذاكرة مؤقتة واحدة | `pivotTable.PivotCache.Refresh()` | يُحدّث جميع الجداول المحورية على تلك الذاكرة المؤقتة المشتركة. |
| تغيّرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | يتخطى رحلة المصدر غير الضرورية. |
| إدراج جميع الجداول المحورية في ذاكرة مؤقتة مشتركة | `pivotCache.GetPivotTables()` | استخدمه للتعداد قبل التحديث بالجملة. |
عمليًا، يُفضّل استخدام واجهات برمجة التطبيقات القائمة على الذاكرة المؤقتة على `RefreshData()` القديمة لكل جدول. إنها واعية بالذاكرات المؤقتة المشتركة، وتتجنّب جلب المصدر المتكرر، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث لديك.

{{< app/cells/assistant language="nodejs-java" >}}
