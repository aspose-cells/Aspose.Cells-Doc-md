---  
title: Node.jsとC++を使ったHigh Low Close（HLC）株価チャートの作成  
linktitle: HLC(高値 安値 終値)株価チャートの作成  
description: Aspose.Cells for Node.js via C++を使用してハイロークローズ株価チャートの作成方法を学びましょう。ステップバイステップのガイドでは、市場データの高値、安値、終値をチャートにプロットして分析と可視化を向上させる方法を説明します。  
keywords: Aspose.Cells for Node.js、ハイロークローズ株価チャート、市場データ、分析、ビジュアライゼーション。  
type: docs  
weight: 181  
url: /ja/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **可能な使用シナリオ**  
ハイロークローズ（HLC）株価チャートは4つのデータ列を使用します。最初の列はカテゴリ（通常は日付、株名も使用可）、次の3列は高値、安値、終値です。各カテゴリーの価格範囲は、低値から高値までの垂直線で示され、終値はこの線の右側に伸びるティックマークで表示されます。  

![todo:image_alt_text](sample.png)  
## **チャートの可視性の改善**  
時には、チャートを直感的に見やすくするために、マーカー（終値）の外観を修正したり、2次軸に表示したりすることがあります。  

![todo:image_alt_text](sample2.png)  
## **サンプルコード**  
次のサンプルコードは[sample Excel file](High-Low-Close.xlsx)をロードし、[output Excel file](out.xlsx)を生成します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:D9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set the marker with the built-in data 
chart.getNSeries().get(2).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(2).getMarker().setMarkerSize(20);
chart.getNSeries().get(2).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(2).getMarker().getArea().setForegroundColor(AsposeCells.Color.Maroon);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
