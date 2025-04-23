---  
title: Exportera Excel till HTML med gridlinjer via Node.js  
linktitle: Exportera Excel till HTML med rutnätslinjer  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: Lär dig hur du exporterar en Excel fil till HTML format med gridlinjer med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Om du vill exportera din Excel-fil till HTML med gridlinjer, använd då egenskapen [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) och ställ in den på **true**.

{{% /alert %}}  
## **Exportera Excel till HTML med rutnätslinjer**  
Följande exempel skapar en arbetsbok, fyller dess kalkylblad med värden och sparar den sedan i HTML-format efter att ha ställt in [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) på **true**.  

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

