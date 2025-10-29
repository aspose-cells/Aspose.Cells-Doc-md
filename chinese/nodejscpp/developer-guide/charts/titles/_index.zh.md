---
title: 通过Node.js利用C++管理Excel图表标题
description: 学习如何使用Aspose.Cells for Node.js via C++在Microsoft Excel中添加和格式化图表及轴标题。我们的指南将展示如何设置不同类型的标题、调整外观以及修改轴标题以增强数据表现和清晰度。
keywords: Aspose.Cells for Node.js via C++，图表标题，轴标题，Microsoft Excel，数据表现，外观。
linktitle: 标题
type: docs
weight: 50
url: /zh/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

在Excel图表中，有两种标题：
1. 图表标题 
1. 轴标题

{{% /alert %}}

## **标题选项**
Aspose.Cells for Node.js via C++还支持在运行时管理图表的标题。通过[Title](https://reference.aspose.com/cells/nodejs-cpp/title/)对象，您可以更改标题的文本、字体和填充格式。

|![todo:image_alt_text](chart_title.png)|

## **设置图表或坐标轴的标题**
您可以使用Microsoft Excel在可视化编辑环境中设置图表及其轴的标题。Aspose.Cells for Node.js via C++还允许开发者在运行时设置图表及其轴的标题。所有图表及其轴都包含一个[Title](https://reference.aspose.com/cells/nodejs-cpp/title/)属性，可以用来设定标题，以下是示例。

以下代码片段演示了如何为图表和轴设置标题。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **高级主题**
- [从ODS文件中读取图表副标题](/cells/zh/nodejs-cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="nodejs-cpp" >}}
