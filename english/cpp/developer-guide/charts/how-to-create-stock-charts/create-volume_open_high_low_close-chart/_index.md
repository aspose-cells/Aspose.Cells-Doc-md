---
title: Create Volume-Open-High-Low-Close(VOHLC) Stock Chart with C++
description: Learn how to create a volume-open-high-low-close stock chart using Aspose.Cells for C++. Our guide will demonstrate how to plot stock market data, including volume, open, high, low, and close prices, onto a chart for better analysis and visualization.
keywords: Aspose.Cells for C++, Volume-Open-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 184
url: /cpp/create-volume-open-high-low-close-stock-chart/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
The fourth stock chart we will look at is the Volume Open High Low Close chart. Again it is important to repeat that you must have the data in the correct order. If you need to rearrange your data table, you should do it before you set up your chart. This chart includes a column for volume immediately after the first (category) column, and the charts include a column chart on the primary axis showing this volume, while the prices are moved to the secondary axis.

![todo:image_alt_text](data.png)

## **Volume-Open-High-Low-Close (VHLC) stock chart**

![todo:image_alt_text](sample.png)

## **Sample Code**
The following sample code loads the [sample Excel file](Volume-Open-High-Low-Close.xlsx) and generates the [output Excel file](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");
    
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);
    
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    
    // Set the legend to be shown
    chart.SetShowLegend(true);
    
    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");
    
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    
    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);
    
    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    
    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});
    
    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
