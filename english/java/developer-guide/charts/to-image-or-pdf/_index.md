---
title: Chart Rendering
linktitle: To Image or Pdf
type: docs
weight: 40
url: /java/chart-rendering/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Creating Charts**

Aspose.Cells APIs support creating a variety of Excel charts as detailed under the topic [Creating & Customizing Excel Charts](/cells/java/creating-and-customizing-charts/). In order to demonstrate the usage of Aspose.Cells APIs to render the charts in image & PDF format, we will create a chart of type Column as per the following snippet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Rendering Charts**

Aspose.Cells APIs support converting the Excel charts to images and PDF formats without requiring any additional tools or applications. In order to provide rendering support, the [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) class has exposed [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) & [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-) methods with a variety of overloads to best suit the application requirements.

### **Rendering Charts to Images**

The [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) method has a variety of overloads to support simple as well as advanced rendering. If the application requirement is to render the chart in its default dimensions, we suggest you use the [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) method as follows.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

It is also possible to render the charts to images with advanced settings. Aspose.Cells APIs have exposed an overload of [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) that can accept an instance of [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) while allowing you to specify parameters such as resolution, rendering hints, image format, and so on.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Rendering Chart to PDF**

In order to render the chart to PDF format, the Aspose.Cells APIs have exposed the [**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-) method with the ability to store the resultant PDF on a disc path or an instance of `OutputStream`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Supported Chart Types for Rendering**

There are a few chart types that are currently not supported for rendering. Such chart types contain **N** in the **Supported** column of the table below.

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
|**BoxWhisker**|BoxWhisker|Y|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|Y|
|**Map**|Map|**N**|

{{% alert color="primary" %}}

If you try to render the non‑supported chart types to image or PDF, you may end up with 0‑sized images or a blank PDF.

{{% /alert %}}

## **Advanced topics**
- [Converting Chart to Image in SVG Format](/cells/java/converting-chart-to-image-in-svg-format/)
- [Create Chart PDF with Desired Page Size](/cells/java/create-chart-pdf-with-desired-page-size/)
- [Export Chart to SVG with viewBox attribute](/cells/java/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="java" >}}
