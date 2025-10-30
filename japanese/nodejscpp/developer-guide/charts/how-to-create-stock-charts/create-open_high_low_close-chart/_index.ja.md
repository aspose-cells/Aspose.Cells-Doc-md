---
title: Open High Low Close（OHLC）株価チャートをC++を使ってNode.jsで作成
description: Aspose.Cells for Node.js via C++を使用してオープンハイロークローズ株価チャートの作成方法を学びましょう。市場データの始値、高値、安値、終値をチャートにプロットして分析と可視化に役立てます。
keywords: Aspose.Cells for Node.js via C++、オープンハイロークローズ株価チャート、市場データ、分析、ビジュアライゼーション。
type: docs
weight: 182
url: /ja/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **可能な使用シナリオ**
Open-High-Low-Close（OHLC）チャートは、カテゴリ、オープン、ハイ、ロー、クローズのデータを使用し、価格の範囲は垂直線で示され、オープンからクローズまでの範囲はより広い浮動バーで示されます。カテゴリ内で価格が上昇する場合（クローズがオープンより高い場合）、バーは1つの色で塗りつぶされ、価格が下落する場合は別の色で塗りつぶされます。この種のチャートは、ローソク足チャートと呼ばれることがよくあります。

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **チャートの可視性の改善**
価格の上昇と下降を示すために黒白よりも色をよく使用します。下の最初のキャンドルスティックのセットでは、赤は上昇、緑は下降を示しています。

![todo:image_alt_text](sample2.png)
## **サンプルコード**
[サンプルExcelファイル](Open-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().getCategoryData("A2:A9");
// Set the DownBars and UpBars with different color
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Red);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
