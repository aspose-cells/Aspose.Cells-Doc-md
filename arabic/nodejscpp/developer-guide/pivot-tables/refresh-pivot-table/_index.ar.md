---
title: تحديث الجداول المحورية في Aspose.Cells for Node.js via C++
linktitle: تحديث الجداول المحورية في Aspose.Cells for Node.js via C++
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Node.js via C++ باستخدام واجهة برمجة تطبيقات تحديث المحاور v26.7+، تتناول هذه المقالة RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, Node.js via C++, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يوفّر Aspose.Cells واجهة برمجة تطبيقات تحديث متعدّدة الطبقات تتيح لك إعادة تحميل بيانات المحور بأربعة نطاقات مختلفة، من المصنف بأكمله وصولًا إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Aspose.Cells for Node.js via C++ v26.7**، يتم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` باعتبارها مُهمَلة، ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والواعية بالذاكرة المؤقتة الموضّحة في هذه المقالة.

{{% /alert %}}

## المقدمة

نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. ففي الخلفية، يحافظ Aspose.Cells على سلسلة بيانات متعدّدة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة تطبيقات التحديث المناسبة لأي موقف.

سلسلة البيانات المكوّنة من أربع طبقات هي:

1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ وهنا يتم جمع جميع البيانات وتجميعها.
3. **PivotTable** — كائن العرض الذي يعرّف حقول الصفوف والأعمدة والقيم والفلاتر. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرةً من مصدر البيانات.
4. **الخلايا** — خلايا `Cells` في ورقة العمل التي يُرسم فيها `PivotTable` القيم المحسوبة والأنماط.

من المفاهيم المهمّة بشكل خاص **الذاكرة المؤقتة المشتركة**. عندما تشير جداول محورية متعددة في مصنف إلى نطاق المصدر نفسه، فإنها تتشارك *ذاكرة مؤقتة واحدة* من نوع `PivotCache`. يمكن أن تشير عدة جداول محورية إلى `PivotCache` واحد، ويؤدي تحديث تلك الذاكرة المؤقتة إلى تحديث كل `PivotTable` تابع لها دفعةً واحدة.

{{% alert color="primary" %}}

يشير `PivotCache.SourceType` (وهو من النوع `PivotTableSourceType`) إلى مصدر بيانات الذاكرة المؤقتة. اعتبارًا من إصدار v26.7، يدعم `PivotCache.Refresh()` نوعي المصادر **`Sheet`** و **`Consolidation`** فقط — أي البيانات الموجودة في نطاقات أوراق العمل. لا يمكن بعد تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) من خلال واجهة برمجة التطبيقات الخاصة بالذاكرة المؤقتة.

{{% /alert %}}

نظرًا لهذه السلسلة، توجد مسارات تحديث أساسية اثنان في Aspose.Cells:

- **`PivotCache.Refresh()`** — يعيد تحميل المصدر إلى الذاكرة المؤقتة ويعيد حساب كل `PivotTable` تابع في عملية واحدة.
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزّنة في الذاكرة المؤقتة بالفعل، دون العودة إلى مصدر البيانات.

جميع السيناريوهات في هذه المقالة تستخدم بيانات مصدر موجودة في خلايا ورقة العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موصوف.

## الاستيرادات المطلوبة

تفترض جميع أمثلة JavaScript في هذه المقالة أنه قد تم تحميل وحدة Aspose.Cells for Node.js via C++ وأن أنواع المحاور موجودة في مساحة الاسم `Aspose.Cells.Pivot`. الإعداد النموذجي هو:

- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (أو الوصول عبر `AsposeCells.Pivot.PivotFieldType`)

## تحديث جميع الجداول المحورية في المصنف

عندما تحتاج إلى التأكد من أن كل ذاكرة محورية وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط واجهة برمجة تطبيقات وأكثرها شمولاً هي `Workbook.RefreshAll()`. تتجاوز مكالمة واحدة المصنف بالكامل — حيث تحدّث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` تابع. هذه هي الطريقة الموصى بها لعمليات التحديث العامة والشاملة حيث لا يكون الأداء موضع قلق.

