---
title: Esporta l area di stampa in HTML con C++
linktitle: Esporta l area di stampa in HTML
type: docs
weight: 60
url: /it/cpp/export-print-area-range-to/
description: Impara come esportare l area di stampa in HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Questo è uno scenario comune in cui è necessario esportare solo l'area di stampa, ovvero un intervallo di celle selezionato, invece di tutto il foglio in HTML. Questa funzione è già disponibile per la generazione PDF; tuttavia, ora puoi eseguire questa operazione anche per HTML. Per prima cosa, imposta l'area di stampa nell'oggetto layout della pagina del foglio di lavoro. Poi, usa il flag [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/) per esportare solo l'intervallo selezionato.

## **Codice di Esempio**

Il seguente esempio di codice carica un workbook e successivamente esporta l'area di stampa in HTML. Il file di esempio per testare questa funzione può essere scaricato dal seguente link:

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
{{< app/cells/assistant language="cpp" >}}
