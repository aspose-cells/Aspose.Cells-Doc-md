---
title: مخططات Sparklines في Aspose.Cells لـ Aspose.Cells for Node.js via Java
linktitle: خطوط المؤشر
description: Aspose.Cells هي مكتبة Node.js via Java للعمل مع ملفات جداول البيانات تدعم إنشاء مخططات Sparklines — وهي مخططات مصغرة تُوضع داخل خلايا ورقة العمل. تشرح هذه المقالة كيفية إضافة وتخصيص مخططات Sparklines الخطية والعمودية والفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, Node.js via Java library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إنشاء مخططات Sparklines داخل خلايا ورقة العمل. تعد مخططات Sparklines مخططات مصغرة تتناسب مع خلية واحدة، وتوفر تمثيلاً بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells مخططات Sparklines الخطية والعمودية ومخططات الفوز/الخسارة، ويمكن تخصيص كل منها من حيث اللون ووزن الخط ونقاط الارتفاع/الانخفاض والعلامات.

{{% /alert %}}

## **المقدمة**

مخططات Sparklines هي مخططات صغيرة داخل الخلية تكون مفيدة عندما تريد عرض اتجاه سريع بجوار صف أو عمود من البيانات دون أن تشغل مساحة مخطط كامل. يدعم Excel ثلاثة أنواع من مخططات Sparklines: **خطية**، **عمودية**، و**فوز/خسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الاسم `com.aspose.cells.Charts`.

في Aspose.Cells، يتم إنشاء كل مخطط Sparkline تضيفه من خلال `worksheet.SparklineGroups.add(...)`، والذي يُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع المخطط ونطاق البيانات والخلية الوجهة والخصائص المرئية مثل لون الخط ووزن الخط والعلامات ومؤشرات نقاط الارتفاع/الانخفاض.

{{% alert color="primary" %}}

يمكن أن يحتوي `SparklineGroup` واحد على مخطط Sparkline واحد أو أكثر تشترك في نفس النمط. عندما تستدعي `add` وتمرر صفًا من البيانات بالإضافة إلى خلية وجهة واحدة، تحصل على مخطط Sparkline واحد داخل تلك الخلية. إذا كان نطاق الوجهة الخاص بك أعرض من خلية واحدة، فسيتم رسم مخطط Sparkline منفصل في كل خلية وجهة، جميعها باستخدام نفس النمط ونطاق البيانات.

{{% /alert %}}

تستعرض هذه المقالة كل نوع من أنواع مخططات Sparklines الثلاثة التي يدعمها Aspose.Cells — **الخطية**، **العمودية**، و**الفوز/الخسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **مخططات Sparklines الخطية**

يرسم مخطط Sparkline الخطي خطًا متصلاً عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات بمرور الوقت. في Aspose.Cells، يتم إنشاء مخطط Sparkline الخطي عن طريق تمرير `SparklineType.Line` إلى طريقة `SparklineGroups.add`.

سير العمل هو نفسه كما في أي نوع آخر من مخططات Sparklines:

