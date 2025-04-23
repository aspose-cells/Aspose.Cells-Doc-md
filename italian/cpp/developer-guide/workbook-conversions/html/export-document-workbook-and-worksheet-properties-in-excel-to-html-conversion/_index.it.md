---
title: Esporta le proprietà del documento, del workbook e del foglio di lavoro nella conversione Excel in HTML con C++
linktitle: Esporta le proprietà del documento, del workbook e del foglio di lavoro nella conversione Excel in HTML
type: docs
weight: 50
url: /it/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Impara come esportare o evitare di esportare le proprietà del Documento, Workbook e Foglio di lavoro durante la conversione di file Excel in HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Quando un file Microsoft Excel viene esportato in HTML usando Microsoft Excel o Aspose.Cells, vengono esportate anche varie tipologie di proprietà del Documento, del Workbook e del Foglio di lavoro, come mostrato nella schermata successiva. È possibile evitare di esportare queste proprietà impostando [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) e [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) su **false**. Il valore predefinito di queste proprietà è **true**. La schermata seguente mostra come appaiono in HTML esportato.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Esporta proprietà del Documento, del Workbook e del Foglio di lavoro nella conversione Excel in HTML**

Il codice di esempio di seguito carica il [file Excel di esempio](61767776.xlsx) e lo converte in HTML senza esportare le proprietà di Documento, Cartella di Lavoro e Foglio di Lavoro nell'[output HTML](61767779.zip).

## **Codice di Esempio**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html";

    // Load the sample Excel file
    Workbook workbook(inputFilePath);

    // Specify Html Save Options
    HtmlSaveOptions options;

    // We do not want to export document, workbook and worksheet properties
    options.SetExportDocumentProperties(false);
    options.SetExportWorkbookProperties(false);
    options.SetExportWorksheetProperties(false);

    // Export the Excel file to Html with Html Save Options
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file exported to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
