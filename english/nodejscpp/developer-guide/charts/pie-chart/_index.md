---
title: Creating Pie Chart with Leader Lines using Node.js via C++
description: Learn how to use Aspose.Cells for Node.js via C++ to create a pie chart with leader lines in Microsoft Excel. Our guide will demonstrate how to add leader lines that connect data points to the legend and enhance the overall clarity of your chart.
keywords: Aspose.Cells for Node.js via C++, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: Pie Chart
type: docs
weight: 45
url: /nodejs-cpp/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

This article explains how to create a pie chart with leader lines from scratch while using Aspose.Cells for Node.js via C++ API. In Excel, the 'Show leader lines' option is set by default so when you create a pie chart in Excel the leader lines are shown. However, while creating a similar chart with Aspose.Cells APIs, you have to explicitly set the [**Series.hasLeaderLines**](https://reference.aspose.com/cells/nodejs-cpp/series/#hasLeaderLines) property.

{{% /alert %}}

To demonstrate the usage of Aspose.Cells for Node.js via C++ API to create a pie chart with leader lines, we will first create a new [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) and input some data that will serve as the series data source. Once the data is in place, we will add a [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) of type [**ChartType.Pie**](https://reference.aspose.com/cells/nodejs-cpp/charttype) to the collection of charts and set its different aspects to get the desired chart view.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);
```

So far we have created a pie chart and set its different aspects. Now we are going to turn on the leader lines for the chart. Please note, to show the leader lines, we have to move the data labels a little.

The following piece of code turns on the leader lines, refresh the chart, and then calculates the data labels' positions to move them accordingly.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);

// Turn on leader lines
chart.getNSeries().get(0).setHasLeaderLines(true);

// Calculate chart
chart.calculate();

// You need to move DataLabels a little leftward or rightward depending on their position to show leader lines
const DELTA = 100;
for (let i = 0; i < chart.getNSeries().get(0).getPoints().getCount(); i++) {
let X = chart.getNSeries().get(0).getPoints().get(i).getDataLabels().getX();
// If it is greater than 2000, then move the X position a little right otherwise move the X position a little left
if (X > 2000)
chart.getNSeries().get(0).getPoints().get(i).getDataLabels().setX(X + DELTA);
else
chart.getNSeries().get(0).getPoints().get(i).getDataLabels().setX(X - DELTA);
}
```

Finally, the following code saves the chart in image format and the workbook in XLSX format.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook in XLSX format
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);

// In order to save the chart image, create an instance of ImageOrPrintOptions
const anOption = new AsposeCells.ImageOrPrintOptions();

// Set image format
anOption.setImageType(AsposeCells.ImageType.Png);

// Set resolution
anOption.setHorizontalResolution(200);
anOption.setVerticalResolution(200);

// Render chart to image
chart.toImage(path.join(dataDir, "output_out.png"), anOption);

// Save the workbook to see chart inside the Excel
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

|**Resultant Pie Chart**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Advance topics**
- [Custom Slice or Sector Colors in Pie Chart](/cells/nodejs-cpp/custom-slice-or-sector-colors-in-pie-chart/)
- [Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart](/cells/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Related Articles

- [Creating Charts](/cells/nodejs-cpp/creating-charts/)
- [Customizing Charts](/cells/nodejs-cpp/customizing-charts/)
- [Data Formatting in Charts](/cells/nodejs-cpp/data-formatting-in-charts/)
- [Setting Chart Appearance](/cells/nodejs-cpp/setting-chart-appearance/)

