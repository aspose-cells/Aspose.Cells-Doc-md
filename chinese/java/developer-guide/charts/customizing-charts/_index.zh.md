---
title: 自定义图表
type: docs
weight: 15
url: /zh/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **创建图表**

使用Aspose.Cells可以向电子表格添加各种图表。 Aspose.Cells提供许多灵活的图表对象。 本主题讨论了Aspose.Cells的图表对象。

### **创建图表很简单**

使用以下示例代码，使用Aspose.Cells简单创建图表：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **创建图表的要点**

在创建图表之前，重要的是了解一些基本概念，这些概念在使用Aspose.Cells创建图表时非常有用。

#### **图表对象**

Aspose.Cells提供了一组特殊的类，用于创建各种类型的图表。 这些类用于创建**图表对象**，作为图表构建模块。 下面列出了图表对象：

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)，图表的轴。
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)，单个Excel图表。
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)，工作表中的图表区域。
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)，图表数据表。
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)，图表中的框架对象。
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)，图表系列中的单个点。
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)，包含一个系列中所有点的集合。
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)，包含 [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 个对象的集合。
- DataLabels，指定 [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)，[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)，[**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline) 等的 DataLabels。
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)，形状的填充格式。
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)，3D 图表的底板。
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)，图表图例。
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)，图表线条。
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)，包含 [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) 个对象的集合。
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)，代表图表或坐标轴中的单个数据系列。
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)，与图表坐标轴上的刻度标签相关联的刻度标记标签。
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)，图表或坐标轴的标题。
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)，图表中的趋势线。
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)，指定数据系列的所有趋势线对象的集合。
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)，3D 图表的墙。

#### **使用图表对象**

如上所述，所有的图表对象都是它们各自类的实例，并提供特定的属性和方法来执行特定的任务。使用图表对象来创建图表。

使用 [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 集合向工作表添加任何类型的图表。[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 集合中的每个项目代表一个 [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 对象。一个 [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 对象封装了所有自定义图表外观所需的图表对象。下一节将展示如何使用一些基本的图表对象来创建一个简单的图表。

### **创建一个简单的图表**

使用 Aspose.Cells 可以创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表都预定义在名为 [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) 的枚举中。预定义的图表类型包括：

|**图表类型**|**描述**|
| :- | :- |
|Column|代表分组柱状图
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
|Scatter|表示散点图|
|ScatterConnectedByCurvesWithDataMarker|表示用曲线连接的散点图，带数据标记|
|ScatterConnectedByCurvesWithoutDataMarker|表示用曲线连接的散点图，无数据标记|
|ScatterConnectedByLinesWithDataMarker|表示用线连接的散点图，带数据标记|
|ScatterConnectedByLinesWithoutDataMarker|表示用线连接的散点图，无数据标记|
|Area|表示面积图|
|AreaStacked|表示堆叠面积图|
|Area100PercentStacked|表示百分比堆叠面积图|
|Area3D|表示3D面积图|
|Area3DStacked|表示3D堆叠面积图|
|Area3D100PercentStacked|表示3D百分比堆叠面积图|
|Doughnut|表示圆环图|
|DoughnutExploded|表示爆炸式环形图|
|Radar|表示雷达图|
|RadarWithDataMarkers|表示带数据标记的雷达图|
|RadarFilled|表示填充雷达图|
|Surface3D|表示3D曲面图|
|SurfaceWireframe3D|表示线框3D曲面图|
|SurfaceContour|表示等高线图表|
|SurfaceContourWireframe|表示线框等高线图表|
|Bubble|表示气泡图表|
|Bubble3D|表示3D气泡图表|
|Cylinder|表示圆柱图表|
|CylinderStacked|表示堆叠圆柱图表|
|Cylinder100PercentStacked|表示100%堆叠圆柱图表|
|CylindricalBar|表示圆柱形条形图。|
|CylindricalBarStacked|表示堆叠圆柱形条形图|
|CylindricalBar100PercentStacked|表示100%堆叠圆柱形条形图|
|CylindricalColumn3D|表示3D圆柱形柱形图|
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
|PyramidBar|代表堆叠金字塔柱状图|
|PyramidBarStacked|代表堆叠金字塔柱状图|
|PyramidBar100PercentStacked|代表100%堆叠金字塔柱状图|
|PyramidColumn3D|代表3D金字塔柱图|
使用Aspose.Cells创建图表：

1. 使用 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) 对象的 [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) 方法将一些数据添加到工作表单元格中。
   这将被用作图表的数据源。
1. 通过在 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 对象中封装的 [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 集合的 *add* 方法添加图表到工作表单中。
1. 使用 [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) 枚举指定图表的类型。
   例如，示例将 [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) 值用作图表类型。
1. 通过传递其索引从 [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 集合中访问新的 [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 对象。
1. 使用封装在 [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 对象中的任何绘图对象来管理图表。
   下面的示例使用 [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 绘图对象指定图表的数据源。

在向图表添加数据源时，数据源可以是单元格范围（如"A1:C3"）、非连续单元格序列（如"A1, A3, A5"）或值序列（如"1,2,3"）。

{{% alert color="primary" %}}

当将单元格范围指定为数据源时，只能设置从左上到右下的范围。例如，"A1:C3" 是有效的，而"C3:A1" 是无效的。

{{% /alert %}}

这些一般步骤可以帮助您创建任何类型的图表。使用不同的绘图对象创建不同的图表。

执行示例代码时，将向工作表添加一个金字塔图表，如下所示。

**带有数据源的金字塔图表**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

要创建气泡图，必须将 [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) 设置为 [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)，并相应地设置几个额外属性，如气泡大小、值和 X 值。执行以下代码后，将向工作表添加气泡图。

**带有数据源的气泡图**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **带有数据标记的折线图**

要创建带有数据标记的折线图，必须将[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)设置为[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS)，并相应地设置一些额外的属性，如背景区域、系列标记、值和X值。执行以下代码后，工作表中将添加一个带有数据标记的折线图。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **创建自定义图表**

到目前为止，在讨论图表时，我们已经看过具有标准格式设置的标准图表。我们仅定义数据源，设置一些属性，然后图表将以其默认格式设置创建。但是Aspose.Cells还支持创建自定义图表，允许开发人员使用自定义格式设置创建图表。

### **创建自定义图表**

开发人员可以使用Aspose.Cells的简单API在运行时创建自定义图表。

图表由数据系列组成。在Aspose.Cells中，每个数据系列由一个[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象表示，而[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)对象则作为[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象的集合。在创建自定义图表时，开发人员可以自由选择不同类型的图表用于不同的数据系列（收集在一个[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)对象中）。

{{% alert color="primary" %}}

目前，Aspose.Cells仅支持结合饼图、折线图、柱形图和堆叠柱形图的自定义图表，但将在未来版本中支持更多的图表。要查看Aspose.Cells支持的标准图表的完整列表，请阅读[图表类型](/cells/zh/java/chart-types/)文章。

{{% /alert %}}

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是，我们在工作表中添加了一个柱形图，结合了一条折线图。

**结合柱形图和折线图的自定义图表**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**编程示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

要查看支持的图表类型列表，请阅读[图表类型](/cells/zh/java/chart-types/)文章。

{{% /alert %}}

