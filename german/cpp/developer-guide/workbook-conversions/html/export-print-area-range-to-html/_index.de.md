---
title: Exportiere Druckbereichsbereich nach HTML mit C++
linktitle: Exportiere Druckbereichsbereich nach HTML
type: docs
weight: 60
url: /de/cpp/export-print-area-range-to/
description: Erfahren Sie, wie Sie den Druckbereichsbereich mit Aspose.Cells for C++ nach HTML exportieren.
---

## **Mögliche Verwendungsszenarien**

Dies ist ein häufiges Szenario, bei dem nur der Druckbereich, also ein ausgewählter Zellbereich, anstelle des gesamten Blatts nach HTML exportiert werden soll. Diese Funktion ist bereits für die PDF-Renderung verfügbar; jetzt können Sie diese Aufgabe auch für HTML ausführen. Zunächst setzen Sie den Druckbereich im Seiten-Setup-Objekt des Arbeitsblatts. Später verwenden Sie das [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/)-Flag, um nur den ausgewählten Bereich zu exportieren.

## **Beispielcode**

Der folgende Beispielcode lädt eine Arbeitsmappe und exportiert dann den Druckbereich nach HTML. Die Testdatei für diese Funktion kann von folgendem Link heruntergeladen werden:

[sampleInlineCharts.xlsx](79527946.xlsx)

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
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
