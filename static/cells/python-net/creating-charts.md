##Create and Manage Chart
Learn how to use Aspose.Cells for Python via .NET to create charts in Microsoft Excel. Our guide will demonstrate the different types of charts that can be created, as well as how to customize their appearance and formatting.
Create a chart in CSharp for Excel and ODS files.
It is possible to add a variety of charts to spreadsheets with Aspose.Cells for Python via .NET. Aspose.Cells for Python via .NET provides many flexible charting objects. This topic discusses Aspose.Cells' charting objects.
## **Creating Charts**
### **Simply Creating a Chart**
It’s simple to create a chart with Aspose.Cells for Python via .NET with the following example codes:
### **Things to Know for Creating a Chart**
Before creating charts it's important to understand some basic concepts that are helpful when creating charts using Aspose.Cells for Python via .NET.
#### **Charting Objects**
Aspose.Cells for Python via .NET provides a special set of classes in the [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts) namespace used to create the charts supported by Aspose.Cells for Python via .NET. These classes are used to create **charting objects**, which act as the chart building blocks. The charting objects are listed below:
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
Add any type of chart to a worksheet using the [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts) collection. Each item in the [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts) collection represents a [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) object. A [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) object encapsulates all other charting objects required to customize the appearance of the chart. The next section shows how to use a few basic charting objects to create a simple chart.
### **Create Chart Using Aspose.Cells for Python via .NET**
**Steps:**
1. Add some data to worksheet cells with the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) object's [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value) method.
This will be used as the data source for the chart.
1. Add a chart to the worksheet by calling the [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection) collection's [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection/add) method, encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) object.
1. Specify the type of chart with the [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) enumeration.
For example, the example below uses the [**ChartType.PYRAMID**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) value as the chart type.
1. Access the new [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) object from the [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection) collection by passing its index.
1. Use any of the charting objects encapsulated in the [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) object to manage the chart.
The example below uses the [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) charting object to specify the chart's data source.
When adding source data to chart, the data source can be a range of cells (such as "A1:C3"), or a sequence of non-contiguous cells (such as "A1, A3, A5"), or a sequence of values (such as "1,2,3").
These general steps allow you to create any type of chart. Use different charting objects to create different charts.
It is possible to create many different types of charts with Aspose.Cells for Python via .NET. All standard charts supported by Aspose.Cells for Python via .NET are pre-defined in an enumeration named [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype).
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
When you assign a range of cells as the data source, you can only set the range from top left to bottom right. For example, "A1:C3" is valid while "C3:A1" is invalid.
#### **Pyramid Chart**
When the example code is executed, a pyramid chart is added to the worksheet.
#### **Line Chart**
In the above example, simply changing the [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) to *Line* creates a line chart. The complete source is provided below. when the code is executed, a line chart is added to the worksheet.
#### **Bubble Chart**
In order to create a bubble chart, the [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) has to be set to [**ChartType.BUBBLE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) and few extra properties such as BubbleSizes, Values & XValues need to be set accordingly. Upon executing the following code, a bubble chart is added to the worksheet.
#### **Line with Data Marker Chart**
In order to create a line with the data marker chart, [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) has to be set to *ChartType.LineWithDataMarkers* and few extra properties such as background area,Series Markers, Values & XValues need to be set accordingly. Upon executing the following code, a line with the data marker chart is added to the worksheet.
## **Advance topics**
- [Read and Manipulate Excel 2016 Charts](https://docs.aspose.com/cells/python-net/read-and-manipulate-excel-2016-charts/)
- [Manage Axes of Excel Charts](https://docs.aspose.com/cells/python-net/chart-axes/)
- [Setting Chart Appearance](https://docs.aspose.com/cells/python-net/setting-chart-appearance/)
- [Chart Types](https://docs.aspose.com/cells/python-net/chart-types/)
- [Customizing Charts](https://docs.aspose.com/cells/python-net/customizing-charts/)
- [Set Data source for the chart](https://docs.aspose.com/cells/python-net/data-formatting-in-charts/)
- [Manage DataLabels of Excel Charts](https://docs.aspose.com/cells/python-net/insert-datalabels-to-chart/)
- [Generate Chart by Processing Smart Markers](https://docs.aspose.com/cells/python-net/generate-chart-by-processing-smart-markers/)
- [Get Worksheet of the Chart](https://docs.aspose.com/cells/python-net/get-worksheet-of-the-chart/)
- [Manage Legend of Excel Charts](https://docs.aspose.com/cells/python-net/chart-legend/)
- [Manipulate Position Size and Designer Chart](https://docs.aspose.com/cells/python-net/manipulate-position-size-and-designer-chart/)
- [Creating Pie Chart with Leader Lines](https://docs.aspose.com/cells/python-net/creating-pie-chart-with-leader-lines/)
- [Shapes in Charts](https://docs.aspose.com/cells/python-net/controls-in-charts/)
- [Manage Titles of Excel Charts](https://docs.aspose.com/cells/python-net/chart-and-axis-titles/)
- [Chart Rendering](https://docs.aspose.com/cells/python-net/chart-rendering/)
- [Get Equation Text of Chart Trendline](https://docs.aspose.com/cells/python-net/get-equation-text-of-chart-trendline/)
