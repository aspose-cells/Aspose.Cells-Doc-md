---
title: خطوط المؤشر في Aspose.Cells for .NET
linktitle: خطوط المؤشر
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط المؤشر — وهي رسوم بيانية مصغرة تُوضع داخل خلايا ورقة العمل. تشرح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشر من النوع الخطي والعمودي والفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة .NET, جدول بيانات, خطوط المؤشر, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشر فوز/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إنشاء خطوط المؤشر داخل خلايا ورقة العمل. خطوط المؤشر هي رسوم بيانية مصغرة تتناسب مع خلية واحدة، وتوفر تمثيلاً بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشر من النوع الخطي والعمودي والفوز/الخسارة، ويمكن تخصيص كل منها فيما يتعلق باللون ووزن الخط ونقاط الارتفاع/الانخفاض والعلامات.

{{% /alert %}}

## **المقدمة**

خطوط المؤشر هي رسوم بيانية صغيرة داخل الخلايا وتكون مفيدة عندما تريد عرض اتجاه سريع بجوار صف أو عمود من البيانات دون أن تأخذ مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشر: **خطي** و**عمودي** و**فوز/خسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات `SparklineGroup` و`SparklineGroupCollection` API الموجودة في مساحة الاسم `Aspose.Cells.Charts`.

في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه من خلال `worksheet.SparklineGroups.Add(...)`، والتي تُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر، ونطاق البيانات، والخلية الوجهة، والخصائص المرئية مثل لون الخط ووزن الخط والعلامات ومؤشرات نقاط الارتفاع/الانخفاض.

{{% alert color="primary" %}}

يمكن أن يحتوي `SparklineGroup` واحد على خط مؤشر واحد أو أكثر تتشارك في نفس النمط. عندما تستدعي `Add` وتمرر صفًا من البيانات بالإضافة إلى خلية وجهة واحدة، تحصل على خط مؤشر واحد داخل تلك الخلية. إذا كان نطاق وجهتك أعرض من خلية واحدة، فسيتم رسم خط مؤشر منفصل في كل خلية وجهة، جميعها تستخدم نفس النمط ونطاق البيانات.

{{% /alert %}}

تستعرض هذه المقالة كل نوع من أنواع خطوط المؤشر الثلاثة التي يدعمها Aspose.Cells — **خطي** و**عمودي** و**فوز/خسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشر الخطية**

يرسم خط المؤشر الخطي خطًا متصلًا عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات عبر الزمن. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي عن طريق تمرير `SparklineType.Line` إلى طريقة `SparklineGroups.Add`.

سير العمل هو نفسه كما في أي نوع آخر من خطوط المؤشر:

1. أنشئ `Workbook` جديدًا وادخل إلى ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدرية (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم خط المؤشر.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس رأسيًا (عمود).
5. اختياريًا، خصّص كائن `SparklineGroup` المُرجع. لخط المؤشر الخطي يمكنك تعيين لون الخط باستخدام `group.Line.Color` (الذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط وزن الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.

ينشئ المثال التالي مصنفًا، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويفعل العلامات لنقاط الارتفاع والانخفاض.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;

            // الخطوة 2: كتابة القيم النموذجية 5, -3, 8, -2, 6 في الخلايا A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);

            // الخطوة 3: إنشاء CellArea يشير إلى الخلية المستهدفة F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // العمود F (مفهرس من 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // الصف 1 (مفهرس من 0)
            dest.EndRow = 0;

            // الخطوة 4: إضافة خط Sparkline من A1:E1 إلى F1
            // تقوم SparklineGroups.Add بإرجاع فهرس المجموعة المضافة حديثاً
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // الخطوة 5: إنشاء CellsColor باللون الأحمر وتعيينه كلون لخط الـ Sparkline
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // الخطوة 6: تمكين علامات النقطة العالية والنقطة المنخفضة
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;

            // الخطوة 7: حفظ المصنف
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **خطوط المؤشر العمودية**

يعرض خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. هذا يجعله مناسبًا تمامًا للبيانات التي يكون مقدارها ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو التعدادات. في Aspose.Cells، يمكنك إنشاء خط المؤشر العمودي عن طريق تمرير `SparklineType.Column` إلى طريقة `SparklineGroups.Add`.

الإجراء يعكس مثال خط المؤشر الخطي:

1. أنشئ `Workbook` جديدًا وادخل إلى ورقة العمل الأولى.
2. املأ نفس نطاق المصدر (A1:E1) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. اختياريًا، خصّص كائن `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.Type` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يستبدل مثال خط المؤشر الخطي.

يكتب المثال أدناه القيم 5 و-3 و8 و-2 و6 في A1:E1 ويعرض خط مؤشر عمودي في F1. تُرسم القيم السالبة كأشرطة تتجه لأسفل والقيم الموجبة كأشرطة تتجه لأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز لمحة.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];

            // الخطوة 2: كتابة قيم عينة في A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }

            // الخطوة 3: إنشاء CellArea تشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;

            // الخطوة 4: إضافة خط مؤشر عمودي إلى خلية الوجهة
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];

            // الخطوة 5: تأكيد نوع خط المؤشر عن طريق قراءة group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);

            // الخطوة 6: حفظ المصنف
            workbook.Save("output_column.xlsx");

            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **خطوط المؤشر للفوز/الخسارة**

