##Manipulate Position Size and Designer Chart with C++
Learn how to use Aspose.Cells for C++ to effectively manipulate the position, size, and designer chart in Microsoft Excel. Our guide will demonstrate how to adjust these properties for improved layout and visualization.
## **Chart Position and Size**
Sometimes, you want to change the position or size of the new or existing chart inside the worksheet. Aspose.Cells provides the [Chart.GetChartObject()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getchartobject/) property to achieve this. You can use its sub-properties to re-size the chart with new **height** and **width** or re-position it with new **X** and **Y** coordinates.
### **Controlling Chart Position and Size**
To change the chart's position (X, Y coordinates) or size (height, width), use these properties:
1. [Chart.GetX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getwidth/)
The following example explains the usage of the above APIs, it loads the existing workbook which contains a chart in its first worksheet. Then it re-sizes and re-positions the chart using Aspose.Cells.
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
## **Manipulating Designer Charts**
There are times when you need to manipulate or modify charts in designer template files. Aspose.Cells fully supports manipulating designer chart contents and elements. The data, chart contents, background image, and formattings can be preserved with accuracy.
### **Manipulating Designer Charts in Template Files**
To manipulate designer charts in template files, use the chart related API. For example, you may use the Worksheet.Charts property to get the existing charts collection in the template file.
#### **Creating a Chart**
The following example shows how to create a pyramid chart. We will manipulate this chart later on.
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
#### **Manipulating the Chart**
The following example shows how to manipulate the existing chart. In this example, we modify the chart created above. In the generated output, note that the date label of one data point has been set to 'United Kingdom, 30K'.
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
#### **Manipulating a Line Chart in the Designer Template**
In this example, we will manipulate a line chart. We will add some data series to the existing chart and change their line colors.
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
