---
title: خطوط المؤشر في Aspose.Cells for Node.js via C++
linktitle: خطوط المؤشر
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط المؤشر (Sparklines) — وهي رسوم بيانية مصغرة تُوضع داخل خلايا ورقة العمل. تشرح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشر الخطية والعمودية وفوز/خسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, Node.js library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إنشاء خطوط المؤشر داخل خلايا ورقة العمل. خطوط المؤشر هي رسوم بيانية مصغرة تتناسب مع خلية واحدة، وتوفر تمثيلاً بصرياً سريعاً لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشر الخطية والعمودية وفوز/خسارة، ويمكن تخصيص كل منها من حيث اللون وسمك الخط ونقاط الأعلى/الأدنى والعلامات.

{{% /alert %}}

## **مقدمة**

خطوط المؤشر هي رسوم بيانية صغيرة داخل الخلية تكون مفيدة عندما تريد عرض اتجاه سريع بجانب صف أو عمود من البيانات دون أن تأخذ مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشر: **خطية**، **عمودية**، و**فوز/خسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الأسماء `Aspose.Cells.Charts`.

في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه من خلال `worksheet.sparklineGroups.add(...)`، والذي يُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر، ونطاق البيانات، والخلية الوجهة، والخصائص المرئية مثل لون الخط وسمكه والعلامات ومؤشرات نقاط الأعلى/الأدنى.

{{% alert color="primary" %}}

يمكن أن يحتوي `SparklineGroup` واحد على خط مؤشر واحد أو أكثر تشترك في نفس النمط. عندما تستدعي `add` وتمرر صفاً من البيانات بالإضافة إلى خلية وجهة واحدة، تحصل على خط مؤشر واحد داخل تلك الخلية. إذا كان نطاق الوجهة أعرض من خلية واحدة، فسيتم رسم خط مؤشر منفصل في كل خلية وجهة، جميعها تستخدم نفس النمط ونطاق البيانات.

{{% /alert %}}

تتناول هذه المقالة كل نوع من أنواع خطوط المؤشر الثلاثة التي يدعمها Aspose.Cells — **خطي**، **عمودي**، و**فوز/خسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشر الخطية**

يرسم خط المؤشر الخطي خطاً متصلاً عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات بمرور الوقت. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي عن طريق تمرير `SparklineType.Line` إلى طريقة `sparklineGroups.add`.

سير العمل هو نفسه كما في أي نوع آخر من خطوط المؤشر:

1. أنشئ `Workbook` جديداً ووصل إلى ورقة العمل الأولى.
2. املأ صفاً من بيانات المصدر (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم خط المؤشر.
4. استدعِ `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يخبر Aspose.Cells أن نطاق البيانات أفقي (صف)، وليس عمودياً (عمود).
5. اختيارياً، خصص كائن `SparklineGroup` المُرجع. لخط المؤشر الخطي، يمكنك تعيين لون الخط باستخدام `group.line.color` (الذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط سمك الخط، وتبديل علامات نقاط الأعلى/الأدنى.
6. احفظ المصنف.

ينشئ المثال التالي مصنفاً، ويكتب القيم 5، -3، 8، -2، 6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويُفعّل العلامات للنقاط الأعلى والأدنى.

```javascript
const AsposeCells = require("aspose.cells");

// الخطوة 1: إنشاء مصنف (Workbook) والحصول على أول ورقة عمل
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// الخطوة 2: كتابة القيم النموذجية 5, -3, 8, -2, 6 في الخلايا A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// الخطوة 3: إنشاء CellArea يشير إلى خلية الوجهة F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // العمود F (مفهرس من 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // الصف 1 (مفهرس من 0)
dest.setEndRow(0);

// الخطوة 4: إضافة سباركلاين خطي من A1:E1 إلى F1
// يقوم SparklineGroups.Add بإرجاع فهرس المجموعة المضافة حديثًا
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);

