---
title: Create and Manage Chart
description: Learn how to use Aspose.Cells for .NET to create charts in Microsoft Excel. Our guide will demonstrate the different types of charts that can be created, as well as how to customize their appearance and formatting.
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: Charts
type: docs
weight: 130
url: /net/creating-charts/
description: Create a chart in CSharp for Excel and ODS files.
keywords: create a chart, make a graph 
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

It is possible to add a variety of charts to spreadsheets with Aspose.Cells. Aspose.Cells provides many flexible charting objects. This topic discusses Aspose.Cells' charting objects.

{{% /alert %}}

## **Creating Charts**

### **Simply Creating a Chart**
It’s simple to create a chart with Aspose.Cells using the following example code:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Things to Know for Creating a Chart**

Before creating charts, it's important to understand some basic concepts that are helpful when creating charts using Aspose.Cells.

#### **Charting Objects**

Aspose.Cells provides a special set of classes in the [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) namespace used to create the charts supported by Aspose.Cells. These classes are used to create **charting objects**, which act as the chart building blocks. The charting objects are listed below:

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

Add any type of chart to a worksheet using the [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) collection. Each item in the [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) collection represents a [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) object. A [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) object encapsulates all other charting objects required to customize the appearance of the chart. The next section shows how to use a few basic charting objects to create a simple chart.

### **Create Chart Using Aspose.Cells**

**Steps:**

1. Add some data to worksheet cells with the [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) object's [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method. This will be used as the data source for the chart.  
2. Add a chart to the worksheet by calling the [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) collection's [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) method, encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) object.  
3. Specify the type of chart with the [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) enumeration. For example, the example below uses the [**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) value as the chart type.  
4. Access the new [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) object from the [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) collection by passing its index.  
5. Use any of the charting objects encapsulated in the [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) object to manage the chart. The example below uses the [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) charting object to specify the chart's data source.

When adding source data to a chart, the data source can be a range of cells (such as "A1:C3"), a sequence of non‑contiguous cells (such as "A1, A3, A5"), or a sequence of values (such as "1,2,3").

These general steps allow you to create any type of chart. Use different charting objects to create different charts.

