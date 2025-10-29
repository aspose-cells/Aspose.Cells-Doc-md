---
title: 如何通过C++在Node.js中创建Sunburst图表
linktitle: 如何创建旭日图表
description: 学习如何在Aspose.Cells for Node.js via C++中创建太阳放射图，此图以圆形展示数据。我们的指南将帮助你设置图表的各种属性和格式，包括数据标签、图例、颜色等。
keywords: Aspose.Cells for Node.js via C++，太阳放射图，创建，设置属性，数据标签，图例，格式，颜色，圆形，数据渲染。
type: docs
weight: 162
url: /zh/nodejs-cpp/creating-sunburst-chart/
---

## **可能的使用场景**
树状图非常适合比较层级内的比例；然而，树状图不擅长显示最大类别与每个数据点之间的层级关系。太阳放射图是更好的视觉图表，用于显示这些关系。太阳放射图理想于显示层级数据。每一层由一个环或圆圈表示，最内层代表层级顶部。没有层级数据（只有一层类别）的太阳放射图类似于甜甜圈图，但具有多个层级的太阳放射图展示了外环与内环的关系。太阳放射图最有效的用途是展示一环如何分解为其贡献部分，而另一种层级图表，树状图，则适合比较相对大小。

![todo:image_alt_text](sample.png)
## **旭日图表**
运行下面的代码后，您将会看到如下所示的旭日图表。

![todo:image_alt_text](result.png)
## **示例代码**
以下示例代码加载 [样本 Excel 文件](sunburst.xlsx) 并生成 [输出 Excel 文件](out.xlsx)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
