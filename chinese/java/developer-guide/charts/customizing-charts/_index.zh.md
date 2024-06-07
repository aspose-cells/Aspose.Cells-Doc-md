---
title: 定制图表
type: docs
weight: 15
url: /zh/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **创建图形**

可以使用Aspose.Cells向电子表格添加多种图表。 Aspose.Cells提供许多灵活的图表对象。 本主题讨论了Aspose.Cells的图表对象。

### **简单创建图表**

使用以下示例代码在Aspose.Cells中创建图表很简单:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **创建图表要了解的事项**

在创建图表之前，了解一些基本概念对于使用Aspose.Cells创建图表很有帮助。

#### **图表对象**

Aspose.Cells提供一组特殊的类，用于创建各种图表。这些类用于创建**图表对象**，即图表构建模块。以下是列出的图表对象:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)，图表的轴。
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)，一个Excel单独的图表。
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)，工作表中的图表区域。
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)，图表数据表。
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)，图表中的框架对象。
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)，图表系列中的单个点。
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)，包含一个系列中的所有点的集合。
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)，包含[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象的集合。
- DataLabels，指定[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)，[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)，[**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)等的DataLabels。
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)，形状的填充格式。
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)，3D图表的底板。
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)，图表图例。
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)，图表线。
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)，包含[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象的集合。
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)，表示图表中的单个数据系列。
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)，与图表轴上的刻度标签相关联的刻度标签。
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)，图表或轴的标题。
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)，图表中的趋势线。
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)，包含指定数据系列的所有趋势线对象的集合。
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)，三维图表的墙壁。

#### **使用图表对象**

如上所述，所有图表对象都是它们各自类的实例，并提供特定属性和方法来执行特定任务。使用图表对象创建图表。

