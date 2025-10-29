---  
title: 通过Node.js与C++管理Excel图表的轴  
description: 了解如何在Aspose.Cells for Node.js via C++中配置图表轴。我们的指南将向您展示如何调整主、次轴，设定范围以及修改其属性，以增强您的图表效果。  
keywords: Aspose.Cells for Node.js via C++，图表轴，配置，主轴，次轴，范围，属性。  
linktitle: 轴  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

在Excel图表中，有3种类型的轴：  
1. 横轴（类别轴）: X轴  
1. 垂直（值）轴：Y轴  
1. 深度（系列）轴：Z轴  

{{% /alert %}}  

## **轴选项**  
 Aspose.Cells for Node.js via C++还允许您在运行时管理图表的轴。使用[Axis](https://reference.aspose.com/cells/nodejs-cpp/axis/)对象，您可以像Excel中一样更改轴的所有选项。  

|![todo:image_alt_text](chart_axes.png)|  

## **管理X和Y轴**  
在Excel图表中，横轴和纵轴是最常用的两种轴。  

 以下代码片段演示了如何设置X轴和Y轴的选项。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **高级主题**  
- [更改刻度标签方向](/cells/zh/nodejs-cpp/change-tick-label-direction/)  
- [确定图表中存在哪些轴](/cells/zh/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [处理Microsoft Excel的图表轴的自动单位](/cells/zh/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [计算图表后读取轴标签](/cells/zh/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [如何在Excel图表中设置类别轴](/cells/zh/nodejs-cpp/how-to-set-category-axis/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
