---
title: Primary and Secondary Axis with C++
linktitle: Primary and Secondary Axis
description: Learn how to understand and work with primary and secondary axes in Aspose.Cells for C++. Our guide will help you understand the differences between primary and secondary axes, and how to configure and use them effectively in your charts.
keywords: Aspose.Cells for C++, primary axes, secondary axes, understanding, differences, configuration, usage.
type: docs
weight: 190
url: /cpp/primary-and-second-axis/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When the numbers in a chart vary widely from data series to data series, or when you have mixed types of data (price and volume), plot one or more data series on a secondary vertical (value) axis. The scale of the secondary vertical axis shows the values for the associated data series. A secondary axis works well in a chart that shows a combination of column and line charts.

## **Handle Primary and Secondary Axis like Microsoft Excel**
Please see the following sample code that creates a new Excel file and puts values of the chart in the first worksheet. Then we add a chart and show the secondary axis.

![todo:image_alt_text](excel.png)

## **Sample Code**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the secondary axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the secondary axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
