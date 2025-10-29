---
title: تعديل الموضع، الحجم وتصميم المخطط باستخدام C++
linktitle: تلاعب بموقع الرسمة وحجمها وتصميم الرسم البياني
description: تعلم كيفية استخدام Aspose.Cells for C++ للتلاعب الفعال بموقع، وحجم، وتصميم المخطط في Microsoft Excel. سيظهر دليلنا كيف تعدل هذه الخصائص لتحسين التخطيط والتصور.
keywords: Aspose.Cells for C++، الموقع، الحجم، تصميم المخطط، Microsoft Excel، التخطيط، التصور.
type: docs
weight: 45
url: /ar/cpp/manipulate-position-size-and-designer-chart/
---

## **الموقع والحجم للرسم البياني**
أحيانًا، تريد تغيير موضع أو حجم المخطط الجديد أو الحالي داخل ورقة العمل. توفر Aspose.Cells الخاصية [Chart.GetChartObject()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getchartobject/) لتحقيق ذلك. يمكنك استخدام خصائصها الفرعية لإعادة تحجيم المخطط باستخدام ارتفاع و عرض جديدين أو إعادة وضعه باستخدام إحداثيات X و Y جديدة.

### **التحكم في موقع الرسم البياني وحجمه**
لاستخدام هذه الخصائص وتغيير موقع الرسم البياني (إحداثيات X و Y) أو حجمه (ارتفاع وعرض):

1. [Chart.GetX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getwidth/)

المثال التالي يشرح استخدام الواجهات البرمجية التطبيقية المذكورة أعلاه، حيث يقوم بتحميل دفتر العمل الحالي الذي يحتوي على رسم بياني في ورقة العمل الأولى. ثم يقوم بتغيير حجم وموضع الرسم البياني باستخدام Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Load the chart from the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Resize the chart
    chart.GetChartObject().SetWidth(400);
    chart.GetChartObject().SetHeight(300);

    // Reposition the chart
    chart.GetChartObject().SetX(250);
    chart.GetChartObject().SetY(150);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart resized and repositioned successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تلاعب الرسوم البيانية للمصمم**
هناك أوقات عندما تحتاج إلى تلاعب أو تعديل الرسوم البيانية في ملفات القوالب المصممة. Aspose.Cells يدعم بشكل كامل تغير محتويات وعناصر الرسم البياني المصممة. يمكن الاحتفاظ بالبيانات ومحتويات الرسم البياني والصورة الخلفية والتنسيقات بدقة.

### **تلاعب الرسوم البيانية لملفات القوالب المصممة**
لتلاعب الرسوم البيانية لملفات القالب المصممة، استخدم واجهة برمجة التطبيق للرسم البياني. على سبيل المثال، يمكنك استخدام خاصية Worksheet.Charts للحصول على مجموعة الرسوم البيانية الحالية في ملف القالب.

#### **إنشاء رسم بياني**
المثال التالي يوضح كيفية إنشاء رسم بياني هرمي. سوف نقوم بتلاعب بهذا الرسم لاحقًا.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    int chartIndex = worksheet.GetCharts().Add(ChartType::Pyramid, 5, 0, 15, 5);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    chart.GetNSeries().Add(u"A1:B3", true);

    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **تلاعب الرسم البياني**
المثال التالي يوضح كيفية تلاعب الرسم البياني الحالي. في هذا المثال، نقوم بتعديل الرسم البياني الذي تم إنشاؤه أعلاه. في الناتج المولد، لاحظ أن تسمية التاريخ لأحد نقاط البيانات تم تعيينها إلى 'المملكة المتحدة، 30 ألف'.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"piechart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the existing file
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Chart chart = sheet.GetCharts().Get(0);

    // Get the data labels in the data series of the third data point
    DataLabels datalabels = chart.GetNSeries().Get(0).GetPoints().Get(2).GetDataLabels();

    // Change the text of the label
    datalabels.SetText(u"Unided Kingdom, 400K ");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data label text updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **تلاعب رسم بياني الخط في القالب المصمم**
في هذا المثال، سنقوم بتلاعب رسم بياني خطي. سنضيف بعض سلاسل البيانات إلى الرسم البياني الحالي وتغيير ألوان خطوطها.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Add the third data series to it
    chart.GetNSeries().Add(U16String(u"{60, 80, 10}"), true);

    // Add another data series (fourth) to it
    chart.GetNSeries().Add(U16String(u"{0.3, 0.7, 1.2}"), true);

    // Plot the fourth data series on the second axis
    chart.GetNSeries().Get(3).SetPlotOnSecondAxis(true);

    // Change the Border color of the second data series
    chart.GetNSeries().Get(1).GetBorder().SetColor(Color::Green());

    // Change the Border color of the third data series
    chart.GetNSeries().Get(2).GetBorder().SetColor(Color::Red());

    // Make the second value axis visible
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
