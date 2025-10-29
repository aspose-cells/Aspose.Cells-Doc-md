---
title: 用Node.js通过C++创建成交量 最高 最低 收盘（VHLC）股票图表
linktitle: 创建成交量高低收（VHLC）股票图表
description: 学习如何使用Aspose.Cells for Node.js via C++创建成交量 最高 最低 收盘股票图表。我们的指南将演示如何在图表中绘制股票市场数据，包括成交量、最高价、最低价和收盘价，以便进行更好的分析和可视化。
keywords: Aspose.Cells for Node.js via C++, 成交量 最高 最低 收盘股票图表, 股票市场数据, 分析, 可视化。
type: docs
weight: 183
url: /zh/nodejs-cpp/create-volume-high-low-close-stock-chart/
---

## **可能的使用场景**
我们要看的第三个股票图表是成交量最高-最低-收盘图。再次强调，必须确保数据的顺序正确。如果需要重新排列数据表，应该在设置图表之前完成。
此图表在第一个（类别）列之后立即包含一列成交量，图表包括在主轴上的一列显示成交量，而价格数据移至次轴。

![todo:image_alt_text](data.png)
## **成交量高低收（VHLC）股票图表**

![todo:image_alt_text](sample.png)
## **示例代码**
以下示例代码加载了 [样本Excel文件](Volume-High-Low-Close.xlsx) 并生成了 [输出Excel文件](out.xlsx)。

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
{{< app/cells/assistant language="nodejs-cpp" >}}
