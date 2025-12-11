---
title: Set Picture as Background Fill in the Chart with Node.js via C++
linktitle: Set Picture as Background Fill in the Chart
description: Learn how to set a picture as the background fill in a chart using Aspose.Cells for Node.js via C++. Our guide will show you how to import and position the picture, adjust its size and color, and apply formatting options to enhance your chart's appearance.
keywords: Aspose.Cells for Node.js via C++, charting, background fill, picture, import, positioning, size, color, formatting.
type: docs
weight: 30
url: /nodejs-cpp/set-picture-as-background-fill-in-the-chart/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to set a gradient, texture, pattern, or picture as fill effects for different objects, such as the plot area, chart area, or legend box of a chart. This document shows how to add an image to a chart's background.

{{% /alert %}}

To achieve this, Aspose.Cells provides the [**Chart.getPlotArea()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getPlotArea--) property. The following code sample demonstrates the use of the [**Chart.getPlotArea()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getPlotArea--) property to set a picture as a background fill in the chart.

## Node.js code to set picture as background fill in the chart

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
let sheet = workbook.getWorksheets().get(0);

// Set the name of the worksheet
sheet.setName("Data");

// Get the cells collection in the sheet.
const cells = workbook.getWorksheets().get(0).getCells();

// Put some values into cells of the Data sheet.
cells.get("A1").putValue("Region");
cells.get("A2").putValue("France");
cells.get("A3").putValue("Germany");
cells.get("A4").putValue("England");
cells.get("A5").putValue("Sweden");
cells.get("A6").putValue("Italy");
cells.get("A7").putValue("Spain");
cells.get("A8").putValue("Portugal");
cells.get("B1").putValue("Sale");
cells.get("B2").putValue(70000);
cells.get("B3").putValue(55000);
cells.get("B4").putValue(30000);
cells.get("B5").putValue(40000);
cells.get("B6").putValue(35000);
cells.get("B7").putValue(32000);
cells.get("B8").putValue(10000);

// Add a chart sheet.
let sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
sheet = workbook.getWorksheets().get(sheetIndex);

// Set the name of the worksheet
sheet.setName("Chart");

// Create chart
let chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 1, 1, 25, 10);
const chart = sheet.getCharts().get(chartIndex);

// Set some properties of the chart plot area.
// To set a picture as the fill format and make the border invisible.
const fs = require("fs");
const data = fs.readFileSync(path.join(dataDir, "aspose.png"));
chart.getPlotArea().getArea().getFillFormat().setImageData(data);
chart.getPlotArea().getBorder().setIsVisible(false);

// Set properties of chart title
chart.getTitle().setText("Sales By Region");
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);
chart.getTitle().getFont().setIsBold(true);
chart.getTitle().getFont().setSize(12);

// Set properties of NSeries
chart.getNSeries().add("Data!B2:B8", true);
chart.getNSeries().setCategoryData("Data!A2:A8");
chart.getNSeries().setIsColorVaried(true);

// Set the legend.
const legend = chart.getLegend();
legend.setPosition(AsposeCells.LegendPositionType.Top);

// Save the Excel file
workbook.save(path.join(dataDir, "column_chart_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
