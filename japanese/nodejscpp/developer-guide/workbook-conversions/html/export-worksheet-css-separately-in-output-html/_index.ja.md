---  
title: Node.js経由でC++を使用した出力HTMLに別途Worksheet CSSをエクスポート  
linktitle: 出力HTMLでワークシートのCSSを別々にエクスポートする  
type: docs  
weight: 80  
url: /ja/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: ExcelファイルをHTMLに変換する際に、ワークシートのCSSを個別にエクスポートする方法をAspose.Cells for Node.js via C++で学習します。  
---  

## **可能な使用シナリオ**

Aspose.Cells for Node.js via C++は、ExcelをHTMLに変換する際にworksheetのCSSを別にエクスポートする機能を提供しています。そのための[**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--)プロパティを使用し、HTMLに保存する際に**true**に設定します。

## **出力HTMLでワークシートのCSSを別々にエクスポートする**

次のサンプルコードは、Excelファイルを作成し、セル**B5**に赤色のテキストを追加して保存します。[**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--)プロパティを使ったHTML形式で保存し、参考として[出力HTML](60489766.zip)も確認できます。サンプルコードによって生成された状態では**stylesheet.css**も含まれています。

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **単一のシートのワークブックをHTMLにエクスポートする**

複数シートのあるワークブックをAspose.Cells for Node.js via C++を使用してHTMLに変換すると、CSSを含むフォルダと複数のHTMLファイルが作成されます。これらのHTMLファイルをブラウザで開くとタブが表示されます。同じ動作は、シートが1つだけのワークブックでも必要です。過去の方法では、シートが1つだけのワークブックには別フォルダは作成されず、HTMLファイルのみが作成されていましたが、そのHTMLをブラウザで開くとタブは表示されません。MS Excelは、シングルシートワークブック用に適切なフォルダとHTMLを作成します。同様の動作をAspose.Cells APIで実現しています。サンプルファイルは以下のリンクからダウンロードできます。

[sampleSingleSheet.xlsx](79527937.xlsx)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

