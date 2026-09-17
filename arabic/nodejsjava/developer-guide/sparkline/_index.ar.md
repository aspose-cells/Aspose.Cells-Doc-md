---
title: خطوط المؤشرات في Aspose.Cells for Node.js via Java
linktitle: خطوط المؤشرات في Aspose.Cells for Node.js via Java
description: Aspose.Cells هي مكتبة Node.js via Java للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط المؤشرات - رسوم بيانية مصغرة تُوضع داخل خلايا ورقة العمل. توضح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشرات الخطية والعمودية وخطوط فوز/خسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة Node.js via Java, جدول بيانات, خطوط المؤشرات, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشر فوز/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells إنشاء خطوط المؤشرات داخل خلايا ورقة العمل. خطوط المؤشرات هي رسوم بيانية مصغرة تتناسب مع خلية واحدة، وتوفر تمثيلًا بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشرات الخطية والعمودية وخطوط فوز/خسارة، ويمكن تخصيص كل منها من حيث اللون وسمك الخط ونقاط القمة/القاع والعلامات.
{{% /alert %}}

## **مقدمة**
خطوط المؤشرات هي رسوم بيانية صغيرة داخل الخلية وتكون مفيدة عندما تريد عرض اتجاه سريع بجانب صف أو عمود من البيانات دون أن تستهلك مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشرات: **خطية**، **عمودية**، و**فوز/خسارة**. يعكس Aspose.Cells هذه القدرة من خلال واجهات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الاسم `com.aspose.cells.Charts`.
في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه من خلال `worksheet.SparklineGroups.add(...)`، الذي يُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر، ونطاق البيانات، وخلية الوجهة، والخصائص المرئية مثل لون الخط، وسمك الخط، والعلامات، ومؤشرات نقاط القمة/القاع.
تستعرض هذه المقالة كل نوع من أنواع خطوط المؤشرات الثلاثة التي يدعمها Aspose.Cells — **الخطية**، **العمودية**، و**فوز/خسارة** — وتوضح كيفية إضافتها، وتخصيص ألوانها، وحفظ المصنف الناتج.

