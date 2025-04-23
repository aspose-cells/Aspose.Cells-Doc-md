---  
title: Esporta Excel in HTML con Linee Griglia tramite Node.js  
linktitle: Esportare Excel in HTML con linee della griglia  
type: docs  
weight: 40  
url: /it/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: Impara come esportare un file Excel in formato HTML con Linee Griglia usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Se desideri esportare il tuo file Excel in HTML con Linee Griglia, utilizza la proprietà [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) e impostala su **true**.

{{% /alert %}}  
## **Esportare Excel in HTML con linee della griglia**  
Il codice di esempio seguente crea una cartella di lavoro, riempie il suo foglio con alcuni valori e lo salva in formato HTML dopo aver impostato [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) su **true**.  

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

