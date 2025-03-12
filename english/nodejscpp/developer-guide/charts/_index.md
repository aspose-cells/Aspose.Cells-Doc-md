---
title: Create and Manage Chart with Node.js via C++
linktitle: Charts
description: Learn how to use Aspose.Cells for Node.js to create charts in Microsoft Excel. Our guide will demonstrate various chart types and how to customize their appearance and formatting.
keywords: Aspose.Cells for Node.js, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
type: docs
weight: 130
url: /nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

It is possible to add a variety of charts to spreadsheets with Aspose.Cells. Aspose.Cells provides many flexible charting objects. This topic discusses Aspose.Cells' charting objects.

{{% /alert %}}

## **Creating Charts**

### **Simply Creating a Chart**
It’s simple to create a chart with Aspose.Cells with the following example codes:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Things to Know for Creating a Chart**

Before creating charts, it's important to understand some basic concepts that are helpful when creating charts using Aspose.Cells.

#### **Charting Objects**

Aspose.Cells provides a special set of classes in the [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells.charts) module used to create the charts supported by Aspose.Cells. These classes are used to create **charting objects**, which act as the chart building blocks. The charting objects are listed below:

- Series, a single data series in a chart.
- Axis, a chart's axis.
- Chart, a single Excel chart.
- ChartArea, the chart area in the worksheet.
- ChartDataTable, a chart data table.
- ChartFrame, the frame object in a chart.
- ChartPoint, a single point in a series in a chart.
- ChartPointCollection, a collection that contains all the points in one series.
- Charts, a collection of Chart objects.
- DataLabels, a collection of all the DataLabel objects for the specified series.
- FillFormat, fill format for a shape.
- Floor, the floor of a 3D chart.
- Legend, the chart legend.
- Line, the chart line.
- SeriesCollection, a collection of Series objects.
- TickLabels, the tick mark labels associated with tick marks on a chart axis.
- Title, the title of a chart or axis.
- Trendline, a trendline in a chart.
- TrendlineCollection, a collection of all Trendline objects for the specified data series.
- Walls, the walls of a 3D chart.

#### **Using Charting Objects**

As mentioned above, all charting objects are instances of their respective classes and provide specific properties and methods to perform specific tasks. Use charting objects to create charts.

Add any type of chart to a worksheet using the [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) collection. Each item in the [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) collection represents a [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) object. A [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) object encapsulates all other charting objects required to customize the appearance of the chart. The next section shows how to use a few basic charting objects to create a simple chart.

### **Create Chart Using Aspose.Cells**

**Steps:**

1. Add some data to worksheet cells with the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/) object's [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells.cell/methods/putvalue/index) method.
   This will be used as the data source for the chart.
1. Add a chart to the worksheet by calling the [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells.charts/chartcollection) collection's [**add**](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells.charts/chartcollection/methods/add) method, encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) object.
1. Specify the type of chart with the [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) enumeration.
   For example, the example below uses the [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells.charts/charttype) value as the chart type.
1. Access the new [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) object from the [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells.charts/chartcollection) collection by passing its index.
1. Use any of the charting objects encapsulated in the [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) object to manage the chart.
   The example below uses the [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) charting object to specify the chart's data source.

When adding source data to the chart, the data source can be a range of cells (such as "A1:C3"), or a sequence of non-contiguous cells (such as "A1, A3, A5"), or a sequence of values (such as "1,2,3").

These general steps allow you to create any type of chart. Use different charting objects to create different charts.

It is possible to create many different types of charts with Aspose.Cells. All standard charts supported by Aspose.Cells are pre-defined in an enumeration named [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).

The pre-defined chart types are:

