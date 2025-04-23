---  
title: 使用Node.js通过C++创建高低收盘（HLC）股票图表  
linktitle: 创建高低收（HLC）股票图表  
description: 学习如何使用Aspose.Cells for Node.js via C++创建高低收盘股票图表。我们的逐步指南将演示如何在图表中绘制股票市场数据，包括最高价、最低价和收盘价，以便进行更好的分析和可视化。  
keywords: Aspose.Cells for Node.js, 高低收盘股票图表, 股票市场数据, 分析, 可视化。  
type: docs  
weight: 181  
url: /zh/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **可能的使用场景**  
高低收盘（HLC）股票图表使用四列数据。第一列是类别，通常是日期，也可以是股票名称。接下来的三列依次为最高价、最低价和收盘价。每个类别的价格范围由一条从最低到最高的垂直线表示，收盘价用向右延伸的刻度线显示。  

![todo:image_alt_text](sample.png)  
## **图表的可见性改进**  
有时，为了使图表看起来更直观，我们可以修改标记（收盘价）的外观，或者在辅助轴上显示它。  

![todo:image_alt_text](sample2.png)  
## **示例代码**  
以下示例代码加载[示例Excel文件](High-Low-Close.xlsx)并生成[输出Excel文件](out.xlsx)。  

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

