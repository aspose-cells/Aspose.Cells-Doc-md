##Z Axis with C++
Learn how to work with the Z-axis in Aspose.Cells for C++. Our guide will help you understand how to configure and customize the Z-axis, including its scale and labels, to enhance your charts.
## **Possible Usage Scenarios**
For some 3-D charts such as 3-D column, 3-D cone, or 3-D pyramid which has a depth (series) axis, also known as the Z axis, that you can change. You can specify the interval between tick marks, axis labels and other operation.
## **Handle Primary and Second Axis like Microsoft Excel**
Please see the following sample code that create a new Excel file and put values of the chart in the first worksheet. Then we add a chart and set the chart type to Column3D, then you can see the Z Axis also called Depth Axis.
![todo:image_alt_text](excel.png)
## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
int main()
{
Aspose::Cells::Startup();
// Create an instance of Workbook
Workbook workbook;
// Get the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Put values to cells for creating chart
worksheet.GetCells().Get(u"A1").PutValue(u"A");
worksheet.GetCells().Get(u"B1").PutValue(u"B");
worksheet.GetCells().Get(u"C1").PutValue(u"C");
worksheet.GetCells().Get(u"A2").PutValue(2);
worksheet.GetCells().Get(u"A3").PutValue(1);
worksheet.GetCells().Get(u"B2").PutValue(2);
worksheet.GetCells().Get(u"B3").PutValue(3);
worksheet.GetCells().Get(u"C2").PutValue(2);
worksheet.GetCells().Get(u"C3").PutValue(3);
// Add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);
// Calculate the chart
chart.Calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.SetChartDataRange(u"A2:C3", true);
// Hide the CategoryAxis axis
chart.GetCategoryAxis().SetIsVisible(false);
// Hide the ValueAxis axis
chart.GetValueAxis().SetIsVisible(false);
// Save the file
workbook.Save(u"ZAxis.xlsx");
Aspose::Cells::Cleanup();
return 0;
}
```
