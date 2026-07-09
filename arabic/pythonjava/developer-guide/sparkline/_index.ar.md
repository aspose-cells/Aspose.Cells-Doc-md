---
title: الشرارات في Aspose.Cells for Python via Java
linktitle: Sparklines
description: Aspose.Cells for Python via Java هي مكتبة Python عبر Java للعمل مع ملفات جداول البيانات، تدعم إنشاء شرارات — وهي رسوم بيانية صغيرة الحجم تُوضع داخل خلايا ورقة العمل. توضح هذه المقالة كيفية إضافة وتخصيص شرارات الخط والعمود والفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة Python عبر Java, جدول بيانات, شرارات, شرارة خط, شرارة عمود, شرارة فوز/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إنشاء شرارات داخل خلايا ورقة العمل. الشرارات هي رسوم بيانية صغيرة الحجم تتناسب مع خلية واحدة، وتوفر تمثيلاً بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells شرارات الخط والعمود والفوز/الخسارة، ويمكن تخصيص كل منها فيما يتعلق باللون ووزن الخط ونقاط الارتفاع/الانخفاض والعلامات.

{{% /alert %}}

## **مقدمة**

الشرارات هي رسوم بيانية صغيرة داخل الخلايا تكون مفيدة عندما تريد عرض اتجاه سريع بجانب صف أو عمود من البيانات دون أن تأخذ مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من الشرارات: **الخط**، **العمود**، و**الفوز/الخسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات `SparklineGroup` و`SparklineGroupCollection` الموجودة في namespace `Aspose.Cells.Charts`.

في Aspose.Cells، يتم إنشاء كل شرارة تضيفها من خلال `worksheet.getSparklineGroups().add(...)`، والذي يُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع الشرارة، ونطاق البيانات، والخلية الوجهة، والخصائص المرئية مثل لون الخط، ووزن الخط، والعلامات، ومؤشرات نقاط الارتفاع/الانخفاض.

{{% alert color="primary" %}}

يمكن أن يحتوي `SparklineGroup` واحد على شرارة واحدة أو أكثر تشترك في نفس النمط. عندما تستدعي `add` وتمرر صفًا من البيانات بالإضافة إلى خلية وجهة واحدة، تحصل على شرارة واحدة داخل تلك الخلية. إذا كان نطاق وجهتك أوسع من خلية واحدة، فسيتم رسم شرارة منفصلة في كل خلية وجهة، باستخدام نفس النمط ونطاق البيانات.

{{% /alert %}}

تستعرض هذه المقالة كل نوع من أنواع الشرارات الثلاثة التي يدعمها Aspose.Cells — **الخط**، **العمود**، و**الفوز/الخسارة** — وتوضح كيفية إضافتها، وتخصيص ألوانها، وحفظ المصنف الناتج.

## **شرارات الخط**

ترسم شرارة الخط خطًا متصلًا عبر نقاط البيانات في سلسلة، مما يجعلها الخيار الأكثر طبيعيًا لإظهار الاتجاهات بمرور الوقت. في Aspose.Cells، يتم إنشاء شرارة الخط عن طريق تمرير `SparklineType.LINE` إلى طريقة `add`.

سير العمل هو نفسه كما هو الحال في أي نوع آخر من الشرارات:

