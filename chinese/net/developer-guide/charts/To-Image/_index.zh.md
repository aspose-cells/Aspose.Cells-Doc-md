---
title: 图表转为图像
description: 学习如何使用 Aspose.Cells for .NET 将图表转换为图像格式，例如 JPEG 或 PNG。我们的指南将演示如何从 Microsoft Excel 导出图表并将其保存为独立图像以供进一步使用和处理。
keywords: Aspose.Cells for .NET，图表转图像，Microsoft Excel，图像转换，导出，独立图像。
linktitle: 图表转为图像
type: docs
weight: 46
url: /zh/net/chart-to-image/
---

## **渲染图表**

Aspose.Cells APIs支持将Excel图表转换为图像格式，无需额外的工具或应用程序。为了提供渲染支持，[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)类已公开了[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)多种方法，最好地满足应用程序的需求。

### **将图表渲染为图像**

[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法具有多种重载，支持简单和高级渲染。如果应用程序的要求是在其默认尺寸下渲染图表，我们建议您使用[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

还可以使用高级设置将图表渲染为图像。Aspose.Cells APIs公开了[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法的重载版本，可接受[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)的实例，并允许指定参数，如分辨率、平滑模式、图像格式等。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

## **支持的图表类型的渲染**

目前有一些不支持渲染的图表类型。这些图表类型在下表的**Supported**列中包含**N**。

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
- [将图表转换为PDF](/cells/zh/net/chart-to-pdf/)
