---  
title: 调整图表数据标签形状以适应文本，支持 Node.js via C++  
linktitle: 调整图表数据标签形状以适应文本  
description: 学习如何在 Aspose.Cells for Node.js via C++ 中调整图表中数据标签的大小以适应文本。我们的指南将向您展示如何调整标签容器的大小和形状，以确保文本正确显示且无截断或重叠。  
keywords: Aspose.Cells for Node.js via C++，制图，数据标签，形状调整，文本适应，截断，重叠。  
type: docs  
weight: 220  
url: /zh/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
Excel应用程序提供了**调整形状以适应文本**选项，用于图表的数据标签，以增大形状的尺寸，以使文本适应其中。  
{{% /alert %}}  

## **如何在Microsoft Excel中调整图表数据标签的形状以适应文本**  

此选项可通过在 Excel 界面中选择图表上的任意数据标签，右键点击并选择 **格式数据标签** 菜单，然后在 **大小与属性** 标签下展开 **对齐方式**，以显示相关属性，包括 **调整形状以适应文本** 选项。  

## **使用 Aspose.Cells for Node.js via C++ 调整图表的数据标签形状以适应文本的方法**  

为了模仿Excel的调整数据标签形状以适应文本的功能，Aspose.Cells API已暴露布尔类型的[**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--)属性。以下代码展示了[**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--)属性的简单使用场景。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
