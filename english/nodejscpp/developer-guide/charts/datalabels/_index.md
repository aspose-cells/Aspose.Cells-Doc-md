---  
title: Manage DataLabels of Excel Charts with Node.js via C++  
description: Learn how to effectively manage data labels in Excel charts using Aspose.Cells for Node.js via C++. This comprehensive guide covers various management tasks, including adding, removing, and modifying labels to enhance chart readability and usability.  
keywords: Aspose.Cells for Node.js, Excel charts, data labels, management, readability, usability, adding, removing, modifying.  
linktitle: DataLabels  
type: docs  
weight: 50  
url: /nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

DataLabels are an important part of a chart.  
We can easily know the value, percentage, etc. of each series  

{{% /alert %}}  

## **DataLabels Options**  
Aspose.Cells for Node.js via C++ also allows managing chart's datalabels at runtime, with the [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/) object, it's simple to move, update and format datalabels of the chart.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Manage the DataLabels of Chart**  
It's simple to manage datalabels of the chart with Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/).  

The following code snippet demonstrates how to manage DataLabels:  

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

## **Advance topics**  
- [Adding Custom Labels to Data Points in the Series of the Chart](/cells/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Disable Text Wrapping for Data Labels of the Chart](/cells/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Resize Chart's Data Label Shape To Fit Text](/cells/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Rich Text Custom Data Label of Chart Point](/cells/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Set the Shape Type of Data Labels of Chart](/cells/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Showing Cell Range as the Data Labels](/cells/nodejs-cpp/showing-cell-range-as-the-data-labels/)  
  