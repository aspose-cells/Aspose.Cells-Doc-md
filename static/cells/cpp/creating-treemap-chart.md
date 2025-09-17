##How to create TreeMap chart with C++
Learn how to create a Treemap chart in Aspose.Cells for C++. Our guide will help you understand the various properties and formatting options available for Treemap charts, including colors, labels, and data representation.
## **Possible Usage Scenarios**
A treemap chart provides a hierarchical view of your data and makes it easy to spot patterns, such as which items are a store's best sellers. The tree branches are represented by rectangles and each sub-branch is shown as a smaller rectangle. The treemap chart displays categories by color and proximity and can easily show lots of data which would be difficult with other chart types.
![todo:image_alt_text](sample.png)
## **TreeMap chart**
After running the code below, you will see the TreeMap chart as shown below.
![todo:image_alt_text](result.png)
## **Sample Code**
The following sample code loads the [sample Excel file](treemap.xlsx) and generates the [output Excel file](out.xlsx).
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create an instance of Workbook
Workbook workbook(u"treemap.xlsx");
// Access the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Add a Treemap chart
int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
Chart chart = worksheet.GetCharts().Get(pieIdx);
// Set the legend can be showed
chart.SetShowLegend(true);
// Set the chart title name
chart.GetTitle().SetText(u"TreeMap Chart");
// Add series data range (D2:F13, actually)
chart.GetNSeries().Add(u"D2:F13", true);
// Set category data (A2:C13 is incorrect)
chart.GetNSeries().SetCategoryData(u"A2:C13");
// Show the DataLabels with category names
chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);
// Fill the PlotArea area with nothing
chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
// Save the Excel file
workbook.Save(u"out.xlsx");
Aspose::Cells::Cleanup();
}
```
