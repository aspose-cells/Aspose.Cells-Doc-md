---  
title: 通过C++用Node.js处理类似微软Excel的图表轴自动单位  
linktitle: 处理图表轴的自动单位，类似Microsoft Excel  
description: 了解如何在Aspose.Cells for Node.js via C++中处理图表轴的自动单位。我们的指南将向您展示如何配置和自定义图表轴的自动单位，包括科学记数法的显示和缩放调整。  
keywords: Aspose.Cells for Node.js via C++、图表轴、自动单位、微软Excel、配置、定制、科学记数法、缩放。  
type: docs  
weight: 120  
url: /zh/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **可能的使用场景**  
早期版本的Aspose.Cells for Node.js via C++在渲染图表为图片或PDF时，不能正确处理图表轴的自动单位。现在，Aspose.Cells for Node.js via C++支持图表轴自动单位的处理。无需代码更改，只需将您的图表转换为图片或PDF，它将像微软Excel那样渲染图表轴。  

## **处理Microsoft Excel的图表轴的自动单位**  
以下示例代码加载了[示例Excel文件](61767755.xlsx)，并生成了[输出PDF图表](61767752.pdf)。截图显示了红色矩形中的图表轴自动单位，并且还将示例Excel文件中的图表与输出的PDF图表进行了比较，两者完全相同。  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **示例代码**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