It is possible to create many different types of charts with Aspose.Cells. All standard charts supported by Aspose.Cells are pre‑defined in an enumeration named [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

The pre‑defined chart types are:

| **Chart Types** | **Description** |
| :- | :- |
| Column | Represents a clustered column chart |
| ColumnStacked | Represents a stacked column chart |
| Column100PercentStacked | Represents a 100 % stacked column chart |
| Column3DClustered | Represents a 3D clustered column chart |
| Column3DStacked | Represents a 3D stacked column chart |
| Column3D100PercentStacked | Represents a 3D 100 % stacked column chart |
| Column3D | Represents a 3D column chart |
| Bar | Represents a clustered bar chart |
| BarStacked | Represents a stacked bar chart |
| Bar100PercentStacked | Represents a 100 % stacked bar chart |
| Bar3DClustered | Represents a 3D clustered bar chart |
| Bar3DStacked | Represents a 3D stacked bar chart |
| Bar3D100PercentStacked | Represents a 3D 100 % stacked bar chart |
| Line | Represents a line chart |
| LineStacked | Represents a stacked line chart |
| Line100PercentStacked | Represents a 100 % stacked line chart |
| LineWithDataMarkers | Represents a line chart with data markers |
| LineStackedWithDataMarkers | Represents a stacked line chart with data markers |
| Line100PercentStackedWithDataMarkers | Represents a 100 % stacked line chart with data markers |
| Line3D | Represents a 3D line chart |
| Pie | Represents a pie chart |
| Pie3D | Represents a 3D pie chart |
| PiePie | Represents a pie‑of‑pie chart |
| PieExploded | Represents an exploded pie chart |
| Pie3DExploded | Represents a 3D exploded pie chart |
| PieBar | Represents a bar‑of‑pie chart |
| Scatter | Represents a scatter chart |
| ScatterConnectedByCurvesWithDataMarker | Represents a scatter chart connected by curves, with data markers |
| ScatterConnectedByCurvesWithoutDataMarker | Represents a scatter chart connected by curves, without data markers |
| ScatterConnectedByLinesWithDataMarker | Represents a scatter chart connected by lines, with data markers |
| ScatterConnectedByLinesWithoutDataMarker | Represents a scatter chart connected by lines, without data markers |
| Area | Represents an area chart |
| AreaStacked | Represents a stacked area chart |
| Area100PercentStacked | Represents a 100 % stacked area chart |
| Area3D | Represents a 3D area chart |
| Area3DStacked | Represents a 3D stacked area chart |
| Area3D100PercentStacked | Represents a 3D 100 % stacked area chart |
| Doughnut | Represents a doughnut chart |
| DoughnutExploded | Represents an exploded doughnut chart |
| Radar | Represents a radar chart |
| RadarWithDataMarkers | Represents a radar chart with data markers |
| RadarFilled | Represents a filled radar chart |
| Surface3D | Represents a 3D surface chart |
| SurfaceWireframe3D | Represents a wireframe 3D surface chart |
| SurfaceContour | Represents a contour chart |
| SurfaceContourWireframe | Represents a wireframe contour chart |
| Bubble | Represents a bubble chart |
| Bubble3D | Represents a 3D bubble chart |
| Cylinder | Represents a cylinder chart |
| CylinderStacked | Represents a stacked cylinder chart |
| Cylinder100PercentStacked | Represents a 100 % stacked cylinder chart |
| CylindricalBar | Represents a cylindrical bar chart |
| CylindricalBarStacked | Represents a stacked cylindrical bar chart |
| CylindricalBar100PercentStacked | Represents a 100 % stacked cylindrical bar chart |
| CylindricalColumn3D | Represents a 3D cylindrical column chart |
| Cone | Represents a cone chart |
| ConeStacked | Represents a stacked cone chart |
| Cone100PercentStacked | Represents a 100 % stacked cone chart |
| ConicalBar | Represents a conical bar chart |
| ConicalBarStacked | Represents a stacked conical bar chart |
| ConicalBar100PercentStacked | Represents a 100 % stacked conical bar chart |
| ConicalColumn3D | Represents a 3D conical column chart |
| Pyramid | Represents a pyramid chart |
| PyramidStacked | Represents a stacked pyramid chart |
| Pyramid100PercentStacked | Represents a 100 % stacked pyramid chart |
| PyramidBar | Represents a pyramid bar chart |
| PyramidBarStacked | Represents a stacked pyramid bar chart |
| PyramidBar100PercentStacked | Represents a 100 % stacked pyramid bar chart |
| PyramidColumn3D | Represents a 3D pyramid column chart |

{{% alert color="primary" %}}

When you assign a range of cells as the data source, you can only set the range from top‑left to bottom‑right. For example, "A1:C3" is valid while "C3:A1" is invalid.

{{% /alert %}}

#### **Pyramid Chart**

When the example code is executed, a pyramid chart is added to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Line Chart**

In the above example, simply changing the [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) to *Line* creates a line chart. The complete source is provided below. When the code is executed, a line chart is added to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Bubble Chart**

To create a bubble chart, the [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) must be set to [**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) and a few extra properties such as **BubbleSizes**, **Values**, and **XValues** need to be set accordingly. Upon executing the following code, a bubble chart is added to the worksheet.

#### **Line with Data Marker Chart**

To create a line chart with data markers, the [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) must be set to *ChartType.LineWithDataMarkers* and a few extra properties such as background area, series markers, **Values**, and **XValues** must be set accordingly. Upon executing the following code, a line chart with data markers is added to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Advanced topics**
- [Read and Manipulate Excel 2016 Charts](/cells/net/read-and-manipulate-excel-2016-charts/)
- [Manage Axes of Excel Charts](/cells/net/chart-axes/)
- [Setting Chart Appearance](/cells/net/setting-chart-appearance/)
- [Chart Types](/cells/net/chart-types/)
- [Customizing Charts](/cells/net/customizing-charts/)
- [Set Data source for the chart](/cells/net/data-formatting-in-charts/)
- [Manage DataLabels of Excel Charts](/cells/net/insert-datalabels-to-chart/)
- [Generate Chart by Processing Smart Markers](/cells/net/generate-chart-by-processing-smart-markers/)
- [Get Worksheet of the Chart](/cells/net/get-worksheet-of-the-chart/)
- [Manage Legend of Excel Charts](/cells/net/chart-legend/)
- [Manipulate Position Size and Designer Chart](/cells/net/manipulate-position-size-and-designer-chart/)
- [Creating Pie Chart with Leader Lines](/cells/net/creating-pie-chart-with-leader-lines/)
- [Shapes in Charts](/cells/net/controls-in-charts/)
- [Manage Titles of Excel Charts](/cells/net/chart-and-axis-titles/)
- [Chart Rendering](/cells/net/chart-rendering/)
- [Get Equation Text of Chart Trendline](/cells/net/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="csharp" >}}
