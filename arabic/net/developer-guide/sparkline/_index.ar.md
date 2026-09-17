---
title: خطوط المؤشر في Aspose.Cells for .NET
linktitle: خطوط المؤشر في Aspose.Cells for .NET
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط المؤشر — وهي رسوم بيانية مصغرة تُوضع داخل خلايا ورقة العمل. تشرح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشر الخطية والعمودية والربح/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة .NET, جدول بيانات, خطوط المؤشر, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشر ربح/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells إنشاء خطوط المؤشر داخل خلايا ورقة العمل. خطوط المؤشر هي رسوم بيانية مصغرة تتناسب مع خلية واحدة، وتوفر تمثيلًا بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشر الخطية والعمودية وخطوط الربح/الخسارة، ويمكن تخصيص كل منها من حيث اللون ووزن الخط ونقاط الارتفاع/الانخفاض والعلامات.

## **مقدمة**
خطوط المؤشر هي رسوم بيانية صغيرة داخل الخلايا، وتكون مفيدة عندما تريد عرض اتجاه سريع بجانب صف أو عمود من البيانات دون شغل مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشر: **خطي** و**عمودي** و**ربح/خسارة**. يعكس Aspose.Cells هذه الإمكانية من خلال واجهات برمجة التطبيقات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الاسم `Aspose.Cells.Charts`.
في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه من خلال `worksheet.SparklineGroups.Add(...)`، والتي تُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر ونطاق البيانات والخلية الوجهة والخصائص المرئية مثل لون الخط ووزن الخط والعلامات ومؤشرات نقاط الارتفاع/الانخفاض.
تستعرض هذه المقالة كل نوع من أنواع خطوط المؤشر الثلاثة التي يدعمها Aspose.Cells — **خطي** و**عمودي** و**ربح/خسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشر الخطية**
يرسم خط المؤشر الخطي خطًا متصلًا عبر نقاط البيانات في السلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات عبر الزمن. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي عن طريق تمرير `SparklineType.Line` إلى طريقة `SparklineGroups.Add`.
1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
2. املأ صفًا من البيانات المصدرية (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم خط المؤشر.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يُخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس عموديًا (عمود).
5. يمكنك اختياريًا تخصيص `SparklineGroup` المُرجع. لخط المؤشر الخطي يمكنك تعيين لون الخط باستخدام `group.Line.Color` (والذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط وزن الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.
ينشئ المثال التالي مصنفًا، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يُخصص لون الخط إلى الأحمر ويمكّن العلامات لنقاط الارتفاع والانخفاض.

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
            // الخطوة 1: إنشاء Workbook والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // الخطوة 2: كتابة قيم العينة 5، -3، 8، -2، 6 في الخلايا A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // الخطوة 3: إنشاء CellArea يشير إلى خلية الوجهة F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // العمود F (مفهرس من 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // الصف 1 (مفهرس من 0)
            dest.EndRow = 0;
            // الخطوة 4: إضافة خط Sparkline من A1:E1 إلى F1
            // SparklineGroups.Add يُرجع فهرس المجموعة المضافة حديثًا
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // الخطوة 5: إنشاء CellsColor أحمر وتعيينه كلون خط الـ Sparkline
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // الخطوة 6: تمكين علامات النقطة العالية والنقطة المنخفضة
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // الخطوة 7: حفظ الـ Workbook
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **خطوط المؤشر العمودية**
يُعرض خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسبًا تمامًا للبيانات التي يكون فيها مقدار القيمة ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو التعدادات. في Aspose.Cells، تُنشئ خط المؤشر العمودي عن طريق تمرير `SparklineType.Column` إلى طريقة `SparklineGroups.Add`.
يتبع الإجراء نفس خطوات مثال خط المؤشر الخطي:
1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
2. املأ نطاق البيانات المصدرية.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. يمكنك اختياريًا تخصيص `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.Type` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يستبدل مثال خط المؤشر الخطي.
يكتب المثال أدناه القيم 5 و-3 و8 و-2 و6 في A1:E1 ويُعرض خط مؤشر عمودي في F1. تُرسم القيم السالبة كأشرطة تتجه للأسفل والقيم الموجبة كأشرطة تتجه للأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بمجرد النظر.

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
            // الخطوة 3: بناء CellArea يشير إلى F1 (فهرس العمود 5، فهرس الصف 0)
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

## **خطوط المؤشر للربح/الخسارة**
خط مؤشر الربح/الخسارة هو نوع خاص من خط المؤشر العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "أعلى" (ربح) وتُرسم القيمة الصفرية أو السالبة كشريط "أسفل" (خسارة). تُستخدم خطوط مؤشر الربح/الخسارة بشكل شائع لتصور تسلسلات الانتصارات والخسائر، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية عبر الزمن.
في Aspose.Cells، يُنشأ خط مؤشر الربح/الخسارة عن طريق تمرير `SparklineType.Stacked` إلى طريقة `SparklineGroups.Add`. (على الرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب عرض الربح/الخسارة.)
1. أنشئ `Workbook` جديدًا ووصل إلى ورقة العمل الأولى.
2. املأ نطاق البيانات المصدرية. نظرًا لأن خطوط مؤشر الربح/الخسارة تعامل كل قيمة إما كربح أو خسارة، فإن مقدار القيمة لا يهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة علوية والقيم غير الموجبة تصبح أشرطة سفلية.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. يمكنك اختياريًا تخصيص `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان مميزة لأشرطة الربح والخسارة.
6. احفظ المصنف تحت اسم ملف مميز حتى يمكن أن تتواجد جميع الأمثلة الثلاثة على القرص.

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
            // الخطوة 1: إنشاء Workbook والحصول على ورقة العمل الأولى
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // الخطوة 2: تعبئة بيانات العينة في الصف 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
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
            // الخطوة 4: إضافة Sparkline من نوع فوز/خسارة (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // الخطوة 5: تخصيص مجموعة Sparkline
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
            // تعيين لون السلسلة الافتراضي (يستخدم للأشرطة الإيجابية)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // الخطوة 6: حفظ الـ Workbook
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **الجمع بين أنواع خطوط المؤشر الثلاثة**
يُنشئ المثال المجمع التالي مصنفًا واحدًا، ويملأ الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يضيف ثلاث مجموعات من خطوط المؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يُظهر الملف الناتج أنماط خطوط المؤشر الثلاثة دفعة واحدة.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// الخطوة 1: إنشاء مصنف والحصول على ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// الخطوة 2: تعبئة بيانات العينة في الصف 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// الخطوة 3: إضافة مجموعة شرارة خطية في F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// تخصيص لون شرارة الخط عبر CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// الخطوة 4: إضافة مجموعة شرارة عمودية في F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// تخصيص لون سلسلة شرارة العمود
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// الخطوة 5: إضافة مجموعة شرارة فوز/خسارة (مكدسة) في F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// تخصيص لون سلسلة شرارة الفوز/الخسارة
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// الخطوة 6: حفظ المصنف
workbook.Save("output_all.xlsx");
```

## **تخصيص مظهر خط المؤشر**
بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.SparklineGroups`، يمكنك قراءة أو تعديل عدة من خصائصه المرئية قبل حفظ المصنف. الخصائص الأكثر شيوعًا في التخصيص هي:
- **`group.Type`** — نوع `SparklineType` (Line أو Column أو Stacked). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.Line.Color`** — لون الخط، معبرًا عنه بـ `CellsColor` تم إنشاؤه عبر `workbook.CreateCellsColor()`. هذه هي الخاصية التي يجب استخدامها للون حد خط المؤشر الخطي.
- **`group.Line.Weight`** — وزن الخط بالنقاط. تؤدي القيم الأعلى إلى خطوط أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تُشغل علامات صغيرة على أعلى وأدنى نقاط البيانات، وهي مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — أعلام تُبدّل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.
لتغيير اللون، دائمًا أنشئ نسخة `CellsColor` وعيّنها إلى الخاصية ذات الصلة. لا تُسند `System.Drawing.Color` مباشرة إلى خصائص لون خط المؤشر — إذ إنها تتوقع نوع `CellsColor` من `Aspose.Cells.Drawing`. تُرجع طريقة `SparklineGroups.Add` نفسها كائن `SparklineGroup` مكتوبًا بالكامل، لذا يمكنك ربط تعيينات الخصائص على القيمة المُرجعة أو تخزينها في متغير محلي وتخصيصه قبل الحفظ.
{{% /alert %}}

## مقالات ذات صلة
- [تحويل خط المؤشر إلى صورة وHTML في Aspose.Cells for .NET](/cells/ar/net/convert-sparkline-to-image-and-html/)
- [إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for .NET](/cells/ar/net/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for .NET](/cells/ar/net/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في جدول محوري](/cells/ar/net/change-page-field-layout/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}