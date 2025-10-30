---  
title: C++ を使用して Node.js 経由で Excel を PDF にレンダリングしながらタイムラインを描画  
linktitle: ExcelをPDFにレンダリングする際のタイムラインの描画  
type: docs  
weight: 60  
url: /ja/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: Aspose.Cells for Node.js via C++でExcelファイルのタイムライン管理  
keywords: Office 2013、Office 2016、Office 2019、および Office 365を使用せずに Node.js 経由で C++ によるタイムラインを PDF にレンダリングする方法  
---  

## **ExcelをPDFにレンダリングする際のタイムラインの描画**  
 タイムラインが適用された Excel ファイルがあり、タイムライン設定を含めて Excel を PDF にエクスポートしたい場合、Aspose.Cells for Node.js via C++はこれをデフォルトでサポートしています。タイムライン付きの Excel ファイルを PDF にエクスポートするだけで、生成された PDF にタイムラインが表示されます。  

以下のサンプルコードは、既存のタイムラインを含む[サンプルExcelファイル](input.xlsx)をロードします。その後、ワークブックを[出力PDFファイル](out.pdf)として保存します。以下のスクリーンショットは、ソースのExcelファイルと生成されたPDFファイルを比較したものです。  

<img src="out.png" width="60%">  

## **サンプルコード**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
