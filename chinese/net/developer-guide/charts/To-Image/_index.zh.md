---
title: 图表到图像
linktitle: 图表到图像
type: docs
weight: 46
url: /zh/net/chart-to-image/
---
##  **渲染图**

Aspose.Cells API 支持将 Excel 图表转换为图像格式，而无需任何其他工具或应用程序。为了提供渲染支持，[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)班级暴露了[**印象**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)具有大量重载的方法，以最好地满足应用程序的要求。

###  **将图表渲染为图像**

这[**图表转图像**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法具有大量重载以支持简单和高级渲染。如果应用程序要求以默认尺寸呈现图表，我们建议您使用[**图表转图像**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法如下。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

也可以使用高级设置将图表渲染为图像。 Aspose.Cells API 公开了重载版本[**图表转图像**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)可以接受实例的方法[**图像或打印选项**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)同时允许指定分辨率、平滑模式、图像格式等参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **支持的渲染图表类型**

有一些图表类型当前不支持渲染。此类图表类型包含**N** 在 ** 支持**下表的列。

|**图表类型**|**图表子类型**|**支持的**|
| :- | :- | :- |
|**柱子**|柱子|*是**|
| |列堆叠|*是**|
| |列 100% 堆叠|*是**|
| |Column3D簇状|*是**|
| |列 3D 堆叠|*是**|
| |Column3D100PercentStacked|*是**|
| |立柱三维|*是**|
|**酒吧**|酒吧|*是**|
| |酒吧堆叠|*是**|
| |Bar100Percent 堆叠|*是**|
| |Bar3DClustered|*是**|
| |Bar3D堆叠|*是**|
| |Bar3D100PercentStacked|*是**|
|**线**|线|*是**|
| |线堆叠|*是**|
| |Line100Percent 堆叠|*是**|
| |带数据标记的线|*是**|
| |LineStackedWithDataMarkers|*是**|
| |Line100PercentStackedWithDataMarkers|*是**|
| |直线三维|*是**|
|**馅饼**|馅饼|*是**|
| |Pie3D|*是**|
| |派派|*是**|
| |馅饼爆炸|*是**|
| |饼图3D分解|*是**|
| |馅饼吧|*是**|
|**分散**|分散|*是**|
| |ScatterConnectedByCurvesWithDataMarker|*是**|
| |ScatterConnectedByCurvesWithoutDataMarker|*是**|
| |ScatterConnectedByLinesWithDataMarker|*是**|
| |ScatterConnectedByLinesWithoutDataMarker|*是**|
|**区域**|区域|*是**|
| |面积堆叠|*是**|
| |面积 100% 堆叠|*是**|
| |三维区域|*是**|
| |Area3D堆叠|*是**|
| |Area3D100PercentStacked|*是**|
|**油炸圈饼**|油炸圈饼|*是**|
| |甜甜圈爆炸|*是**|
|**雷达**|雷达|*是**|
| |带数据标记的雷达|*是**|
| |雷达填充|*是**|
|**表面**|Surface3D|N|
| |表面线框3D|N|
| |表面轮廓|N|
| |表面轮廓线框|N|
|**气泡**|气泡|*是**|
| |泡泡3D|N|
|**库存**|股价高低收盘|*是**|
| |股票开高低收|*是**|
| |StockVolumeHighLow关闭|*是**|
| |StockVolumeOpenHighLowClose|*是**|
|**圆柱**|圆柱|*是**|
| |圆柱叠层|*是**|
| |圆柱100%堆叠|*是**|
| |圆柱棒|*是**|
| |圆柱形条堆叠|*是**|
| |CylindricalBar100PercentStacked|*是**|
| |圆柱3D|*是**|
|**锥体**|锥体|*是**|
| |圆锥堆叠|*是**|
| |Cone100Percent堆叠|*是**|
| |锥形棒|*是**|
| |锥形条堆叠|*是**|
| |ConicalBar100PercentStacked|*是**|
| |锥形柱3D|*是**|
|**金字塔**|金字塔|*是**|
| |金字塔堆叠|*是**|
| |金字塔100%堆积|*是**|
| |金字塔酒吧|*是**|
| |金字塔酒吧堆叠|*是**|
| |PyramidBar100PercentStacked|*是**|
| |金字塔柱3D|*是**|
|**盒须**|盒须|Y|
|**漏斗**|漏斗|*是**|
|**帕累托线**|帕累托线|*是**|
|**森伯斯特**|森伯斯特|*是**|
|**树形图**|树形图|*是**|
|**瀑布**|瀑布|*是**|
|**直方图**|直方图|Y|
|**地图**|地图|*N**|

{{% alert color="primary" %}}

如果您尝试将不受支持的图表类型呈现为图像或 PDF，您最终可能会得到 0 大小的图像或空白 PDF。

{{% /alert %}}

##  **推进主题**
- [将图表转换为 PDF](/cells/zh/net/chart-to-pdf/)
