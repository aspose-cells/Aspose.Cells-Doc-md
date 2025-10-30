---  
title: Exportar rango de área de impresión a HTML con Node.js a través de C++  
linktitle: Exportar rango de área de impresión a HTML  
type: docs  
weight: 60  
url: /es/nodejs-cpp/export-print-area-range-to/  
---  

## **Escenarios de uso posibles**

Este es un escenario común donde solo necesitamos exportar el área de impresión, es decir, un rango seleccionado de celdas, en lugar de toda la hoja a HTML. Esta función ya está disponible para renderizado en PDF, pero ahora también puedes hacerlo en HTML. Primero, establece el área de impresión en el objeto de configuración de página de la hoja. Luego, usa la bandera [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--) para exportar solo el rango seleccionado.

## Código de Muestra

El siguiente código de muestra carga un libro de trabajo y luego exporta el área de impresión al HTML. Puede descargar el archivo de muestra para probar esta característica desde el siguiente enlace:

[sampleInlineCharts.xlsx](79527946.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleInlineCharts.xlsx");

// Load the Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access the sheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area.
worksheet.getPageSetup().setPrintArea("D2:M20");

// Initialize HtmlSaveOptions
const options = new AsposeCells.HtmlSaveOptions();

// Set flag to export print area only
options.setExportPrintAreaOnly(true);

// Save to HTML format
const outputFilePath = path.join(dataDir, "outputInlineCharts.html");
workbook.save(outputFilePath, options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
