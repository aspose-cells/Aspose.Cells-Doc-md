---  
title: Node.js経由でC++を使用した印刷範囲をHTMLにエクスポート  
linktitle: HTMLに印刷エリア範囲をエクスポートする  
type: docs  
weight: 60  
url: /ja/nodejs-cpp/export-print-area-range-to/  
---  

## **可能な使用シナリオ**

印刷範囲、つまり選択したセル範囲のみをHTMLにエクスポートする必要がある一般的な場面です。この機能はすでにPDFレンダリングには利用可能ですが、今度はHTMLでも行えます。まず、ワークシートのページ設定オブジェクトに印刷範囲を設定し、その後、[**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--)フラグを使用して選択範囲だけをエクスポートします。

## サンプルコード

次のサンプルコードはワークブックをロードし、プリントエリアをHTMLにエクスポートします。この機能のテスト用にサンプルファイルを以下のリンクからダウンロードできます。

[sampleInlineCharts.xlsx](79527946.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleInlineCharts.xlsx");

// Load the Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access the sheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area.
worksheet.getPageSetup().setPrintArea("D2:M20");

// Initialize HtmlSaveOptions
const options = new AsposeCells.HtmlSaveOptions();

// Set flag to export print area only
options.setExportPrintAreaOnly(true);

// Save to HTML format
const outputFilePath = path.join(dataDir, "outputInlineCharts.html");
workbook.save(outputFilePath, options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
