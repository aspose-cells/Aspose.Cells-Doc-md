---
title: 自定义图表
type: docs
weight: 15
url: /zh/java/creating-and-customizing-charts/
---
## **创建图表**

可以使用 Aspose.Cells 向电子表格添加各种图表。Aspose.Cells 提供了许多灵活的图表对象。本主题讨论 Aspose.Cells' 图表对象。

### **简单地创建一个图表**

使用以下示例代码创建带有 Aspose.Cells 的图表很简单：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **创建图表的注意事项**

在创建图表之前，了解一些在使用 Aspose.Cells 创建图表时有用的基本概念非常重要。

#### **图表对象**

Aspose.Cells 提供了一组特殊的类，用于创建各种图表。这些类用于创建**图表对象**，它们充当图表构建块。图表对象如下所列：

- [**轴**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), 图表的轴。
- [**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)，单个 Excel 图表。
- [**图表区**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)，工作表中的图表区域。
- [**图表数据表**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)图表数据表。
- [**图表框**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)图表中的框架对象。
- [**图表点**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)图表系列中的单个点。
- [**图表点集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)，一个包含一个系列中所有点的集合。
- [**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 的集合[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象。
-  DataLabels，指定的DataLabels[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**图表点**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**趋势线**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)， ETC。
- [**填充格式**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)形状的填充格式。
- [**地面**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)3D 图表的底部。
- [**传奇**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)图表图例。
- [**线**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), 图表线。
- [**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 的集合[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象。
- [**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), 代表图表中的单个数据系列。
- [**刻度标签**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)，与图表轴上的刻度线关联的刻度线标签。
- [**标题**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)图表或轴的标题。
- [**趋势线**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), 图表中的趋势线。
- [**趋势线系列**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)指定数据系列的所有趋势线对象的集合。
- [**墙壁**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), 3D 图表的墙壁。

#### **使用图表对象**

如上所述，所有图表对象都是其各自类的实例，并提供特定的属性和方法来执行特定的任务。使用图表对象创建图表。

使用[**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)收藏。中的每一项[**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)集合代表一个[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)目的。一种[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象封装了自定义图表外观所需的所有图表对象。下一节将展示如何使用一些基本的图表对象来创建一个简单的图表。

### **创建一个简单的图表**

使用 Aspose.Cells 可以创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表都预定义在一个名为[**图表类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType).预定义的图表类型是：

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
|带数据标记的雷达|代表带有数据标记的雷达图|
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
|CylindricalBar100PercentStacked|表示 100% 堆积柱形条形图|
|圆柱3D|表示 3D 圆柱柱形图|
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
要使用 Aspose.Cells 创建图表：

1. 将一些数据添加到工作表单元格中[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)对象的[**设定值**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)方法。
这将用作图表的数据源。
1. 通过调用将图表添加到工作表[**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)收藏的[*添加*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) 方法，封装在[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)目的。
1. 指定图表类型[**图表类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)枚举。
例如，该示例使用[**ChartType.金字塔**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)值作为图表类型。
1. 访问新的[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象来自[**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)通过传递其索引进行收集。
1. 使用封装在[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象来管理图表。
下面的示例使用[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)图表对象指定图表的数据源。

向图表添加源数据时，数据源可以是单元格区域（如“A1:C3”），也可以是不连续的单元格序列（如“A1,A3,A5”），也可以是值（例如“1,2,3”）。

{{% alert color="primary" %}}

将单元格范围指定为数据源时，只能将范围设置为从左上角到右下角。例如，“A1:C3”有效，“C3:A1”无效。

{{% /alert %}}

这些一般步骤允许您创建任何类型的图表。使用不同的图表对象来创建不同的图表。

执行示例代码时，金字塔图将添加到工作表中，如下所示。

**金字塔图及其数据源**

![待办事项：图片_替代_文本](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

要创建气泡图，[**图表类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)必须设置为[**图表类型.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)并且需要相应地设置一些额外的属性，例如 BubbleSizes、Values 和 XValues。执行以下代码后，气泡图将添加到工作表中，如下所示。

**气泡图及其数据源**

![待办事项：图片_替代_文本](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **符合数据标记图表**

要创建带有数据标记图表的线条，[**图表类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)必须设置为[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS)并且需要相应地设置一些额外的属性，例如背景区域、系列标记、值和 XValues。执行以下代码后，带有数据标记图表的行将添加到工作表中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **创建自定义图表**

到目前为止，当我们讨论图表时，我们已经查看了具有标准格式设置的标准图表。我们只定义数据源，设置一些属性，并使用默认格式设置创建图表。但 Aspose.Cells 还支持创建自定义图表，允许开发者创建具有自己格式设置的图表。

### **创建自定义图表**

开发人员可以使用 Aspose.Cells 简单 API 在运行时创建自定义图表。

图表由数据系列组成。 Aspose.Cells 中的每个数据系列都由一个[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象而[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)对象作为集合[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象。创建自定义图表时，开发人员可以自由地为不同的数据系列（收集在一个[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)目的）。

{{% alert color="primary" %}}

目前 Aspose.Cells 仅支持结合饼图、折线图、柱形图和柱形堆栈图的自定义图表，但未来版本将支持更多图表。有关 Aspose.Cells 支持的标准图表的完整列表，请阅读[图表类型](/cells/zh/java/chart-types/)文章。

{{% /alert %}}

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是我们向工作表添加了一个柱形图和一个折线图。

**组合柱形图和折线图的自定义图表**

![待办事项：图片_替代_文本](creating-and-customizing-charts_3.png)

**编程实例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

要查看支持的图表类型列表，请阅读[图表类型](/cells/zh/java/chart-types/)文章。

{{% /alert %}}

