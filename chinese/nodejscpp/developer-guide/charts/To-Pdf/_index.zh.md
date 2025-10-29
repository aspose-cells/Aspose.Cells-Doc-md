---  
title: ## 通过Node.js利用C++将图表导出为PDF  
linktitle: 图表转换为PDF  
description: 学习如何使用Aspose.Cells for Node.js via C++将图表转换为PDF文档。本指南演示如何从Microsoft Excel导出图表并以PDF格式保存，以便进一步分发和归档。  
keywords: Aspose.Cells for Node.js via C++，图表转PDF，Microsoft Excel，PDF转换，导出，分发，归档。  
type: docs  
weight: 47  
url: /zh/nodejs-cpp/chart-to-pdf/  
---  

## **将图表渲染为PDF**

为了将图表渲染为PDF格式，Aspose.Cells API提供了[**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-)方法，可以将生成的PDF存储在磁盘路径或Stream中。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to PDF
chart.toPdf(path.join(dataDir, "chartPDF_out.pdf"));
```

## **使用所需的页面大小创建图表PDF**  
你可以使用Aspose.Cells创建符合你需求的页面大小的图表PDF，并指定图表在页面内的对齐方式（如顶部、底部、居中、左侧、右侧等）。输出图表可以保存在Stream中或存储在磁盘上。以下示例加载[示例Excel文件](64716906.xlsx)，访问工作表内的第一个图表，然后转换为[输出PDF](64716907.pdf)，并设置所需的页面尺寸。截图显示输出PDF的页面尺寸为7x7，符合代码中的规格，图表水平和垂直均居中。

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **示例代码**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing the chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateChartPDFWithDesiredPageSize.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet.
const chart = worksheet.getCharts().get(0);

// Create chart pdf with desired page size.
chart.toPdf(path.join(outputDir, "outputCreateChartPDFWithDesiredPageSize.pdf"), 7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
