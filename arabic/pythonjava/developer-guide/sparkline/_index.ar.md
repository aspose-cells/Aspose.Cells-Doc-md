---
title: الرسوم البيانية المصغرة في Aspose.Cells for Python via Java
linktitle: الرسوم البيانية المصغرة في Aspose.Cells for Python via Java
description: Aspose.Cells هي مكتبة Python عبر Java للعمل مع ملفات جداول البيانات تدعم إنشاء الرسوم البيانية المصغرة، وهي رسوم بيانية صغيرة الحجم توضع داخل خلايا ورقة العمل. توضح هذه المقالة كيفية إضافة الرسوم البيانية المصغرة الخطية والعمودية والفوز/الخسارة وتخصيصها باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة Python عبر Java, جداول البيانات, الرسوم البيانية المصغرة, الرسم البياني المصغر الخطي, الرسم البياني المصغر العمودي, الرسم البياني المصغر للفوز/الخسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells يدعم إنشاء الرسوم البيانية المصغرة داخل خلايا ورقة العمل. الرسوم البيانية المصغرة هي رسوم بيانية صغيرة الحجم تتسع داخل خلية واحدة، وتوفر تمثيلاً بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells الرسوم البيانية المصغرة الخطية والعمودية والفوز/الخسارة، ويمكن تخصيص كل منها من حيث اللون ووزن الخط ونقاط الارتفاع/الانخفاض والعلامات.

## **المقدمة**
الرسوم البيانية المصغرة هي رسوم بيانية صغيرة داخل الخلايا، وهي مفيدة عندما تريد عرض اتجاه سريع بجوار صف أو عمود من البيانات دون أخذ مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من الرسوم البيانية المصغرة: **الخطية**، و**العمودية**، و**الفوز/الخسارة**. يدعم Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الأسماء `Aspose.Cells.Charts`.
في Aspose.Cells، يتم إنشاء كل رسم بياني مصغر تضيفه من خلال `worksheet.getSparklineGroups().add(...)`، والذي يُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع الرسم البياني المصغر، ونطاق البيانات، والخلية الوجهة، والخصائص المرئية مثل لون الخط، ووزن الخط، والعلامات، ومؤشرات نقاط الارتفاع/الانخفاض.
تتناول هذه المقالة كل نوع من أنواع الرسوم البيانية المصغرة الثلاثة التي يدعمها Aspose.Cells — **الخطية**، و**العمودية**، و**الفوز/الخسارة** — وتوضح كيفية إضافتها، وتخصيص ألوانها، وحفظ المصنف الناتج.

