---
title: Quell Excel Datei ohne Diagramme mit C++ laden
linktitle: Quell Excel Datei ohne Diagramme laden
type: docs
weight: 420
url: /de/cpp/load-source-excel-file-without-charts/
description: Erfahren Sie, wie Sie eine Excel Datei ohne Diagramme mit Aspose.Cells und C++ laden.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, Ihre Excel-Datei ohne Diagramme zu laden. Bitte verwenden Sie die Eigenschaft [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) dafür.

{{% /alert %}}

## **Laden von Tabellenkalkulationen ohne Diagramme**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei ohne Diagramme und speichert sie im PDF-Format.

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
