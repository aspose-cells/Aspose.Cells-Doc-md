---
title: 用Node.js通过C++创建开盘 最高 最低 收盘（OHLC）股票图表
description: 学习如何使用Aspose.Cells for Node.js via C++创建开盘 最高 最低 收盘股票图表。我们的指南将演示如何在图表中绘制股票市场数据，包括开盘价、最高价、最低价和收盘价，以便进行更好的分析和可视化。
keywords: Aspose.Cells for Node.js via C++, 开盘 最高 最低 收盘股票图表, 股票市场数据, 分析, 可视化。
type: docs
weight: 182
url: /zh/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **可能的使用场景**
开-高-低-收（OHLC）图表使用五列数据，分别是类别、开盘、最高、最低和收盘。每个类别的价格范围再次通过垂直线表示，开盘价格和收盘价格之间的范围由一个更宽的浮动条表示；如果该类别的价格上升（收盘价高于开盘价），则该条将填充一种颜色，而如果价格下降，则用另一种颜色填充。这种图表通常被称为蜡烛图。

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **图表的可见性改进**
我们通常用颜色而非黑白来表示价格的上涨与下降。在下面第一组蜡烛图中，红色表示上涨，绿色表示下降。

![todo:image_alt_text](sample2.png)
## **示例代码**
以下示例代码加载了[示例Excel文件](Open-High-Low-Close.xlsx)，并生成了[输出Excel文件](out.xlsx)。

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
