---  
title: Node.jsを通じたC++でのスプレッドシート変換時のWordArtのグラデーション塗りつぶしのレンダリング  
linktitle: スプレッドシートをHTMLに変換する際のWordArtのグラデーションフィルをレンダリング  
type: docs  
weight: 90  
url: /ja/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Aspose.Cells for Node.js via C++を使用してスプレッドシートをHTMLに変換する際にWordArtのグラデーション塗りつぶしをレンダリングする方法を学びます。  
---  

## **可能な使用シナリオ**  
Aspose.Cells 17.1以前は、ExcelファイルをHTML形式に変換した際にWordArtのグラデーション塗りつぶしをレンダリングしませんでした。Aspose.Cells 17.1以降は、WordArtのグラデーション塗りつぶしがサポートされました。以下のスクリーンショットは、Aspose.Cells 17.1と旧バージョンを使用してExcelファイルを変換した際のグラデーション塗りつぶしの効果を比較したものです。  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **スプレッドシートをHTMLに変換する際のWordArtのグラデーションフィルをレンダリング**  
以下のサンプルコードは、[ソースExcelファイル](22774111.xlsx)を[出力HTML形式](22774109.zip)に変換します。ソースExcelファイルには、上記スクリーンショットのようなグラデーション塗りつぶしのWordArtオブジェクトが含まれています。  

## **サンプルコード**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceGradientFill.xlsx");

// Read the source excel file having text with gradient fill
const workbook = new AsposeCells.Workbook(filePath);

// Save workbook to html format
workbook.save(path.join(dataDir, "out_sourceGradientFill.html"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
