---
title: Ocultar contenido sobrepuesto con CrossHideRight al guardar en HTML con Node.js mediante C++
linktitle: Ocultar contenido superpuesto con CrossHideRight al guardar en HTML
type: docs
weight: 100
url: /es/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, puedes especificar diferentes tipos de cruce para cadenas de celdas. Por defecto, Aspose.Cells genera HTML según Microsoft Excel, pero cuando cambias el tipo de cruce a [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype), oculta todas las cadenas a la derecha de la celda que están sobrepuestas o que se superponen con la cadena de la celda.

## **Ocultar contenido superpuesto con CrossHideRight al guardar en Html**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](64716894.xlsx) y lo guarda en [HTML de salida](64716893.zip) después de configurar [**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--) como [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). La captura de pantalla explica cómo [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) afecta HTML de salida respecto a la salida predeterminada.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