// الخطوة 5: إنشاء لون خلايا أحمر وتعيينه كلون لخط السباركلاين
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// الخطوة 6: تفعيل علامات النقطة العالية والنقطة المنخفضة
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// الخطوة 7: حفظ المصنف
workbook.save("output_line.xlsx");
```

## **خطوط المؤشر العمودية**

يُقدم خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسباً تماماً للبيانات التي يكون مقدارها ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدادات. في Aspose.Cells، تنشئ خط المؤشر العمودي عن طريق تمرير `SparklineType.Column` إلى طريقة `sparklineGroups.add`.

يتطابق الإجراء مع مثال خط المؤشر الخطي:

1. أنشئ `Workbook` جديداً ووصل إلى ورقة العمل الأولى.
2. املأ نطاق المصدر نفسه (A1:E1) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. اختيارياً، خصص كائن `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.type` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يستبدل مثال خط المؤشر الخطي.

يكتب المثال أدناه القيم 5، -3، 8، -2، 6 في A1:E1 ويُقدم خط مؤشر عمودي في F1. تُرسم القيم السالبة كأشرطة تتجه للأسفل والقيم الموجبة كأشرطة تتجه للأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة سريعة.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// الخطوة 2: كتابة قيم عينة في A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// الخطوة 3: إنشاء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// الخطوة 4: إضافة مخطط بياني عمودي إلى خلية الوجهة
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// الخطوة 5: تأكيد نوع المخطط البياني عن طريق قراءة group.Type
console.log("Sparkline Type added: " + group.getType());

// الخطوة 6: حفظ المصنف
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **خطوط المؤشر فوز/خسارة**

خط المؤشر فوز/خسارة هو نسخة خاصة من خط المؤشر العمودي مصممة لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "أعلى" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "أسفل" (خسارة). تُستخدم خطوط المؤشر فوز/خسارة بشكل شائع لتصور سلاسل الفوز والخسارة ونتائج النجاح/الفشل أو أي نتيجة ثنائية بمرور الوقت.

في Aspose.Cells، يتم إنشاء خط المؤشر فوز/خسارة عن طريق تمرير `SparklineType.Stacked` إلى طريقة `sparklineGroups.add`. (على الرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب العرض فوز/خسارة.)

الإجراء هو نفسه كما في النوعين الآخرين:

1. أنشئ `Workbook` جديداً ووصل إلى ورقة العمل الأولى.
2. املأ نطاق المصدر. نظراً لأن خطوط المؤشر فوز/خسارة تعامل كل قيمة إما كفوز أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة علوية والقيم غير الموجبة تصبح أشرطة سفلية.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. اختيارياً، خصص كائن `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان تأكيد لأشرطة الفوز والخسارة.
6. احفظ المصنف تحت اسم ملف مميز حتى يمكن أن تتعايش الأمثلة الثلاثة على القرص.

يستخدم المثال أدناه نفس بيانات الإدخال كما في القسمين السابقين. تُفسر القيم 5، -3، 8، -2، 6 على أنها فوز، خسارة، فوز، خسارة، فوز — ويعكس خط المؤشر المرسوم في F1 هذا النمط بالضبط.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// الخطوة 2: تعبئة بيانات تجريبية في الصف 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// الخطوة 3: إنشاء CellArea يشير إلى F1 (العمود 5، الصف 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // الصف 1
dest.setEndRow(0);

// الخطوة 4: إضافة خط مؤثر Win/Loss (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);

// الخطوة 5: تخصيص مجموعة الخطوط المؤثرة
// تمكين علامات النقاط العالية والمنخفضة
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// تعيين لون النقطة العالية إلى الأخضر
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);

// تعيين لون النقطة المنخفضة إلى الأحمر
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);

// تعيين لون النقطة السلبية إلى البرتقالي
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);

