---
title: Exportar comentarios al guardar un archivo de Excel en HTML con Node.js a través de C++
linktitle: Exportar Comentarios al Guardar Archivo Excel en HTML
type: docs
weight: 40
url: /es/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, los comentarios no se exportan. Sin embargo, Aspose.Cells for Node.js via C++ ofrece esta función usando la propiedad [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). Si la configuras en **true**, los comentarios presentes en tu archivo de Excel también se mostrarán en el HTML.

## **Exportar comentarios al guardar archivo de Excel como HTML**

El siguiente código de muestra explica el uso de la propiedad [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). La captura de pantalla muestra el efecto del código en el HTML cuando está establecido en **verdadero**. Descargue el [archivo de Excel de muestra](50528260.xlsx) y el [HTML generado](5052826.txt) para referencia.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
