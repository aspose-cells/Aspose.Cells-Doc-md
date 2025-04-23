---
title: 图表转为图像
description: 学习如何使用 Aspose.Cells for Python via .NET 将图表转换为 JPEG 或 PNG 等图像格式。我们的指南将演示如何导出 Microsoft Excel 中的图表并将其保存为独立的图像以便后续使用和处理。
keywords: Aspose.Cells for Python via .NET，图表转图片，Microsoft Excel，图像转换，导出，独立图像。
linktitle: 图表转为图像
type: docs
weight: 46
url: /zh/python-net/chart-to-image/
---

## **渲染图表**

Aspose.Cells for Python via .NET API 支持将 Excel 图表转换为图像格式，无需任何额外的工具或应用程序。为了提供渲染支持，[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) 类提供了 [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) 方法以及多种重载以最佳适应应用需求。

### **将图表渲染为图像**

[**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image)方法具有多种重载，支持简单和高级渲染。如果应用程序的要求是在其默认尺寸下渲染图表，我们建议您使用[**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image)方法。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImage.py" >}}

也可以使用高级设置将图表渲染为图像。Aspose.Cells for Python via .NET API 提供了 [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) 方法的重载版本，可以接受 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/) 实例，并允许指定诸如分辨率、平滑模式、图像格式等参数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.py" >}}

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
- [将图表转换为PDF](/cells/zh/python-net/chart-to-pdf/)