خط المؤشر للفوز/الخسارة هو نوع خاص من خط المؤشر العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "لأعلى" (فوز) وتُرسم القيمة الصفرية أو السالبة كشريط "لأسفل" (خسارة). تُستخدم خطوط المؤشر للفوز/الخسارة بشكل شائع لتصور تتابعات الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية عبر الزمن.

في Aspose.Cells، يتم إنشاء خط المؤشر للفوز/الخسارة عن طريق تمرير `SparklineType.Stacked` إلى طريقة `SparklineGroups.Add`. (على الرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب عرض الفوز/الخسارة.)

الإجراء هو نفسه كما في النوعين الآخرين:

1. أنشئ `Workbook` جديدًا وادخل إلى ورقة العمل الأولى.
2. املأ نطاق المصدر. نظرًا لأن خطوط المؤشر للفوز/الخسارة تعامل كل قيمة إما على أنها فوز أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة لأعلى والقيم غير الموجبة تصبح أشرطة لأسفل.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. اختياريًا، خصّص كائن `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان مميزة لأشرطة الفوز والخسارة.
6. احفظ المصنف تحت اسم ملف مميز حتى يمكن أن تتعايش الأمثلة الثلاثة على القرص.

يستخدم المثال أدناه نفس بيانات الإدخال كما في القسمين السابقين. تُفسر القيم 5 و-3 و8 و-2 و6 على أنها فوز وخسارة وفوز وخسارة وفوز — وخط المؤشر المرسوم في F1 يعكس هذا النمط بالتحديد.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";

            // الخطوة 2: ملء بيانات عينة في الصف 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);

            // الخطوة 3: بناء CellArea يشير إلى F1 (العمود 5، الصف 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // الصف 1
            dest.EndRow = 0;

            // الخطوة 4: إضافة سباركلاين Win/Loss (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];

            // الخطوة 5: تخصيص مجموعة السباركلاين
            // تمكين علامات النقطة العالية والنقطة المنخفضة
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;

            // تعيين لون النقطة العالية إلى الأخضر
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;

            // تعيين لون النقطة المنخفضة إلى الأحمر
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;

            // تعيين لون النقطة السلبية إلى البرتقالي
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;

            // تعيين لون السلسلة الافتراضي (المستخدم للأشرطة الإيجابية)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;

            // الخطوة 6: حفظ المصنف
            workbook.Save("output_winloss.xlsx");

            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **الجمع بين الأنواع الثلاثة لخطوط المؤشر**

ينتج كل مثال من الأمثلة الثلاثة السابقة المصنف الخاص به بحيث يكون من السهل فحص ملفات الإخراج بمعزل عن غيرها. في السيناريو الحقيقي، مع ذلك، غالبًا ما ترغب في مقارنة عدة سلاسل بيانات جنبًا إلى جنب. أنظف طريقة للقيام بذلك هي وضع أكثر من مجموعة خطوط مؤشر في نفس ورقة العمل، مع كل مجموعة تعرض نمطًا مختلفًا.

يمكنك إضافة كائنات `SparklineGroup` متعددة إلى نفس `SparklineGroupCollection`، ويمكن لكل مجموعة استهداف خلية وجهة مختلفة أو نطاق مختلف. على سبيل المثال، يمكنك وضع خط مؤشر خطي في F1، وخط مؤشر عمودي في F2، وخط مؤشر فوز/خسارة في F3 — جميعها تقرأ من نفس بيانات المصدر في الصف 1 — بحيث يمكن للقارئ رؤية ثلاثة معالجات بصرية مختلفة لنفس الأرقام.

ينشئ المثال المدمج أدناه مصنفًا واحدًا، ويملأ الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يضيف ثلاث مجموعات خطوط مؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يوضح الملف الناتج جميع أنماط خطوط المؤشر الثلاثة مرة واحدة.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// الخطوة 2: ملء بيانات نموذجية في الصف 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// الخطوة 3: إضافة مجموعة خطوط مؤشر مصغر عند F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];

// تخصيص لون خط المؤشر المصغر عبر CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;

// الخطوة 4: إضافة مجموعة أعمدة مؤشر مصغر عند F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];

// تخصيص لون سلسلة عمود المؤشر المصغر
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;

// الخطوة 5: إضافة مجموعة مؤشر مصغر فوز/خسارة (مكدس) عند F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];

// تخصيص لون سلسلة مؤشر الفوز/الخسارة المصغر
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;

// الخطوة 6: حفظ المصنف
workbook.Save("output_all.xlsx");
```