## **الرسوم البيانية المصغرة الخطية**
يرسم الرسم البياني المصغر الخطي خطًا متصلًا عبر نقاط البيانات في السلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات عبر الزمن. في Aspose.Cells، يتم إنشاء الرسم البياني المصغر الخطي بتمرير `SparklineType.LINE` إلى طريقة `add`.
1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدرية (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم الرسم البياني المصغر.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يخبر Aspose.Cells أن نطاق البيانات أفقي (صف)، وليس رأسيًا (عمود).
5. خصص اختياريًا `SparklineGroup` المُرجع. بالنسبة للرسم البياني المصغر الخطي، يمكنك ضبط لون الخط باستخدام `group.getLine().getColor()` (والذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط وزن الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.
ينشئ المثال التالي مصنفًا، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف رسمًا بيانيًا مصغرًا خطيًا في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويفعل علامات نقاط الارتفاع والانخفاض.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)
# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
jpype.shutdownJVM()
```

## **الرسوم البيانية المصغرة العمودية**
يعرض الرسم البياني المصغر العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسبًا تمامًا للبيانات التي يكون مقدارها ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدادات. في Aspose.Cells، تنشئ الرسم البياني المصغر العمودي بتمرير `SparklineType.COLUMN` إلى طريقة `add`.
يتطابق الإجراء مع مثال الرسم البياني المصغر الخطي:
1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. خصص اختياريًا `SparklineGroup` الناتج — على سبيل المثال، عن طريق ضبط `group.getType()` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يستبدل مثال الرسم البياني المصغر الخطي.
يكتب المثال التالي القيم 5 و-3 و8 و-2 و6 في A1:E1 ويعرض رسمًا بيانيًا مصغرًا عموديًا في F1. تُرسم القيم السالبة كأشرطة تتجه لأسفل والقيم الموجبة كأشرطة تتجه لأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة واحدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType
# الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# الخطوة 2: كتابة قيم نموذجية في A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])
# الخطوة 3: بناء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)
# الخطوة 4: إضافة خط Sparkline عمودي إلى خلية الوجهة
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)
# الخطوة 5: تأكيد نوع خط Sparkline عن طريق قراءة group.Type
print("Sparkline Type added: " + str(group.getType()))
# الخطوة 6: حفظ المصنف
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
jpype.shutdownJVM()
```

## **الرسوم البيانية المصغرة للفوز/الخسارة**
الرسم البياني المصغر للفوز/الخسارة هو نوع خاص من الرسم البياني المصغر العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "لأعلى" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "لأسفل" (خسارة). تُستخدم الرسوم البيانية المصغرة للفوز/الخسارة بشكل شائع لتصوير تسلسلات الانتصارات والخسائر، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية عبر الزمن.
في Aspose.Cells، يتم إنشاء الرسم البياني المصغر للفوز/الخسارة بتمرير `SparklineType.STACKED` إلى طريقة `add`. (على الرغم من الاسم، فإن `SparklineType.STACKED` هي قيمة التعداد المستخدمة لطلب عرض الفوز/الخسارة.)
1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
2. املأ نطاق المصدر. لأن الرسوم البيانية المصغرة للفوز/الخسارة تتعامل مع كل قيمة إما كفوز أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة لأعلى والقيم غير الموجبة تصبح أشرطة لأسفل.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. خصص اختياريًا `SparklineGroup` المُرجع، على سبيل المثال عن طريق ضبط ألوان التمييز لأشرطة الفوز والخسارة.
6. احفظ المصنف تحت اسم ملف مميز حتى يمكن أن تتعايش جميع الأمثلة الثلاثة على القرص.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)
# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)
# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)
# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)
# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
jpype.shutdownJVM()
```

## **دمج جميع أنواع الرسوم البيانية المصغرة الثلاثة**
ينشئ المثال المدمج التالي مصنفًا واحدًا، ويملأ الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يضيف ثلاث مجموعات من الرسوم البيانية المصغرة في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يُظهر الملف الناتج أنماط الرسوم البيانية المصغرة الثلاثة دفعة واحدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Add a Line sparkline group at F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)
# Customize the line sparkline color via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)
# Step 4: Add a Column sparkline group at F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)
# Customize the column sparkline series color
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)
# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)
# Customize the win/loss sparkline series color
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)
# Step 6: Save the workbook
workbook.save("output_all.xlsx")
jpype.shutdownJVM()
```

## **تخصيص مظهر الرسم البياني المصغر**
بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.getSparklineGroups()`، يمكنك قراءة أو تعديل عدة من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر شيوعًا في التخصيص هي:
- **`group.getType()`** — الـ `SparklineType` (LINE أو COLUMN أو STACKED). يتم ضبطه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.getLine().getColor()`** — لون الخط، معبرًا عنه كـ `CellsColor` تم إنشاؤه عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون خط الرسم البياني المصغر الخطي.
- **`group.getLine().getWeight()`** — وزن الخط بالنقاط. تنتج القيم الأعلى خطوطًا أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تشغل علامات صغيرة على أعلى وأدنى نقاط البيانات، مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — أعلام تبدل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.
لتغيير اللون، أنشئ دائمًا مثيل `CellsColor` وقم بتعيينه إلى الخاصية ذات الصلة. لا تُسند `java.awt.Color` مباشرة إلى خصائص لون الرسم البياني المصغر — فهي تتوقع نوع `CellsColor` من `Aspose.Cells.Drawing`. تُرجع طريقة `add` نفسها كائن `SparklineGroup` مكتوبًا بالكامل، حتى تتمكن من ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}