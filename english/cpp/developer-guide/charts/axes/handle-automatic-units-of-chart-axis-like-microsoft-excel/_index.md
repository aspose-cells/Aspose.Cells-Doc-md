---
title: Handle Automatic Units of Chart Axis like Microsoft Excel with C++
linktitle: Handle Automatic Units of Chart Axis
description: Learn how to handle automatic units on chart axes in Aspose.Cells for C++, similar to Microsoft Excel. Our guide will show you how to configure and customize automatic units on a chart axis, including the display of scientific notation and adjusting the scale.
keywords: Aspose.Cells for C++, chart axes, automatic units, Microsoft Excel, configuration, customization, scientific notation, scaling.
type: docs
weight: 120
url: /cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Early versions of Aspose.Cells were not able to handle automatic units of the chart axis properly when the chart is rendered to image or PDF. Now, Aspose.Cells supports the handling of automatic units of the chart axis. There is no code change. Just convert your chart into image or PDF and it will render the chart axis just like Microsoft Excel renders it.

## **Handle Automatic Units of Chart Axis like Microsoft Excel**
The following sample code loads the [sample Excel file](61767755.xlsx) and generates the [output PDF chart](61767752.pdf). The screenshot shows the automatic units of chart axis in red rectangles and also compares the sample Excel file chart with the output PDF chart. Both are exactly similar.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **Sample Code**
```c++
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

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
