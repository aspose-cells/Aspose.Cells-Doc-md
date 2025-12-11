---
title: Manipulate Position, Size, and Designer Chart with Node.js via C++
linktitle: Manipulate Position, Size, and Designer Chart
description: Learn how to use Aspose.Cells for Node.js via C++ to effectively manipulate the position, size, and designer chart in Microsoft Excel. Our guide will demonstrate how to adjust these properties for improved layout and visualization.
keywords: Aspose.Cells for Node.js via C++, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /nodejs-cpp/manipulate-position-size-and-designer-chart/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Chart Position and Size**
Sometimes, you want to change the position or size of a new or existing chart inside the worksheet. Aspose.Cells provides the [Chart.getChartObject()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getChartObject--) property to achieve this. You can use its sub‑properties to resize the chart with new **height** and **width** or reposition it with new **X** and **Y** coordinates.

### **Controlling Chart Position and Size**
To change the chart's position (X, Y coordinates) or size (height, width), use these properties:

1. [Shape.getX()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getX--)
2. [Shape.getY()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getY--)
3. [Shape.getHeight()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getHeight--)
4. [Shape.getWidth()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getWidth--)

The following example explains the usage of the above APIs; it loads an existing workbook that contains a chart in its first worksheet, then resizes and repositions the chart using Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart.xls");

// Loads the workbook which contains the chart
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(1);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

// Resize the chart
chart.getChartObject().setWidth(400);
chart.getChartObject().setHeight(300);

// Reposition the chart
chart.getChartObject().setX(250);
chart.getChartObject().setY(150);

// Output the file
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Manipulating Designer Charts**
There are times when you need to manipulate or modify charts in designer template files. Aspose.Cells fully supports manipulating designer chart contents and elements. The data, chart contents, background image, and formatting can be preserved with accuracy.

### **Manipulating Designer Charts in Template Files**
To manipulate designer charts in template files, use the chart‑related API. For example, you may use the `Worksheet.getCharts()` property to get the existing charts collection in the template file.

#### **Creating a Chart**
The following example shows how to create a pyramid chart. We will manipulate this chart later on.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Manipulating the Chart**
The following example shows how to manipulate the existing chart. In this example, we modify the chart created above. In the generated output, note that the data label of one data point has been set to “United Kingdom, 30K”.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "piechart.xls");

// Loads the existing file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Get the data labels in the data series of the third data point.
const dataLabels = chart.getNSeries().get(0).getPoints().get(2).getDataLabels();

// Change the text of the label.
dataLabels.setText("United Kingdom, 400K");

// Save the Excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Manipulating a Line Chart in the Designer Template**
In this example, we will manipulate a line chart. We will add some data series to the existing chart and change their line colors.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Get the designer chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add the third data series to it.
chart.getNSeries().add("{60, 80, 10}", true);

// Add another data series (fourth) to it.
chart.getNSeries().add("{0.3, 0.7, 1.2}", true);

// Plot the fourth data series on the second axis.
chart.getNSeries().get(3).setPlotOnSecondAxis(true);

// Change the border color of the second data series.
chart.getNSeries().get(1).getBorder().setColor(AsposeCells.Color.Green);

// Change the border color of the third data series.
chart.getNSeries().get(2).getBorder().setColor(AsposeCells.Color.Red);

// Make the second value axis visible.
chart.getSecondValueAxis().setIsVisible(true);

// Save the Excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
