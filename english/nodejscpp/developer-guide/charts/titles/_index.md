---
title: Manage Titles of Excel Charts with Node.js via C++
description: Learn how to use Aspose.Cells for Node.js via C++ to add and format chart and axis titles in Microsoft Excel. Our guide will demonstrate how to set different types of titles, adjust their appearance, and modify axis titles for better data representation and clarity.
keywords: Aspose.Cells for Node.js via C++, Chart Titles, Axis Titles, Microsoft Excel, Data Representation, Appearance.
linktitle: Titles
type: docs
weight: 50
url: /nodejs-cpp/chart-and-axis-titles/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In Excel charts, there are 2 kinds of titles:
1. Chart Title  
2. Axis Titles

{{% /alert %}}

## **Title Options**
Aspose.Cells for Node.js via C++ also allows managing chart titles at runtime. With the [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) object, you can change text, font, and fill format for titles.

|![todo:image_alt_text](chart_title.png)|

## **Setting the Titles of Charts or Axes**
You can use Microsoft Excel to set the titles of a chart and its axes in a WYSIWYG environment. Aspose.Cells for Node.js via C++ also allows developers to set the titles of a chart and its axes at runtime. All charts and their axes contain a [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) property that can be used to set their titles as shown below in an example.

The following code snippet demonstrates how to set titles to charts and axes.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cells to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of the category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of the value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Advanced topics**
- [Read Chart Subtitle from ODS File](/cells/nodejs-cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="nodejs-cpp" >}}