يُنشئ المثال التالي مصنفًا يحتوي على نطاق مصدر Fruit/Year/Amount، ويُنشئ جدولًا محوريًا واحدًا، ويُعدّل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لجلب كل شيء محدثًا في مكالمة واحدة.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين حقول الجدول المحوري: Fruit إلى الصفوف، Year إلى الأعمدة، Amount إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تعديل عدة قيم Amount في بيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// تحديث كل جدول محوري / ذاكرة تخزين مؤقت للجدول المحوري في المصنف
workbook.refreshAll();

// حفظ المصنف
workbook.save("output.xlsx");
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة

أحيانًا تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى معروفة بأنها غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، يوفّر Aspose.Cells `Worksheet.RefreshPivotTables()`، وهي واجهة مقيّدة بمثيل `Worksheet` واحد.

هذه الطريقة أكثر انتقائية من `Workbook.RefreshAll()`: لا يتم تحديث سوى الجداول المحورية الموجودة في ورقة العمل المستهدفة، مع ترك أي جداول محورية في أوراق العمل الأخرى دون مساس.

يملأ المثال التالي بيانات المصدر نفسها Fruit/Year/Amount، ويُضيف جدولًا محوريًا في ورقة العمل الأولى، ويُعدّل بعض قيم المصدر، ثم يحدّث الجداول المحورية في تلك الورقة فقط.

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

عندما تريد تحكمًا دقيقًا في جدول محوري واحد، توفّر لك واجهة برمجة التطبيقات القائمة على الذاكرة المؤقتة خيارين. يعتمد الاختيار بينهما على ما تغيّر فعلاً: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه.

### تغيّرت بيانات المصدر — استخدم `PivotCache.Refresh()`

إذا تغيّرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر إلى الذاكرة المؤقتة ثم تعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة المؤقتة.

{{% alert color="primary" %}}

لأن الجداول المحورية تتشارك نسخة `PivotCache` واحدة، فإن استدعاء `PivotCache.Refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على تلك الذاكرة المؤقتة نفسها — وليس فقط الجدول الذي تشير إليه. إذا كان هناك جدولان محوريان يتشاركان نطاق المصدر نفسه، فإن تحديث ذاكرة مؤقتة واحدة يحدّث كليهما.

{{% /alert %}}

يُنشئ المثال التالي جدولين محوريين على نطاق المصدر نفسه لإثبات سلوك الذاكرة المؤقتة المشتركة هذا، ويُعدّل بعض قيم المصدر، ثم يحدّث من خلال مرجع ذاكرة مؤقتة واحد.

```javascript
const AsposeCells = require("aspose.cells");

// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// كتابة صف العناوين: الفاكهة / السنة / الكمية
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// كتابة ما يقارب 9 صفوف بيانات (عنب / توت أزرق / كيوي / كرز عبر عامي 2020-2021)
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

// إضافة أول جدول محوري "Pivot1" مثبت عند الخلية E3، نطاق المصدر A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// تعيين الحقول لـ Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// إضافة جدول محوري ثانٍ "Pivot2" مثبت عند E15 باستخدام نفس نطاق المصدر A1:C9
// يتشارك كل من Pivot1 و Pivot2 ذاكرة تخزين مؤقت للمحور واحدة لأن نطاق المصدر متطابق.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// تعيين نفس الحقول لـ Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تعديل قيم خلايا الكمية في بيانات المصدر لمحاكاة تغيير في البيانات
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// تحديث ذاكرة التخزين المؤقت للمحور المشتركة.
// لأن Pivot1 و Pivot2 يتشاركان نفس ذاكرة التخزين المؤقت، فإن هذه المكالمة الواحدة
// تحدث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المحدث.
pivotTable1.getPivotCache().refresh();

