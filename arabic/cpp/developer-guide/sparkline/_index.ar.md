---
title: خطوط المؤشر في Aspose.Cells for C++
linktitle: خطوط المؤشر في Aspose.Cells for C++
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات تدعم إنشاء خطوط المؤشر، وهي رسوم بيانية مصغرة توضع داخل خلايا ورقة العمل. توضح هذه المقالة كيفية إضافة وتخصيص خطوط المؤشر الخطية والعمودية والفوز/الخسارة باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, خطوط المؤشر, خط مؤشر خطي, خط مؤشر عمودي, خط مؤشر فوز/خسارة, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ar/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells إنشاء خطوط المؤشر داخل خلايا ورقة العمل. خطوط المؤشر هي رسوم بيانية مصغرة تتناسب مع خلية واحدة، وتوفر تمثيلاً بصريًا سريعًا لاتجاهات البيانات. يدعم Aspose.Cells خطوط المؤشر الخطية والعمودية والفوز/الخسارة، ويمكن تخصيص كل منها من حيث اللون ووزن الخط ونقاط الارتفاع/الانخفاض والعلامات.
{{% /alert %}}

## **مقدمة**
خطوط المؤشر هي رسوم بيانية صغيرة داخل الخلايا تكون مفيدة عندما تريد عرض اتجاه سريع بجوار صف أو عمود من البيانات دون أن تشغل مساحة رسم بياني كامل. يدعم Excel ثلاثة أنواع من خطوط المؤشر: **الخطي**، و**العمودي**، و**الفوز/الخسارة**. يعكس Aspose.Cells هذه القدرة من خلال واجهات `SparklineGroup` و`SparklineGroupCollection` الموجودة في مساحة الاسم `Aspose.Cells.Charts`.
في Aspose.Cells، يتم إنشاء كل خط مؤشر تضيفه من خلال `worksheet.SparklineGroups.Add(...)`، والذي يُرجع كائن `SparklineGroup`. يمكنك بعد ذلك استخدام هذا الكائن لتعيين نوع خط المؤشر ونطاق البيانات والخلية الوجهة والخصائص المرئية مثل لون الخط ووزنه والعلامات ومؤشرات نقاط الارتفاع/الانخفاض.
تستعرض هذه المقالة كل نوع من أنواع خطوط المؤشر الثلاثة التي يدعمها Aspose.Cells — **الخطي**، و**العمودي**، و**الفوز/الخسارة** — وتوضح كيفية إضافتها وتخصيص ألوانها وحفظ المصنف الناتج.

## **خطوط المؤشر الخطية**
يرسم خط المؤشر الخطي خطًا متواصلًا يمر عبر نقاط البيانات في سلسلة، مما يجعله الخيار الأكثر طبيعية لإظهار الاتجاهات عبر الزمن. في Aspose.Cells، يتم إنشاء خط المؤشر الخطي عن طريق تمرير `SparklineType.Line` إلى الطريقة `SparklineGroups.Add`.
1. أنشئ `Workbook` جديدًا واعرض ورقة العمل الأولى.
2. املأ صفًا من بيانات المصدر (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة حيث سيتم رسم خط المؤشر.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. الوسيط الثالث — `false` — يخبر Aspose.Cells بأن نطاق البيانات أفقي (صف)، وليس عموديًا (عمود).
5. اختياريًا، خصص كائن `SparklineGroup` المُرجع. لخط المؤشر الخطي يمكنك تعيين لون الخط باستخدام `group.Line.Color` (والذي يتوقع `CellsColor` من `Aspose.Cells.Drawing`)، وضبط وزن الخط، وتبديل علامات نقاط الارتفاع/الانخفاض.
6. احفظ المصنف.
يُنشئ المثال التالي مصنفًا، ويكتب القيم 5 و-3 و8 و-2 و6 في الخلايا من A1 إلى E1، ويضيف خط مؤشر خطي في الخلية F1 يتتبع تلك القيم. كما يخصص لون الخط إلى الأحمر ويُفعّل العلامات لنقاط الارتفاع والانخفاض.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // Step 3: Build a CellArea pointing to destination cell F1
    CellArea dest;
    dest.StartColumn = 5;   // column F (0-indexed)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // row 1 (0-indexed)
    dest.EndRow = 0;
    // Step 4: Add a Line sparkline from A1:E1 into F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // Step 5: Create a red CellsColor and assign it to the sparkline line color
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // Step 6: Enable high-point and low-point markers
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // Step 7: Save the workbook
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **خطوط المؤشر العمودية**
يعرض خط المؤشر العمودي كل نقطة بيانات كشريط عمودي. وهذا يجعله مناسبًا تمامًا للبيانات التي يكون مقدارها ذا معنى — على سبيل المثال، أرقام المبيعات الشهرية أو العدادات. في Aspose.Cells، تنشئ خط المؤشر العمودي عن طريق تمرير `SparklineType.Column` إلى الطريقة `SparklineGroups.Add`.
يعكس الإجراء مثال خط المؤشر الخطي:
1. أنشئ `Workbook` جديدًا واعرض ورقة العمل الأولى.
2. املأ صفًا من بيانات المصدر (على سبيل المثال، الصف 1، الأعمدة من A إلى E) بالقيم التي تريد تصورها.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. اختياريًا، خصص `SparklineGroup` الناتج — على سبيل المثال، عن طريق تعيين `group.Type` لتأكيد النوع، أو عن طريق تعديل لون الشريط.
6. احفظ المصنف في ملف إخراج منفصل حتى لا يكتب فوق مثال خط المؤشر الخطي.
يكتب المثال أدناه القيم 5 و-3 و8 و-2 و6 في A1:E1 ويعرض خط مؤشر عمودي في F1. يتم رسم القيم السالبة كأشرطة تتجه لأسفل والقيم الموجبة كأشرطة تتجه لأعلى، مما يجعل المساهمات الموجبة والسالبة سهلة التمييز بنظرة واحدة.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Step 1: Create a Workbook and get the first worksheet
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // Step 2: Write sample values into A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }
    // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // Step 4: Add a Column sparkline to the destination cell
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);
    // Step 5: Confirm the sparkline type by reading group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;
    // Step 6: Save the workbook
    wb.Save(u"output_column.xlsx");
    std::cout << "Workbook saved as output_column.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **خطوط المؤشر للفوز/الخسارة**
