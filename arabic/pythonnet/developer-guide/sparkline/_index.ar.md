---
title: خطوط المؤشر في Aspose.Cells for Python via .NET
linktitle: خطوط المؤشر في Aspose.Cells for Python via .NET
description: Aspose.Cells هي مكتبة Python للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط المؤشر — وهي رسوم بيانية صغيرة الحجم توضع داخل خلايا ورقة العمل. توضح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشر من النوع الخطي والعمودي والفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة Python, جدول بيانات, خطوط المؤشر, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشر فوز/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells إنشاء خطوط المؤشر داخل خلايا ورقة العمل. خطوط المؤشر هي رسوم بيانية صغيرة الحجم تتسع داخل خلية واحدة، وتوفر تمثيلاً بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشر من النوع الخطي والعمودي والفوز/الخسارة، ويمكن تخصيص كل منها من حيث اللون وسمك الخط ونقاط الارتفاع/الانخفاض والعلامات.

## **المقدمة**
خطوط المؤشر هي رسوم بيانية صغيرة داخل الخلية تكون مفيدة عندما تريد عرض اتجاه سريع بجانب صف أو عمود من البيانات دون أن تستهلك مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشر: **خطي** و**عمودي** و**فوز/خسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الأسماء `aspose.cells.charts`.
في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه من خلال `worksheet.sparkline_groups.add(...)`، والذي يُرجع كائنًا من نوع `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر، ونطاق البيانات، والخلية الوجهة، والخصائص المرئية مثل لون الخط وسمكه والعلامات ومؤشرات نقاط الارتفاع/الانخفاض.
تستعرض هذه المقالة كلًا من أنواع خطوط المؤشر الثلاثة التي يدعمها Aspose.Cells — **الخطي** و**العمودي** و**الفوز/الخسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشر الخطية**
يرسم خط المؤشر الخطي خطًا متصلًا عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات عبر الزمن. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي بتمرير `SparklineType.Line` إلى طريقة `sparkline_groups.add`.
1. أنشئ `Workbook` جديدًا واطلع على ورقة العمل الأولى.
2. املأ صفًا من بيانات المصدر (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصويرها بصريًا.
3. أنشئ `CellArea` يصف خلية الوجهة التي سيتم رسم خط المؤشر فيها.
4. استدعِ `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. تشير الوسيطة الثالثة — `False` — إلى Aspose.Cells بأن نطاق البيانات أفقي (صف) وليس رأسيًا (عمود).
5. خصص اختياريًا كائن `SparklineGroup` المُعاد. بالنسبة لخط المؤشر الخطي، يمكنك تعيين لون الخط باستخدام `group.line.color` (والذي يتوقع `CellsColor` من `aspose.cells.drawing`)، وضبط سمك الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.
يُنشئ المثال التالي مصنفًا، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويفعل علامات لنقطتي الارتفاع والانخفاض.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True
# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

## **خطوط المؤشر العمودية**
يعرض خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسبًا تمامًا للبيانات التي يكون فيها المقدار ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو التعدادات. في Aspose.Cells، تنشئ خط المؤشر العمودي بتمرير `SparklineType.Column` إلى طريقة `sparkline_groups.add`.
الإجراءات مماثلة لمثال خط المؤشر الخطي:
1. أنشئ `Workbook` جديدًا واطلع على ورقة العمل الأولى.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. خصص اختياريًا كائن `SparklineGroup` الناتج — على سبيل المثال، بتعيين `group.type` لتأكيد النوع، أو بضبط لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يستبدل مثال خط المؤشر الخطي.
يكتب المثال أدناه القيم 5 و-3 و8 و-2 و6 في A1:E1 ويعرض خط مؤشر عمودي في F1. تُرسم القيم السالبة كأشرطة تتجه للأسفل والقيم الموجبة كأشرطة تتجه للأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة واحدة.

