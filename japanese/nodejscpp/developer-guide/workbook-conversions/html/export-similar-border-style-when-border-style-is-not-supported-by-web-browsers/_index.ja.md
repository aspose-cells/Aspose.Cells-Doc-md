---  
title: Node.jsを使ったWebブラウザでサポートされていないBorder Styleの代替Border Styleのエクスポート方法  
linktitle: Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする  
type: docs  
weight: 70  
url: /ja/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Aspose.Cells for Node.js via C++を使ったExcelのHTML変換時にWebブラウザにサポートされていないボーダーをエクスポートする方法を学びます。  
---  

## **可能な使用シナリオ**  

Microsoft Excelは、Webブラウザではサポートされていない一部の破線境界線をサポートしています。これらのExcelファイルを HTML に変換する際にAspose.Cells for Node.js via C++を使用すると、そのような境界線は削除されます。ただし、Aspose.Cellsは[**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--)プロパティを設定することでこれらの境界線の表示もサポートできます。値を**true**に設定すると、サポートされていない境界線もHTMLファイルにエクスポートされます。  

## **Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする**  

次のサンプルコードは、いくつかのサポートされていないボーダーを含むExcelファイル（[サンプルExcelファイル](64716806.xlsx)）を読み込み、スクリーンショットは次のとおりです。[**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--)プロパティの効果も示しています。  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
