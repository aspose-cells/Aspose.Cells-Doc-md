##Set Picture as Background Fill in the Chart with C++
Learn how to set a picture as the background fill in a chart using Aspose.Cells for C++. Our guide will show you how to import and position the picture, adjust its size and color, and apply formatting options to enhance your chart's appearance.
Aspose.Cells allows you to set a gradient, texture, pattern, or picture as fill effects for different objects, such as the plot area, chart area, or legend box of a chart. This document shows how to add an image to a chart's background.
To achieve this, Aspose.Cells provides the [**Chart.GetImageData()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/getimagedata/) property. The following code sample demonstrates the use of [**Chart.GetImageData()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/getimagedata/) property to set a picture as a background fill in the chart.
## C++ code to set picture as background fill in the chart
```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
int main() {
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
Workbook workbook;
Worksheet sheet = workbook.GetWorksheets().Get(0);
sheet.SetName(u"Data");
Cells cells = sheet.GetCells();
cells.Get(u"A1").PutValue(u"Region");
cells.Get(u"A2").PutValue(u"France");
cells.Get(u"A3").PutValue(u"Germany");
cells.Get(u"A4").PutValue(u"England");
cells.Get(u"A5").PutValue(u"Sweden");
cells.Get(u"A6").PutValue(u"Italy");
cells.Get(u"A7").PutValue(u"Spain");
cells.Get(u"A8").PutValue(u"Portugal");
cells.Get(u"B1").PutValue(u"Sale");
cells.Get(u"B2").PutValue(70000);
cells.Get(u"B3").PutValue(55000);
cells.Get(u"B4").PutValue(30000);
cells.Get(u"B5").PutValue(40000);
cells.Get(u"B6").PutValue(35000);
cells.Get(u"B7").PutValue(32000);
cells.Get(u"B8").PutValue(10000);
int sheetIndex = workbook.GetWorksheets().Add(SheetType::Chart);
sheet = workbook.GetWorksheets().Get(sheetIndex);
sheet.SetName(u"Chart");
int chartIndex = sheet.GetCharts().Add(ChartType::Column, 1, 1, 25, 10);
Chart chart = sheet.GetCharts().Get(chartIndex);
std::ifstream fs((srcDir + u"aspose.png").ToUtf8(), std::ios::binary);
std::vector<uint8_t> data((std::istreambuf_iterator<char>(fs)), std::istreambuf_iterator<char>());
Aspose::Cells::Vector<uint8_t> asposeData(data.data(), data.size());
chart.GetPlotArea().GetArea().GetFillFormat().SetImageData(asposeData);
chart.GetPlotArea().GetBorder().SetIsVisible(false);
chart.GetTitle().SetText(u"Sales By Region");
chart.GetTitle().GetFont().SetColor(Color::Blue());
chart.GetTitle().GetFont().SetIsBold(true);
chart.GetTitle().GetFont().SetSize(12);
chart.GetNSeries().Add(u"Data!B2:B8", true);
chart.GetNSeries().SetCategoryData(u"Data!A2:A8");
chart.GetNSeries().SetIsColorVaried(true);
Legend legend = chart.GetLegend();
legend.SetPosition(LegendPositionType::Top);
workbook.Save(outDir + u"column_chart_out.xls");
Aspose::Cells::Cleanup();
return 0;
}
```