```python
import aspose.cells as ac
# الخطوة 1: إنشاء Workbook والحصول على ورقة العمل الأولى
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# الخطوة 2: كتابة قيم عينة في A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])
# الخطوة 3: إنشاء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0
# الخطوة 4: إضافة سبارك لاين عمودية إلى خلية الوجهة
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# الخطوة 5: تأكيد نوع سبارك لاين عن طريق قراءة group.Type
print("Sparkline Type added: " + str(group.type))
# الخطوة 6: حفظ الـ workbook
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **خطوط المؤشر من نوع الفوز/خسارة**
خط مؤشر الفوز/الخسارة هو نسخة خاصة من خط المؤشر العمودي مصممة لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "لأعلى" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "لأسفل" (خسارة). تُستخدم خطوط مؤشر الفوز/الخسارة بشكل شائع لتصوير تتابعات الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية عبر الزمن.
في Aspose.Cells، يتم إنشاء خط مؤشر الفوز/الخسارة بتمرير `SparklineType.Stacked` إلى طريقة `sparkline_groups.add`. (بالرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب عرض الفوز/الخسارة.)
1. أنشئ `Workbook` جديدًا واطلع على ورقة العمل الأولى.
2. املأ نطاق المصدر. ولأن خطوط مؤشر الفوز/الخسارة تتعامل مع كل قيمة إما على أنها فوز أو خسارة، فإن مقدار القيمة لا يهم — بل يهم فقط إشارتها. تصبح القيم الموجبة أشرطة لأعلى وتصبح القيم غير الموجبة أشرطة لأسفل.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. خصص اختياريًا كائن `SparklineGroup` المُعاد، على سبيل المثال بتعيين ألوان تمييزية لأشرطة الفوز والخسارة.
6. احفظ المصنف تحت اسم ملف مميز حتى يمكن للأمثلة الثلاثة جميعها التعايش على القرص.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

## **الجمع بين أنواع خطوط المؤشر الثلاثة**
يُنشئ المثال المجمع التالي مصنفًا واحدًا، ويملأ الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يضيف ثلاث مجموعات من خطوط المؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يُظهر الملف الناتج أنماط خطوط المؤشر الثلاثة جميعها مرة واحدة.

```python
import aspose.cells as ac
import System.Drawing
# الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# الخطوة 3: إضافة مجموعة خطوط مؤشر صغيرة في F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]
# تخصيص لون خط المؤشر الصغير عبر CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color
# الخطوة 4: إضافة مجموعة أعمدة مؤشر صغيرة في F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]
# تخصيص لون سلسلة المؤشر الصغير العمودي
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color
# الخطوة 5: إضافة مجموعة مؤشر صغير للفوز/الخسارة (مكدس) في F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]
# تخصيص لون سلسلة المؤشر الصغير للفوز/الخسارة
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color
# الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx")
```

## **تخصيص مظهر خط المؤشر**
بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.sparkline_groups`، يمكنك قراءة أو تعديل عدة من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر شيوعًا في التخصيص هي:
- **`group.type`** — وهو `SparklineType` (Line أو Column أو Stacked). يُضبط عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.line.color`** — لون الخط، يُعبر عنه كـ `CellsColor` يُنشأ عبر `workbook.create_cells_color()`. هذه هي الخاصية المستخدمة لتحديد لون خط خط المؤشر الخطي.
- **`group.line.weight`** — سمك الخط بالنقاط. القيم الأعلى تُنتج خطوطًا أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تُفعّل علامات صغيرة على أعلى وأدنى نقاط البيانات، وهي مفيدة للتأكيد على القيم القصوى.
- **علامات على النقاط الأولى/الأخيرة/السالبة** — أعلام تُبدّل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.
لتغيير لون، أنشئ دائمًا نسخة `CellsColor` وعيّنها إلى الخاصية المعنية. تتوقع خصائص لون خط المؤشر نوع `CellsColor` من `aspose.cells.drawing` — لا تُسند قيمة لون خام إليها مباشرةً. تُرجع طريقة `sparkline_groups.add` نفسها كائنًا من نوع `SparklineGroup` مكتمل النوع، لذا يمكنك ربط تعيينات الخصائص على القيمة المُعادة أو تخزينها في متغير محلي وتخصيصه قبل الحفظ.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}