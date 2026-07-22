---
title: خطوط المؤشر في Aspose.Cells for Python via .NET
linktitle: خطوط المؤشر
description: Aspose.Cells هي مكتبة Python للعمل مع ملفات جداول البيانات التي تدعم إنشاء خطوط المؤشر - وهي رسوم بيانية صغيرة الحجم توضع داخل خلايا ورقة العمل. تشرح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشر الخطية والعمودية والفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة Python, جدول بيانات, خطوط المؤشر, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشر فوز/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إنشاء خطوط المؤشر داخل خلايا ورقة العمل. خطوط المؤشر هي رسوم بيانية صغيرة الحجم تتناسب مع خلية واحدة، وتوفر تمثيلًا مرئيًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشر الخطية والعمودية والفوز/الخسارة، ويمكن تخصيص كل منها من حيث اللون وسمك الخط والنقاط العالية/المنخفضة والعلامات.

{{% /alert %}}

## **المقدمة**

خطوط المؤشر هي رسوم بيانية صغيرة داخل الخلايا تكون مفيدة عندما تريد عرض اتجاه سريع بجوار صف أو عمود من البيانات دون أن تشغل مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشر: **خطي**، و**عمودي**، و**فوز/خسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الأسماء `aspose.cells.charts`.

في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه من خلال `worksheet.sparkline_groups.add(...)`، والتي تُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر، ونطاق البيانات، والخلية الوجهة، والخصائص المرئية مثل لون الخط وسمكه والعلامات ومؤشرات النقاط العالية/المنخفضة.

{{% alert color="primary" %}}

يمكن أن يحتوي `SparklineGroup` واحد على خط مؤشر واحد أو أكثر تشترك في نفس النمط. عندما تستدعي `add` وتمرر صفًا من البيانات بالإضافة إلى خلية وجهة واحدة، تحصل على خط مؤشر واحد داخل تلك الخلية. إذا كان نطاق الوجهة أوسع من خلية واحدة، فسيتم رسم خط مؤشر منفصل في كل خلية وجهة، جميعها تستخدم نفس النمط ونطاق البيانات.

{{% /alert %}}

تستعرض هذه المقالة كل نوع من أنواع خطوط المؤشر الثلاثة التي يدعمها Aspose.Cells — **الخطي**، و**العمودي**، و**الفوز/الخسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشر الخطية**

يرسم خط المؤشر الخطي خطًا متصلًا عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات بمرور الوقت. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي عن طريق تمرير `SparklineType.Line` إلى طريقة `sparkline_groups.add`.

سير العمل هو نفسه كما في أي نوع آخر من خطوط المؤشر:

1. أنشئ `Workbook` جديدًا واطلع على ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدر (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم خط المؤشر.
4. استدعِ `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. الوسيط الثالث — `False` — يخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس رأسيًا (عمود).
5. اختياريًا، خصص كائن `SparklineGroup` المُرجع. بالنسبة لخط المؤشر الخطي، يمكنك تعيين لون الخط باستخدام `group.line.color` (والذي يتوقع `CellsColor` من `aspose.cells.drawing`)، وضبط سمك الخط، وتبديل علامات النقاط العالية/المنخفضة.
6. احفظ المصنف.

ينشئ المثال التالي مصنفًا، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويفعل علامات النقاط العالية والمنخفضة.

```python
import aspose.cells as ac
import System.Drawing

# الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# الخطوة 2: كتابة قيم عينة 5، -3، 8، -2، 6 في الخلايا A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# الخطوة 3: بناء منطقة خلايا تشير إلى خلية الوجهة F1
dest = ac.CellArea()
dest.start_column = 5   # العمود F (مفهرس من 0)
dest.end_column = 5
dest.start_row = 0      # الصف 1 (مفهرس من 0)
dest.end_row = 0

# الخطوة 4: إضافة خط مؤشر مصغر من A1:E1 إلى F1
# يُرجع SparklineGroups.Add فهرس المجموعة المضافة حديثًا
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# الخطوة 5: إنشاء CellsColor أحمر وتعيينه إلى لون خط المؤشر المصغر
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# الخطوة 6: تمكين علامات النقاط العالية والمنخفضة
group.show_high_point = True
group.show_low_point = True

# الخطوة 7: حفظ المصنف
workbook.save("output_line.xlsx")
```

## **خطوط المؤشر العمودية**

يعرض خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسبًا تمامًا للبيانات التي يكون مقدارها ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدادات. في Aspose.Cells، يمكنك إنشاء خط المؤشر العمودي عن طريق تمرير `SparklineType.Column` إلى طريقة `sparkline_groups.add`.

يتطابق الإجراء مع مثال خط المؤشر الخطي:

1. أنشئ `Workbook` جديدًا واطلع على ورقة العمل الأولى.
2. املأ نفس نطاق المصدر (A1:E1) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. اختياريًا، خصص كائن `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.type` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يستبدل مثال خط المؤشر الخطي.

يكتب المثال أدناه القيم 5 و-3 و8 و-2 و6 في A1:E1 ويعرض خط مؤشر عمودي في F1. يتم رسم القيم السالبة كأشرطة تتجه إلى الأسفل والقيم الموجبة كأشرطة تتجه إلى الأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة سريعة.

```python
import aspose.cells as ac

# الخطوة 1: إنشاء مصنف (Workbook) والحصول على ورقة العمل الأولى
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# الخطوة 2: كتابة قيم عينة في النطاق A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# الخطوة 3: إنشاء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# الخطوة 4: إضافة خط مؤشر (sparkline) عمودي إلى خلية الوجهة
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# الخطوة 5: تأكيد نوع خط المؤشر (sparkline) عن طريق قراءة group.Type
print("Sparkline Type added: " + str(group.type))

# الخطوة 6: حفظ المصنف
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **خطوط المؤشر للفوز/الخسارة**

خط مؤشر الفوز/الخسارة هو متغير خاص من خط المؤشر العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "صاعد" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "هابط" (خسارة). تُستخدم خطوط مؤشر الفوز/الخسارة بشكل شائع لتصور تسلسلات الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية بمرور الوقت.

في Aspose.Cells، يتم إنشاء خط مؤشر الفوز/الخسارة عن طريق تمرير `SparklineType.Stacked` إلى طريقة `sparkline_groups.add`. (على الرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب عرض الفوز/الخسارة.)

الإجراء هو نفسه كما في النوعين الآخرين:

1. أنشئ `Workbook` جديدًا واطلع على ورقة العمل الأولى.
2. املأ نطاق المصدر. نظرًا لأن خطوط مؤشر الفوز/الخسارة تعامل كل قيمة إما على أنها فوز أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة صاعدة والقيم غير الموجبة تصبح أشرطة هابطة.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. اختياريًا، خصص كائن `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان مميزة لأشرطة الفوز والخسارة.
6. احفظ المصنف باسم ملف مميز حتى يمكن للأمثلة الثلاثة أن تتعايش على القرص.

يستخدم المثال أدناه نفس بيانات الإدخال كما في القسمين السابقين. تُفسر القيم 5 و-3 و8 و-2 و6 على أنها فوز وخسارة وفوز وخسارة وفوز — ويعكس خط المؤشر المرسوم في F1 هذا النمط تمامًا.

```python
import aspose.cells as ac
import System.Drawing

# الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# الخطوة 2: تعبئة بيانات عينة في الصف 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# الخطوة 3: إنشاء CellArea يشير إلى F1 (العمود 5، الصف 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # الصف 1
dest.end_row = 0

# الخطوة 4: إضافة سباركلاين Win/Loss (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# الخطوة 5: تخصيص مجموعة سباركلاين
# تمكين علامات النقاط العالية والمنخفضة
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# تعيين لون النقطة العالية إلى الأخضر
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# تعيين لون النقطة المنخفضة إلى الأحمر
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# تعيين لون النقطة السلبية إلى البرتقالي
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# تعيين لون السلسلة الافتراضي (المستخدم للأشرطة الموجبة)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# الخطوة 6: حفظ المصنف
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **الجمع بين أنواع خطوط المؤشر الثلاثة**

ينتج كل مثال من الأمثلة الثلاثة السابقة مصنفًا خاصًا به بحيث يسهل فحص ملفات الإخراج بمعزل عن غيرها. ومع ذلك، في السيناريو الواقعي، غالبًا ما ترغب في مقارنة عدة سلاسل بيانات جنبًا إلى جنب. أنظف طريقة للقيام بذلك هي وضع أكثر من مجموعة خطوط مؤشر في نفس ورقة العمل، حيث تعرض كل مجموعة نمطًا مختلفًا.

يمكنك إضافة كائنات `SparklineGroup` متعددة إلى نفس `SparklineGroupCollection`، ويمكن لكل مجموعة استهداف خلية وجهة مختلفة أو نطاق مختلف. على سبيل المثال، يمكنك وضع خط مؤشر خطي في F1، وخط مؤشر عمودي في F2، وخط مؤشر فوز/خسارة في F3 — جميعها تقرأ من نفس بيانات المصدر في الصف 1 — بحيث يمكن للقارئ رؤية ثلاثة معالجات مرئية مختلفة لنفس الأرقام.

ينشئ المثال المجمع أدناه مصنفًا واحدًا، ويمأ الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يضيف ثلاث مجموعات خطوط مؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يوضح الملف الناتج أنماط خطوط المؤشر الثلاثة في وقت واحد.

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

# الخطوة 3: إضافة مجموعة سباركلاين خطية في F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# تخصيص لون سباركلاين الخطي عبر CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# الخطوة 4: إضافة مجموعة سباركلاين عمودية في F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# تخصيص لون سلسلة سباركلاين العمودية
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# الخطوة 5: إضافة مجموعة سباركلاين فوز/خسارة (مكدسة) في F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# تخصيص لون سلسلة سباركلاين الفوز/الخسارة
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

عندما تجمع بين مجموعات خطوط مؤشر متعددة في ورقة عمل واحدة، تكون كل مجموعة مستقلة. يمكنها مشاركة نفس نطاق المصدر أو استخدام نطاقات مصدر مختلفة، ويمكن تصميمها بشكل مستقل. وهذا يجعل من السهل إنشاء "لوحة معلومات" صغيرة من التصورات داخل الخلايا مباشرة داخل ورقة عمل موجودة.

{{% /alert %}}

## **تخصيص مظهر خط المؤشر**

بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.sparkline_groups`، يمكنك قراءة أو تعديل العديد من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر شيوعًا للتخصيص هي:

- **`group.type`** — `SparklineType` (خطي، أو عمودي، أو مكدس). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.line.color`** — لون الخط، معبرًا عنه بـ `CellsColor` تم إنشاؤه عبر `workbook.create_cells_color()`. هذه هي الخاصية التي يجب استخدامها للون ضربة خط المؤشر الخطي.
- **`group.line.weight`** — سمك الخط بالنقاط. تنتج القيم الأعلى خطوطًا أسمك.
- **علامات النقاط العالية/المنخفضة** — علامات تعمل على تشغيل علامات صغيرة على أعلى وأدنى نقاط البيانات، مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — علامات تعمل على تبديل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.

لتغيير اللون، أنشئ دائمًا نسخة `CellsColor` وقم بتعيينها إلى الخاصية ذات الصلة. تتوقع خصائص لون خط المؤشر النوع `CellsColor` من `aspose.cells.drawing` — لا تعين قيمة لون خام مباشرة إليها. طريقة `sparkline_groups.add` نفسها تُرجع كائن `SparklineGroup` مكتوبًا بالكامل، حتى تتمكن من ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.



{{< app/cells/assistant language="python" >}}