// حفظ المصنف
workbook.save("output.xlsx");
```

### تغيّر العرض/التخطيط فقط — استخدم `CalculateData()`

إذا *لم* تتغيّر بيانات المصدر ولكن تغيّرت إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا داعي للعودة إلى مصدر البيانات. تحتفظ الذاكرة المؤقتة بالفعل بالبيانات الصحيحة؛ فقط `PivotTable` المعروض يحتاج إلى إعادة حساب. في هذه الحالة، `pivotTable.CalculateData()` هو الخيار الصحيح.

يتجنّب ذلك جلبًا غير ضروريًا من المصدر وهو أسرع بكثير عندما تتشارك عدة جداول محورية نفس الذاكرة المؤقتة.

يُعدّل المثال التالي خاصية غير مصدر في الجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من الذاكرة المؤقتة الموجودة.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// كتابة 8 صفوف من البيانات (الصفوف 2-9، لتطابق نطاق المصدر A1:C9)
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

// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، ومصدره A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين الحقول: الفاكهة إلى الصف، السنة إلى العمود، المبلغ إلى البيانات
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// تعديل خاصية عرض/تخطيط — هذا تغيير خاص بالعرض فقط،
// لذلك لا يتطلب إعادة قراءة بيانات المصدر من خلال PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// تقوم calculateData() بإعادة عرض هذا الجدول المحوري (البيانات + النمط) من
// البيانات المحفوظة بالفعل في PivotCache. نظرًا لأن بيانات المصدر لم تتغير،
// لا يتم إجراء أي رحلة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب
// القيم المخزنة مؤقتًا إلى خلايا ورقة العمل.
pivotTable.calculateData();

// حفظ المصنف على القرص
workbook.save("output.xlsx");
```

## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache

غالبًا ما يحتوي المصنف على عدة جداول محورية جميعها تستند إلى ذاكرة مؤقتة مشتركة واحدة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعة، أو لتشخيص تأثير الذاكرة المؤقتة المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة المجموعة الكاملة لكل `PivotTable` يعتمد على الذاكرة المؤقتة المعطاة.

هذه أيضًا الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان فعلاً نفس نسخة `PivotCache`: يمكنك مقارنة مراجع الذاكرة المؤقتة، أو ببساطة تكرار المجموعة التي تُرجعها `GetPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.

يُنشئ المثال التالي جدولين محوريين على نطاق المصدر نفسه، ويتحقق من أنهما يتشاركان نفس نسخة الذاكرة المؤقتة، ثم يُعدّد الجداول المحورية في تلك الذاكرة.

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
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## الانتقال من `PivotTable.RefreshData()` المُهمَلة

قبل Aspose.Cells for Aspose.Cells for Node.js via C++ v26.7، كانت الطريقة المعيارية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من إصدار v26.7، يتم وضع علامة على هذه الطريقة باعتبارها **مُهمَلة** ويجب استبدالها بواجهات برمجة التطبيقات الواعية بالذاكرة المؤقتة الموضّحة أعلاه.

هناك سببان يجعل نهج `RefreshData()` لكل جدول مشكلة في المصنفات الواقعية:

- يعيد جلب البيانات من المصدر *في كل* مرة يتم استدعاؤها فيها، حتى عندما لا يكون المصدر قد تغيّر.
- تُحدّث كل مكالمة الذاكرة المؤقتة المشتركة بالكامل. عندما تتشارك عدة جداول محورية ذاكرة مؤقتة واحدة، فإن استدعاء `RefreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس الذاكرة المؤقتة مرارًا وتكرارًا، وهو أمر بطيء جدًا.

البدائل الموصى بها هي:

- **تحديث جميع الجداول المحورية في المصنف** → استخدم `workbook.refreshAll();`
- **تحديث بعضها** → استخدم `pivotTable.PivotCache.Refresh();` لذاكرة مؤقتة واحدة. ولأن الذاكرة المؤقتة مشتركة، فإن هذه المكالمة الواحدة تُحدّث كل جدول محوري مبني فوق تلك الذاكرة المؤقتة. يمكن تخطّي الجداول المحورية الأخرى التي تستند إلى ذاكرة مؤقتة مُحدّثة بالفعل بأمان.
- **تغيّر عرض/تخطيط المحور فقط** → استخدم `pivotTable.CalculateData();` لإعادة العرض من الذاكرة المؤقتة الموجودة دون أي عودة إلى المصدر.

