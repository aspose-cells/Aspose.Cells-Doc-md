---
title: Exportar rango de área de impresión a HTML con C++
linktitle: Exportar rango de área de impresión a HTML
type: docs
weight: 60
url: /es/cpp/export-print-area-range-to/
description: Aprenda cómo exportar el rango del área de impresión a HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Este es un escenario común donde necesitamos exportar solo el área de impresión, es decir, un rango seleccionado de celdas, en lugar de toda la hoja a HTML. Esta función ya está disponible para renderizado en PDF; sin embargo, ahora también puede realizar esta tarea en HTML. Primero, configure el área de impresión en el objeto de configuración de página de la hoja. Luego, use la bandera [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/) para exportar solo el rango seleccionado.

## **Código de muestra**

El siguiente código de ejemplo carga un libro y luego exporta el área de impresión a HTML. El archivo de prueba para esta función se puede descargar desde el siguiente enlace:

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
