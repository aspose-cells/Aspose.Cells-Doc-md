---
title: Chart Rendering
type: docs
weight: 50
url: /net/chart-rendering/
---

## **Creating Charts**

Aspose.Cells APIs support to create a verity of Excel charts as detailed under the topic [Creating & Customizing Excel Charts](/cells/net/creating-and-customizing-charts/). In order to demonstrate the usage of Aspose.Cells APIs to render the charts in image & PDF format, we will create a chart of type Column as per the following snippet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingCreatingChart.cs" >}}

## **Rendering Charts**

Aspose.Cells APIs support to convert the Excel Charts to images and PDF formats without requiring any additional tools or applications. In order to provide rendering support, the [**Chart**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart) class has exposed [**ToImage**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**ToPdf**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) methods with a verity of overloads to best suit the application requirements.

### **Rendering Charts to Images**

The [**Chart.ToImage**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**ToPdf**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) method has a verity of overloads to support simple as well as advanced rendering. If the application requirement is to render the chart in its default dimensions, we suggest you use the [**Chart.ToImage**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) method as follow.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

It is also possible to render the charts to images with advanced settings. Aspose.Cells APIs have exposed an overload version of [**Chart.ToImage**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) method that could accept an instance of [**ImageOrPrintOptions**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), while allowing to specify parameters such as resolution, smoothing mode, image format and so on.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **Rendering Chart to PDF**

In order to render the chart to PDF format, the Aspose.Cells APIs have exposed the [**Chart.ToPdf**](https://apireference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) method with the ability to store the resultant PDF on disc path or Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Supported Chart Types for Rendering**

There are a few chart types that are currently not supported for rendering. Such chart types contain **N** in the **Supported** column of the below table.

|**Chart type**|**Chart sub-type**|**Supported**|
| :- | :- | :- |
|**Column**|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|**Bar**|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|**Line**|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|**Pie**|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|**Scatter**|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Area**|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|**Doughnut**|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|**Radar**|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**Bubble**|Bubble|**Y**|
| |Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|**Cylinder**|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|**Cone**|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|N|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|N|
|**Map**|Map|**Y**|

{{% alert color="primary" %}}

In case you try to render the non-supported chart types to image or PDF, you may end up with 0 sized images or blank PDF.

{{% /alert %}}
