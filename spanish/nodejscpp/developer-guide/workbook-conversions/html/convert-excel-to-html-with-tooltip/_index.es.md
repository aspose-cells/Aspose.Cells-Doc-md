---  
title: Convertir Excel a HTML con tooltip usando Node.js mediante C++  
linktitle: Convertir Excel a HTML con tooltip  
type: docs  
weight: 200  
url: /es/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Aprende cómo convertir archivos Excel a formato HTML con tooltips para mostrar el texto completo usando Aspose.Cells for Node.js via C++.  
---  

## **Convertir Excel a HTML con tooltip**

Podría haber casos en los que el texto se recorta en el HTML generado y quieres mostrar el texto completo como tooltip al pasar el cursor. Aspose.Cells for Node.js via C++ soporta esto proporcionando la propiedad [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--). Configurar la propiedad [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) a **true** agregará el texto completo como tooltip en el HTML generado.

La siguiente imagen muestra el tooltip en el archivo HTML generado.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

El siguiente ejemplo carga el [archivo fuente de Excel](98107416.xlsx) y genera el [archivo HTML de salida](98107417.zip) con el tooltip.

Código de muestra

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

