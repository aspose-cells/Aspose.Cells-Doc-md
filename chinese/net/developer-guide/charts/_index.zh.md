---
title: 创建和管理图表
description: 了解如何使用 Aspose.Cells for .NET 在 Microsoft Excel 中创建图表。我们的指南将演示可以创建的不同类型的图表，以及如何自定义其外观和格式。
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: 图表
type: docs
weight: 130
url: /zh/net/creating-charts/
description: 在 CSharp for Excel 和 ODS 文件中创建图表。
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

可以使用 Aspose.Cells 将各种图表添加到电子表格中。Aspose.Cells 提供许多灵活的图表对象。本主题讨论 Aspose.Cells' 图表对象。

{{% /alert %}}

##  **创建图表**

###  **简单地创建图表**
使用以下示例代码创建一个包含 Aspose.Cells 的图表很简单：
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

###  **创建图表的注意事项**

在创建图表之前，了解一些基本概念非常重要，这些概念在使用 Aspose.Cells 创建图表时很有帮助。

####  **绘制对象图表**

Aspose.Cells 提供了一组特殊的类[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)用于创建 Aspose.Cells 支持的图表的命名空间。这些类用于创建*图表对象**，充当图表构建块。图表对象如下所示：

- 系列，图表中的单个数据系列。
- 轴，图表的轴。
- 图表，单个 Excel 图表。
- ChartArea，工作表中的图表区域。
- ChartDataTable，图表数据表。
- ChartFrame，图表中的框架对象。
- ChartPoint，图表中一系列的单个点。
- ChartPointCollection，包含一个系列中所有点的集合。
- 图表，图表对象的集合。
- DataLabels，指定系列的所有 DataLabel 对象的集合。
- FillFormat，形状的填充格式。
- 下限，3D 图表的下限。
- 图例，图表图例。
- 线，图表线。
- SeriesCollection，Series 对象的集合。
- TickLabels，与图表轴上的刻度线关联的刻度线标签。
- 标题，图表或轴的标题。
- 趋势线，图表中的趋势线。
- TrendlineCollection，指定数据系列的所有 Trendline 对象的集合。
- 墙，3D 图表的墙。

####  **使用图表对象**

如上所述，所有图表对象都是其各自类的实例，并提供特定的属性和方法来执行特定的任务。使用图表对象创建图表。

使用以下命令将任何类型的图表添加到工作表中[**图表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)收藏。中的每一项[**图表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)集合代表一个[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)目的。 A[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)对象封装了自定义图表外观所需的所有其他图表对象。下一节将介绍如何使用一些基本的图表对象来创建简单的图表。

###  **使用 Aspose.Cells 创建图表**

**脚步：**

