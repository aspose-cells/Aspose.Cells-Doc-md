---
title: Exportar CSS de la hoja de cálculo por separado en HTML de salida con C++
linktitle: Exportar la hoja de estilos CSS por separado en el HTML de salida
type: docs
weight: 80
url: /es/cpp/export-worksheet-css-separately-in-output/
description: Aprende cómo exportar el CSS de la hoja de trabajo por separado al convertir archivos de Excel a HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Aspose.Cells ofrece la función para exportar el CSS de la hoja de trabajo por separado cuando conviertes tu archivo de Excel a HTML. Por favor, usa la propiedad [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/) para este propósito y configúralo en **true** al guardar el archivo de Excel en formato HTML.

## **Exportar la hoja de estilos CSS por separado en el HTML de salida**

El siguiente código de ejemplo crea un archivo de Excel, agrega algo de texto en la celda **B5** en color **Rojo** y luego lo guarda en formato HTML usando la propiedad [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/). Por favor, consulta el [HTML de salida](60489766.zip) generado por el código para referencia. Encontrarás el archivo **stylesheet.css** dentro como resultado del código de ejemplo.

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Exportar libro de una sola hoja a HTML**

Cuando un libro con múltiples hojas se convierte a HTML usando Aspose.Cells, crea un archivo HTML junto con una carpeta que contiene CSS y múltiples archivos HTML. Cuando se abre este archivo HTML en el navegador, las pestañas son visibles. El mismo comportamiento es necesario para un libro con una sola hoja de trabajo cuando se convierte a HTML. Antes, no se creaba una carpeta separada para libros de una sola hoja, solo se creaba un archivo HTML. Dicho archivo HTML no muestra una pestaña al abrirlo en el navegador. MS Excel crea una carpeta y un HTML adecuados para una sola hoja también, por lo que se implementa el mismo comportamiento usando las API de Aspose.Cells. El archivo de ejemplo se puede descargar desde el siguiente enlace para usar en el código de ejemplo a continuación:

[sampleSingleSheet.xlsx](79527937.xlsx)

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
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
