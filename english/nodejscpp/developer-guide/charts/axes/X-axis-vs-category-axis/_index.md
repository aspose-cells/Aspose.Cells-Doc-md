---
title: X Axis Vs. Category Axis with Node.js via C++
linktitle: X Axis Vs. Category Axis
description: Learn how to differentiate between the X axis and the Category axis in Aspose.Cells for Node.js via C++. Our guide will help you understand the differences in their usage and properties, and how to configure them according to your needs.
keywords: Aspose.Cells for Node.js via C++, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /nodejs-cpp/X-axis-vs-category-axis/
---

## **Possible Usage Scenarios**
There are different types of X axes. While the Y axis is a Value type axis, the X axis can be a Category type axis or a Value type axis. Using a Value axis, the data is treated as continuously varying numerical data, and the marker is placed at a point along the axis which varies according to its numerical value. Using a Category axis, the data is treated as a sequence of non-numerical text labels, and the marker is placed at a point along the axis according to its position in the sequence. The sample below illustrates the difference between Value and Category Axes.
Our sample data is shown in the [sample Table file](sample.png) below. The first column contains our X axis data, which can be treated as Categories or as Values. Note that the numbers are not equally spaced, nor do they even appear in numerical order.

![todo:image_alt_text](sample.png)
## **Handle X and Category axis like Microsoft Excel**
We will display this data on two types of chart, the first chart is XY (Scatter) chart X as Value Axis, the second chart is line chart X as Category Axis.

![todo:image_alt_text](compare.png)
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
