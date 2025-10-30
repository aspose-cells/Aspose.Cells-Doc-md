---
title: Node.jsとC++を使用してコンボチャートを作成する方法
linktitle: コンボチャートの作成方法
description: Aspose.Cells for Node.js via C++を使用してコンボチャートを作成する方法を学びます。さまざまなチャートタイプを組み合わせて効果的なデータ提示を行う方法を解説します。
keywords: Aspose.Cells for Node.js via C++, コンボチャート, チャートタイプの組み合わせ, データ提示, 効果的な可視化。
type: docs
weight: 73
url: /ja/nodejs-cpp/create-combo-chart/
---

## **可能な使用シナリオ**
Excelのコンボチャートを使用すると、データを理解しやすくするために複数のチャートタイプを簡単に組み合わせることができます。コンボチャートは、価格と数量などのさまざまな種類のデータを含む場合に便利です。また、データの数値が系列ごとに大幅に変動する場合にもコンボチャートが有効です。
次のデータセットを例に取ると、これらのデータは[**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/)で言及されたデータに非常に類似していることがわかります。"総収入"に対応するseries0をラインチャートとして可視化したい場合は、どのように進めればよいでしょうか？

![todo:image_alt_text](sample.png)
## **コンボチャート**
以下のコードを実行すると、以下に示すようにコンボチャートが表示されます。

![todo:image_alt_text](result.png)
## **サンプルコード**
以下のサンプルコードは、[サンプルExcelファイル](combo.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "combo.xlsx");

// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a stock volume (VHLC)
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 15, 0, 34, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Combo Chart");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E12", true);
// Set category data 
chart.getNSeries().get(0).setXValues("A2:A12");  // Corrected method

// Set the Series[1] Series[2] and Series[3] to different Marker Style
for (let j = 0; j < chart.getNSeries().getCount(); j++) {
switch (j) {
case 1:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Circle);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Pink);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 2:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Orange);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 3:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Square);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.LightBlue);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
}
}
// Set the chart type for Series[0] 
chart.getNSeries().get(0).setType(AsposeCells.ChartType.Line);
// Set style for the border of first series
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Solid);
// Set Color for the first series
chart.getNSeries().get(0).getBorder().setColor(AsposeCells.Color.DarkBlue);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
