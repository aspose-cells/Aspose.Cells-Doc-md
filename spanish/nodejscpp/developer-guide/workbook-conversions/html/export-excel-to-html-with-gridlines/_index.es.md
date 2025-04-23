---  
title: Exportar Excel a HTML con cuadrícula de líneas usando Node.js  
linktitle: Exportar Excel a HTML con Líneas de Cuadrícula  
type: docs  
weight: 40  
url: /es/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: Aprende cómo exportar un archivo de Excel a formato HTML con líneas de cuadrícula usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Si deseas exportar tu archivo de Excel en HTML con líneas de cuadrícula, utiliza la propiedad [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) y configúrala en **true**.

{{% /alert %}}  
## **Exportar Excel a HTML con Líneas de Cuadrícula**  
El siguiente código de ejemplo crea un libro, llena su hoja con algunos valores y luego lo guarda en formato HTML después de configurar [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) en **true**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create your workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Fill worksheet with some integer values
for (let r = 0; r < 10; r++) {
for (let c = 0; c < 10; c++) {
ws.getCells().get(r, c).putValue(r * 1);
}
}

// Save your workbook in HTML format and export gridlines
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportGridLines(true);
wb.save(path.join(dataDir, "ExportToHTMLWithGridLines_out.html"), opts);
```  

