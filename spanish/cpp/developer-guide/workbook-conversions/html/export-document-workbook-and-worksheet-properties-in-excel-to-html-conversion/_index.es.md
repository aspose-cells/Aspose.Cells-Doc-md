---
title: Exportar Propiedades del Libro y de la Hoja de Cálculo en la conversión de Excel a HTML con C++
linktitle: Exportar Propiedades del Libro y de la Hoja en la conversión de Excel a HTML
type: docs
weight: 50
url: /es/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Aprenda cómo exportar o evitar exportar propiedades del Documento, Libro y Hoja de cálculo al convertir archivos de Excel en HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando un archivo de Microsoft Excel se exporta a HTML usando Microsoft Excel o Aspose.Cells, también exporta varios tipos de propiedades del Documento, Libro y Hoja de cálculo como se muestra en la siguiente captura de pantalla. Puedes evitar exportar estas propiedades configurando [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) y [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) en **false**. El valor predeterminado de estas propiedades es **true**. La siguiente captura muestra cómo se ven estas propiedades en el HTML exportado.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportar Propiedades del Documento, Libro y Hoja en la conversión de Excel a HTML**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767776.xlsx) y lo convierte a HTML sin exportar las propiedades del Documento, Libro y Hoja en el [HTML de salida](61767779.zip).

## **Código de muestra**

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