使用 [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 集合向工作表中添加任何类型的图表。[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 集合中的每个项代表一个 [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 对象。[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 对象封装了定制图表外观所需的所有图表对象。下一节将展示如何使用一些基本的图表对象创建一个简单的图表。

### **创建简单图表**

使用 Aspose.Cells 可以创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表都预定义在名为 [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) 的枚举中。预定义的图表类型有:

|**图表类型**|**描述**|
| :- | :- |
|Column|代表分组柱形图|
|ColumnStacked|代表堆叠柱形图|
|Column100PercentStacked|代表百分比堆叠柱形图|
|Column3DClustered|代表3D分组柱形图|
|Column3DStacked|代表3D堆叠柱形图|
|Column3D100PercentStacked|代表3D百分比堆叠柱形图|
|Column3D|代表3D柱形图|
|Bar|代表分组条形图|
|BarStacked|代表堆叠条形图|
|Bar100PercentStacked|代表百分比堆叠条形图|
|Bar3DClustered|代表3D分组条形图|
|Bar3DStacked|代表3D堆叠条形图|
|Bar3D100PercentStacked|代表3D百分比堆叠条形图|
|Line|代表折线图|
|LineStacked|代表堆叠折线图|
|Line100PercentStacked|代表百分比堆叠折线图|
|LineWithDataMarkers|代表带数据标记的折线图|
|LineStackedWithDataMarkers|代表带数据标记的堆叠折线图|
|Line100PercentStackedWithDataMarkers|代表带数据标记的百分比堆叠折线图|
|Line3D|代表3D折线图|
|Pie|代表饼图|
|Pie3D|代表3D饼图|
|PiePie|代表饼状图的饼状图|
|PieExploded|代表分裂的饼图|
|Pie3DExploded|代表3D分裂的饼图|
|PieBar|代表饼图的柱状图|
|Scatter|代表散点图|
|ScatterConnectedByCurvesWithDataMarker|代表带数据标记的曲线连接的散点图|
|ScatterConnectedByCurvesWithoutDataMarker|代表不带数据标记的曲线连接的散点图|
|ScatterConnectedByLinesWithDataMarker|代表带数据标记的线连接的散点图|
|ScatterConnectedByLinesWithoutDataMarker|代表不带数据标记的线连接的散点图|
|Area|代表面积图表|
|AreaStacked|代表堆积面积图表|
|Area100PercentStacked|代表100%堆积面积图表|
|Area3D|代表3D面积图表|
|Area3DStacked|代表3D堆积面积图表|
|Area3D100PercentStacked|代表3D 100%堆积面积图表|
|Doughnut|代表环形图|
|DoughnutExploded|代表爆裂环形图|
|Radar|代表雷达图|
|RadarWithDataMarkers|代表带数据标记的雷达图|
|RadarFilled|代表填充雷达图|
|Surface3D|代表3D曲面图|
|SurfaceWireframe3D|代表线框 3D 表面图|
|SurfaceContour|代表等高线图|
|SurfaceContourWireframe|代表线框等高线图|
|Bubble|代表气泡图|
|Bubble3D|代表3D气泡图|
|Cylinder|代表圆柱图|
|CylinderStacked|代表堆积圆柱图|
|Cylinder100PercentStacked|代表100%堆积圆柱图|
|CylindricalBar|代表圆柱柱状图|
|CylindricalBarStacked|代表堆叠圆柱柱状图|
|CylindricalBar100PercentStacked|代表100%堆叠圆柱柱状图|
|CylindricalColumn3D|代表3D圆柱柱状图|
|Cone|代表圆锥图|
|ConeStacked|代表堆积圆锥图|
|Cone100PercentStacked|代表100%堆积圆锥图|
|ConicalBar|代表圆锥条形图|
|ConicalBarStacked|代表堆积圆锥条形图|
|ConicalBar100PercentStacked|代表100%堆积圆锥条形图|
|ConicalColumn3D|表示3D圆锥形柱状图|
|Pyramid|表示金字塔图|
|PyramidStacked|表示堆叠金字塔图|
|Pyramid100PercentStacked|表示百分比堆叠金字塔图|
|PyramidBar|代表金字塔柱状图|
|PyramidBarStacked|表示堆叠金字塔柱状图|
|PyramidBar100PercentStacked|表示百分比堆叠金字塔柱状图|
|PyramidColumn3D|表示3D金字塔柱状图|
要使用 Aspose.Cells 创建图表：

1. 使用[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)对象的[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)方法向工作表单元格添加一些数据。
   这将用作图表的数据源。
1.通过调用 [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) 集合的 [*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int)) 方法，封装在 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 对象中，在工作表中添加一个图表。
1. 使用[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)枚举指定图表类型。
   例如，示例使用 [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) 值作为图表类型。
1. 通过传递索引从[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)集合中获取新的[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)对象。
1. 使用 [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 封装的任何图表对象来管理图表。
   下面的示例使用 [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 图表对象指定图表的数据源。

在向图表添加源数据时，数据源可以是一系列单元格（例如"A1:C3"），或者是一系列不相邻的单元格（例如"A1, A3, A5"），或者是一系列值（例如"1,2,3"）。

{{% alert color="primary" %}}

当您将一组单元格指定为数据源时，只能设置从左上到右下的范围。例如，“A1:C3”为有效值，而“C3:A1”为无效值。

{{% /alert %}}

这些一般步骤允许您创建任何类型的图表。使用不同的图表对象来创建不同的图表。

执行示例代码时，将在工作表中添加一个金字塔图表，如下所示。

**金字塔图表及其数据源**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

要创建气泡图，需要将 [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) 设为 [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)，并相应地设置几个额外的属性，如气泡大小、值和 X 值。执行以下代码后，将在工作表中添加一个气泡图表，如下所示。

**气泡图表及其数据源**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **带数据标记的折线图表**

要创建带有数据标记的折线图，必须将 [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) 设为 [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS)，并相应地设置几个额外的属性，如背景区域、系列标记、值和 X 值。执行以下代码后，将在工作表中添加一个带有数据标记的折线图。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **创建自定义图表**

到目前为止，当我们讨论图表时，我们看了一些具有标准格式设置的标准图表。我们只定义数据源，设置一些属性，图表就会根据其默认格式设置创建。但是 Aspose.Cells 还支持创建自定义图表，允许开发人员使用自定义格式设置创建图表。

### **创建自定义图表**

开发人员可以使用 Aspose.Cells 简单的 API 在运行时创建自定义图表。

图表由数据系列组成。Aspose.Cells中的每个数据系列由[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象表示，而[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)对象用作[**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)对象的集合。在创建自定义图表时，开发人员可以根据需要为不同的数据系列（收集在[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)对象中）使用不同类型的图表。

{{% alert color="primary" %}}

目前Aspose.Cells仅支持合并饼图、折线图、柱状图和堆积柱状图的自定义图表，但将在将来的版本中支持更多类型的图表。有关Aspose.Cells支持的标准图表的完整列表，请阅读 [图表类型](/cells/zh/java/chart-types/) 文章。

{{% /alert %}}

下面的示例代码演示了如何创建自定义图表。在这个示例中，我们将使用柱状图作为第一个数据系列，使用折线图作为第二个系列。结果是我们在工作表中添加了一个组合了柱状图和折线图的图表。

**自定义图表结合了柱状图和折线图**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**编程示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

要查看支持的图表类型列表，请阅读 [图表类型](/cells/zh/java/chart-types/) 文章。

{{% /alert %}}

