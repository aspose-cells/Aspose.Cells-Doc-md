---
title: Manage Legend of Excel Charts with C++
linktitle: Legend
description: Learn how to utilize Aspose.Cells for C++ to effectively use and customize chart legends in Microsoft Excel. Our comprehensive guide explains the legend's functionality, how to access and modify it, as well as how to improve visualization and data understanding with legends.
keywords: Aspose.Cells for C++, Chart Legends, Microsoft Excel, Visualization, Data Understanding.
type: docs
weight: 50
url: /cpp/chart-legend/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Legend Options**
Aspose.Cells also allows you to manage a chart's legend at runtime. With the [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/) object, the legend can be moved, updated, and formatted.

|![todo:image_alt_text](chart_legend.png)|

## **Setting the Legend of a Chart**
It's simple to manage a chart's legend using Aspose.Cells' [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/).

The following code snippet demonstrates how to manage the legend:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from cell A1 to B3
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to the left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Advanced Topics**
- [Set text of chart legend entry fill to none using Aspose.Cells](/cells/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="cpp" >}}
