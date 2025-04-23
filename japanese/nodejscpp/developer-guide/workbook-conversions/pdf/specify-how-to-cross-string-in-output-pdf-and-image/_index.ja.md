---  
title: Node.js経由のC++を使って出力PDFや画像内の文字列のクロスマッピング方法を指定  
linktitle: 出力PDFおよびイメージで文字列をクロスする方法を指定します。  
type: docs  
weight: 120  
url: /ja/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Aspose.Cells for Node.js via C++を使用して、出力PDF/画像における文字のはみ出し制御を行う方法を学びます。  
---  

## **可能な使用シナリオ**

セルに文字列やテキストが含まれている場合、その文字列がセルの幅を超えると、次の列のセルがnullまたは空の場合に文字列がはみ出します。ExcelをPDF/画像に保存する際に、[**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype)列挙型を使用してこのはみ出しを制御できます。以下の値を持ちます：

- **TextCrossType.Default**：MS Excelのように次のセルに依存して文字列を表示。次のセルがnullの場合は文字列がはみ出すか切り詰められます。

- **TextCrossType.CrossKeep**：MS Excelのように文字列を表示し、PDFや画像にエクスポートします。

- **TextCrossType.CrossOverride**：文字列をすべて他のセルにまたがって表示し、また交差したセルのテキストを上書きします。

- **TextCrossType.StrictInCell**: セルの幅内で文字列のみを表示します。

## **TextCrossTypeを使用して出力PDF/イメージで文字列をクロスする方法を指定します。**

以下のサンプルコードは、サンプルのExcelファイルを読み込み、異なる[**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype)を指定してPDF／画像形式に保存します。サンプルExcelファイルと出力ファイルは以下のリンクからダウンロード可能です：

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### サンプルコード

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

