---
title: Carica file Excel di origine senza grafici con C++
linktitle: Carica file Excel di origine senza grafici
type: docs
weight: 420
url: /it/cpp/load-source-excel-file-without-charts/
description: Impara come caricare un file Excel senza grafici usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells consente di caricare il file Excel senza grafici. Si usi la proprietà [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) a questo scopo.

{{% /alert %}}

## **Carica foglio di calcolo senza grafici**

Il seguente esempio carica il file Excel di esempio senza grafici e lo salva in formato PDF in output.

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
{{< app/cells/assistant language="cpp" >}}
