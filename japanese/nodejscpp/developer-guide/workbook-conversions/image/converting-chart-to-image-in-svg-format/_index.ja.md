---  
title: C++を使用したNode.js経由のSVG形式へのチャート変換  
linktitle: SVG形式でチャートを画像に変換  
type: docs  
weight: 240  
url: /ja/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Aspose.Cells for Node.js via C++を使用してチャートをSVG形式画像に変換する方法を学びます。  
---  

{{% alert color="primary" %}}  

スケーラブル・ベクター・グラフィックス（SVG）は、二次元グラフィックス用のXMLベースのベクター画像形式であり、対話性やアニメーションもサポートしています。SVG仕様は、1999年以来世界広範囲のウェブ consortium（W3C） によって開発されたオープンスタンダードです。  

SVG画像とその動作はXMLテキストファイルで定義されています。これにより、検索、索引付け、スクリプト作成、圧縮が可能です。SVG画像はXMLファイルとして任意のテキストエディタで作成および編集できますが、一般的には図形作成ソフトウェアで作成されます。  

Aspose.Cellsは、チャートをBMP、JPEG、PNG、GIF、SVGなどさまざまなフォーマットの画像として保存できます。この記事では、チャートをSVG形式に保存する方法を説明します。  

{{% /alert %}}  

次のサンプルコードは、Aspose.Cellsを使用してチャートをSVG形式の画像に変換する方法について説明しています。このコードは、ソースとなるMicrosoft Excelファイルを読み込み、次に最初のワークシートで見つかった最初のチャートをSVG形式で保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