1. أنشئ `Workbook` جديدًا واحصل على ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدرية (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم الشرارة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس رأسيًا (عمود).
5. اختياريًا، خصص `SparklineGroup` المُرجع. لشرارة الخط، يمكنك تعيين لون الخط باستخدام `group.getLine().getColor()` (والذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط وزن الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.

ينشئ المثال التالي مصنفًا، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف شرارة خط في الخلية F1 تتبع تلك القيم. كما يُخصّص لون الخط إلى الأحمر ويُفعّل العلامات لنقاط الارتفاع والانخفاض.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# الخطوة 2: كتابة قيم عينة 5، -3، 8، -2، 6 في الخلايا A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# الخطوة 3: بناء CellArea تشير إلى خلية الوجهة F1
dest = CellArea()
dest.setStartColumn(5)  # العمود F (مفهرس من 0)
dest.setEndColumn(5)
dest.setStartRow(0)     # الصف 1 (مفهرس من 0)
dest.setEndRow(0)

# الخطوة 4: إضافة خط مؤشر من A1:E1 إلى F1
# SparklineGroups.add يُرجع فهرس المجموعة المُضافة حديثًا
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون خط المؤشر
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# الخطوة 6: تمكين علامات النقاط العالية والمنخفضة
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# الخطوة 7: حفظ المصنف
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **شرارات العمود**

تُصيّر شرارة العمود كل نقطة بيانات كشريط عمودي. هذا يجعلها مناسبة تمامًا للبيانات التي يكون فيها المقدار ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدّ. في Aspose.Cells، تُنشئ شرارة العمود عن طريق تمرير `SparklineType.COLUMN` إلى طريقة `add`.

الإجراء يعكس مثال شرارة الخط:

1. أنشئ `Workbook` جديدًا واحصل على ورقة العمل الأولى.
2. املأ نفس نطاق المصدر (A1:E1) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. اختياريًا، خصص `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.getType()` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل بحيث لا يستبدل مثال شرارة الخط.

يكتب المثال أدناه القيم 5 و-3 و8 و-2 و6 في A1:E1 ويُصيّر شرارة عمود في F1. تُرسم القيم السالبة كأشرطة تتجه للأسفل والقيم الموجبة كأشرطة تتجه للأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة واحدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# الخطوة 2: كتابة قيم عينة في A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# الخطوة 3: بناء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# الخطوة 4: إضافة خط مؤشر عمودي إلى خلية الوجهة
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# الخطوة 5: تأكيد نوع خط المؤشر عن طريق قراءة group.Type
print("Sparkline Type added: " + str(group.getType()))

# الخطوة 6: حفظ المصنف
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **شرارات الفوز/الخسارة**

شرارة الفوز/الخسارة هي نوع خاص من شرارة العمود مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "صاعد" (فوز) والقيمة الصفرية أو السالبة كشريط "هابط" (خسارة). تُستخدم شرارات الفوز/الخسارة بشكل شائع لتصوير تسلسلات الانتصارات والخسائر، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية بمرور الوقت.

في Aspose.Cells، تُنشأ شرارة الفوز/الخسارة عن طريق تمرير `SparklineType.STACKED` إلى طريقة `add`. (على الرغم من الاسم، فإن `SparklineType.STACKED` هو قيمة enum المستخدمة لطلب عرض الفوز/الخسارة.)

الإجراء هو نفسه كما في النوعين الآخرين:

1. أنشئ `Workbook` جديدًا واحصل على ورقة العمل الأولى.
2. املأ نطاق المصدر. نظرًا لأن شرارات الفوز/الخسارة تعامل كل قيمة إما على أنها فوز أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها. تصبح القيم الموجبة أشرطة صاعدة والقيم غير الموجبة تصبح أشرطة هابطة.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. اختياريًا، خصص `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان بارزة لأشرطة الفوز والخسارة.
6. احفظ المصنف تحت اسم ملف مميز بحيث يمكن للأمثلة الثلاثة أن تتعايش على القرص.

يستخدم المثال أدناه نفس بيانات الإدخال كما في القسمين السابقين. تُفسر القيم 5 و-3 و8 و-2 و6 على أنها فوز وخسارة وفوز وخسارة وفوز — والشرارة المرسومة في F1 تعكس هذا النمط تمامًا.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# الخطوة 2: تعبئة بيانات نموذجية في الصف 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# الخطوة 3: بناء CellArea يشير إلى F1 (العمود 5، الصف 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # الصف 1
dest.setEndRow(0)

# الخطوة 4: إضافة سباركلاين Win/Loss (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# الخطوة 5: تخصيص مجموعة سباركلاين
# تمكين علامات النقاط العالية والمنخفضة
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# تعيين لون النقطة العالية إلى الأخضر
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# تعيين لون النقطة المنخفضة إلى الأحمر
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# تعيين لون النقطة السلبية إلى البرتقالي
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# تعيين لون السلسلة الافتراضي (المستخدم للأشرطة الموجبة)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# الخطوة 6: حفظ المصنف
workbook.save("output_winloss.xlsx")

print("تم حفظ المصنف بنجاح: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **دمج جميع أنواع الشرارات الثلاثة**

ينتج كل مثال من الأمثلة الثلاثة السابقة مصنفًا خاصًا به بحيث تكون ملفات الإخراج سهلة الفحص بمعزل عن غيرها. ومع ذلك، في سيناريو واقعي، غالبًا ما ترغب في مقارنة عدة سلاسل بيانات جنبًا إلى جنب. أنظف طريقة للقيام بذلك هي وضع أكثر من مجموعة شرارات واحدة في نفس ورقة العمل، بحيث تُصيّر كل مجموعة نمطًا مختلفًا.

يمكنك إضافة كائنات `SparklineGroup` متعددة إلى نفس `SparklineGroupCollection`، ويمكن لكل مجموعة استهداف خلية وجهة مختلفة أو نطاق مختلف. على سبيل المثال، يمكنك وضع شرارة خط في F1، وشرارة عمود في F2، وشرارة فوز/خسارة في F3 — جميعها تقرأ من نفس البيانات المصدرية في الصف 1 — بحيث يمكن للقارئ رؤية ثلاثة تمثيلات بصرية مختلفة لنفس الأرقام.

ينشئ المثال المدمج أدناه مصنفًا واحدًا، ويملى الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يضيف ثلاث مجموعات شرارات في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يُظهر الملف الناتج جميع أنماط الشرارات الثلاثة مرة واحدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# الخطوة 3: إضافة مجموعة خطوط مؤشر سباركلين في F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# تخصيص لون خط سباركلين عبر CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# الخطوة 4: إضافة مجموعة أعمدة سباركلين في F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# تخصيص لون سلسلة أعمدة سباركلين
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# الخطوة 5: إضافة مجموعة سباركلين فوز/خسارة (مكدسة) في F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# تخصيص لون سلسلة سباركلين فوز/خسارة
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # برتقالي داكن
stackedGroup.setSeriesColor(stackedColor)

# الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

عندما تدمج مجموعات شرارات متعددة في ورقة عمل واحدة، تكون كل مجموعة مستقلة. يمكنها مشاركة نفس نطاق المصدر أو استخدام نطاقات مصدر مختلفة، ويمكن تنسيقها بشكل مستقل. هذا يجعل من السهل بناء "لوحة معلومات" صغيرة من التصورات داخل الخلايا مباشرة داخل ورقة عمل موجودة.

{{% /alert %}}

## **تخصيص مظهر الشرارة**

بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.getSparklineGroups()`، يمكنك قراءة أو تعديل عدة من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر شيوعًا في التخصيص هي:

- **`group.getType()`** — نوع `SparklineType` (LINE، COLUMN، أو STACKED). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.getLine().getColor()`** — لون الخط، معبرًا عنه كـ `CellsColor` تم إنشاؤه عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون خط شرارة الخط.
- **`group.getLine().getWeight()`** — وزن الخط بالنقاط. القيم الأعلى تنتج خطوطًا أكثر سمكًا.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تُفعّل علامات صغيرة على نقاط البيانات الأعلى والأدنى، مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — أعلام تُبدّل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.

لتغيير اللون، أنشئ دائمًا مثيل `CellsColor` وعيّنه إلى الخاصية ذات الصلة. لا تُعيّن `java.awt.Color` مباشرة إلى خصائص لون الشرارة — فهي تتوقع نوع `CellsColor` من `Aspose.Cells.Drawing`. طريقة `add` نفسها تُرجع كائن `SparklineGroup` مكتوب بالكامل، بحيث يمكنك ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.



{{< app/cells/assistant language="python" >}}