خط مؤشر الفوز/الخسارة هو نوع خاص من خط المؤشر العمودي مصمم لإظهار نتيجتين فقط: تُرسم القيمة الموجبة كشريط "لأعلى" (فوز) والقيمة الصفرية أو السالبة تُرسم كشريط "لأسفل" (خسارة). تُستخدم خطوط المؤشر للفوز/الخسارة بشكل شائع لتصوير تسلسلات من الانتصارات والهزائم، أو نتائج النجاح/الفشل، أو أي نتيجة ثنائية عبر الزمن.
في Aspose.Cells، يتم إنشاء خط مؤشر الفوز/الخسارة عن طريق تمرير `SparklineType.Stacked` إلى الطريقة `SparklineGroups.Add`. (على الرغم من الاسم، فإن `SparklineType.Stacked` هو قيمة التعداد المستخدمة لطلب عرض الفوز/الخسارة.)
1. أنشئ `Workbook` جديدًا واعرض ورقة العمل الأولى.
2. املأ نطاق المصدر. نظرًا لأن خطوط مؤشر الفوز/الخسارة تتعامل مع كل قيمة إما كفوز أو خسارة، فإن مقدار القيمة غير مهم — فقط إشارتها هي المهمة. تصبح القيم الموجبة أشرطة لأعلى والقيم غير الموجبة تصبح أشرطة لأسفل.
3. أنشئ `CellArea` يصف خلية الوجهة.
4. استدعِ `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. اختياريًا، خصص كائن `SparklineGroup` المُرجع، على سبيل المثال عن طريق تعيين ألوان تأكيد لأشرطة الفوز والخسارة.
6. احفظ المصنف باسم ملف مميز حتى يمكن للأمثلة الثلاثة جميعها التعايش على القرص.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // row 1
    dest.EndRow = 0;
    // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);
    // Step 5: Customize the sparkline group
    // Enable high-point and low-point markers
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // Set the high-point color to green
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // Set the low-point color to red
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // Set the negative-point color to orange
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // Set the default series color (used for positive bars)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // Step 6: Save the workbook
    workbook.Save(u"output_winloss.xlsx");
    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الجمع بين الأنواع الثلاثة لخطوط المؤشر**
يُنشئ المثال المجمع أدناه مصنفًا واحدًا، ويملأ الصف 1 بالقيم 5 و-3 و8 و-2 و6، ثم يضيف ثلاث مجموعات خطوط مؤشر في الخلايا F1 وF2 وF3 — واحدة من كل نوع — بحيث يُظهر الملف الناتج أنماط خطوط المؤشر الثلاثة كلها دفعة واحدة.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Step 2: Populate sample data in row 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Step 3: Add a Line sparkline group at F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // Customize the line sparkline color via CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // Step 4: Add a Column sparkline group at F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // Customize the column sparkline series color
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // Step 5: Add a Win/Loss (Stacked) sparkline group at F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // Customize the win/loss sparkline series color
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // Step 6: Save the workbook
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تخصيص مظهر خط المؤشر**
بمجرد إنشاء `SparklineGroup` وإضافته إلى `worksheet.SparklineGroups`، يمكنك قراءة أو تعديل عدة خصائص مرئية له قبل حفظ المصنف. الخصائص الأكثر شيوعًا في التخصيص هي:
- **`group.Type`** — `SparklineType` (Line أو Column أو Stacked). يتم تعيينه عند إضافة المجموعة، ولكن يمكنك قراءته مرة أخرى للتأكيد.
- **`group.Line.Color`** — لون الخط، معبرًا عنه بـ `CellsColor` تم إنشاؤه عبر `workbook.CreateCellsColor()`. هذه هي الخاصية المستخدمة للون خط المؤشر الخطي.
- **`group.Line.Weight`** — وزن الخط بالنقاط. تنتج القيم الأعلى خطوطًا أسمك.
- **علامات نقاط الارتفاع/الانخفاض** — أعلام تشغل علامات صغيرة على أعلى وأدنى نقاط البيانات، مفيدة للتأكيد على القيم القصوى.
- **علامات النقاط الأولى/الأخيرة/السالبة** — أعلام تبدل العلامات على نقاط البيانات الأولى والأخيرة والسالبة.
لتغيير اللون، أنشئ دائمًا مثيلًا من `CellsColor` وعينه إلى الخاصية المعنية. لا تعين قيمة لون خام مباشرة إلى خصائص لون خط المؤشر — فهي تتوقع النوع `CellsColor` من `Aspose.Cells.Drawing`. ترجع الطريقة `SparklineGroups.Add` نفسها كائن `SparklineGroup` مكتوبًا بالكامل، بحيث يمكنك سلسلة تعيينات الخصائص على القيمة المُرجعة أو تخزينه في متغير محلي وتخصيصه قبل الحفظ.

{{< app/cells/assistant language="cpp" >}}