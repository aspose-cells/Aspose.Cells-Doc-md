---  
title: Exportar estilo de borde similar cuando el estilo de borde no es soportado por navegadores web con Node.js a través de C++  
linktitle: Exportar un Estilo de Borde Similar cuando el Estilo de Borde no es compatible con los Navegadores Web  
type: docs  
weight: 70  
url: /es/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Aprende cómo exportar bordes que no son soportados por navegadores web al convertir archivos de Excel a HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Microsoft Excel soporta algunos tipos de bordes discontinuos que no son compatibles con los navegadores web. Cuando conviertes un archivo de Excel en HTML usando Aspose.Cells for Node.js via C++, estos bordes se eliminan. Sin embargo, Aspose.Cells también puede soportar la visualización de estos bordes con la propiedad [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--). Por favor, configura su valor como **true** y los bordes no soportados también se exportarán al archivo HTML.  

## **Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web**  

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](64716806.xlsx) que contiene algunos bordes no soportados como se muestra en la siguiente captura de pantalla. La captura ilustra además el efecto de la propiedad [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) dentro del [HTML de salida](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

