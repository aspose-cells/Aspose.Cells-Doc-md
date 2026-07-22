---
title: تحديث الجداول المحورية في Aspose.Cells for Node.js via Java
linktitle: تحديث الجداول المحورية في Aspose.Cells for Node.js via Java
description: تعرّف على كيفية تحديث الجداول المحورية في Aspose.Cells for Node.js via Java باستخدام واجهة برمجة التطبيقات لتحديث الجداول المحورية في الإصدار v26.7+. تتناول هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, Node.js, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يوفر Aspose.Cells واجهة برمجة تطبيقات للتحديث متعدد الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري على أربعة نطاقات مختلفة — من المصنف بالكامل وصولاً إلى جدول محوري واحد. بدءًا من الإصدار **Aspose.Cells for Node.js via Java v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` باعتبارها مهملة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمدركة لذاكرة التخزين المؤقت الموضحة في هذه المقالة.

{{% /alert %}}

## مقدمة

نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. خلف الكواليس، يحتفظ Aspose.Cells بسلسلة بيانات متعدد الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.

سلسلة البيانات ذات الطبقات الأربع هي:

1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق التجميع حيث توجد القيم الأولية.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. يتم بناء كل جدول محوري فوق `PivotCache`؛ حيث يتم جمع وتجميع جميع البيانات هنا.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرة من مصدر البيانات.
4. **الخلايا** — `Cells` الخاصة بورقة العمل التي يقوم `PivotTable` بعرض القيم والأنماط المحسوبة فيها.

من المفاهيم المهمة بشكل خاص **ذاكرة التخزين المؤقت المشتركة**. عندما تشير جداول محورية متعددة في مصنف إلى نفس نطاق المصدر، فإنها تتشارك *مثيلًا واحدًا* من `PivotCache`. يمكن الإشارة إلى `PivotCache` واحد بواسطة العديد من الجداول المحورية، ويؤدي تحديث ذاكرة التخزين المؤقت تلك إلى تحديث كل `PivotTable` تابع لها دفعة واحدة.

{{% alert color="primary" %}}

يشير `PivotCache.SourceType` (التعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، تدعم `PivotCache.Refresh()` أنواع المصادر **`Sheet`** و **`Consolidation`** فقط — أي البيانات الموجودة في نطاقات ورقة العمل. لا يمكن تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) من خلال واجهة برمجة تطبيقات ذاكرة التخزين المؤقت حتى الآن.

{{% /alert %}}

نظرًا لهذه السلسلة، هناك مساران أساسيان للتحديث في Aspose.Cells:

- **`PivotCache.Refresh()`** — يعيد تحميل البيانات من المصدر إلى ذاكرة التخزين المؤقت ويعيد حساب جميع `PivotTable` التابعة في عملية واحدة.
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون الحاجة إلى العودة إلى مصدر البيانات.

تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر من خلايا ورقة العمل، لذلك فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.

## الاستيرادات المطلوبة

تتطلب جميع أمثلة JavaScript في هذه المقالة وحدة Aspose.Cells for Node.js via Java. توجد أنواع الجداول المحورية في مساحة الاسم `Aspose.Cells.Pivot`، وهي جزء من نفس الوحدة:

- `const aspose = require('aspose.cells');`
- أو لاستيرادات محددة: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## تحديث جميع الجداول المحورية في المصنف

عندما تحتاج إلى ضمان أن تعكس كل ذاكرة تخزين مؤقت للجدول المحوري وكل جدول محوري في المصنف أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.RefreshAll()`. تتجاوز هذه المكالمة الواحدة المصنف بالكامل — حيث تقوم بتحديث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` تابع. هذه هي الطريقة الموصى بها لتحديثات المستندات الكاملة العامة عندما لا يكون الأداء مصدر قلق.

ينشئ المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولاً محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لجلب كل شيء حتى تاريخه في مكالمة واحدة.

```javascript
const AsposeCells = require("aspose.cells");

// إنشاء مصنف جديد
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// كتابة صف الرأس في الخلايا A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر عامي 2020 و2021)
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

// تحديث كل جدول محوري / ذاكرة تخزين مؤقت للجدول المحوري في المصنف
workbook.refreshAll();

// حفظ المصنف
workbook.save("output.xlsx");
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة

في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل محددة واحدة — على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.RefreshPivotTables()`، التي يتم تحديد نطاقها على مثيل `Worksheet` واحد.

تكون هذه أكثر انتقائية من `Workbook.RefreshAll()`: حيث يتم تحديث الجداول المحورية الموجودة في ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية في أوراق العمل الأخرى دون تغيير.

يملأ المثال التالي بيانات المصدر نفسها الخاصة بـ Fruit/Year/Amount، ويضيف جدولاً محوريًا في ورقة العمل الأولى، ويعدل بعض قيم المصدر، ثم يحدث فقط الجداول المحورية في ورقة العمل تلك.

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

عندما تريد التحكم الدقيق في جدول محوري واحد، توفر لك واجهة برمجة التطبيقات المستندة إلى ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه فقط.

### تغيير بيانات المصدر — استخدم `PivotCache.Refresh()`

إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الإدخال الصحيحة هي `pivotTable.PivotCache.Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت تلك.

{{% alert color="primary" %}}

نظرًا لأن الجداول المحورية تتشارك مثيلًا واحدًا من `PivotCache`، فإن استدعاء `PivotCache.Refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على نفس ذاكرة التخزين المؤقت — وليس فقط الجدول الذي تشير إليه. إذا كان جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث ذاكرة تخزين مؤقت واحدة يحدث كلاهما.

{{% /alert %}}

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لتوضيح سلوك ذاكرة التخزين المؤقت المشتركة، ويعدل بعض قيم المصدر، ثم يحدث من خلال مرجع ذاكرة تخزين مؤقت واحد.

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

// إضافة الجدول المحوري الأول "Pivot1" مثبت في الخلية E3، نطاق المصدر A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// تعيين الحقول لـ Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// إضافة الجدول المحوري الثاني "Pivot2" مثبت في E15 باستخدام نفس نطاق المصدر A1:C9
// يتشارك كل من Pivot1 و Pivot2 في ذاكرة تخزين مؤقتة واحدة للجدول المحوري لأن نطاق المصدر متطابق.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// تعيين نفس الحقول لـ Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تعديل قيم خلايا المبلغ في بيانات المصدر لمحاكاة تغيير في البيانات
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// تحديث ذاكرة التخزين المؤقتة المشتركة للجدول المحوري.
// نظرًا لأن Pivot1 و Pivot2 يتشاركان نفس ذاكرة التخزين المؤقتة للجدول المحوري، فإن هذه المكالمة الواحدة تحدّث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المحدّث.
pivotTable1.getPivotCache().refresh();

// حفظ المصنف
workbook.save("output.xlsx");
```

### تغيير العرض/التخطيط فقط — استخدم `CalculateData()`

إذا *لم* تتغير بيانات المصدر ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة؛ فقط يحتاج `PivotTable` المعروض إلى إعادة حساب. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار الصحيح.

يتجنب هذا الجلب غير الضروري للمصدر وهو أسرع بكثير عندما تتشارك العديد من الجداول المحورية نفس ذاكرة التخزين المؤقت.

يعدل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// كتابة 8 صفوف من البيانات (الصفوف من 2 إلى 9، بما يتناسب مع نطاق المصدر A1:C9)
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

// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، مع المصدر من A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين الحقول: الفاكهة إلى الصف، السنة إلى العمود، المبلغ إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تعديل خاصية عرض/تخطيط — هذا تغيير يخص العرض فقط،
// لذا فهو لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() يعيد عرض هذا الجدول المحوري (البيانات + النمط) من
// البيانات الموجودة بالفعل في PivotCache. نظرًا لأن بيانات المصدر لم تتغير،
// لا يتم إجراء أي رحلة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتًا
// في خلايا ورقة العمل.
pivotTable.calculateData();

// حفظ المصنف على القرص
workbook.save("output.xlsx");
```

## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل إجراء تحديث مجمع، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.

هذه أيضًا هي الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان بالفعل مثيل `PivotCache` نفسه: يمكنك مقارنة مراجع ذاكرة التخزين المؤقت، أو ببساطة تكرار المجموعة التي تم إرجاعها بواسطة `GetPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان مثيل ذاكرة التخزين المؤقت نفسه، ثم يعدد الجداول المحورية لذاكرة التخزين المؤقت.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## الانتقال من الطريقة المهملة `PivotTable.RefreshData()`

قبل Aspose.Cells for Node.js via Java v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة باعتبارها **مهملة** ويجب استبدالها بواجهات برمجة التطبيقات المدركة لذاكرة التخزين المؤقت الموضحة أعلاه.

هناك سببان يجعل نهج `RefreshData()` لكل جدول يمثل مشكلة في المصنفات الواقعية:

- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤها، حتى عندما لا يكون المصدر قد تغير.
- يقوم كل استدعاء بتحديث ذاكرة التخزين المؤقت المشتركة بالكامل. عندما تتشارك العديد من الجداول المحورية ذاكرة تخزين مؤقت واحدة، فإن استدعاء `RefreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس ذاكرة التخزين المؤقت مرارًا وتكرارًا، وهو بطيء جدًا.

البدائل الموصى بها هي:

- **تحديث جميع الجداول المحورية في المصنف** → استخدم `workbook.refreshAll();`
- **تحديث بعضها** → استخدم `pivotTable.getPivotCache().refresh();` لذاكرة تخزين مؤقت واحدة. نظرًا لأن ذاكرة التخزين المؤقت مشتركة، فإن هذه المكالمة الواحدة تحدث كل جدول محوري مبني فوق ذاكرة التخزين المؤقت تلك. يمكن تخطي الجداول المحورية الأخرى التي تجلس على ذاكرة تخزين مؤقت تم تحديثها بالفعل بأمان.
- **تغير عرض/تخطيط الجدول المحوري فقط** → استخدم `pivotTable.calculateData();` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة دون أي رحلة ذهاب وإياب إلى المصدر.

يوضح المثال التالي النمط الجديد الفعال للمصنفات التي تحتوي على جداول محورية متعددة تتشارك ذاكرة تخزين مؤقت واحدة.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- بناء بيانات المصدر: فاكهة / سنة / مبلغ (الترويسة + 9 صفوف) ---
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
// يشترك كل من Pivot1 و Pivot2 في PivotCache واحد أساسي.
// هذا هو بالضبط السيناريو الذي يصبح فيه نهج RefreshData() القديم لكل جدول
// غير فعال: تحديث جدول واحد يعيد جلب ذاكرة التخزين المؤقت بأكملها
// المشتركة، لذا فإن تحديث N جداول يقوم بنفس الجلب المكلف N مرات.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- تعديل عدة قيم للمبلغ في بيانات المصدر ---
sheet.getCells().get("C2").putValue(5000);   // عنب 2020
sheet.getCells().get("C5").putValue(7500);   // كرز 2020
sheet.getCells().get("C9").putValue(9500);   // كرز 2021

// --- النمط المهجور (قبل 26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // يعيد الجلب من المصدر، ويحدّث ذاكرة التخزين المؤقت بالكامل
// pivotTable2.refreshData();  // يعيد الجلب مرة أخرى — ذاكرة التخزين المؤقت حديثة بالفعل!
// كل استدعاء يعيد بناء ذاكرة التخزين المؤقت المشتركة، لذا N جداول = N عمليات جلب متكررة.

// --- النمط الجديد v26.7+: قم بتحديث ذاكرة التخزين المؤقت مرة واحدة، ثم أعد العرض حسب الحاجة ---
// استدعاء واحد لـ PivotCache.Refresh() يسحب القيم المعدلة إلى ذاكرة التخزين المؤقت
// المشتركة ويعيد حساب عرض كل جدول محوري يشير إليها.
// نظرًا لأن Pivot1 و Pivot2 يشتركان في PivotCache واحد، فإن هذا الاستدعاء الواحد يحدّث
// كلا الجدولين — لا حاجة لذهاب وإياب ثانٍ إلى المصدر.
pivotTable1.getPivotCache().refresh();

// CalculateData() يعيد عرض عرض الجدول المحوري فقط (البيانات + النمط)
// من البيانات المحفوظة بالفعل في ذاكرة التخزين المؤقت — ولا يلمس المصدر.
// نستدعيه على Pivot2 هنا فقط لتوضيح واجهة برمجة التطبيقات: بعد تحديث ذاكرة التخزين المؤقت
// مرة واحدة، يمكن إعادة عرض أي جدول تابع دون
// العودة إلى المصدر. استخدم CalculateData() بمفردها عندما تتغير فقط
// إعدادات عرض/تخطيط الجدول المحوري وتكون ذاكرة التخزين المؤقت حديثة.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟

يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة.

| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|----------------------------------|---------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.RefreshPivotTables()` | محددة بورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.Refresh()` | يحدث جميع الجداول المحورية على ذاكرة التخزين المؤقت المشتركة تلك. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | يتجنب رحلة غير ضرورية إلى المصدر. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.GetPivotTables()` | استخدم للتعداد قبل التحديث المجمع. |

عمليًا، يُفضل استخدام واجهات برمجة التطبيقات المستندة إلى ذاكرة التخزين المؤقت بدلاً من `RefreshData()` المهمل لكل جدول. إنها مدركة لذاكرة التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر الزائدة عن الحاجة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث الخاصة بك.

{{< app/cells/assistant language="javascript" >}}