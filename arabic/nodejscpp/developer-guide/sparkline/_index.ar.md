---
title: خطوط المؤشر في Aspose.Cells for Node.js via C++
linktitle: خطوط المؤشر في Aspose.Cells for Node.js via C++
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات، تدعم إنشاء خطوط المؤشر — وهي رسوم بيانية صغيرة تُوضع داخل خلايا ورقة العمل. يوضح هذا المقال كيفية إضافة وتخصيص خطوط المؤشر الخطية والعمودية وخطوط الفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة Node.js, جدول بيانات, خطوط المؤشر, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشر فوز/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells إنشاء خطوط المؤشر داخل خلايا ورقة العمل. خطوط المؤشر هي رسوم بيانية صغيرة الحجم تتناسب مع خلية واحدة، وتوفر تمثيلًا بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشر الخطية والعمودية وخطوط الفوز/الخسارة، ويمكن تخصيص كل منها من حيث اللون ووزن الخط ونقاط القمة/القاع والعلامات.
{{% /alert %}}

## **المقدمة**
خطوط المؤشر هي رسوم بيانية صغيرة الحجم داخل الخلية وتكون مفيدة عندما تريد عرض اتجاه سريع بجوار صف أو عمود من البيانات دون أن تستهلك مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشر: **خطية**، **عمودية**، و**فوز/خسارة**. يعكس Aspose.Cells هذه القدرة من خلال واجهات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الاسم `Aspose.Cells.Charts`.
في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه عبر `worksheet.sparklineGroups.add(...)`، والتي تُرجع كائنًا من نوع `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر ونطاق البيانات والخلية الهدف والخصائص البصرية مثل لون الخط ووزن الخط والعلامات ومؤشرات نقاط القمة/القاع.
يستعرض هذا المقال كلًا من أنواع خطوط المؤشر الثلاثة التي يدعمها Aspose.Cells — **الخطية**، **العمودية**، و**الفوز/الخسارة** — ويوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشر الخطية**
يرسم خط المؤشر الخطي خطًا متصلًا عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات عبر الزمن. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي بتمرير `SparklineType.Line` إلى طريقة `sparklineGroups.add`.
1. أنشئ `Workbook` جديدًا وانتقل إلى ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدرية (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف الخلية الهدف التي سيتم فيها رسم خط المؤشر.
4. استدعِ `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس عمودي (عمود).
5. يمكنك اختياريًا تخصيص كائن `SparklineGroup` المُعاد. لخط المؤشر الخطي، يمكنك تعيين لون الخط باستخدام `group.line.color` (الذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط وزن الخط، وتبديل علامات نقاط القمة/القاع.
6. احفظ المصنف.
يُنشئ المثال التالي مصنفًا، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يُخصص لون الخط إلى الأحمر ويُفعّل العلامات لنقطتي القمة والقاع.

```javascript
const AsposeCells = require("aspose.cells");
// الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// الخطوة 2: كتابة قيم العينة 5، -3، 8، -2، 6 في الخلايا A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// الخطوة 3: بناء CellArea يشير إلى خلية الوجهة F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // العمود F (مفهرس من 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // الصف 1 (مفهرس من 0)
dest.setEndRow(0);
// الخطوة 4: إضافة خط مؤشر مصغر من A1:E1 إلى F1
// تُرجع SparklineGroups.Add فهرس المجموعة المُضافة حديثًا
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون خط المؤشر المصغر
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// الخطوة 6: تمكين علامات النقاط العليا والدنيا
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// الخطوة 7: حفظ المصنف
workbook.save("output_line.xlsx");
```

## **خطوط المؤشر العمودية**
يعرض خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسبًا تمامًا للبيانات التي يكون فيها المقدار ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدادات. في Aspose.Cells، تُنشئ خط المؤشر العمودي بتمرير `SparklineType.Column` إلى طريقة `sparklineGroups.add`.
يتبع الإجراء مثال خط المؤشر الخطي:
1. أنشئ `Workbook` جديدًا وانتقل إلى ورقة العمل الأولى.
3. أنشئ `CellArea` يصف الخلية الهدف.
4. استدعِ `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. يمكنك اختياريًا تخصيص كائن `SparklineGroup` الناتج — على سبيل المثال، بتعيين `group.type` لتأكيد النوع، أو بضبط لون الأعمدة.
6. احفظ المصنف في ملف إخراج منفصل بحيث لا يستبدل مثال خط المؤشر الخطي.
يكتب المثال أدناه القيم 5 و-3 و8 و-2 و6 في A1:E1 ويرسم خط مؤشر عمودي في F1. تُرسم القيم السالبة كأعمدة تتجه للأسفل والقيم الموجبة كأعمدة تتجه للأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة الملاحظة بنظرة واحدة.

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
// الخطوة 4: إضافة سباركلاين عمود إلى خلية الوجهة
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// الخطوة 5: تأكيد نوع سباركلاين من خلال قراءة group.Type
console.log("Sparkline Type added: " + group.getType());
// الخطوة 6: حفظ المصنف
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **خطوط المؤشر من نوع فوز/خسارة**
خط المؤشر من نوع فوز/خسارة هو تباين خاص لخط المؤشر العمودي مصمم لإظهار نتيجتين فقط: القيمة الموجبة تُرسم كشريط "أعلى" (فوز)، والقيمة الصفرية أو السالبة تُرسم كشريط "أسفل" (خسارة). تُستخدم خطوط المؤشر من نوع فوز/خسارة بشكل شائع لتصوير تتابعات الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية عبر الزمن.
في Aspose.Cells، يُنشأ خط المؤشر من نوع فوز/خسارة بتمرير `SparklineType.Stacked` إلى طريقة `sparklineGroups.add`. (بالرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب العرض من نوع فوز/خسارة.)
1. أنشئ `Workbook` جديدًا وانتقل إلى ورقة العمل الأولى.
2. املأ نطاق البيانات المصدرية. ولأن خطوط المؤشر من نوع فوز/خسارة تتعامل مع كل قيمة إما على أنها فوز أو خسارة, فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة علوية وتصبح القيم غير الموجبة أشرطة سفلية.
3. أنشئ `CellArea` يصف الخلية الهدف.
4. استدعِ `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. يمكنك اختياريًا تخصيص كائن `SparklineGroup` المُعاد، مثل تعيين ألوان مميزة لأشرطة الفوز والخسارة.
6. احفظ المصنف باسم ملف مميز بحيث يمكن للأمثلة الثلاثة جميعها التعايش على القرص.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// الخطوة 2: تعبئة بيانات العينة في الصف 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// الخطوة 3: إنشاء CellArea تشير إلى F1 (العمود 5، الصف 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // الصف 1
dest.setEndRow(0);
// الخطوة 4: إضافة سباركلاين Win/Loss (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// الخطوة 5: تخصيص مجموعة سباركلاين
// تفعيل علامتي النقطة المرتفعة والمنخفضة
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// تعيين لون النقطة المرتفعة إلى الأخضر
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// تعيين لون النقطة المنخفضة إلى الأحمر
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// تعيين لون النقاط السالبة إلى البرتقالي
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// تعيين لون السلسلة الافتراضي (يُستخدم للأشرطة الموجبة)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// الخطوة 6: حفظ المصنف
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **دمج أنواع خطوط المؤشر الثلاثة معًا**
يُنشئ المثال المدمج أدناه مصنفًا واحدًا، ويملأ الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يُضيف ثلاث مجموعات من خطوط المؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يُظهر الملف الناتج أنماط خطوط المؤشر الثلاثة جميعها دفعة واحدة.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// الخطوة 3: إضافة مجموعة خط مؤشر أداء رئيسي عند F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// تخصيص لون خط المؤشر الرئيسي عبر CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// الخطوة 4: إضافة مجموعة عمود مؤشر أداء رئيسي عند F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// تخصيص لون سلسلة المؤشر العمودي
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// الخطوة 5: إضافة مجموعة فوز/خسارة (مكدسة) لمؤشر أداء رئيسي عند F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// تخصيص لون سلسلة مؤشر الفوز/الخسارة
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx");
```

## **تخصيص مظهر خط المؤشر**
بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.sparklineGroups`، يمكنك قراءة أو تعديل عدة خصائص بصرية له قبل حفظ المصنف. أكثر الخصائص شيوعًا في التخصيص هي:
- **`group.type`** — نوع `SparklineType` (Line أو Column أو Stacked). يُحدد عند إضافة المجموعة، ولكن يمكنك قراءته لتأكيده.
- **`group.line.color`** — لون الخط، يُعبر عنه كـ `CellsColor` يُنشأ عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون خط المؤشر الخطي.
- **`group.line.weight`** — وزن الخط بالنقاط. القيم الأكبر تنتج خطوطًا أسمك.
- **علامات نقطتي القمة/القاع** — علامات تُفعّل علامات صغيرة على نقطتي البيانات الأعلى والأدنى، وهي مفيدة لتسليط الضوء على القيم القصوى.
- **علامات النقطتين الأولى والأخيرة والسالبة** — علامات تُبدّل علامات على نقاط البيانات الأولى والأخيرة والسالبة.
لتغيير لون، أنشئ دائمًا نسخة من `CellsColor` وعيّنها إلى الخاصية ذات الصلة. لا تُعيّن `System.Drawing.Color` مباشرةً إلى خصائص لون خط المؤشر — فهي تتوقع نوع `CellsColor` من `Aspose.Cells.Drawing`. طريقة `sparklineGroups.add` نفسها تُرجع كائن `SparklineGroup` مُنوعًا بالكامل، لذا يمكنك تسلسل تعيينات الخصائص على القيمة المُعادة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.

{{< app/cells/assistant language="javascript" >}}