---
title: 自定义图表
type: docs
weight: 15
url: /zh/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---
##  **创建图表**

可以使用 Aspose.Cells 将各种图表添加到电子表格中。Aspose.Cells 提供许多灵活的图表对象。本主题讨论 Aspose.Cells' 图表对象。

###  **简单地创建图表**

使用以下示例代码创建一个包含 Aspose.Cells 的图表很简单：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


###  **创建图表的注意事项**

在创建图表之前，了解一些基本概念非常重要，这些概念在使用 Aspose.Cells 创建图表时很有帮助。

####  **绘制对象图表**

Aspose.Cells 提供了一组特殊的类用于创建各种图表。这些类用于创建*图表对象**，充当图表构建块。图表对象如下所示：

- [**轴**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)，图表的轴。
- [**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)，单个 Excel 图表。
- [**图表区**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)，工作表中的图表区域。
- [**图表数据表**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)，图表数据表。
- [**图表框架**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)，图表中的框架对象。
- [**图表点**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)，图表中系列中的单个点。
- [**图表点集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)，包含一个系列中所有点的集合。
- [**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)，一个集合[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象。
-  DataLabels，指定的DataLabels[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**图表点**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**趋势线**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)， ETC。
- [**填充格式**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)，形状的填充格式。
- [**地面**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)，3D 图表的底面。
- [**传奇**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)，图表图例。
- [**线**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)，图表线。
- [**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)，一个集合[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象。
- [**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)，表示图表中的单个数据系列。
- [**刻度标签**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)，与图表轴上的刻度线关联的刻度线标签。
- [**标题**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)，图表或轴的标题。
- [**趋势线**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)，图表中的趋势线。
- [**趋势线系列**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)，指定数据系列的所有趋势线对象的集合。
- [**墙壁**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)，3D 图表的墙壁。

####  **使用图表对象**

如上所述，所有图表对象都是其各自类的实例，并提供特定的属性和方法来执行特定的任务。使用图表对象创建图表。

使用以下命令将任何类型的图表添加到工作表中[**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)收藏。中的每一项[**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)集合代表一个[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)目的。 A[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象封装了自定义图表外观所需的所有图表对象。下一节将介绍如何使用一些基本的图表对象来创建简单的图表。

###  **创建一个简单的图表**

可以使用 Aspose.Cells 创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表均在名为的枚举中预定义[**图表类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)。预定义的图表类型有：

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
要使用 Aspose.Cells 创建图表：

1. 使用以下命令将一些数据添加到工作表单元格中[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)对象的[**设定值**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)方法。
这将用作图表的数据源。
1. 通过调用将图表添加到工作表[**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)收藏的[*添加*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) 方法，封装在[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)目的。
1. 指定图表类型[**图表类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)枚举。
例如，该示例使用[**图表类型.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)值作为图表类型。
1. 访问新的[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象从[**图表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)通过传递其索引来收集。
1. 使用封装在中的任何图表对象[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)管理图表的对象。
下面的示例使用[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)图表对象来指定图表的数据源。

将源数据添加到图表时，数据源可以是一系列单元格（例如“A1:C3”），也可以是一系列不连续的单元格（例如“A1、A3、A5”），或者是一系列单元格。值（例如“1,2,3”）。

{{% alert color="primary" %}}

将单元格范围指定为数据源时，只能设置从左上角到右下角的范围。例如，“A1:C3”有效，“C3:A1”无效。

{{% /alert %}}

这些常规步骤允许您创建任何类型的图表。使用不同的图表对象来创建不同的图表。

执行示例代码时，金字塔图将添加到工作表中，如下所示。

**金字塔图及其数据源**

![待办事项：图像_替代_文本](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

要创建气泡图，[**图表类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)必须设置为[**图表类型.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)并且需要相应地设置一些额外的属性，例如 BubbleSizes、Values 和 XValues。执行以下代码后，气泡图将添加到工作表中，如下所示。

**气泡图及其数据源**

![待办事项：图像_替代_文本](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

####  **带数据标记图表的线条**

要创建带有数据标记图表的线条，[**图表类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)必须设置为[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS)并且需要相应地设置一些额外的属性，例如背景区域、系列标记、值和 XValues。执行以下代码后，带有数据标记图表的行将添加到工作表中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

##  **创建自定义图表**

到目前为止，当我们讨论图表时，我们已经研究了具有标准格式设置的标准图表。我们仅定义数据源，设置一些属性，然后使用默认格式设置创建图表。但Aspose.Cells还支持创建自定义图表，允许开发人员使用自己的格式设置创建图表。

###  **创建自定义图表**

开发人员可以使用 Aspose.Cells simple API 在运行时创建自定义图表。

图表由一系列数据组成。 Aspose.Cells中的每个数据系列都由一个表示[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象而[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)对象作为集合[**系列**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象。创建自定义图表时，开发人员可以自由地将不同类型的图表用于不同的数据系列（收集在一个[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)目的）。

{{% alert color="primary" %}}

目前 Aspose.Cells 仅支持组合饼图、折线图、柱形图和柱状堆栈图的自定义图表，但未来版本将支持更多图表。有关 Aspose.Cells 支持的标准图表的完整列表，请阅读[图表类型](/cells/zh/java/chart-types/)文章。

{{% /alert %}}

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将使用柱形图表示第一个数据系列，使用折线图表示第二个数据系列。结果是我们将柱形图与折线图组合添加到工作表中。

**结合柱形图和折线图的自定义图表**

![待办事项：图像_替代_文本](creating-and-customizing-charts_3.png)

**编程实例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

要查看支持的图表类型列表，请阅读[图表类型](/cells/zh/java/chart-types/)文章。

{{% /alert %}}

