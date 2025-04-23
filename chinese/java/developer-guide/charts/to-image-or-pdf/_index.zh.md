---
title: 图表渲染
linktitle: 转换为图像或PDF
type: docs
weight: 40
url: /zh/java/chart-rendering/
---

## **创建图表**

Aspose.Cells API支持创建各种类型的Excel图表，详细信息请参阅[创建和自定义Excel图表](/cells/zh/java/creating-and-customizing-charts/)专题。为了演示如何使用Aspose.Cells API以图像和PDF格式呈现图表，我们将根据以下片段创建一个列类型的图表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **渲染图表**

Aspose.Cells API支持将Excel图表转换为图像和PDF格式，而无需额外的工具或应用程序。为了提供渲染支持，[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)类已公开了[**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-)和[**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-)方法，具有各种重载以最好地满足应用程序的要求。

### **将图表渲染为图像**

[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-)方法具有各种重载，以支持简单和高级渲染。如果应用程序要求以其默认尺寸渲染图表，建议您使用[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-)方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

还可以使用高级设置将图表渲染为图像。Aspose.Cells API公开了[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-)方法的重载版本，该版本可以接受[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)的实例，同时允许指定参数，如分辨率、渲染提示、图像格式等。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **将图表渲染为PDF**

为了将图表渲染为PDF格式，Aspose.Cells API公开了[**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-)方法，可以将结果PDF存储在磁盘路径或输出流的实例中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **支持的图表类型的渲染**

目前不支持渲染的一些图表类型。此类图表类型在下表的**Supported**列中包含**N**。

|图表类型|图表子类型|支持
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

如果尝试将不受支持的图表类型渲染为图像或PDF，则可能会得到大小为0的图像或空白PDF。

{{% /alert %}}


## **高级主题**
- [将图表转换为SVG格式图像](/cells/zh/java/converting-chart-to-image-in-svg-format/)
- [使用所需的页面大小创建图表PDF](/cells/zh/java/create-chart-pdf-with-desired-page-size/)
- [使用viewBox属性将图表导出为SVG](/cells/zh/java/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="java" >}}
