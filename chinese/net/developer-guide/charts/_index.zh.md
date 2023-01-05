---
title: 创建和管理图表
linktitle: 图表
type: docs
weight: 130
url: /zh/net/creating-charts/
description: 在 CSharp 中为 Excel 和 ODS 文件创建图表。
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

可以使用 Aspose.Cells 向电子表格添加各种图表。Aspose.Cells 提供了许多灵活的图表对象。本主题讨论 Aspose.Cells' 图表对象。

{{% /alert %}}

## **创建图表**

### **简单地创建一个图表**
使用以下示例代码创建带有 Aspose.Cells 的图表很简单：
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **创建图表的注意事项**

在创建图表之前，了解一些在使用 Aspose.Cells 创建图表时有用的基本概念非常重要。

#### **图表对象**

Aspose.Cells 提供了一组特殊的类[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)用于创建 Aspose.Cells 支持的图表的命名空间。这些类用于创建**图表对象**，它们充当图表构建块。图表对象如下所列：

- 系列，图表中的单个数据系列。
- 轴，图表的轴。
- 图表，单个 Excel 图表。
- ChartArea，工作表中的图表区域。
- ChartDataTable，图表数据表。
- ChartFrame，图表中的框架对象。
- ChartPoint，图表系列中的单个点。
- ChartPointCollection，一个包含一个系列中所有点的集合。
- 图表，图表对象的集合。
- DataLabels，指定系列的所有 DataLabel 对象的集合。
- FillFormat，形状的填充格式。
- 地板，3D 图表的地板。
- 图例，图表图例。
- 线，图表线。
- SeriesCollection，Series 对象的集合。
- TickLabels，与图表轴上的刻度线关联的刻度线标签。
- 标题，图表或轴的标题。
- 趋势线，图表中的趋势线。
- TrendlineCollection，指定数据系列的所有趋势线对象的集合。
- 墙壁，3D 图表的墙壁。

#### **使用图表对象**

如上所述，所有图表对象都是其各自类的实例，并提供特定的属性和方法来执行特定的任务。使用图表对象创建图表。

使用[**图表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)收藏。中的每一项[**图表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)集合代表一个[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)目的。一种[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)对象封装了自定义图表外观所需的所有其他图表对象。下一节将展示如何使用一些基本的图表对象来创建一个简单的图表。

### **使用 Aspose.Cells 创建图表**

**脚步：**