يُظهر المثال التالي النمط الفعّال الجديد للمصنفات التي تحتوي على جداول محورية متعددة تتشارك ذاكرة مؤقتة واحدة.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- بناء بيانات المصدر: الفاكهة / السنة / المبلغ (ترويسة + 9 صفوف) ---
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

// --- إضافة جدول محوري أول (Pivot1) في الخلية الوجهة E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- إضافة الجدول المحوري الثاني (Pivot2) على نفس نطاق المصدر ---
// يتشارك كل من Pivot1 و Pivot2 ذاكرة تخزين مؤقت محورية واحدة أساسية.
// هذا هو بالضبط السيناريو الذي يصبح فيه نهج RefreshData() القديم لكل جدول
// غير فعّال: تحديث جدول واحد يعيد جلب كامل
// الذاكرة المشتركة، لذلك تحديث عدد N من الجداول يقوم بنفس الجلب المكلف N مرة.
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
// pivotTable1.RefreshData();  // يعيد الجلب من المصدر، يحدث كامل الذاكرة المؤقتة
// pivotTable2.RefreshData();  // يعيد الجلب مرة أخرى — الذاكرة المؤقتة حديثة بالفعل!
// كل استدعاء يعيد بناء الذاكرة المشتركة، لذلك عدد N جداول = N جلب متكرر.

// --- نمط جديد في v26.7+: تحديث الذاكرة المؤقتة مرة واحدة، ثم إعادة العرض حسب الحاجة ---
// استدعاء واحد لـ PivotCache.Refresh() يسحب القيم المعدلة إلى الذاكرة المشتركة
// ويعيد حساب عرض كل جدول محوري يشير إليها.
// ولأن Pivot1 و Pivot2 يتشاركان ذاكرة محورية واحدة، فإن هذا الاستدعاء الواحد يحدث
// كلا الجدولين — لا حاجة لذهاب وإياب ثانٍ إلى المصدر.
pivotTable1.getPivotCache().refresh();

// CalculateData() يعيد عرض عرض الجدول المحوري فقط (البيانات + النمط)
// من البيانات الموجودة بالفعل في الذاكرة المؤقتة — ولا يلمس المصدر.
// نستدعيها على Pivot2 هنا فقط لتوضيح الواجهة: بعد تحديث الذاكرة المؤقتة
// مرة واحدة، يمكن إعادة عرض أي جدول تابع دون
// العودة إلى المصدر. استخدم CalculateData() بمفردها عندما تتغير فقط
// إعدادات عرض/تخطيط الجدول المحوري وتكون الذاكرة المؤقتة حالية.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## أي واجهة تحديث يجب أن أستخدم؟

يلخّص الجدول التالي واجهات التحديث المتاحة ومتى تختار كل واحدة منها.

| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع الذواكر المؤقتة والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.RefreshPivotTables()` | مقيّدة بورقة عمل واحدة. |
| تغيّرت بيانات المصدر لذاكرة مؤقتة واحدة | `pivotTable.PivotCache.Refresh()` | يحدّث جميع الجداول المحورية على تلك الذاكرة المؤقتة المشتركة. |
| تغيّرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | يتجنّب العودة غير الضرورية إلى المصدر. |
| سرد جميع الجداول المحورية في ذاكرة مؤقتة مشتركة | `pivotCache.GetPivotTables()` | تُستخدم للتعداد قبل التحديث بالجملة. |

عمليًا، يُفضّل استخدام واجهات برمجة التطبيقات القائمة على الذاكرة المؤقتة بدلاً من `RefreshData()` المُهمَلة لكل جدول. إنها تعي بالذاكر المؤقتة المشتركة، وتتجنّب جلب المصدر بشكل متكرّر، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث لديك.

{{< app/cells/assistant language="javascript" >}}