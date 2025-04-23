---  
title: Node.jsを使ったグリッド線付きExcelのHTMLへのエクスポート  
linktitle: グリッドライン付きでExcelをHTMLにエクスポートする  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/export-excel-to-html-with-gridlines/  
description: Aspose.Cells for Node.js via C++を使用して、グリッド線付きのExcelファイルをHTML形式にエクスポートする方法を学びます。  
---  

{{% alert color="primary" %}}  

[HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--)プロパティを使用して、グリッド線付きのExcelをHTMLにエクスポートし、**true**に設定してください。

{{% /alert %}}  
## **グリッドライン付きでExcelをHTMLにエクスポートする**  
次のサンプルコードは、ワークブックを作成し、いくつかの値を入力して、その後[HtmlSaveOptions.getExportGridLines()](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportGridLines--)を**true**に設定してHTML形式で保存します。  

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

