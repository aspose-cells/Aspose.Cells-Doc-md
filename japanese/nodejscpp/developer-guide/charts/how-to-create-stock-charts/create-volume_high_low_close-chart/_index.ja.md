---
title: Volume High Low Close（VHLC）株価チャートをNode.jsとC++で作成
linktitle: 出来高 高値 安値 終値（VHLC）株価チャートを作成する
description: Aspose.Cells for Node.js via C++を使ったボリュームハイロークローズ株価チャートの作成方法を学びましょう。市場データのボリューム、高値、安値、終値のプロット手順を解説します。
keywords: Aspose.Cells for Node.js via C++、ボリュームハイロークローズ株価チャート、市場データ、分析、ビジュアライゼーション。
type: docs
weight: 183
url: /ja/nodejs-cpp/create-volume-high-low-close-stock-chart/
---

## **可能な使用シナリオ**
次に紹介する株価チャートはボリュームハイロークローズチャートです。データの順番が正しいことが重要です。データテーブルを並べ替える必要がある場合は、チャート設定前に行ってください。
このチャートには、最初の（カテゴリー）列の直後にボリューム列があり、主要軸の上にこのボリュームを示す棒グラフがあり、価格は副軸に移動しています。

![todo:image_alt_text](data.png)
## **出来高-高値-安値-終値（VHLC）株価チャート**

![todo:image_alt_text](sample.png)
## **サンプルコード**
[サンプルExcelファイル](Volume-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series(Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
