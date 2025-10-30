---  
title: Exportar CSS de la hoja de cálculo por separado en HTML de salida con Node.js mediante C++  
linktitle: Exportar la hoja de estilos CSS por separado en el HTML de salida  
type: docs  
weight: 80  
url: /es/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: Aprende cómo exportar CSS de la hoja de cálculo por separado al convertir un archivo de Excel a HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**

Aspose.Cells for Node.js via C++ ofrece la función para exportar el CSS de la hoja de cálculo por separado al convertir tu archivo de Excel a HTML. Por favor, usa la propiedad [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--) para este propósito y configúrala como **true** al guardar el archivo de Excel en formato HTML.

## **Exportar la hoja de estilos CSS por separado en el HTML de salida**

El siguiente código de ejemplo crea un archivo de Excel, agrega algo de texto en la celda **B5** en color **Rojo** y luego lo guarda en formato HTML usando la propiedad [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--). Por favor, mira el [HTML de salida](60489766.zip) generado por el código para referencia. Encontrarás **stylesheet.css** dentro de él como resultado del código de ejemplo.

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **Exportar un libro de una sola hoja a HTML**

Cuando un libro de trabajo con varias hojas se convierte a HTML usando Aspose.Cells for Node.js via C++, crea un archivo HTML junto con una carpeta que contiene CSS y múltiples archivos HTML. Cuando abres este archivo HTML en el navegador, las pestañas son visibles. El mismo comportamiento es necesario para un libro con una sola hoja de trabajo cuando se convierte a HTML. Antes, no se creaba una carpeta separada para libros con una sola hoja, y solo se generaba un archivo HTML. Dicho archivo HTML no muestra pestañas al abrirse en el navegador. MS Excel también crea la carpeta adecuada y HTML para una sola hoja, por lo que se implementa el mismo comportamiento usando las APIs de Aspose.Cells. El archivo de ejemplo se puede descargar desde el siguiente enlace para usar en el código de ejemplo a continuación:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
