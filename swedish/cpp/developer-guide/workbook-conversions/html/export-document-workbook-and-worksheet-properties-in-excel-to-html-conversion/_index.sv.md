---
title: Exportera dokumentbok och kalkylbladsattribut i Excel till HTML omvandling
linktitle: Exportera dokumentbok och kalkylbladsattribut i Excel till HTML omvandling
type: docs
weight: 50
url: /sv/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Lär dig hur du exporterar eller undviker att exportera dokument , arbetsboks och kalkylbladsattribut vid konvertering av Excel till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När en Microsoft Excel-fil exporteras till HTML med Microsoft Excel eller Aspose.Cells, exporteras även olika typer av dokument-, arbetsboks- och kalkylbladsattribut, som visas i följande skärmbild. Du kan undvika att exportera dessa egenskaper genom att ställa in [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) och [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) till **false**. Standardvärdet är **true**. Följande skärmbild visar hur dessa egenskaper ser ut i exporterad HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportera dokument-, arbetsboks- och kalkylbladsattribut i Excel till HTML-omvandling**

Följande exempel kod laddar [exempel-Excel-filen](61767776.xlsx) och konverterar den till HTML utan att exportera dokument-, arbetsboks- och kalkylbladsattribut i [utdata-HTML](61767779.zip).

## **Exempelkod**

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
{{< app/cells/assistant language="cpp" >}}
