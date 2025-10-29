---
title: 使用 C++ 通过 Node.js 管理 Excel 图表的图例
description: 学习如何利用Aspose.Cells for Node.js via C++有效利用和自定义 Microsoft Excel 中的图表图例。我们的全面指南解释了图例的功能，如何访问和修改它，以及如何通过图例改善可视化和数据理解。
keywords: Aspose.Cells for Node.js via C++，图表图例，Microsoft Excel，可视化，数据理解。
linktitle: 图例
type: docs
weight: 50
url: /zh/nodejs-cpp/chart-legend/
---

## **图例选项**
Aspose.Cells for Node.js via C++ 也允许在运行时管理图表的图例。 [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/) 对象可以移动、更新和格式化。

|![todo:image_alt_text](chart_legend.png)|

## **设置图表的图例**
使用 Aspose.Cells [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/) 很容易管理图表的图例。

以下代码片段演示如何管理图例：


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Move the legend to left
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Left);

// Set font color of the legend
chart.getLegend().getFont().setColor(AsposeCells.Color.Blue);

// Save the file
workbook.save("chart_legend.xlsx");
```

## **高级主题**
- [使用Aspose.Cells将图例条目填充的文本设置为无](/cells/zh/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
