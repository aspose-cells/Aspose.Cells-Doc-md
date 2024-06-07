---
title: 图表格式
type: docs
weight: 20
url: /zh/java/chart-formatting/
---

## **设置图表外观**

在 [图表类型](/cells/zh/java/chart-types/) 中，我们简要介绍了 Aspose.Cells 提供的各种图表和图表对象类型。

在本文中，我们讨论了如何通过设置许多不同属性来自定义图表的外观：

- [设置图表区域](/cells/zh/java/chart-formatting/#setting-chart-area)。
- [设置图表线条](/cells/zh/java/chart-formatting/#setting-chart-lines)。
- [应用主题](/cells/zh/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts)。
- [为图表和轴设置标题](/cells/zh/java/chart-formatting/#setting-the-titles-of-charts-or-axes)。
- [处理网格线](/cells/zh/java/chart-formatting/#setting-major-gridlines)。
- [为后墙和侧墙设置边框](/cells/zh/java/chart-formatting/#setting-borders-for-back-and-side-walls)。

### **设置图表区域**

图表中有不同类型的区域，Aspose.Cells 提供了修改每个区域外观的灵活性。开发人员可以通过更改其前景色、背景色和填充格式等来应用不同的格式设置。

在下面的示例中，我们已在图表的不同类型区域上应用了不同的格式设置。这些区域包括：

- 绘图区域
- 图表区域
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 区域
- 单个点的面积为一个 [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

执行示例代码后，工作表中将添加一个柱状图，如下所示:

**带填充区域的柱状图** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **设置图表线条**

开发人员还可以在示例中所示的 [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 的线条或数据标记上应用不同类型的样式。执行示例代码后，工作表中将添加一个柱状图，如下所示:

**应用线条样式后的柱状图** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **应用Microsoft Excel 2007/2010主题到图表**

开发人员可以像示例中所示那样，为 [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 或其他图表对象应用不同的 Microsoft Excel 主题和颜色。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **设置图表或轴的标题**

您可以使用 Microsoft Excel 在所示的 WYSIWYG 环境中设置图表及其轴的标题。

**使用 Microsoft Excel 设置图表及其轴的标题** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells 还允许开发人员在运行时设置图表及其轴的标题。所有图表及其轴都含有一个 [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text) 方法，可用于设置它们的标题，如示例中所示。执行示例代码后，工作表中将添加一个柱状图，如下所示:

**设置标题后的柱状图** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **设置主要网格线**

#### **隐藏主要网格线**

开发人员可以通过使用 [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line) 对象的 [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) 方法来控制主要网格线的可见性。隐藏主要网格线后，工作表中添加的柱状图将呈现以下外观:

**带隐藏主要网格线的柱状图** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **更改主要网格线设置**

开发人员不仅可以控制主要网格线的可见性，还可以控制其他属性，包括颜色等。设置主要网格线的颜色后，工作表中添加的柱状图将呈现以下外观:

**带彩色主要网格线的柱状图** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **设置背景和侧面墙的边框**

自 Microsoft Excel 2007 发布以来，3D 图表的墙壁被分为两部分：侧墙和背墙，请使用两个 [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) 对象分别表示它们，您可以通过 [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) 和 [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall) 来访问它们。

下面的示例显示了如何通过使用不同属性设置侧墙的边框。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **更改图表位置和大小**

有时，您想要更改工作表中新建或现有图表的位置或大小。Aspose.Cells 提供 [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) 属性来实现这一点。您可以使用其子属性重新调整图表的新 **高度** 和 **宽度**，或者使用新的 **X** 和 **Y** 坐标重新定位它。

### **修改图表的位置和大小**

要更改图表的位置（X、Y 坐标）和大小（高度、宽度），请使用以下属性:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

下面的示例说明了上述属性的用法。它加载了包含图表的现有工作簿的第一个工作表。然后重新调整图表的大小和位置，并保存工作簿。

在执行示例代码之前，源文件如下所示:

**执行示例代码之前的图表大小和位置** 

![todo:image_alt_text](chart-formatting_7.png)

执行后，输出文件如下所示:

**执行示例代码后的图表大小和位置** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **操纵设计图表**

在某些情况下，您可能需要操纵或修改设计模板文件中的图表。Aspose.Cells 完全支持操纵带有其内容和元素的设计图表。数据、图表内容、背景图像和格式可以准确保留。

### **在模板文件中操纵设计图表**

要在模板文件中操纵设计图表，请使用与所有图表相关的 API 调用。例如，使用 [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) 属性获取模板文件中现有的图表集合。

#### **创建图表**

以下示例展示了如何创建饼图。我们稍后将操纵该图表。以下输出是由代码生成的。

**输入饼图** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **操作图表**

以下示例展示了如何操纵现有图表。在这个例子中，我们修改了上面创建的图表。以下输出由代码生成。请注意，图表标题的颜色已从蓝色更改为黑色，'England 30000' 已更改为 'United Kingdom, 30K'。

**饼图已被修改** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **在设计模板中操作折线图**

在此示例中，我们将操作一条折线图。 我们将向现有图表添加一些数据系列并更改它们的线条颜色。

首先看一下设计师线图。

**输入线图** 

![todo:image_alt_text](chart-formatting_11.png)

现在我们使用下面的代码操纵线图 (包含在 **linechart.xls** 文件中)。以下输出由代码生成。

**被操纵的线图** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **使用迷你图**

Microsoft Excel 2010可以以前所未有的方式分析信息。它允许用户通过新的数据分析和可视化工具追踪和突出重要的数据趋势。迷你图是一种迷你图表，您可以将其放在单元格内，以便同时查看数据和图表。正确使用迷你图，可以加快数据分析的速度并更直观。它们还提供信息的简单视图，避免了使用许多繁杂图表的拥挤工作表。

Aspose.Cells提供了一个API来操作电子表格中的迷你图。

### **Microsoft Excel中的迷你图**

在Microsoft Excel 2010中插入迷你图：

1. 选择要显示迷你图的单元格。为了便于查看，选择数据旁边的单元格。
1. 在功能区上单击 **插入**，然后在 **迷你图** 组中选择 **列**。

![todo:image_alt_text](chart-formatting_13.png)

1. 选择或输入工作表中包含原始数据的单元格范围。
   图表出现。

迷你图表有助您查看趋势，例如，垒球联赛的胜利或失败记录。迷你图表甚至可以总结每支球队在联赛中的整个赛季。

![todo:image_alt_text](chart-formatting_14.png)

### **使用Aspose.Cells进行迷你图**

开发人员可以使用Aspose.Cells提供的API创建、删除或读取迷你图表 (在模板文件中)。通过为给定的数据范围添加自定义图形，开发人员可以自由地向选定的单元格区域添加不同类型的微小图表。

以下示例演示了迷你图功能。示例显示如何：

1. 打开一个简单的模板文件。
1. 读取工作表的迷你图信息。
1. 为给定的数据范围添加新的迷你图到单元格区域。
1. 将Excel文件保存到磁盘。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **将3D格式应用到图表**

您可能需要3D图表样式，以便根据您的情况获得所需的结果。Aspose.Cells APIs提供了相关的API，可以应用Microsoft Excel 2007的3D格式，正如本文所示。

### **将3D格式设置到图表**

下面提供了一个完整的示例，演示如何创建一个图表并应用Microsoft Excel 2007的3D格式。执行上述示例代码后，工作表中将添加一个列图 (带有3D效果) 如下所示。

**带有3D格式的列图**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

有关支持的2D和3D图表的完整列表，请参阅 [渲染支持的图表类型](/cells/zh/java/chart-rendering/#supported-chart-types-for-rendering)。

{{% /alert %}}

## **高级主题**
- [设置图表的背景填充为图片](/cells/zh/java/set-picture-as-background-fill-in-the-chart/)
