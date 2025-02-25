---  
title: Add WordArt Watermark to Chart with Node.js via C++  
linktitle: Add WordArt Watermark to Chart  
description: Learn how to use Aspose.Cells for Node.js via C++ to add a WordArt watermark to a chart in Microsoft Excel. Our guide will demonstrate how to create and position a WordArt watermark to enhance the visual appeal and uniqueness of your chart.  
keywords: Aspose.Cells for Node.js, WordArt Watermark, Chart Watermark, Microsoft Excel, Visual Appeal, Chart Uniqueness.  
type: docs  
weight: 50  
url: /nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

You can use WordArt to add special text effects to spreadsheets. For example, stretch a title, decorate text, make the text fit a preset shape, or apply the affected text to a chart’s plot area as a watermark. The WordArt becomes an object that you can move or position in your spreadsheets to add decoration.  

The following example shows how to add a WordArt shape as a watermark for the chart plot area.  

{{% /alert %}}  

The following example shows how to add a WordArt shape as a watermark for an existing chart’s plot area.  

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
  