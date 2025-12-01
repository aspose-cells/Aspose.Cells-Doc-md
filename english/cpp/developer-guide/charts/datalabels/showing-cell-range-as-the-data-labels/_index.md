---
title: Showing Cell Range as the Data Labels with C++
linktitle: Showing Cell Range as the Data Labels
description: Learn how to show a range of cells as data labels in charts using Aspose.Cells for C++. Our guide will demonstrate how to link the labels to your data source and format them to provide accurate and meaningful information in your charts.
keywords: Aspose.Cells for C++, charting, data labels, cell range, data source, formatting, accuracy, meaningful information.
type: docs
weight: 130
url: /cpp/showing-cell-range-as-the-data-labels/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In Microsoft Excel 2013, you can display a cell range for data labels. Aspose.Cells supports this feature.

{{% /alert %}}

## **Check-box to Show Cell Range as Data Labels**

To show the cell range as data labels in Microsoft Excel:

1. Select the series data labels and right-click to open the context menu.
1. Select **Format Data Labels**. Label options are displayed.
1. Select or clear the option **Label Contains - Value From Cells**.

The sample code below accesses a chart series data labels and sets the [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/) property to **true** to select the **Label Contains - Value From Cells** option.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
