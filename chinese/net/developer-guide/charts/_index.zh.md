---
title: 创建和管理图表
description: 学习如何使用Aspose.Cells for .NET在Microsoft Excel中创建图表。我们的指南将演示可以创建的不同类型的图表，以及如何自定义其外观和格式。
keywords: Aspose.Cells for .NET、图表创建、Microsoft Excel、图表类型、自定义、外观、格式。
linktitle: 图表
type: docs
weight: 130
url: /zh/net/creating-charts/
description: 在C#中为Excel和ODS文件创建图表。
keywords: 创建一个图表，制作一个图形 
---

{{% alert color="primary" %}}

使用Aspose.Cells可以向电子表格添加各种图表。 Aspose.Cells提供许多灵活的图表对象。 本主题讨论了Aspose.Cells的图表对象。

{{% /alert %}}

## **创建图表**

### **创建图表很简单**
使用以下示例代码轻松创建一个Aspose.Cells的图表：
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **创建图表的要点**

在创建图表之前，重要的是了解一些基本概念，这些概念在使用Aspose.Cells创建图表时非常有用。

#### **图表对象**

Aspose.Cells提供了一组特殊的类，位于[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)命名空间中，用于创建Aspose.Cells支持的图表。这些类用于创建**图表对象**，充当图表构建的基础。以下是图表对象的列表:

- Series，图表中的单个数据系列。
- Axis，图表的坐标轴。
- Chart，单个Excel图表。
- ChartArea，工作表中的图表区域。
- ChartDataTable，图表数据表。
- ChartFrame，图表中的框架对象。
- ChartPoint，图表中系列中的单个点。
- ChartPointCollection，包含一个系列中所有点的集合。
- Charts，Chart对象的集合。
- DataLabels，指定系列的所有DataLabel对象的集合。
- FillFormat，形状的填充格式。
- Floor，3D图表的底板。
- Legend，图表图例。
- Line，图表线条。
- SeriesCollection，Series对象的集合。
- TickLabels，与图表轴上的刻度标记相关联的刻度标签。
- Title，图表或坐标轴的标题。
- Trendline，图表中的趋势线。
- TrendlineCollection, 指定数据系列的所有趋势线对象的集合。
- Walls, 3D 图表的墙壁。

#### **使用图表对象**

如上所述，所有的图表对象都是它们各自类的实例，并提供特定的属性和方法来执行特定的任务。使用图表对象来创建图表。

使用 [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) 集合可以向工作表添加任何类型的图表。 [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) 集合中的每个项目代表一个 [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) 对象。 [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) 对象封装了所有其他图表对象，以自定义图表的外观。下一部分介绍如何使用一些基本的图表对象创建一个简单的图表。

### **使用 Aspose.Cells 创建图表**

**步骤:**

