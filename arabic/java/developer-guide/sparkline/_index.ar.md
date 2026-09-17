---
title: خطوط المؤشر في Aspose.Cells for Java
linktitle: خطوط المؤشر في Aspose.Cells for Java
description: Aspose.Cells هي مكتبة Java للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط المؤشر، وهي مخططات صغيرة تُوضع داخل خلايا ورقة العمل. توضح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشر الخطية والعمودية والفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة Java, جداول البيانات, خطوط المؤشر, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشر فوز/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells يدعم إنشاء خطوط المؤشر داخل خلايا ورقة العمل. خطوط المؤشر هي مخططات صغيرة الحجم تناسب خلية واحدة، وتوفر تمثيلاً بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشر الخطية والعمودية والفوز/الخسارة، ويمكن تخصيص كل منها من حيث اللون وسمك الخط ونقاط الارتفاع/الانخفاض والعلامات.

## **مقدمة**
خطوط المؤشر هي مخططات صغيرة داخل الخلية تكون مفيدة عندما تريد عرض اتجاه سريع بجوار صف أو عمود من البيانات دون أن تشغل مساحة مخطط كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشر: **خطي**، و**عمودي**، و**فوز/خسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الأسماء `Aspose.Cells.Charts`.
في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه من خلال `worksheet.getSparklineGroups().add(...)`، والذي يُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر، ونطاق البيانات، والخلية الوجهة، والخصائص المرئية مثل لون الخط وسمكه والعلامات ومؤشرات نقاط الارتفاع/الانخفاض.
تستعرض هذه المقالة كل نوع من أنواع خطوط المؤشر الثلاثة التي يدعمها Aspose.Cells — **خطي**، و**عمودي**، و**فوز/خسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشر الخطية**
يرسم خط المؤشر الخطي خطًا متصلًا عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات بمرور الوقت. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي عن طريق تمرير `SparklineType.LINE` إلى طريقة `add`.
1. أنشئ `Workbook` جديدًا وانتقل إلى ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدرية (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف الخلية الوجهة حيث سيتم رسم خط المؤشر.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. المعامل الثالث — `false` — يخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس رأسيًا (عمود).
5. خصص اختياريًا `SparklineGroup` المُرجع. لخط المؤشر الخطي يمكنك تعيين لون الخط باستخدام `group.getLine().setColor(...)` (الذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط سمك الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.
ينشئ المثال التالي مصنفًا، ويكتب القيم 5، -3، 8، -2، 6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويفعل علامات لنقاط الارتفاع والانخفاض.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();
            // الخطوة 2: كتابة قيم العينة 5، -3، 8، -2، 6 في الخلايا A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);
            // الخطوة 3: بناء CellArea يشير إلى خلية الوجهة F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // العمود F (مؤشر يبدأ من 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // الصف 1 (مؤشر يبدأ من 0)
            dest.EndRow = 0;
            // الخطوة 4: إضافة سباركلاين خطي من A1:E1 إلى F1
            // SparklineGroups.add يُرجع فهرس المجموعة المُضافة حديثًا
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون خط سباركلاين
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);
            // الخطوة 6: تمكين علامات النقطة العالية والنقطة المنخفضة
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);
            // الخطوة 7: حفظ المصنف
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **خطوط المؤشر العمودية**
يعرض خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. هذا يجعله مناسبًا تمامًا للبيانات التي يكون مقدارها ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدّ. في Aspose.Cells، يمكنك إنشاء خط المؤشر العمودي عن طريق تمرير `SparklineType.COLUMN` إلى طريقة `add`.
الإجراء يماثل مثال خط المؤشر الخطي:
1. أنشئ `Workbook` جديدًا وانتقل إلى ورقة العمل الأولى.
3. أنشئ `CellArea` يصف الخلية الوجهة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. خصص اختياريًا `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.getType()` لتأكيد النوع، أو عن طريق ضبط لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يحل محل مثال خط المؤشر الخطي.
يكتب المثال التالي القيم 5، -3، 8، -2، 6 في A1:E1 ويعرض خط مؤشر عمودي في F1. تُرسم القيم السالبة كأشرطة تتجه للأسفل والقيم الموجبة كأشرطة تتجه للأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة الملاحظة بنظرة واحدة.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// كتابة قيم نموذجية في A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// إنشاء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// إضافة مخطط عمودي إلى خلية الوجهة
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// التأكد من نوع المخطط المصغر بقراءة group.Type
System.out.println("Sparkline Type added: " + group.getType());
// حفظ المصنف
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **خطوط المؤشر للفوز/الخسارة**
خط مؤشر الفوز/الخسارة هو نوع خاص من خط المؤشر العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "صاعد" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "هابط" (خسارة). تُستخدم خطوط مؤشر الفوز/الخسارة بشكل شائع لتصوير تسلسلات الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية بمرور الوقت.
في Aspose.Cells، يتم إنشاء خط مؤشر الفوز/الخسارة عن طريق تمرير `SparklineType.STACKED` إلى طريقة `add`. (على الرغم من الاسم، فإن `SparklineType.STACKED` هي قيمة التعداد المستخدمة لطلب عرض الفوز/الخسارة.)
1. أنشئ `Workbook` جديدًا وانتقل إلى ورقة العمل الأولى.
2. املأ نطاق المصدر. نظرًا لأن خطوط مؤشر الفوز/الخسارة تعامل كل قيمة إما كفوز أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها. تصبح القيم الموجبة أشرطة صاعدة وتصبح القيم غير الموجبة أشرطة هابطة.
3. أنشئ `CellArea` يصف الخلية الوجهة.
4. استدعِ `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. خصص اختياريًا `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان تأكيد لأشرطة الفوز والخسارة.
6. احفظ المصنف باسم ملف مميز حتى تتعايش الأمثلة الثلاثة على القرص.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// ملء البيانات النموذجية
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// إنشاء CellArea يشير إلى F1 (العمود 5، الصف 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// إضافة سباركلاين فوز/خسارة (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// تخصيص مجموعة سباركلاين
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
// تعيين لون السلسلة الافتراضي (يُستخدم للأشرطة الإيجابية)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // تقريب SteelBlue
group.setSeriesColor(seriesColor);
// حفظ المصنف
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **الجمع بين أنواع خطوط المؤشر الثلاثة**
ينشئ المثال المدمج التالي مصنفًا واحدًا، ويملأ الصف 1 بالقيم 5، -3، 8، -2، 6، ثم يضيف ثلاث مجموعات خطوط مؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يوضح الملف الناتج أنماط خطوط المؤشر الثلاثة دفعة واحدة.

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
// الخطوة 3: إضافة مجموعة خط المؤشر المصغر في F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// تخصيص لون خط سلسلة المؤشر المصغر عبر CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// الخطوة 4: إضافة مجموعة عمود المؤشر المصغر في F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// تخصيص لون سلسلة عمود المؤشر المصغر
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// الخطوة 5: إضافة مجموعة فوز/خسارة (مكدسة) المؤشر المصغر في F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // إصلاح: استخدام طريقة المصنع الثابتة
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// تخصيص لون سلسلة فوز/خسارة المؤشر المصغر
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// الخطوة 6: حفظ المصنف
workbook.save("output_all.xlsx");
```

## **تخصيص مظهر خط المؤشر**
بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.getSparklineGroups()`، يمكنك قراءة أو تعديل العديد من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر شيوعًا في التخصيص هي:
- **`group.getType()`** — وهو `SparklineType` (LINE أو COLUMN أو STACKED). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.getLine().setColor(...)`** — لون الخط، معبرًا عنه بـ `CellsColor` يتم إنشاؤه عبر `workbook.createCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون ضربة خط المؤشر الخطي.
- **`group.getLine().setWeight(...)`** — سمك الخط بالنقاط. القيم الأعلى تنتج خطوطًا أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — علامات تُفعّل علامات صغيرة على أعلى وأدنى نقاط البيانات، مفيدة للتأكيد على القيم القصوى.
- **علامات نقاط البداية/النهاية/السالبة** — علامات تُبدّل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.
لتغيير اللون، أنشئ دائمًا نسخة `CellsColor` وعيّنها إلى الخاصية ذات الصلة. لا تعيّن `java.awt.Color` مباشرة إلى خصائص ألوان خطوط المؤشر — فهي تتوقع نوع `CellsColor` من `Aspose.Cells.Drawing`. طريقة `add` نفسها تُرجع كائن `SparklineGroup` مكتوبًا بالكامل، لذا يمكنك ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينه في متغير محلي وتخصيصه قبل الحفظ.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}