{{% alert color="primary" %}}

عندما تجمع بين مجموعات خطوط مؤشر متعددة في ورقة عمل واحدة، تكون كل مجموعة مستقلة. يمكنها مشاركة نفس نطاق المصدر أو استخدام نطاقات مصدر مختلفة، ويمكن تنسيقها بشكل مستقل. هذا يجعل من السهل بناء "لوحة معلومات" صغيرة من التصورات داخل الخلايا مباشرة داخل ورقة عمل موجودة.

{{% /alert %}}

## **تخصيص مظهر خط المؤشر**

بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.SparklineGroups`، يمكنك قراءة أو تعديل عدة من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر شيوعًا للتخصيص هي:

- **`group.Type`** — نوع `SparklineType` (خطي أو عمودي أو مكدس). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.Line.Color`** — لون الخط، معبرًا عنه بـ `CellsColor` تم إنشاؤه عبر `workbook.CreateCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون ضربة خط المؤشر الخطي.
- **`group.Line.Weight`** — وزن الخط بالنقاط. تنتج القيم الأعلى خطوطًا أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تشغل علامات صغيرة على أعلى وأدنى نقاط البيانات، مفيدة للتأكيد على القيم القصوى.
- **علامات نقاط البداية/النهاية/السالب** — أعلام تبدل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.

لتغيير لون، أنشئ دائمًا مثيل `CellsColor` وقم بتعيينه إلى الخاصية ذات الصلة. لا تعين `System.Drawing.Color` مباشرة إلى خصائص لون خط المؤشر — إنها تتوقع نوع `CellsColor` من `Aspose.Cells.Drawing`. طريقة `SparklineGroups.Add` نفسها تُرجع كائن `SparklineGroup` مكتوب بالكامل، حتى تتمكن من ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصها قبل الحفظ.

## **مقالات ذات صلة**

- [الوصول إلى خلايا ورقة العمل](/cells/ar/net/accessing-cells-of-a-worksheet/)
- [تنسيق خلايا ورقة العمل في مصنف](/cells/ar/net/format-worksheet-cells-in-a-workbook/)
- [تخصيص الرسوم البيانية](/cells/ar/net/customizing-charts/)
- [إنشاء رسوم بيانية ديناميكية](/cells/ar/net/create-dynamic-charts/)
- [إدارة بيانات ملفات Excel](/cells/ar/net/cells-data/)

{{< app/cells/assistant language="csharp" >}}