// تعيين لون السلسلة الافتراضي (يستخدم للأشرطة الإيجابية)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// الخطوة 6: حفظ المصنف
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **الجمع بين أنواع خطوط المؤشر الثلاثة**

ينتج كل من الأمثلة الثلاثة السابقة مصنفه الخاص بحيث تكون ملفات الإخراج سهلة الفحص بمعزل عن غيرها. ومع ذلك، في سيناريو العالم الحقيقي، غالباً ما ترغب في مقارنة عدة سلاسل بيانات جنباً إلى جنب. إن أنظف طريقة للقيام بذلك هي وضع أكثر من مجموعة خطوط مؤشر واحدة في نفس ورقة العمل، بحيث تُقدم كل مجموعة نمطاً مختلفاً.

يمكنك إضافة كائنات `SparklineGroup` متعددة إلى نفس `SparklineGroupCollection`، ويمكن أن تستهدف كل مجموعة خلية وجهة مختلفة أو نطاقاً مختلفاً. على سبيل المثال، يمكنك وضع خط مؤشر خطي في F1، وخط مؤشر عمودي في F2، وخط مؤشر فوز/خسارة في F3 — جميعها تقرأ من نفس بيانات المصدر في الصف 1 — حتى يتمكن القارئ من رؤية ثلاثة معالجات بصرية مختلفة لنفس الأرقام.

ينشئ المثال المدمج أدناه مصنفاً واحداً، ويملأ الصف 1 بالقيم 5، -3، 8، -2، 6، ثم يضيف ثلاث مجموعات خطوط مؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يُظهر الملف الناتج جميع أنماط خطوط المؤشر الثلاثة دفعة واحدة.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// الخطوة 3: إضافة مجموعة سباركلاين خطية في F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// تخصيص لون سباركلاين الخطي عبر CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// الخطوة 4: إضافة مجموعة سباركلاين عمودية في F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// تخصيص لون سلسلة سباركلاين العمودية
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// الخطوة 5: إضافة مجموعة سباركلاين فوز/خسارة (مكدسة) في F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// تخصيص لون سلسلة سباركلاين فوز/خسارة
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

عندما تجمع بين مجموعات خطوط مؤشر متعددة في ورقة عمل واحدة، تكون كل مجموعة مستقلة. يمكنها مشاركة نفس نطاق المصدر أو استخدام نطاقات مصدر مختلفة، ويمكن تنسيقها بشكل مستقل. وهذا يجعل من السهل بناء "لوحة معلومات" صغيرة من التصورات داخل الخلية مباشرة داخل ورقة عمل موجودة.

{{% /alert %}}

## **تخصيص مظهر خط المؤشر**

بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.sparklineGroups`، يمكنك قراءة أو تعديل عدة من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر شيوعاً التي يتم تخصيصها هي:

- **`group.type`** — نوع `SparklineType` (Line، أو Column، أو Stacked). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.line.color`** — لون الخط، معبراً عنه بـ `CellsColor` تم إنشاؤه عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون خط المؤشر الخطي.
- **`group.line.weight`** — سمك الخط بالنقاط. تنتج القيم الأعلى خطوطاً أسمك.
- **علامات نقاط الأعلى/الأدنى** — أعلام تُشغل علامات صغيرة على أعلى وأدنى نقاط البيانات، مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — أعلام تُبدل علامات على نقاط البيانات الأولى والأخيرة والسالبة.

لتغيير اللون، أنشئ دائماً نسخة `CellsColor` وقم بتعيينها إلى الخاصية ذات الصلة. لا تُسند `System.Drawing.Color` مباشرةً إلى خصائص لون خط المؤشر — فهي تتوقع النوع `CellsColor` من `Aspose.Cells.Drawing`. طريقة `sparklineGroups.add` نفسها تُرجع كائن `SparklineGroup` مُعرَّف النوع بالكامل، بحيث يمكنك ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.



{{< app/cells/assistant language="javascript" >}}