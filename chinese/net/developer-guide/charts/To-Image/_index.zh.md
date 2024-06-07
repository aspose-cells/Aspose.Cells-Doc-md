---
title: 转换图表为图片
description: 学习如何使用Aspose.Cells for .NET将图表转换为图像格式，如JPEG或PNG。我们的指南将演示如何从Microsoft Excel导出图表并保存为独立图像以供进一步使用和处理。
keywords: Aspose.Cells for .NET, 图表转图片, Microsoft Excel, 图像转换, 导出, 独立图片。
linktitle: 转换图表为图片
type: docs
weight: 46
url: /zh/net/chart-to-image/
---

## **图表渲染**

Aspose.Cells API支持将Excel图表转换为图像格式，无需使用任何额外的工具或应用程序。为提供渲染支持，[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)类已暴露了[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)种方法，以最佳适应应用程序要求。

### **将图表渲染为图像**

[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法具有各种重载以支持简单和高级渲染。如果应用程序要求以默认尺寸渲染图表，建议使用[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

也可以使用高级设置将图表渲染为图像。Aspose.Cells API已经暴露了一个重载版本的[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法，可以接受[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)实例，同时允许指定参数，如分辨率、平滑模式、图像格式等。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

## **支持的图表类型用于渲染**

目前尚不支持某些图表类型的渲染。这些类型的图表在下表的**Supported**列中包含**N**。

|**图表类型**|**图表子类型**|**支持**|
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

在尝试将不支持的图表类型渲染为图像或PDF时，可能会得到大小为0的图像或空白PDF。

{{% /alert %}}

## **高级主题**
- [将图表转换为PDF](/cells/zh/net/chart-to-pdf/)
