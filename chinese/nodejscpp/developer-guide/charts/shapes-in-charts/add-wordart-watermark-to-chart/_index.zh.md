---  
title: 使用Node.js via C++在图表上添加WordArt水印  
linktitle: 向图表添加WordArt水印  
description: 学习如何使用Aspose.Cells for Node.js via C++在Microsoft Excel的图表中添加WordArt水印。我们的指南将演示如何创建和定位WordArt水印，以增强图表的视觉吸引力和独特性。  
keywords: Aspose.Cells for Node.js，WordArt水印，图表水印，Microsoft Excel，视觉吸引力，图表唯一性。  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

您可以使用WordArt向电子表格添加特殊文本效果。例如，可以拉伸标题、装饰文本、使文本适应预设形状，或将受影响的文本应用到图表的绘图区作为水印。WordArt成为一个对象，您可以在电子表格中移动或定位以添加装饰。  

以下示例显示如何向图表的绘图区添加WordArt形状作为水印。  

{{% /alert %}}  

以下示例显示如何为现有图表的绘图区添加WordArt形状作为水印。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Open the existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add a WordArt watermark (shape) to the chart's plot area.
const wordart = chart.getShapes().addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

// Get the shape's fill format.
const wordArtFormat = wordart.getFill();

// Set the transparency.
wordArtFormat.setTransparency(0.9);

// Get the line format.
const lineFormat = wordart.getLine();

// Set Line format to invisible.
lineFormat.setWeight(0.0);

// Save the excel file.
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