1. 将一些数据添加到工作表单元格中[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)对象的[**认沽价值**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。
这将用作图表的数据源。
1. 通过调用将图表添加到工作表[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)收藏的[**添加**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add)方法，封装在[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)目的。
1. 指定图表类型[**图表类型**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)枚举。
例如，下面的示例使用[**ChartType.金字塔**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)值作为图表类型。
1. 访问新的[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)对象来自[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)通过传递其索引进行收集。
1. 使用封装在[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)对象来管理图表。
下面的示例使用[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)图表对象指定图表的数据源。

向图表添加源数据时，数据源可以是单元格区域（如“A1:C3”），也可以是不连续的单元格序列（如“A1,A3,A5”），也可以是值（例如“1,2,3”）。

这些一般步骤允许您创建任何类型的图表。使用不同的图表对象来创建不同的图表。

使用 Aspose.Cells 可以创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表都预定义在一个名为[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

预定义的图表类型是：

|**图表类型**|**描述**|
|:- |:- |
|柱子|表示簇状柱形图|
|列堆叠|表示堆积柱形图|
|列 100% 堆叠|表示 100% 堆积柱形图|
|Column3D簇状|表示 3D 簇状柱形图|
|列 3D 堆叠|表示 3D 堆积柱形图|
|Column3D100PercentStacked|表示 3D 100% 堆积柱形图|
|立柱三维|表示 3D 柱形图|
|酒吧|表示簇状条形图|
|酒吧堆叠|表示堆积条形图|
|Bar100Percent 堆叠|表示 100% 堆积条形图|
|Bar3DClustered|表示 3D 簇状条形图|
|Bar3D堆叠|表示 3D 堆积条形图|
|Bar3D100PercentStacked|表示 3D 100% 堆积条形图|
|线|代表折线图|
|线堆叠|表示堆叠折线图|
|Line100Percent 堆叠|表示 100% 堆叠折线图|
|带数据标记的线|表示带有数据标记的折线图|
|LineStackedWithDataMarkers|表示带有数据标记的堆积折线图|
|Line100PercentStackedWithDataMarkers|表示带有数据标记的 100% 堆叠折线图|
|直线三维|表示 3D 折线图|
|馅饼|代表饼图|
|Pie3D|表示 3D 饼图|
|派派|表示饼图的饼图|
|馅饼爆炸|代表分解饼图|
|饼图3D分解|表示 3D 爆炸饼图|
|馅饼吧|代表饼图条|
|分散|代表散点图|
|ScatterConnectedByCurvesWithDataMarker|表示由曲线连接的散点图，带有数据标记|
|ScatterConnectedByCurvesWithoutDataMarker|表示由曲线连接的散点图，没有数据标记|
|ScatterConnectedByLinesWithDataMarker|表示由线连接的散点图，带有数据标记|
|ScatterConnectedByLinesWithoutDataMarker|表示由线连接的散点图，没有数据标记|
|区域|代表面积图|
|面积堆叠|表示堆积面积图|
|面积 100% 堆叠|表示 100% 堆积面积图|
|三维区域|表示 3D 面积图|
|Area3D堆叠|表示 3D 堆积面积图|
|Area3D100PercentStacked|表示 3D 100% 堆积面积图|
|油炸圈饼|代表甜甜圈图|
|甜甜圈爆炸|代表爆炸甜甜圈图|
|雷达|代表雷达图|
|带数据标记的雷达|用数据标记表示雷达图|
|雷达填充|表示填充雷达图|
|Surface3D|表示 3D 曲面图|
|表面线框3D|表示线框 3D 曲面图|
|表面轮廓|代表等高线图|
|表面轮廓线框|表示线框等高线图|
|气泡|代表气泡图|
|泡泡3D|代表3D气泡图|
|圆柱|表示柱面图|
|圆柱叠层|表示堆积柱面图|
|圆柱100%堆叠|表示 100% 堆积柱面图|
|圆柱棒|表示圆柱形条形图。|
|圆柱形条堆叠|表示堆积柱形条形图|
|CylindericalBar100PercentStacked|表示 100% 堆积柱形条形图|
|圆柱柱3D|表示 3D 圆柱柱形图|
|锥体|代表圆锥图|
|圆锥堆叠|表示堆叠圆锥图|
|Cone100Percent堆叠|表示 100% 堆积圆锥图|
|锥形棒|代表锥形条形图|
|锥形条堆叠|表示堆叠圆锥形条形图|
|ConicalBar100PercentStacked|表示 100% 堆积锥形条形图|
|锥形柱3D|表示 3D 锥形柱形图|
|金字塔|代表金字塔图|
|金字塔堆叠|表示堆积金字塔图|
|金字塔100%堆积|表示 100% 堆积金字塔图|
|金字塔酒吧|代表金字塔条形图|
|金字塔酒吧堆叠|表示堆积金字塔条形图|
|PyramidBar100PercentStacked|表示 100% 堆积金字塔条形图|
|金字塔柱3D|表示 3D 金字塔柱形图|
{{% alert color="primary" %}}

当您指定一个单元格范围作为数据源时，您只能设置从左上角到右下角的范围。例如，“A1:C3”有效，“C3:A1”无效。

{{% /alert %}}

#### **金字塔图**

执行示例代码时，金字塔图将添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **折线图**

在上面的示例中，只需更改[**图表类型**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)到*线*创建折线图。下面提供了完整的源代码。执行代码时，工作表中会添加一个折线图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **气泡图**

为了创建气泡图，[**图表类型**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)必须设置为[**ChartType.气泡**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)并且需要相应地设置一些额外的属性，例如 BubbleSizes、Values 和 XValues。执行以下代码后，气泡图将添加到工作表中。

#### **符合数据标记图表**

为了用数据标记图表创建一条线，[**图表类型**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)必须设置为*ChartType.LineWithDataMarkers*并且需要相应地设置一些额外的属性，例如背景区域、系列标记、值和 X 值。执行以下代码后，带有数据标记图表的一行将添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **推进主题**
- [读取和操作 Excel 2016 图表](/cells/zh/net/read-and-manipulate-excel-2016-charts/)
- [管理 Excel 图表的轴](/cells/zh/net/chart-axes/)
- [设置图表外观](/cells/zh/net/setting-chart-appearance/)
- [图表类型](/cells/zh/net/chart-types/)
- [自定义图表](/cells/zh/net/customizing-charts/)
- [为图表设置数据源](/cells/zh/net/data-formatting-in-charts/)
- [管理 Excel 图表的数据标签](/cells/zh/net/insert-datalabels-to-chart/)
- [通过处理智能标记生成图表](/cells/zh/net/generate-chart-by-processing-smart-markers/)
- [获取图表的工作表](/cells/zh/net/get-worksheet-of-the-chart/)
- [管理 Excel 图表图例](/cells/zh/net/chart-legend/)
- [操纵头寸规模和设计师图表](/cells/zh/net/manipulate-position-size-and-designer-chart/)
- [创建带引导线的饼图](/cells/zh/net/creating-pie-chart-with-leader-lines/)
- [图表中的形状](/cells/zh/net/controls-in-charts/)
- [管理 Excel 图表的标题](/cells/zh/net/chart-and-axis-titles/)
- [图表渲染](/cells/zh/net/chart-rendering/)
- [获取图表趋势线的公式文本](/cells/zh/net/get-equation-text-of-chart-trendline/)