1. 使用 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 对象的 [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 方法将一些数据添加到工作表单元格中。
   这将被用作图表的数据源。
1. 通过调用 [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) 集合的 [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) 方法在工作表中添加一个图表，该方法封装在 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 对象中。
1. 使用 [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) 枚举指定图表的类型。
   例如，下面的示例使用 [**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) 值作为图表类型。
1. 通过传递其索引从 [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) 集合中访问新的 [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) 对象。
1. 使用封装在 [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) 对象中的任何绘图对象来管理图表。
   下面的示例使用 [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) 绘图对象指定图表的数据源。

在向图表添加数据源时，数据源可以是单元格范围（如"A1:C3"）、非连续单元格序列（如"A1, A3, A5"）或值序列（如"1,2,3"）。

这些一般步骤可以帮助您创建任何类型的图表。使用不同的绘图对象创建不同的图表。

使用 Aspose.Cells 可以创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表都预先定义在名为 [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) 的枚举中。

预定义的图表类型包括：

|**图表类型**|**描述**|
| :- | :- |
|Column| 表示簇状柱形图表|
|ColumnStacked|代表堆积柱状图
|Column100PercentStacked|代表100%堆积柱状图
|Column3DClustered|代表3D分组柱状图
|Column3DStacked|表示3D堆叠柱形图|
|Column3D100PercentStacked|表示3D 100%堆叠柱形图|
|Column3D|表示3D柱形图|
|Bar|表示分组条形图|
|BarStacked|表示堆叠条形图|
|Bar100PercentStacked|表示100%堆叠条形图|
|Bar3DClustered|表示3D分组条形图|
|Bar3DStacked|表示3D堆叠条形图|
|Bar3D100PercentStacked|表示3D 100%堆叠条形图|
|Line|表示折线图|
|LineStacked|表示堆叠折线图|
|Line100PercentStacked|表示100%堆叠折线图|
|LineWithDataMarkers|表示带有数据标记的折线图|
|LineStackedWithDataMarkers|表示带有数据标记的堆叠折线图|
|Line100PercentStackedWithDataMarkers|表示带有数据标记的100%堆叠折线图|
|Line3D|表示3D折线图|
|Pie|表示饼图|
|Pie3D|表示3D饼图|
|PiePie|表示饼图中的饼图|
|PieExploded|表示爆炸饼图|
|Pie3DExploded|表示3D饼图(爆炸式)|
|PieBar|表示饼图的条形图|
|Scatter|代表散点图
|ScatterConnectedByCurvesWithDataMarker|代表用曲线连接的散点图，带有数据标记
|ScatterConnectedByCurvesWithoutDataMarker|代表用曲线连接的散点图，没有数据标记
|ScatterConnectedByLinesWithDataMarker|代表用线连接的散点图，带有数据标记
|ScatterConnectedByLinesWithoutDataMarker|代表用线连接的散点图，没有数据标记
|Area|表示面积图|
|AreaStacked|表示堆叠面积图|
|Area100PercentStacked|表示百分比堆叠面积图|
|Area3D|表示3D面积图|
|Area3DStacked|表示3D堆叠面积图|
|Area3D100PercentStacked|表示3D百分比堆叠面积图|
|Doughnut|表示圆环图|
|DoughnutExploded|表示爆炸式环形图|
|Radar|代表雷达图
|RadarWithDataMarkers|代表带有数据标记的雷达图
|RadarFilled|表示填充雷达图|
|Surface3D|表示3D曲面图|
|SurfaceWireframe3D|代表三维线框表面图表|
|SurfaceContour|表示等高线图表|
|SurfaceContourWireframe|表示线框等高线图表|
|Bubble|表示气泡图表|
|Bubble3D|表示3D气泡图表|
|Cylinder|表示圆柱图表|
|CylinderStacked|表示堆叠圆柱图表|
|Cylinder100PercentStacked|表示100%堆叠圆柱图表|
|CylindericalBar|代表圆柱棒图表|
|CylindericalBarStacked|代表堆叠圆柱棒图表|
|CylindericalBar100PercentStacked|代表百分比堆叠圆柱棒图表|
|CylindericalColumn3D|代表3D圆柱柱状图表|
|Cone|表示圆锥图表|
|ConeStacked|表示堆叠圆锥图表|
|Cone100PercentStacked|表示100%堆叠圆锥图表|
|ConicalBar|表示圆锥形条形图|
|ConicalBarStacked|表示堆叠圆锥形条形图|
|ConicalBar100PercentStacked|表示100%堆叠圆锥形条形图|
|ConicalColumn3D|表示3D圆锥形柱形图|
|Pyramid|表示金字塔图表|
|PyramidStacked|表示堆叠金字塔图表|
|Pyramid100PercentStacked|代表100%的堆叠金字塔图表|
|PyramidBar|代表金字塔柱状图|
|PyramidBarStacked|代表堆叠金字塔柱状图|
|PyramidBar100PercentStacked|代表100%堆叠金字塔柱状图|
|PyramidColumn3D|代表3D金字塔柱图|
{{% alert color="primary" %}}

当您将一系列单元格指定为数据源时，只能从左上到右下设置范围。例如，“A1:C3”是有效的，而“C3:A1”是无效的。

{{% /alert %}}

#### **金字塔图**

执行示例代码后，将在工作表中添加一个金字塔图表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **折线图**

在上面的示例中，仅将[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)更改为*Line*即可创建折线图。完整的源代码如下所示。执行代码后，将在工作表中添加一个折线图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **气泡图**

为了创建气泡图，必须将[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)设置为[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)，并相应地设置一些额外属性，例如BubbleSizes，Values & XValues。执行以下代码后，将在工作表中添加一个气泡图。

#### **带有数据标记的折线图**

要创建带有数据标记的折线图，必须将[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)设置为*ChartType.LineWithDataMarkers*，并相应地设置一些额外属性，如背景区域、Series Markers、Values & XValues。执行以下代码后，将在工作表中添加带有数据标记的折线图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **高级主题**
- [读取和操作Excel 2016图表](/cells/zh/net/read-and-manipulate-excel-2016-charts/)
- [管理Excel图表的坐标轴](/cells/zh/net/chart-axes/)
- [设置图表外观](/cells/zh/net/setting-chart-appearance/)
- [图表类型](/cells/zh/net/chart-types/)
- [自定义图表](/cells/zh/net/customizing-charts/)
- [为图表设置数据源](/cells/zh/net/data-formatting-in-charts/)
- [管理Excel图表的数据标签](/cells/zh/net/insert-datalabels-to-chart/)
- [通过处理智能标记生成图表](/cells/zh/net/generate-chart-by-processing-smart-markers/)
- [获取图表的工作表](/cells/zh/net/get-worksheet-of-the-chart/)
- [管理Excel图表的图例](/cells/zh/net/chart-legend/)
- [操纵位置大小和设计者图表](/cells/zh/net/manipulate-position-size-and-designer-chart/)
- [使用带有引线的饼图](/cells/zh/net/creating-pie-chart-with-leader-lines/)
- [图表中的形状](/cells/zh/net/controls-in-charts/)
- [管理Excel图表的标题](/cells/zh/net/chart-and-axis-titles/)
- [图表渲染](/cells/zh/net/chart-rendering/)
- [获取图表趋势线的方程文本](/cells/zh/net/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="csharp" >}}
