---
title: Exporter les propriétés du classeur et des feuilles de calcul dans la conversion Excel en HTML avec C++
linktitle: Exporter les propriétés du document, du classeur et de la feuille de calcul dans la conversion Excel en HTML
type: docs
weight: 50
url: /fr/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Apprenez comment exporter ou éviter d exporter les propriétés du document, du classeur et de la feuille lors de la conversion de fichiers Excel en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Lorsqu’un fichier Microsoft Excel est exporté en HTML à l’aide de Microsoft Excel ou Aspose.Cells, il exporte également divers types de propriétés du document, du classeur et de la feuille comme indiqué dans la capture d’écran suivante. Vous pouvez éviter d’exporter ces propriétés en réglant [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) et [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) sur **false**. La valeur par défaut de ces propriétés est **true**. La capture d’écran suivante montre l’apparence de ces propriétés dans le HTML exporté.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exporter les propriétés du document, du classeur et de la feuille dans la conversion Excel en HTML**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767776.xlsx) et le convertit en HTML sans exporter les propriétés du document, du classeur et de la feuille de calcul dans le [HTML de sortie](61767779.zip).

## **Code d'exemple**

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
