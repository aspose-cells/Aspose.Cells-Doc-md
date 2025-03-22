---
title: Manage DataLabels of Excel Charts with C++
linktitle: DataLabels
type: docs
weight: 50
url: /cpp/insert-datalabels-to-chart/
description: Learn how to effectively manage data labels in Excel charts using Aspose.Cells for C++. Our comprehensive guide covers various management tasks, including adding, removing, and modifying labels to enhance chart readability and usability.
keywords: Aspose.Cells for C++, Excel charts, data labels, management, readability, usability, adding, removing, modifying.
---

{{% alert color="primary" %}}

DataLabels are an important part of a chart. We can easily know the value, percentage, etc. of each series.

{{% /alert %}}

## **DataLabels Options**
Aspose.Cells also allows managing chart's datalabels at runtime with the [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/) object. It's simple to move, update, and format datalabels of the chart.

|![todo:image_alt_text](chart_datalabels.png)|

## **Manage the DataLabels of Chart**
It's simple to manage datalabels of the chart with Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/).

The following code snippet demonstrates how to manage DataLabels:

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

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Advance Topics**
- [Adding Custom Labels to Data Points in the Series of the Chart](/cells/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [Disable Text Wrapping for Data Labels of the Chart](/cells/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [Resize Chart's Data Label Shape To Fit Text](/cells/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [Rich Text Custom Data Label of Chart Point](/cells/cpp/rich-text-custom-data-label-of-chart-point/)
- [Set the Shape Type of Data Labels of Chart](/cells/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [Showing Cell Range as the Data Labels](/cells/cpp/showing-cell-range-as-the-data-labels/)