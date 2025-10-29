---  
title: 通过Node.js和C++管理Excel图表的数据标签  
description: 学习如何使用Aspose.Cells for Node.js via C++有效管理Excel图表中的数据标签。本指南涵盖添加、删除和修改标签等各种管理任务，以增强图表的可读性和实用性。  
keywords: Aspose.Cells for Node.js，Excel图表，数据标签，管理，可读性，用途，添加，删除，修改。  
linktitle: 数据标签  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

数据标签是图表的重要组成部分。  
我们可以轻松地了解每个系列的值、百分比等。  

{{% /alert %}}  

## **数据标签选项**  
Aspose.Cells for Node.js via C++还允许在运行时管理图表的数据标签，使用[DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/)对象，简单地移动、更新和格式化图表的数据标签。  

|![todo:image_alt_text](chart_datalabels.png)|  

## **管理图表的数据标签**  
 使用Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/)轻松管理图表的数据标签。  

以下代码片段演示了如何管理DataLabels：  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **高级主题**  
- [向图表系列的数据点添加自定义标签](/cells/zh/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [禁用图表的数据标签文本换行](/cells/zh/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [调整图表数据标签形状以适应文本](/cells/zh/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [图表点的富文本自定义数据标签](/cells/zh/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [设置图表数据标签的形状类型](/cells/zh/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [将单元格范围显示为数据标签](/cells/zh/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