|**Chart Types**|**Description**|
| :- | :- |
|Column|Represents Clustered Column Chart|
|ColumnStacked|Represents Stacked Column Chart|
|Column100PercentStacked|Represents 100% Stacked Column Chart|
|Column3DClustered|Represents 3D Clustered Column Chart|
|Column3DStacked|Represents 3D Stacked Column Chart|
|Column3D100PercentStacked|Represents 3D 100% Stacked Column Chart|
|Column3D|Represents 3D Column Chart|
|Bar|Represents Clustered Bar Chart|
|BarStacked|Represents Stacked Bar Chart|
|Bar100PercentStacked|Represents 100% Stacked Bar Chart|
|Bar3DClustered|Represents 3D Clustered Bar Chart|
|Bar3DStacked|Represents 3D Stacked Bar Chart|
|Bar3D100PercentStacked|Represents 3D 100% Stacked Bar Chart|
|Line|Represents Line Chart|
|LineStacked|Represents Stacked Line Chart|
|Line100PercentStacked|Represents 100% Stacked Line Chart|
|LineWithDataMarkers|Represents Line Chart with data markers|
|LineStackedWithDataMarkers|Represents Stacked Line Chart with data markers|
|Line100PercentStackedWithDataMarkers|Represents 100% Stacked Line Chart with data markers|
|Line3D|Represents 3D Line Chart|
|Pie|Represents Pie Chart|
|Pie3D|Represents 3D Pie Chart|
|PiePie|Represents Pie of Pie Chart|
|PieExploded|Represents Exploded Pie Chart|
|Pie3DExploded|Represents 3D Exploded Pie Chart|
|PieBar|Represents Bar of Pie Chart|
|Scatter|Represents Scatter Chart|
|ScatterConnectedByCurvesWithDataMarker|Represents Scatter Chart connected by curves, with data markers|
|ScatterConnectedByCurvesWithoutDataMarker|Represents Scatter Chart connected by curves, without data markers|
|ScatterConnectedByLinesWithDataMarker|Represents Scatter Chart connected by lines, with data markers|
|ScatterConnectedByLinesWithoutDataMarker|Represents Scatter Chart connected by lines, without data markers|
|Area|Represents Area Chart|
|AreaStacked|Represents Stacked Area Chart|
|Area100PercentStacked|Represents 100% Stacked Area Chart|
|Area3D|Represents 3D Area Chart|
|Area3DStacked|Represents 3D Stacked Area Chart|
|Area3D100PercentStacked|Represents 3D 100% Stacked Area Chart|
|Doughnut|Represents Doughnut Chart|
|DoughnutExploded|Represents Exploded Doughnut Chart|
|Radar|Represents Radar Chart|
|RadarWithDataMarkers|Represents Radar Chart with data markers|
|RadarFilled|Represents Filled Radar Chart|
|Surface3D|Represents 3D Surface Chart|
|SurfaceWireframe3D|Represents Wireframe 3D Surface Chart|
|SurfaceContour|Represents Contour Chart|
|SurfaceContourWireframe|Represents Wireframe Contour Chart|
|Bubble|Represents Bubble Chart|
|Bubble3D|Represents 3D Bubble Chart|
|Cylinder|Represents Cylinder Chart|
|CylinderStacked|Represents Stacked Cylinder Chart|
|Cylinder100PercentStacked|Represents 100% Stacked Cylinder Chart|
|CylindericalBar|Represents Cylindrical Bar Chart.|
|CylindericalBarStacked|Represents Stacked Cylindrical Bar Chart|
|CylindericalBar100PercentStacked|Represents 100% Stacked Cylindrical Bar Chart|
|CylindericalColumn3D|Represents 3D Cylindrical Column Chart|
|Cone|Represents Cone Chart|
|ConeStacked|Represents Stacked Cone Chart|
|Cone100PercentStacked|Represents 100% Stacked Cone Chart|
|ConicalBar|Represents Conical Bar Chart|
|ConicalBarStacked|Represents Stacked Conical Bar Chart|
|ConicalBar100PercentStacked|Represents 100% Stacked Conical Bar Chart|
|ConicalColumn3D|Represents 3D Conical Column Chart|
|Pyramid|Represents Pyramid Chart|
|PyramidStacked|Represents Stacked Pyramid Chart|
|Pyramid100PercentStacked|Represents 100% Stacked Pyramid Chart|
|PyramidBar|Represents Pyramid Bar Chart|
|PyramidBarStacked|Represents Stacked Pyramid Bar Chart|
|PyramidBar100PercentStacked|Represents 100% Stacked Pyramid Bar Chart|
|PyramidColumn3D|Represents 3D Pyramid Column Chart|
{{% alert color="primary" %}}

When you assign a range of cells as the data source, you can only set the range from top left to bottom right. For example, "A1:C3" is valid while "C3:A1" is invalid.

{{% /alert %}}

#### **Pyramid Chart**

When the example code is executed, a pyramid chart is added to the worksheet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
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
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Line Chart**

In the above example, simply changing the [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) to *Line* creates a line chart. The complete source is provided below. when the code is executed, a line chart is added to the worksheet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

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
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Bubble Chart**

In order to create a bubble chart, the [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) has to be set to [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells.charts/charttype) and a few extra properties such as BubbleSizes, Values & XValues need to be set accordingly. Upon executing the following code, a bubble chart is added to the worksheet.

#### **Line with Data Marker Chart**

In order to create a line with the data marker chart, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) has to be set to *ChartType.LineWithDataMarkers* and a few extra properties such as background area, Series Markers, Values & XValues need to be set accordingly. Upon executing the following code, a line with the data marker chart is added to the worksheet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Advance topics**
- [Read and Manipulate Excel 2016 Charts](/cells/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Manage Axes of Excel Charts](/cells/nodejs-cpp/chart-axes/)
- [Setting Chart Appearance](/cells/nodejs-cpp/setting-chart-appearance/)
- [Chart Types](/cells/nodejs-cpp/chart-types/)
- [Customizing Charts](/cells/nodejs-cpp/customizing-charts/)
- [Set Data source for the chart](/cells/nodejs-cpp/data-formatting-in-charts/)
- [Manage DataLabels of Excel Charts](/cells/nodejs-cpp/insert-datalabels-to-chart/)
- [Generate Chart by Processing Smart Markers](/cells/nodejs-cpp/generate-chart-by-processing-smart-markers/)
- [Get Worksheet of the Chart](/cells/nodejs-cpp/get-worksheet-of-the-chart/)
- [Manage Legend of Excel Charts](/cells/nodejs-cpp/chart-legend/)
- [Manipulate Position Size and Designer Chart](/cells/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [Creating Pie Chart with Leader Lines](/cells/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [Shapes in Charts](/cells/nodejs-cpp/controls-in-charts/)
- [Manage Titles of Excel Charts](/cells/nodejs-cpp/chart-and-axis-titles/)
- [Chart Rendering](/cells/nodejs-cpp/chart-rendering/)
- [Get Equation Text of Chart Trendline](/cells/nodejs-cpp/get-equation-text-of-chart-trendline/)
