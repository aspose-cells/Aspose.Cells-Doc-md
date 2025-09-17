##Manage Axes of Excel Charts with C++
Learn how to configure chart axes in Aspose.Cells for C++. Our guide will show you how to adjust the primary and secondary axes, set their ranges, and modify their properties to enhance your charts.
In Excel charts, there are 3 kinds of Axes:
1. Horizontal (Category) Axis : X Axis
1. Vertical (Value) Axis : Y Axis
1. Depth (Series) Axis : Z Axis
## **Axis Options**
Aspose.Cells also allows you to manage chart's axes at runtime. With the [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) object, you can change all options of the Axis as done in Excel.
|![todo:image_alt_text](chart_axes.png)|
## **Manage X and Y Axes**
In Excel charts, horizontal and vertical axes are the two most popular axes to use.
The following code snippet demonstrates how to set the options of X and Y axes.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
int main()
{
Aspose::Cells::Startup();
// Instantiating a Workbook object
Workbook workbook;
// Adding a new worksheet to the Workbook object
int sheetIndex = workbook.GetWorksheets().Add();
// Obtaining the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);
// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
worksheet.GetCells().Get(u"A2").PutValue(50);
worksheet.GetCells().Get(u"A3").PutValue(100);
worksheet.GetCells().Get(u"A4").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
worksheet.GetCells().Get(u"B2").PutValue(60);
worksheet.GetCells().Get(u"B3").PutValue(32);
worksheet.GetCells().Get(u"B4").PutValue(50);
// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.SetChartDataRange(u"A1:B4", true);
// Hiding X axis
chart.GetCategoryAxis().SetIsVisible(false);
// Setting max value of Y axis
chart.GetValueAxis().SetMaxValue(200);
// Setting major unit
chart.GetValueAxis().SetMajorUnit(50);
// Save the file
workbook.Save(u"chart_axes.xlsx");
Aspose::Cells::Cleanup();
}
```
## **Advance Topics**
- [Change Tick Label Direction](https://docs.aspose.com/cells/cpp/change-tick-label-direction/)
- [Determine which Axis exists in the Chart](https://docs.aspose.com/cells/cpp/determine-which-axis-exists-in-the-chart/)
- [Handle Automatic Units of Chart Axis like Microsoft Excel](https://docs.aspose.com/cells/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [Read Axis Labels after Calculating the Chart](https://docs.aspose.com/cells/cpp/read-axis-labels-after-calculating-the-chart/)
- [How to Set Category Axis in Excel Chart](https://docs.aspose.com/cells/cpp/how-to-set-category-axis/)
