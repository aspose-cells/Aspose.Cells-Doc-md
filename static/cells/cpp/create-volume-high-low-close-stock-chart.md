##Create Volume-High-Low-Close(VHLC) Stock Chart with C++
Learn how to create a volume-high-low-close stock chart using Aspose.Cells for C++. Our guide will demonstrate how to plot stock market data, including volume, high, low, and close prices, onto a chart for better analysis and visualization.
## **Possible Usage Scenarios**
The third stock chart we will look at is the Volume High Low Close chart. Again it is important to repeat that you must have the data in the correct order. If you need to rearrange your data table, you should do it before you set up your chart. This chart includes a column for volume immediately after the first (category) column, and the charts include a column chart on the primary axis showing this volume, while the prices are moved to the secondary axis.
![todo:image_alt_text](data.png)
## **Volume-High-Low-Close (VHLC) stock chart**
![todo:image_alt_text](sample.png)
## **Sample Code**
The following sample code loads the [sample Excel file](Volume-High-Low-Close.xlsx) and generates the [output Excel file](out.xlsx).
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create an instance of Workbook
Workbook workbook(u"Volume-High-Low-Close.xlsx");
// Access the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Create High-Low-Close Stock Chart
int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
Chart chart = worksheet.GetCharts().Get(pieIdx);
// Set the legend can be showed
chart.SetShowLegend(true);
// Set the chart title name
chart.GetTitle().SetText(u"Volume-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.GetLegend().SetPosition(LegendPositionType::Bottom);
// Set data range
chart.SetChartDataRange(u"A1:E9", true);
// Set category data
chart.GetNSeries().SetCategoryData(u"A2:A9");
// Set Color for the first series (Volume) data
chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{ 79, 129, 189 });
// Fill the PlotArea area with nothing
chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
// Save the Excel file
workbook.Save(u"out.xlsx");
std::cout << "Chart created and saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
