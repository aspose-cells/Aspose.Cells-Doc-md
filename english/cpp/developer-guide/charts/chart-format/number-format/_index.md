---
title: Set the Values Format Code of Chart Series with C++
linktitle: Number Format
type: docs
weight: 100
url: /cpp/set-the-values-format-code-of-chart-series/
description: Learn how to set the values format code of chart series in Aspose.Cells for C++. Our guide will help you understand how to format your chart series data using the appropriate format code, allowing you to present your data accurately and professionally.
keywords: Aspose.Cells for C++, chart series, values format code, formatting, data presentation, accuracy, professionalism.
---

## **Possible Usage Scenarios**
You can set the values format code of chart series using the [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) property. This property is not only useful for the series which is based on the range inside the worksheet but also works well for the series created with an array of values.

## **Set the Values Format Code of Chart Series**
The following sample code adds a series in the empty chart which has no series before. It adds the series using the array of values. Once, it adds the series, it formats it with the code `$#,##0` using the [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) property and the number `10000` becomes `$10,000`. The screenshot shows the effect of code on the [sample Excel file](51740712.xlsx) and [output Excel file](51740713.xlsx) after execution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Sample Code**
```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```