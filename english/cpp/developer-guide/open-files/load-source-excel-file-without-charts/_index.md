---
title: Load Source Excel File Without Charts with C++
linktitle: Load Source Excel File Without Charts
type: docs
weight: 420
url: /cpp/load-source-excel-file-without-charts/
description: Learn how to load an Excel file without charts using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to load your Excel file without charts. Please use [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/loadfilter/) property for this purpose.

{{% /alert %}}

## **Load Spreadsheet Without Charts**

The following sample code loads the sample Excel file without charts and saves it in output PDF format.

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

    // Specify the load options and filter the data
    LoadOptions options;

    // Include everything except charts
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xlsx";

    // Load the workbook with specified load options
    Workbook workbook(inputFilePath, options);

    // Path of output PDF file
    U16String outputFilePath = outDir + u"ResultWithoutChart.pdf";

    // Save the workbook in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully without charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```