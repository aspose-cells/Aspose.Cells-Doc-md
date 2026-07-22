---
title: الخطوط البيانية المصغرة في Aspose.Cells for Java
linktitle: خطوط المؤشر
description: Aspose.Cells هي مكتبة Java للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط بيانية مصغرة — رسوم بيانية صغيرة موضوعة داخل خلايا أوراق العمل. تشرح هذه المقالة كيفية إضافة وتخصيص الخطوط البيانية المصغرة الخطية والعمودية وخطوط الفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة Java, جداول البيانات, خطوط بيانية مصغرة, خط بياني مصغر خطي, خط بياني مصغر عمودي, خط بياني مصغر للفوز/الخسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إنشاء خطوط بيانية مصغرة داخل خلايا أوراق العمل. الخطوط البيانية المصغرة هي رسوم بيانية صغيرة تتناسب مع خلية واحدة، وتوفر تمثيلاً بصرياً سريعاً لاتجاهات البيانات. يدعم Aspose.Cells الخطوط البيانية المصغرة الخطية والعمودية وخطوط الفوز/الخسارة، ويمكن تخصيص كل منها من حيث اللون وسمك الخط ونقاط الارتفاع/الانخفاض والعلامات.

{{% /alert %}}

## **مقدمة**

الخطوط البيانية المصغرة هي رسوم بيانية صغيرة داخل الخلايا تكون مفيدة عندما تريد عرض اتجاه سريع بجانب صف أو عمود من البيانات دون أن تشغل مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من الخطوط البيانية المصغرة: **خطية**، **عمودية**، و**فوز/خسارة**. تعكس Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الأسماء `Aspose.Cells.Charts`.

في Aspose.Cells، يتم إنشاء كل خط بياني مصغر تضيفه من خلال `worksheet.getSparklineGroups().add(...)`، التي تُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع الخط البياني المصغر ونطاق البيانات والخلية الوجهة والخصائص المرئية مثل لون الخط وسمكه والعلامات ومؤشرات نقاط الارتفاع/الانخفاض.

{{% alert color="primary" %}}

يمكن أن يحتوي `SparklineGroup` الواحد على خط بياني مصغر واحد أو أكثر تتشارك في نفس النمط. عندما تستدعي `add` وتمرر صفاً من البيانات بالإضافة إلى خلية وجهة واحدة، تحصل على خط بياني مصغر واحد داخل تلك الخلية. إذا كان نطاق الوجهة أوسع من خلية واحدة، فسيتم رسم خط بياني مصغر منفصل في كل خلية وجهة، باستخدام جميعها نفس النمط ونطاق البيانات.

{{% /alert %}}

تتناول هذه المقالة كل نوع من أنواع الخطوط البيانية المصغرة الثلاثة التي يدعمها Aspose.Cells — **خطية**، **عمودية**، و**فوز/خسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **الخطوط البيانية المصغرة الخطية**

يرسم الخط البياني المصغر الخطي خطاً متصلاً عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات عبر الزمن. في Aspose.Cells، يتم إنشاء خط بياني مصغر خطي عن طريق تمرير `SparklineType.LINE` إلى طريقة `add`.

سير العمل هو نفسه كما في أي نوع آخر من الخطوط البيانية المصغرة:

1. أنشئ `Workbook` جديداً واستخدم ورقة العمل الأولى.
2. املأ صفاً من بيانات المصدر (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم الخط البياني المصغر.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يخبر Aspose.Cells أن نطاق البيانات أفقي (صف)، وليس عمودياً (عمود).
5. اختيارياً، خصص `SparklineGroup` المُرجع. بالنسبة إلى خط بياني مصغر خطي، يمكنك تعيين لون الخط باستخدام `group.getLine().setColor(...)` (الذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط سمك الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.

ينشئ المثال التالي مصنفاً، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف خطاً بيانياً مصغراً خطياً في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويمكّن علامات نقاط الارتفاع والانخفاض.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // الخطوة 1: إنشاء Workbook والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // الخطوة 2: كتابة قيم نموذجية 5، -3، 8، -2، 6 في الخلايا A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // الخطوة 3: بناء CellArea يشير إلى خلية الوجهة F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // العمود F (مفهرس من 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // الصف 1 (مفهرس من 0)
            dest.EndRow = 0;

            // الخطوة 4: إضافة خط مؤشر sparkline من A1:E1 إلى F1
            // SparklineGroups.add يُرجع فهرس المجموعة المضافة حديثًا
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون خط الـ sparkline
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // الخطوة 6: تمكين علامات النقاط العالية والمنخفضة
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // الخطوة 7: حفظ الـ workbook
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **الخطوط البيانية المصغرة العمودية**

يُعرض الخط البياني المصغر العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسباً جداً للبيانات التي يكون مقدارها ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدادات. في Aspose.Cells، تُنشئ خطاً بيانياً مصغراً عمودياً عن طريق تمرير `SparklineType.COLUMN` إلى طريقة `add`.

يتطابق الإجراء مع مثال الخط البياني المصغر الخطي:

1. أنشئ `Workbook` جديداً واستخدم ورقة العمل الأولى.
2. املأ نطاق المصدر نفسه (A1:E1) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. اختيارياً، خصص `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.getType()` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يحل محل مثال الخط البياني المصغر الخطي.

يكتب المثال أدناه القيم 5 و-3 و8 و-2 و6 في A1:E1 ويُعرض خطاً بيانياً مصغراً عمودياً في F1. تُرسم القيم السالبة كأشرطة تتجه للأسفل والقيم الموجبة كأشرطة تتجه للأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة سريعة.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// كتابة قيم نموذجية في A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// إنشاء CellArea تشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// إضافة Sparkline عمودي إلى خلية الوجهة
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// تأكيد نوع sparkline عن طريق قراءة group.Type
System.out.println("Sparkline Type added: " + group.getType());

// حفظ المصنف
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **الخطوط البيانية المصغرة للفوز/الخسارة**

الخط البياني المصغر للفوز/الخسارة هو نوع خاص من الخط البياني المصغر العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "أعلى" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "أسفل" (خسارة). تُستخدم الخطوط البيانية المصغرة للفوز/الخسارة بشكل شائع لتصور تسلسلات الانتصارات والخسائر، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية عبر الزمن.

في Aspose.Cells، يتم إنشاء خط بياني مصغر للفوز/الخسارة عن طريق تمرير `SparklineType.STACKED` إلى طريقة `add`. (على الرغم من الاسم، فإن `SparklineType.STACKED` هو قيمة التعداد المستخدمة لطلب عرض الفوز/الخسارة.)

الإجراء هو نفسه كما في النوعين الآخرين:

1. أنشئ `Workbook` جديداً واستخدم ورقة العمل الأولى.
2. املأ نطاق المصدر. ولأن الخطوط البيانية المصغرة للفوز/الخسارة تتعامل مع كل قيمة إما على أنها فوز أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة علوية والقيم غير الموجبة تصبح أشرطة سفلية.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. اختيارياً، خصص `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان مميزة لأشرطة الفوز والخسارة.
6. احفظ المصنف تحت اسم ملف مميز بحيث يمكن للأمثلة الثلاثة جميعها التعايش على القرص.

يستخدم المثال أدناه نفس بيانات الإدخال كما في القسمين السابقين. تُفسر القيم 5 و-3 و8 و-2 و6 على أنها فوز وخسارة وفوز وخسارة وفوز — ويعكس الخط البياني المصغر المرسوم في F1 هذا النمط بالضبط.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// تعبئة بيانات نموذجية
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// بناء CellArea يشير إلى F1 (العمود 5، الصف 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// إضافة خط مؤشر Win/Loss (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// تخصيص مجموعة خط المؤشر
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// تعيين لون النقطة العالية إلى الأخضر
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// تعيين لون النقطة المنخفضة إلى الأحمر
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// تعيين لون النقطة السلبية إلى البرتقالي
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// تعيين لون السلسلة الافتراضي (يستخدم للأشرطة الموجبة)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // تقريب لـ SteelBlue
group.setSeriesColor(seriesColor);

// حفظ المصنف
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **الجمع بين أنواع الخطوط البيانية المصغرة الثلاثة**

ينتج كل من الأمثلة الثلاثة السابقة مصنفه الخاص بحيث يسهل فحص ملفات الإخراج بمعزل عن غيرها. ومع ذلك، في السيناريو الحقيقي، غالباً ما ترغب في مقارنة عدة سلاسل بيانات جنباً إلى جنب. أنظف طريقة للقيام بذلك هي وضع أكثر من مجموعة خطوط بيانية مصغرة في نفس ورقة العمل، بحيث تعرض كل مجموعة نمطاً مختلفاً.

يمكنك إضافة كائنات `SparklineGroup` متعددة إلى نفس `SparklineGroupCollection`، ويمكن لكل مجموعة استهداف خلية وجهة مختلفة أو نطاق مختلف. على سبيل المثال، يمكنك وضع خط بياني مصغر خطي في F1، وخط بياني مصغر عمودي في F2، وخط بياني مصغر للفوز/الخسارة في F3 — جميعها تقرأ من نفس بيانات المصدر في الصف 1 — بحيث يمكن للقارئ رؤية ثلاثة معالجات بصرية مختلفة لنفس الأرقام.

يُنشئ المثال المجمع أدناه مصنفاً واحداً، ويملأ الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يضيف ثلاث مجموعات خطوط بيانية مصغرة في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يوضح الملف الناتج جميع أنماط الخطوط البيانية المصغرة الثلاثة في وقت واحد.

```java
import com.aspose.cells.*;

// الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// الخطوة 3: إضافة مجموعة خطوط مؤشر الأداء عند F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// الخطوة 4: إضافة مجموعة أعمدة مؤشر الأداء عند F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Customize the column sparkline series color
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// الخطوة 5: إضافة مجموعة مؤشر الأداء للفوز/الخسارة (المكدسة) عند F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

عندما تجمع بين مجموعات خطوط بيانية مصغرة متعددة في ورقة عمل واحدة، تكون كل مجموعة مستقلة. يمكنها مشاركة نفس نطاق المصدر أو استخدام نطاقات مصدر مختلفة، ويمكن تنسيقها بشكل مستقل. وهذا يجعل من السهل بناء "لوحة معلومات" صغيرة من التصورات داخل الخلايا مباشرة داخل ورقة عمل موجودة.

{{% /alert %}}

## **تخصيص مظهر الخط البياني المصغر**

بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.getSparklineGroups()`، يمكنك قراءة أو تعديل عدة خصائص مرئية له قبل حفظ المصنف. الخصائص الأكثر شيوعاً للتخصيص هي:

- **`group.getType()`** — الـ `SparklineType` (LINE أو COLUMN أو STACKED). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.getLine().setColor(...)`** — لون الخط، معبراً عنه بـ `CellsColor` تم إنشاؤه عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون ضربة الخط البياني المصغر الخطي.
- **`group.getLine().setWeight(...)`** — سمك الخط بالنقاط. تنتج القيم الأعلى خطوطاً أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تُشغل علامات صغيرة على أعلى وأدنى نقاط البيانات، وهي مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — أعلام تبدل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.

لتغيير لون، أنشئ دائماً نسخة `CellsColor` وعينها للخاصية المعنية. لا تعين `java.awt.Color` مباشرة إلى خصائص ألوان الخط البياني المصغر — فهي تتوقع النوع `CellsColor` من `Aspose.Cells.Drawing`. طريقة `add` نفسها تُرجع كائن `SparklineGroup` مكتوباً بالكامل، لذا يمكنك ربط تعيينات الخصائص على قيمة الإرجاع أو تخزينه في متغير محلي وتخصيصه قبل الحفظ.



`java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // الخطوة 1: إنشاء Workbook والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // الخطوة 2: كتابة قيم نموذجية 5، -3، 8، -2، 6 في الخلايا A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // الخطوة 3: بناء CellArea يشير إلى خلية الوجهة F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // العمود F (مفهرس من 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // الصف 1 (مفهرس من 0)
            dest.EndRow = 0;

            // الخطوة 4: إضافة خط مؤشر sparkline من A1:E1 إلى F1
            // SparklineGroups.add يُرجع فهرس المجموعة المضافة حديثًا
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون خط الـ sparkline
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // الخطوة 6: تمكين علامات النقاط العالية والمنخفضة
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // الخطوة 7: حفظ الـ workbook
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
``java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// كتابة قيم نموذجية في A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// إنشاء CellArea تشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// إضافة Sparkline عمودي إلى خلية الوجهة
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// تأكيد نوع sparkline عن طريق قراءة group.Type
System.out.println("Sparkline Type added: " + group.getType());

// حفظ المصنف
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
``java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// تعبئة بيانات نموذجية
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// بناء CellArea يشير إلى F1 (العمود 5، الصف 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// إضافة خط مؤشر Win/Loss (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// تخصيص مجموعة خط المؤشر
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// تعيين لون النقطة العالية إلى الأخضر
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// تعيين لون النقطة المنخفضة إلى الأحمر
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// تعيين لون النقطة السلبية إلى البرتقالي
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// تعيين لون السلسلة الافتراضي (يستخدم للأشرطة الموجبة)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // تقريب لـ SteelBlue
group.setSeriesColor(seriesColor);

// حفظ المصنف
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
``java
import com.aspose.cells.*;

// الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// الخطوة 3: إضافة مجموعة خطوط مؤشر الأداء عند F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// الخطوة 4: إضافة مجموعة أعمدة مؤشر الأداء عند F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Customize the column sparkline series color
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// الخطوة 5: إضافة مجموعة مؤشر الأداء للفوز/الخسارة (المكدسة) عند F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx");
`java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // الخطوة 1: إنشاء Workbook والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // الخطوة 2: كتابة قيم نموذجية 5، -3، 8، -2، 6 في الخلايا A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // الخطوة 3: بناء CellArea يشير إلى خلية الوجهة F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // العمود F (مفهرس من 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // الصف 1 (مفهرس من 0)
            dest.EndRow = 0;

            // الخطوة 4: إضافة خط مؤشر sparkline من A1:E1 إلى F1
            // SparklineGroups.add يُرجع فهرس المجموعة المضافة حديثًا
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون خط الـ sparkline
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // الخطوة 6: تمكين علامات النقاط العالية والمنخفضة
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // الخطوة 7: حفظ الـ workbook
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// كتابة قيم نموذجية في A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// إنشاء CellArea تشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// إضافة Sparkline عمودي إلى خلية الوجهة
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// تأكيد نوع sparkline عن طريق قراءة group.Type
System.out.println("Sparkline Type added: " + group.getType());

// حفظ المصنف
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// تعبئة بيانات نموذجية
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// بناء CellArea يشير إلى F1 (العمود 5، الصف 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// إضافة خط مؤشر Win/Loss (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// تخصيص مجموعة خط المؤشر
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// تعيين لون النقطة العالية إلى الأخضر
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// تعيين لون النقطة المنخفضة إلى الأحمر
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// تعيين لون النقطة السلبية إلى البرتقالي
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// تعيين لون السلسلة الافتراضي (يستخدم للأشرطة الموجبة)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // تقريب لـ SteelBlue
group.setSeriesColor(seriesColor);

// حفظ المصنف
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");java
import com.aspose.cells.*;

// الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// الخطوة 3: إضافة مجموعة خطوط مؤشر الأداء عند F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// الخطوة 4: إضافة مجموعة أعمدة مؤشر الأداء عند F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Customize the column sparkline series color
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// الخطوة 5: إضافة مجموعة مؤشر الأداء للفوز/الخسارة (المكدسة) عند F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx");
{{% alert color="primary" %}}

عندما تجمع بين مجموعات خطوط بيانية مصغرة متعددة في ورقة عمل واحدة، تكون كل مجموعة مستقلة. يمكنها مشاركة نفس نطاق المصدر أو استخدام نطاقات مصدر مختلفة، ويمكن تنسيقها بشكل مستقل. وهذا يجعل من السهل بناء "لوحة معلومات" صغيرة من التصورات داخل الخلايا مباشرة داخل ورقة عمل موجودة.

{{% /alert %}}

## **تخصيص مظهر الخط البياني المصغر**

بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.getSparklineGroups()`، يمكنك قراءة أو تعديل عدة خصائص مرئية له قبل حفظ المصنف. الخصائص الأكثر شيوعاً للتخصيص هي:

- **`group.getType()`** — الـ `SparklineType` (LINE أو COLUMN أو STACKED). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.getLine().setColor(...)`** — لون الخط، معبراً عنه بـ `CellsColor` تم إنشاؤه عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون ضربة الخط البياني المصغر الخطي.
- **`group.getLine().setWeight(...)`** — سمك الخط بالنقاط. تنتج القيم الأعلى خطوطاً أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تُشغل علامات صغيرة على أعلى وأدنى نقاط البيانات، وهي مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — أعلام تبدل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.

لتغيير لون، أنشئ دائماً نسخة `CellsColor` وعينها للخاصية المعنية. لا تعين `java.awt.Color` مباشرة إلى خصائص ألوان الخط البياني المصغر — فهي تتوقع النوع `CellsColor` من `Aspose.Cells.Drawing`. طريقة `add` نفسها تُرجع كائن `SparklineGroup` مكتوباً بالكامل، لذا يمكنك ربط تعيينات الخصائص على قيمة الإرجاع أو تخزينه في متغير محلي وتخصيصه قبل الحفظ.



{{< app/cells/assistant language"java" >}}