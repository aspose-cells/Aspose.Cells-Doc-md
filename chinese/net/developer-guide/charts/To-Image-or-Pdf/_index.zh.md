---
title: 图表渲染
linktitle: 图像或 Pdf
type: docs
weight: 45
url: /zh/net/chart-rendering/
---
## **渲染图**

 Aspose.Cells API 支持将 Excel 图表转换为图像和 PDF 格式，无需任何其他工具或应用程序。为了提供渲染支持，[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)班级暴露了[**印象**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**到PDF**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)具有大量重载的方法，以最好地满足应用程序的要求。

### **将图表渲染为图像**

这[**图表转图像**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**到PDF**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)方法具有大量重载以支持简单和高级渲染。如果应用程序要求以默认尺寸呈现图表，我们建议您使用[**图表转图像**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)方法如下。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

也可以使用高级设置将图表渲染为图像。 Aspose.Cells API 公开了重载版本[**图表转图像**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)可以接受实例的方法[**图像或打印选项**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)同时允许指定分辨率、平滑模式、图像格式等参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **渲染图到 PDF**

为了将图表呈现为 PDF 格式，Aspose.Cells API 公开了[**图表.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)方法能够将结果 PDF 存储在光盘路径或流中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **支持的渲染图表类型**

有一些图表类型当前不支持渲染。此类图表类型包含**N** 在**支持下表的**列。

|**图表类型**|**图表子类型**|**支持的**|
|:- |:- |:- |
|**柱子**|柱子|**Y**|
||列堆叠|**Y**|
||列 100% 堆叠|**Y**|
||Column3D簇状|**Y**|
||列 3D 堆叠|**Y**|
||Column3D100PercentStacked|**Y**|
||立柱三维|**Y**|
|**酒吧**|酒吧|**Y**|
||酒吧堆叠|**Y**|
||Bar100Percent 堆叠|**Y**|
||Bar3DClustered|**Y**|
||Bar3D堆叠|**Y**|
||Bar3D100PercentStacked|**Y**|
|**线**|线|**Y**|
||线堆叠|**Y**|
||Line100Percent 堆叠|**Y**|
||带数据标记的线|**Y**|
||LineStackedWithDataMarkers|**Y**|
||Line100PercentStackedWithDataMarkers|**Y**|
||直线三维|**Y**|
|**馅饼**|馅饼|**Y**|
||Pie3D|**Y**|
||派派|**Y**|
||馅饼爆炸|**Y**|
||饼图3D分解|**Y**|
||馅饼吧|**Y**|
|**分散**|分散|**Y**|
||ScatterConnectedByCurvesWithDataMarker|**Y**|
||ScatterConnectedByCurvesWithoutDataMarker|**Y**|
||ScatterConnectedByLinesWithDataMarker|**Y**|
||ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**区域**|区域|**Y**|
||面积堆叠|**Y**|
||面积 100% 堆叠|**Y**|
||三维区域|**Y**|
||Area3D堆叠|**Y**|
||Area3D100PercentStacked|**Y**|
|**油炸圈饼**|油炸圈饼|**Y**|
||甜甜圈爆炸|**Y**|
|**雷达**|雷达|**Y**|
||带数据标记的雷达|**Y**|
||雷达填充|**Y**|
|**表面**|Surface3D|否|
||表面线框3D|否|
||表面轮廓|否|
||表面轮廓线框|否|
|**气泡**|气泡|**Y**|
||泡泡3D|否|
|**库存**|股价高低收盘|**Y**|
||股票开高低收|**Y**|
||StockVolumeHighLow关闭|**Y**|
||StockVolumeOpenHighLowClose|**Y**|
|**圆柱**|圆柱|**Y**|
||圆柱叠层|**Y**|
||圆柱100%堆叠|**Y**|
||圆柱棒|**Y**|
||圆柱形条堆叠|**Y**|
||CylindricalBar100PercentStacked|**Y**|
||圆柱3D|**Y**|
|**锥体**|锥体|**Y**|
||圆锥堆叠|**Y**|
||Cone100Percent堆叠|**Y**|
||锥形棒|**Y**|
||锥形条堆叠|**Y**|
||ConicalBar100PercentStacked|**Y**|
||锥形柱3D|**Y**|
|**金字塔**|金字塔|**Y**|
||金字塔堆叠|**Y**|
||金字塔100%堆积|**Y**|
||金字塔酒吧|**Y**|
||金字塔酒吧堆叠|**Y**|
||PyramidBar100PercentStacked|**Y**|
||金字塔柱3D|**Y**|
|**盒须**|盒须|是|
|**漏斗**|漏斗|**Y**|
|**帕累托线**|帕累托线|**Y**|
|**森伯斯特**|森伯斯特|**Y**|
|**树形图**|树形图|**Y**|
|**瀑布**|瀑布|**Y**|
|**直方图**|直方图|是|
|**地图**|地图|**N**|

{{% alert color="primary" %}}

如果您尝试将不受支持的图表类型呈现为图像或 PDF，您最终可能会得到 0 大小的图像或空白 PDF。

{{% /alert %}}

## **推进主题**
- [将图表转换为具有所需页面大小的 PDF](/cells/zh/net/chart-to-pdf/)
