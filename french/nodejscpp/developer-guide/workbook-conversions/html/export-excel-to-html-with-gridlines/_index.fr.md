---  
title: Exporter Excel en HTML avec lignes de grille via Node.js  
linktitle: Exporter Excel en HTML avec les lignes de grille  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: Apprenez comment exporter un fichier Excel en format HTML avec lignes de grille en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Si vous souhaitez exporter votre fichier Excel en HTML avec lignes de grille, utilisez la propriété [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) et réglez-la sur **true**.

{{% /alert %}}  
## **Exporter Excel au format HTML avec des lignes de grille**  
Le code d'exemple ci-dessous crée un classeur, remplit sa feuille avec quelques valeurs, puis le sauvegarde au format HTML après avoir réglé [HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--) sur **true**.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
