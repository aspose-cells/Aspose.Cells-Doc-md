+++
title = "Chart Rendering" 
description = "" 
weight = 12267 
+++

Aspose.Cells for .NET : Chart Rendering  

# Aspose.Cells for .NET : Chart Rendering


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Creating Charts](#ChartRendering-CreatingCharts)
*   2 [Rendering Charts](#ChartRendering-RenderingCharts)
    *   2.1 [Rendering Charts to Images](#ChartRendering-RenderingChartstoImages)
    *   2.2 [Rendering Chart to PDF](#ChartRendering-RenderingCharttoPDF)
*   3 [Supported Chart Types for Rendering](#ChartRendering-SupportedChartTypesforRendering)
{{< /panel >}}
 

## Creating Charts

Aspose.Cells APIs support to create a verity of Excel charts as detailed under the topic [Creating & Customizing Excel Charts](https://docs2.aspose.com/cells/net/developerguide/charts/creating+and+customizing+charts). In order to demonstrate the usage of Aspose.Cells APIs to render the charts in image & PDF format, we will create a chart of type Column as per the following snippet.

## Rendering Charts

Aspose.Cells APIs support to convert the Excel Charts to images and PDF formats without requiring any additional tools or applications. In order to provide rendering support, the [Chart](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart) class has exposed [ToImage](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [ToPdf](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) methods with a verity of overloads to best suit the application requirements.

#### Rendering Charts to Images

The [Chart.ToImage](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) method has a verity of overloads to support simple as well as advanced rendering. If the application requirement is to render the chart in its default dimensions, we suggest you use the [Chart.ToImage](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) method as follow.

It is also possible to render the charts to images with advanced settings. Aspose.Cells APIs have exposed an overload version of [Chart.ToImage](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) method that could accept an instance of [ImageOrPrintOptions](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), while allowing to specify parameters such as resolution, smoothing mode, image format and so on.

#### Rendering Chart to PDF

In order to render the chart to PDF format, the Aspose.Cells APIs have exposed the [Chart.ToPdf](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) method with the ability to store the resultant PDF on disc path or `Stream`.

## Supported Chart Types for Rendering

There are a few chart types that are currently not supported for rendering. Such chart types contain **N** in the **Supported** column of the below table.

{{< table style="table-striped" >}}
|Chart type|Chart sub-type|Supported|
|:----|:----|:----|
|Column|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|Bar|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**
|Line|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|Pie|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|Scatter|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|Area|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|Doughnut|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|Radar|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|Surface|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|Bubble|Bubble|**Y**|
| |Bubble3D|N|
|Stock|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|Cylinder|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|Cone|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|Pyramid|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
{{< /table >}}

