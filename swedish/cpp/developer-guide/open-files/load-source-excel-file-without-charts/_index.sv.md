---
title: Ladda käll Excel fil utan diagram med C++
linktitle: Ladda käll Excel fil utan diagram
type: docs
weight: 420
url: /sv/cpp/load-source-excel-file-without-charts/
description: Lär dig hur du laddar en Excel fil utan diagram med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells låter dig ladda din Excel-fil utan diagram. Vänligen använd [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) för detta ändamål.

{{% /alert %}}

## **Ladda kalkylblad utan diagram**

Följande exempel laddar exempel-Excel-filen utan diagram och sparar den i PDF-format.

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