1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدرية (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم مخطط Sparkline.
4. استدعِ `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس عموديًا (عمود).
5. اختياريًا، خصص `SparklineGroup` المُرجع. بالنسبة لمخطط Sparkline الخطي، يمكنك تعيين لون الخط باستخدام `group.Line.Color` (والذي يتوقع `CellsColor` من `com.aspose.cells.Drawing`)، وضبط وزن الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.

ينشئ المثال التالي مصنفًا، ويكتب القيم 5، -3، 8، -2، 6 في الخلايا من A1 إلى E1، ويضيف مخطط Sparkline خطي في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويمكّن العلامات لنقطتي الارتفاع والانخفاض.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// الخطوة 2: كتابة القيم النموذجية 5, -3, 8, -2, 6 في الخلايا A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// الخطوة 3: إنشاء CellArea يشير إلى خلية الوجهة F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // العمود F (مفهرس من 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // الصف 1 (مفهرس من 0)
dest.setEndRow(0);

// الخطوة 4: إضافة خط اتجاه (Sparkline) من A1:E1 إلى F1
// SparklineGroups.Add يُرجع فهرس المجموعة المُضافة حديثاً
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون لخط الاتجاه
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// الخطوة 6: تفعيل علامات النقطة العليا والنقطة الدنيا
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// الخطوة 7: حفظ المصنف
workbook.save("output_line.xlsx");
```

## **مخططات Sparklines العمودية**

يعرض مخطط Sparkline العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسبًا تمامًا للبيانات التي يكون فيها المقدار ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو التعدادات. في Aspose.Cells، يمكنك إنشاء مخطط Sparkline عمودي عن طريق تمرير `SparklineType.Column` إلى طريقة `SparklineGroups.add`.

الإجراء يعكس مثال مخطط Sparkline الخطي:

1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
2. املأ نطاق المصدر نفسه (A1:E1) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. اختياريًا، خصص `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.Type` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يستبدل مثال مخطط Sparkline الخطي.

يكتب المثال أدناه القيم 5، -3، 8، -2، 6 في A1:E1 ويعرض مخطط Sparkline عمودي في F1. تُرسم القيم السالبة كأشرطة تتجه لأسفل والقيم الموجبة كأشرطة تتجه لأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة سريعة.

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

// الخطوة 4: إضافة مخطط مصغر عمودي إلى خلية الوجهة
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// الخطوة 5: تأكيد نوع المخطط المصغر بقراءة group.Type
console.log("Sparkline Type added: " + group.getType());

// الخطوة 6: حفظ المصنف
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **مخططات Sparklines للفوز/الخسارة**

مخطط Sparkline للفوز/الخسارة هو متغير خاص من مخطط Sparkline العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "لأعلى" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "لأسفل" (خسارة). تُستخدم مخططات Sparklines للفوز/الخسارة بشكل شائع لتصور تتابعات الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية بمرور الوقت.

في Aspose.Cells، يتم إنشاء مخطط Sparkline للفوز/الخسارة عن طريق تمرير `SparklineType.Stacked` إلى طريقة `SparklineGroups.add`. (على الرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب عرض الفوز/الخسارة.)

الإجراء هو نفسه كما في النوعين الآخرين:

1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
2. املأ نطاق المصدر. نظرًا لأن مخططات Sparklines للفوز/الخسارة تعامل كل قيمة إما على أنها فوز أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة لأعلى والقيم غير الموجبة تصبح أشرطة لأسفل.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. اختياريًا، خصص `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان مميزة لأشرطة الفوز والخسارة.
6. احفظ المصنف تحت اسم ملف مميز بحيث يمكن أن تتعايش الأمثلة الثلاثة على القرص.

يستخدم المثال أدناه نفس بيانات الإدخال كالقسمين السابقين. تُفسر القيم 5، -3، 8، -2، 6 على أنها فوز، خسارة، فوز، خسارة، فوز — ويعكس مخطط Sparkline المرسوم في F1 هذا النمط تمامًا.

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

// الخطوة 4: إضافة خط مؤشر الفوز/الخسارة (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// الخطوة 5: تخصيص مجموعة خط المؤشر
// تمكين علامات النقاط العالية والمنخفضة
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

// تعيين لون السلسلة الافتراضي (مستخدم للأعمدة الموجبة)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// الخطوة 6: حفظ المصنف
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **الجمع بين أنواع مخططات Sparklines الثلاثة**

ينتج كل مثال من الأمثلة الثلاثة السابقة مصنفًا خاصًا به بحيث يسهل فحص ملفات الإخراج بشكل منفصل. ومع ذلك، في سيناريو العالم الحقيقي، غالبًا ما ترغب في مقارنة عدة سلاسل بيانات جنبًا إلى جنب. أنظف طريقة للقيام بذلك هي وضع أكثر من مجموعة مخططات Sparkline في ورقة العمل نفسها، حيث تقوم كل مجموعة بعرض نمط مختلف.

يمكنك إضافة كائنات `SparklineGroup` متعددة إلى نفس `SparklineGroupCollection`، ويمكن لكل مجموعة استهداف خلية وجهة مختلفة أو نطاق مختلف. على سبيل المثال، يمكنك وضع مخطط Sparkline خطي في F1، ومخطط Sparkline عمودي في F2، ومخطط Sparkline للفوز/الخسارة في F3 — جميعها تقرأ من نفس بيانات المصدر في الصف 1 — حتى يتمكن القارئ من رؤية ثلاثة معالجات بصرية مختلفة لنفس الأرقام.

ينشئ المثال المدمج أدناه مصنفًا واحدًا، ويمأ الصف 1 بالقيم 5، -3، 8، -2، 6، ثم يضيف ثلاث مجموعات من مخططات Sparklines في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يوضح الملف الناتج جميع أنماط مخططات Sparklines الثلاثة دفعة واحدة.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// الخطوة 2: ملء بيانات تجريبية في الصف 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// الخطوة 3: إضافة مجموعة خط مؤشر أداء في F1
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

// الخطوة 4: إضافة مجموعة عمود مؤشر أداء في F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// تخصيص لون سلسلة عمود مؤشر الأداء
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// الخطوة 5: إضافة مجموعة مؤشر أداء فوز/خسارة (مكدس) في F3
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

{{% alert color="primary" %}}

عندما تجمع بين مجموعات متعددة من مخططات Sparklines في ورقة عمل واحدة، تكون كل مجموعة مستقلة. يمكنها مشاركة نفس نطاق المصدر أو استخدام نطاقات مصدر مختلفة، ويمكن تنسيقها بشكل مستقل. وهذا يجعل من السهل بناء "لوحة معلومات" صغيرة من التصورات داخل الخلية مباشرة داخل ورقة عمل موجودة.

{{% /alert %}}

## **تخصيص مظهر مخطط Sparkline**

بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.SparklineGroups`، يمكنك قراءة أو تعديل عدة خصائص مرئية له قبل حفظ المصنف. الخصائص الأكثر تخصيصًا شيوعًا هي:

- **`group.Type`** — نوع `SparklineType` (خطي، عمودي، أو مكدس). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.Line.Color`** — لون الخط، معبرًا عنه بـ `CellsColor` تم إنشاؤه عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون خط مخطط Sparkline الخطي.
- **`group.Line.Weight`** — وزن الخط بالنقاط. تنتج القيم الأعلى خطوطًا أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تُشغّل علامات صغيرة على أعلى وأدنى نقاط البيانات، وهي مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — أعلام تُبدّل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.

لتغيير لون، أنشئ دائمًا مثيلًا من `CellsColor` وقم بتعيينه إلى الخاصية ذات الصلة. لا تقم بتعيين `java.awt.Color` مباشرةً إلى خصائص لون مخطط Sparkline — فهي تتوقع نوع `CellsColor` من `com.aspose.cells.Drawing`. طريقة `SparklineGroups.add` نفسها تُرجع كائن `SparklineGroup` مكتوبًا بالكامل، حتى تتمكن من ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.



{{< app/cells/assistant language="javascript" >}}