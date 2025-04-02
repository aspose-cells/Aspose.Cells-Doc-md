---
title: Setting Chart Appearance with Node.js via C++
description: Learn how to configure the appearance of charts in Aspose.Cells for Node.js via C++. Our guide will show you how to modify chart layouts, colors, fonts, and effects to achieve the desired visual style and enhance your worksheets.
keywords: Aspose.Cells for Node.js via C++, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
linktitle: Chart Format
type: docs
weight: 20
url: /nodejs-cpp/setting-chart-appearance/
---

## **Setting Chart Appearance**
In How to Create a Chart we gave a brief introduction to the types of charts and charting objects offered by Aspose.Cells, and described how to create one. This article discusses how to customize the appearance of charts by setting their properties:

- Setting the chart area.
- Setting chart lines.
- Applying themes.
- Setting titles to charts and axes.
- Working with gridlines.

### **Setting Chart Area**
There are different kinds of areas in a chart and Aspose.Cells provides the flexibility to modify the appearance of each area. Developers can apply different formatting settings on an area by changing its foreground color, background color, and fill format etc.

In the example given below, we have applied different formatting settings on different kinds of areas of a chart. These areas include:

- Plot area
- Chart area
- SeriesCollection area
- Area of a single point in a SeriesCollection

The following code snippet demonstrates how to set the chart area.

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

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(new AsposeCells.Color(0, 0, 255));

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(new AsposeCells.Color(255, 255, 0));

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(255, 0, 0));

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(new AsposeCells.Color(0, 255, 255));

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Setting Chart Lines**
Developers can also apply different kinds of styles on the lines or data markers of the [SeriesCollection](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/). The following code snippet demonstrates how to set chart lines using Aspose.Cells API.

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

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
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

// Applying a dotted line style on the lines of a SeriesCollection
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Dot);

// Applying a triangular marker style on the data markers of a SeriesCollection
chart.getNSeries().get(0).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Triangle);

// Setting the weight of all lines in a SeriesCollection to medium
chart.getNSeries().get(1).getBorder().setWeight(AsposeCells.WeightType.MediumLine);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Applying Microsoft Excel 2007/2010 Themes to Charts**
Developers can apply different Microsoft Excel themes/colors to [SeriesCollection](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) or other chart objects as shown below in the example.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");

// Loads the workbook containing the chart
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first chart in the sheet
const chart = worksheet.getCharts().get(0);

// Specify the FillFormat's type to Solid Fill of the first series
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.Solid);

// Get the CellsColor of SolidFill
const cc = chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().getCellsColor();

// Create a theme in Accent style
cc.setThemeColor(new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent6, 0.6));

// Apply the theme to the series
chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().setCellsColor(cc);

// Save the Excel file
workbook.save(path.join(dataDir, "output.out.xlsx"));
```

### **Setting the Titles of Charts or Axes**
You can use Microsoft Excel to set the titles of a chart and its axes in a WYSIWYG environment. Aspose.Cells also allows developers to set the titles of a chart and its axes at runtime. All charts and their axes contain a [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) property that can be used to set their titles as shown below in an example.

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

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
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

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Working with Major Gridlines**
It is possible to customize the look of major gridlines. Hide or show gridlines, or define their color and other settings. Below, we show how to hide gridlines and how to change their color.

#### **Hiding Major Gridlines**
Developers can control the visibility of major gridlines by setting the [isVisible()](https://reference.aspose.com/cells/nodejs-cpp/line/#isVisible--) property of the [Line](https://reference.aspose.com/cells/nodejs-cpp/line/) object to **true** or **false**.

The following code snippet demonstrates how to hide major gridlines. After hiding the major gridlines, a column chart will be added to the worksheet will have not gridlines.

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

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
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

// Hiding the major gridlines of Category Axis
chart.getCategoryAxis().getMajorGridLines().setIsVisible(false);

// Hiding the major gridlines of Value Axis
chart.getValueAxis().getMajorGridLines().setIsVisible(false);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Changing Major Gridlines Settings**
Developers cannot only control the visibility of major gridlines but also other properties including its color etc.

The following code snippet demonstrates how to change the major gridlines' color. After setting the color of the major gridlines, a column chart will be added to the worksheet with modified gridlines.

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

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
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

// Setting the color of Category Axis' major gridlines to silver
chart.getCategoryAxis().getMajorGridLines().setColor(AsposeCells.Color.Silver);

// Setting the color of Value Axis' major gridlines to red
chart.getValueAxis().getMajorGridLines().setColor(AsposeCells.Color.Red);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Advance topics**
- [Set the Values Format Code of Chart Series](/cells/nodejs-cpp/set-the-values-format-code-of-chart-series/)
- [Set Picture as Background Fill in the Chart](/cells/nodejs-cpp/set-picture-as-background-fill-in-the-chart/)