1. 使用以下命令将一些数据添加到工作表单元格中[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)对象的[**看跌期权**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。
这将用作图表的数据源。
1. 通过调用将图表添加到工作表[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)收藏的[**添加**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add)方法，封装在[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)目的。
1. 指定图表类型[**图表类型**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)枚举。
例如，下面的示例使用[**图表类型.金字塔**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)值作为图表类型。
1. 访问新的[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)对象从[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)通过传递其索引来收集。
1. 使用封装在中的任何图表对象[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)管理图表的对象。
下面的示例使用[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)图表对象来指定图表的数据源。

将源数据添加到图表时，数据源可以是一系列单元格（例如“A1:C3”），也可以是一系列不连续的单元格（例如“A1、A3、A5”），或者是一系列单元格。值（例如“1,2,3”）。

这些常规步骤允许您创建任何类型的图表。使用不同的图表对象来创建不同的图表。

可以使用 Aspose.Cells 创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表均在名为的枚举中预定义[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

预定义的图表类型有：

|**图表类型**|**描述**|
| :- | :- |
|柱子|表示簇状柱形图|
|列堆叠|表示堆积柱形图|
|列100%堆积|表示 100% 堆积柱形图|
|柱状3D簇状|表示 3D 簇状柱形图|
|柱3D堆叠|表示 3D 堆积柱形图|
|Column3D100PercentStacked|表示 3D 100% 堆积柱形图|
|柱三维|代表 3D 柱形图|
|酒吧|表示簇状条形图|
|条形堆叠|表示堆积条形图|
|条形100%堆叠|代表 100% 堆积条形图|
|Bar3D簇状|表示 3D 簇状条形图|
|酒吧3D堆叠|表示 3D 堆叠条形图|
|Bar3D100百分比堆叠|表示 3D 100% 堆积条形图|
|线|代表折线图|
|线堆叠|表示堆积折线图|
|线 100% 堆叠|代表 100% 堆积折线图|
|带数据标记的线|表示带有数据标记的折线图|
|带数据标记的线堆叠|表示带有数据标记的堆积折线图|
|带数据标记的 Line100PercentStacked|表示带数据标记的 100% 堆积折线图|
|线三维|代表 3D 折线图|
|馅饼|代表饼图|
|饼图3D|代表 3D 饼图|
|派派|代表饼图的饼图|
|馅饼爆炸了|代表爆炸饼图|
|饼图3D爆炸|代表 3D 分解饼图|
|饼图栏|代表饼图条形图|
|分散|代表散点图|
|通过带有数据标记的曲线连接的散点图|表示由曲线连接的散点图，带有数据标记|
|不带数据标记的按曲线连接的散点图|表示由曲线连接的散点图，没有数据标记|
|ScatterConnectedByLinesWithDataMarker|表示由线连接的散点图，带有数据标记|
|不带数据标记的按行分散连接|表示由线条连接的散点图，没有数据标记|
|区域|代表面积图|
|堆积面积|代表堆积面积图|
|面积100%堆叠|代表 100% 堆积面积图|
|三维区域|代表 3D 面积图|
|区域3D堆叠|表示 3D 堆积面积图|
|Area3D100PercentStacked|表示 3D 100% 堆积面积图|
|油炸圈饼|代表圆环图|
|甜甜圈爆炸|代表爆炸圆环图|
|雷达|代表雷达图|
|带数据标记的雷达|表示带有数据标记的雷达图|
|雷达填充|代表填充雷达图|
|表面3D|代表 3D 曲面图|
|表面线框3D|表示线框 3D 曲面图|
|表面轮廓|代表等值线图|
|表面轮廓线框|表示线框轮廓图|
|气泡|代表气泡图|
|泡泡3D|代表 3D 气泡图|
|圆柱|代表圆柱图|
|圆筒堆叠|代表堆积圆柱图|
|气缸100%堆叠|代表 100% 堆叠圆柱图|
|圆柱棒|代表圆柱形条形图。|
|圆柱形条堆叠|表示堆积圆柱形条形图|
|圆柱形条100%堆叠|表示 100% 堆积圆柱形条形图|
|圆柱3D|表示 3D 柱形图|
|锥体|代表圆锥图|
|圆锥堆叠|表示堆积锥图|
|锥体100%堆叠|代表 100% 堆积圆锥图|
|锥形棒|代表圆锥形条形图|
|锥形条堆叠|表示堆积圆锥形条形图|
|锥形条100%堆叠|表示 100% 堆积圆锥形条形图|
|圆锥柱3D|表示 3D 圆锥形柱形图|
|金字塔|代表金字塔图|
|金字塔堆积|代表堆积金字塔图|
|金字塔100%堆叠|代表 100% 堆积金字塔图|
|金字塔酒吧|代表金字塔条形图|
|金字塔酒吧堆积|表示堆积金字塔条形图|
|金字塔条形图100%堆叠|表示 100% 堆积金字塔条形图|
|金字塔柱3D|表示 3D 金字塔柱形图|
{{% alert color="primary" %}}

当您指定一个单元格范围作为数据源时，您只能设置从左上角到右下角的范围。例如，“A1:C3”有效，“C3:A1”无效。

{{% /alert %}}

####  **金字塔图**

执行示例代码时，金字塔图将添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

####  **折线图**

在上面的例子中，只需更改[**图表类型**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)到*线*创建折线图。下面提供了完整的来源。执行代码时，折线图将添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

####  **气泡图**

为了创建气泡图，[**图表类型**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)必须设置为[**图表类型.气泡**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)并且需要相应地设置一些额外的属性，例如 BubbleSizes、Values 和 XValues。执行以下代码后，气泡图将添加到工作表中。

####  **带数据标记图表的线条**

为了使用数据标记图表创建一条线，[**图表类型**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)必须设置为*ChartType.LineWithDataMarkers*并且需要相应地设置一些额外的属性，例如背景区域、系列标记、值和 XValues。执行以下代码后，带有数据标记图表的行将添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

##  **高级主题**
- [阅读和操作 Excel 2016 图表](/cells/zh/net/read-and-manipulate-excel-2016-charts/)
- [管理 Excel 图表的轴](/cells/zh/net/chart-axes/)
- [设置图表外观](/cells/zh/net/setting-chart-appearance/)
- [图表类型](/cells/zh/net/chart-types/)
- [自定义图表](/cells/zh/net/customizing-charts/)
- [设置图表的数据源](/cells/zh/net/data-formatting-in-charts/)
- [管理 Excel 图表的数据标签](/cells/zh/net/insert-datalabels-to-chart/)
- [通过处理智能标记生成图表](/cells/zh/net/generate-chart-by-processing-smart-markers/)
- [获取图表工作表](/cells/zh/net/get-worksheet-of-the-chart/)
- [管理 Excel 图表图例](/cells/zh/net/chart-legend/)
- [操纵头寸规模和设计图表](/cells/zh/net/manipulate-position-size-and-designer-chart/)
- [创建带有引导线的饼图](/cells/zh/net/creating-pie-chart-with-leader-lines/)
- [图表中的形状](/cells/zh/net/controls-in-charts/)
- [管理 Excel 图表的标题](/cells/zh/net/chart-and-axis-titles/)
- [图表渲染](/cells/zh/net/chart-rendering/)
- [获取图表趋势线的方程文本](/cells/zh/net/get-equation-text-of-chart-trendline/)
