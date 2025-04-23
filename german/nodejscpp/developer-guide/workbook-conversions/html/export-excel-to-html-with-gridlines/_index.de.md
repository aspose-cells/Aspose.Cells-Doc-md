---  
title: Excel nach HTML mit Gitterlinien exportieren via Node.js  
linktitle: Excel in HTML mit Gitterlinien exportieren  
type: docs  
weight: 40  
url: /de/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: Lernen Sie, wie Sie eine Excel Datei mit Gitterlinien im HTML Format mit Aspose.Cells for Node.js via C++ exportieren.  
---  

{{% alert color="primary" %}}  

Wenn Sie Ihre Excel-Datei mit Gitterlinien exportieren möchten, verwenden Sie bitte die [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) Eigenschaft und setzen Sie sie auf **true**.

{{% /alert %}}  
## **Excel in HTML mit Rasterlinien exportieren**  
Der folgende Beispielcode erstellt eine Arbeitsmappe, füllt das Arbeitsblatt mit einigen Werten und speichert sie anschließend im HTML-Format, nachdem die [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) auf **true** gesetzt wurde.  

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