## **خطوط المؤشرات الخطية**
يرسم خط المؤشر الخطي خطًا متصلًا عبر نقاط البيانات في السلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات عبر الزمن. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي بتمرير `SparklineType.Line` إلى طريقة `SparklineGroups.add`.
1. أنشئ `Workbook` جديدًا وافتح ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدرية (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصويرها بيانيًا.
3. أنشئ `CellArea` يصف خلية الوجهة التي سيتم رسم خط المؤشرات فيها.
4. استدعِ `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يُخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس عموديًا (عمود).
5. خصص اختياريًا `SparklineGroup` المُرجع. لخط المؤشر الخطي يمكنك تعيين لون الخط باستخدام `group.Line.Color` (الذي يتوقع `CellsColor` من `com.aspose.cells.Drawing`)، وضبط سمك الخط، وتبديل علامات نقاط القمة/القاع.
6. احفظ المصنف.
ينشئ المثال التالي مصنفًا، ويكتب القيم 5، -3، 8، -2، 6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويُفعِّل علامات لنقاط القمة والقاع.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// الخطوة 2: كتابة قيم عينة 5، -3، 8، -2، 6 في الخلايا A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// الخطوة 3: بناء منطقة CellArea تشير إلى خلية الوجهة F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // العمود F (مفهرس من 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // الصف 1 (مفهرس من 0)
dest.setEndRow(0);
// الخطوة 4: إضافة سباركلاين خطي من A1:E1 إلى F1
// SparklineGroups.Add يُرجع فهرس المجموعة المُضافة حديثًا
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// الخطوة 5: إنشاء لون أحمر CellsColor وتعيينه كلون خط سباركلاين
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// الخطوة 6: تمكين علامات النقطة العالية والنقطة المنخفضة
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// الخطوة 7: حفظ المصنف
workbook.save("output_line.xlsx");
```

## **خطوط المؤشرات العمودية**
يُصير خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. هذا يجعله مناسبًا تمامًا للبيانات التي يكون لمقدارها معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدّ. في Aspose.Cells، تُنشئ خط المؤشر العمودي بتمرير `SparklineType.Column` إلى طريقة `SparklineGroups.add`.
تعكس الإجراء مثال خط المؤشر الخطي:
1. أنشئ `Workbook` جديدًا وافتح ورقة العمل الأولى.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. خصص اختياريًا `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.Type` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل بحيث لا يستبدل مثال خط المؤشرات الخطي.
يكتب المثال أدناه القيم 5، -3، 8، -2، 6 في A1:E1 ويُصير خط مؤشر عمودي في F1. تُرسم القيم السالبة كأشرطة تتجه للأسفل والقيم الموجبة كأشرطة تتجه للأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بمجرد النظر.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// الخطوة 2: كتابة قيم العينة في A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// الخطوة 3: بناء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// الخطوة 4: إضافة Column sparkline إلى خلية الوجهة
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// الخطوة 5: تأكيد نوع الـ sparkline عن طريق قراءة group.Type
console.log("Sparkline Type added: " + group.getType());
// الخطوة 6: حفظ المصنف
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **خطوط المؤشرات فوز/خسارة**
خط المؤشر فوز/خسارة هو نسخة خاصة من خط المؤشر العمودي مصممة لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "علوي" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "سفلي" (خسارة). تُستخدم خطوط المؤشرات فوز/خسارة بشكل شائع لتصوير تسلسلات من الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية عبر الزمن.
في Aspose.Cells، يتم إنشاء خط المؤشر فوز/خسارة بتمرير `SparklineType.Stacked` إلى طريقة `SparklineGroups.add`. (بالرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب التصيير الخاص بفوز/خسارة.)
1. أنشئ `Workbook` جديدًا وافتح ورقة العمل الأولى.
2. املأ نطاق المصدر. نظرًا لأن خطوط المؤشرات فوز/خسارة تتعامل مع كل قيمة كفوز أو خسارة، فإن مقدار القيمة لا يهم — بل فقط إشارتها. تصبح القيم الموجبة أشرطة علوية والقيم غير الموجبة تصبح أشرطة سفلية.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. خصص اختياريًا `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان تأكيد لأشرطة الفوز والخسارة.
6. احفظ المصنف تحت اسم ملف مميز بحيث يمكن للأمثلة الثلاثة أن تتعايش على القرص.

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
// الخطوة 3: إنشاء CellArea يشير إلى F1 (العمود 5، الصف 0)
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
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// الخطوة 5: تخصيص مجموعة سباركلاين
// تفعيل علامات النقاط العالية والمنخفضة
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// تعيين لون النقطة العالية إلى الأخضر
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// تعيين لون النقطة المنخفضة إلى الأحمر
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// تعيين لون النقطة السلبية إلى البرتقالي
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// تعيين لون السلسلة الافتراضي (يستخدم للأشرطة الإيجابية)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// الخطوة 6: حفظ المصنف
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **الجمع بين أنواع خطوط المؤشرات الثلاثة**
ينشئ المثال المجمع أدناه مصنفًا واحدًا، ويمتلئ الصف 1 بالقيم 5، -3، 8، -2، 6، ثم يضيف ثلاث مجموعات من خطوط المؤشرات في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يُظهر الملف الناتج أنماط خطوط المؤشرات الثلاثة دفعة واحدة.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// الخطوة 3: إضافة مجموعة خط مؤشر الأداء في F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// تخصيص لون خط مؤشر الأداء عبر CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// الخطوة 4: إضافة مجموعة مؤشر أداء عمودية في F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// تخصيص لون سلسلة مؤشر الأداء العمودي
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// الخطوة 5: إضافة مجموعة مؤشر أداء الفوز/الخسارة (المكدسة) في F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// تخصيص لون سلسلة مؤشر أداء الفوز/الخسارة
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx");
```

## **تخصيص مظهر خط المؤشر**
بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.SparklineGroups`، يمكنك قراءة أو تعديل عدة خصائص مرئية له قبل حفظ المصنف. الخصائص الأكثر شيوعًا في التخصيص هي:
- **`group.Type`** — الـ`SparklineType` (Line أو Column أو Stacked). يتم تعيينه عند إضافة المجموعة، لكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.Line.Color`** — لون الخط، معبرًا عنه بـ`CellsColor` تم إنشاؤه عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون ضربة خط المؤشر الخطي.
- **`group.Line.Weight`** — سمك الخط بالنقاط. القيم الأعلى تنتج خطوطًا أسمك.
- **علامات نقاط القمة/القاع** — أعلام تُفعّل علامات صغيرة على أعلى وأدنى نقاط البيانات، مفيدة للتأكيد على القيم القصوى.
- **علامات نقاط الأولى/الأخيرة/السالبة** — أعلام تُبدّل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.
لتغيير اللون، أنشئ دائمًا نسخة `CellsColor` وعيّنها إلى الخاصية ذات الصلة. لا تعيّن `java.awt.Color` مباشرة إلى خصائص لون خط المؤشر — فهي تتوقع النوع `CellsColor` من `com.aspose.cells.Drawing`. إن طريقة `SparklineGroups.add` نفسها تُرجع كائن `SparklineGroup` مكتوبًا بالكامل، بحيث يمكنك ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.

{{< app/cells/assistant language="javascript" >}}