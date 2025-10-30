---
title: Volume Open High Low Close（VOHLC）株価チャートをC++とNode.jsで作成
description: Aspose.Cells for Node.js via C++を使用してボリュームオープンハイロークローズ株価チャートの作成方法を学びましょう。市場データのボリューム、始値、高値、安値、終値のプロット方法を解説します。
keywords: Aspose.Cells for Node.js via C++、ボリュームオープンハイロークローズ株価チャート、市場データ、分析、ビジュアライゼーション。
type: docs
weight: 184
url: /ja/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **可能な使用シナリオ**
次に紹介する株価チャートはボリュームオープンハイロークローズチャートです。データの順番を守ることが重要です。必要に応じてデータテーブルを並べ替えてください。このチャートには、最初の（カテゴリ）列の直後にボリュームの列があり、主要軸にこのボリュームを示す棒グラフを配置し、価格は副軸に移動しています。

![todo:image_alt_text](data.png)
## **出来高-オープン-高値-安値-終値（VOHLC）株価チャート**

![todo:image_alt_text](sample.png)
## **サンプルコード**
[サンプルExcelファイル](Volume-Open-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:F9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series (Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
