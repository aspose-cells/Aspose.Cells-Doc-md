---
title: 图表格式
type: docs
weight: 20
url: /zh/java/chart-formatting/
---
## **设置图表外观**

在[图表类型](/cells/zh/java/chart-types/)，我们简单介绍了Aspose.Cells提供的图表类型和图表对象。

在本文中，我们讨论了如何通过设置许多不同的属性来自定义图表的外观：

- [设置图表区域](/cells/zh/java/chart-formatting/#setting-chart-area).
- [设置图表线条](/cells/zh/java/chart-formatting/#setting-chart-lines).
- [应用主题](/cells/zh/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [设置图表和坐标轴的标题](/cells/zh/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [使用网格线](/cells/zh/java/chart-formatting/#setting-major-gridlines).
- [为后墙和侧墙设置边框](/cells/zh/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **设置图表区**

图表中有不同类型的区域，Aspose.Cells 提供了修改每个区域外观的灵活性。开发人员可以通过更改前景色、背景色和填充格式等，在一个区域上应用不同的格式设置。

在下面给出的示例中，我们对图表的不同类型区域应用了不同的格式设置。这些领域包括：

- 地块面积
- 图表区
- [**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)区域
- 一个点的面积[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

执行示例代码后，将在工作表中添加一个柱形图，如下所示：

**带有填充区域的柱形图** 

![待办事项：图像_替代_文本](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **设置图表线**

开发人员还可以在线条或数据标记上应用不同类型的样式[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)如下例所示。执行示例代码会在工作表中添加一个柱形图，如下所示：

**应用线条样式后的柱形图** 

![待办事项：图像_替代_文本](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **将 Microsoft Excel 2007/2010 主题应用于图表**

开发人员可以应用不同的 Microsoft Excel 主题和颜色到[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)或其他图表对象，如下例所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **设置图表或坐标轴的标题**

您可以使用 Microsoft Excel 在所见即所得环境中设置图表的标题及其轴，如下所示。

**使用 Microsoft Excel 设置图表及其轴的标题** 

![待办事项：图像_替代_文本](chart-formatting_3.png)

Aspose.Cells 还允许开发人员在运行时设置图表的标题及其轴。所有图表及其轴都包含一个[**标题.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)可用于设置其标题的方法，如下例所示。执行示例代码后，将在工作表中添加一个柱形图，如下所示：

**设置标题后的柱状图** 

![待办事项：图像_替代_文本](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **设置主要网格线**

#### **隐藏主要网格线**

开发人员可以通过使用[**设置可见**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible)的方法[**线**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)目的。隐藏主要网格线后，添加到工作表的柱形图具有以下外观：

**隐藏主要网格线的柱形图** 

![待办事项：图像_替代_文本](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **更改主要网格线设置**

开发人员不仅可以控制主要网格线的可见性，还可以控制其他属性，包括颜色等。设置主要网格线的颜色后，添加到工作表的柱形图将具有以下外观：

**带有彩色主要网格线的柱形图** 

![待办事项：图像_替代_文本](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **设置背墙和侧墙的边框**

自Microsoft Excel 2007发布以来，3D图表的墙被分为侧墙和后墙两部分，所以我们必须使用两个[**墙壁**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)对象来分别表示它们，您可以使用[**图表.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall)和[**图表.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

下面给出的示例显示了如何使用不同的属性设置侧壁的边框。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **更改图表位置和大小**

有时，您想要更改工作表中新图表或现有图表的位置或大小。 Aspose.Cells 提供了[**图表.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject)财产来实现这一点。您可以使用它的子属性来重新调整图表的大小**高度**和**宽度**或用新的重新定位**X** 和**Y** 坐标。

### **修改图表的位置和大小**

要更改图表的位置（X、Y 坐标）和大小（高度、宽度），请使用以下属性：

1. [**Chart.getChartObject().get/setWidth() 方法**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**图表.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**图表.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**图表.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

下面的例子解释了上述属性的用法。它加载现有工作簿，该工作簿在其第一个工作表中包含一个图表。然后重新调整图表的大小和位置并保存工作簿。

在示例代码执行之前，源文件如下所示：

**示例代码执行前的图表大小和位置** 

![待办事项：图像_替代_文本](chart-formatting_7.png)

执行后，输出文件如下所示：

**示例代码执行后的图表大小和位置** 

![待办事项：图像_替代_文本](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **操纵设计师图表**

有时您可能需要操作或修改设计器模板文件中的图表。 Aspose.Cells 完全支持使用其内容和元素来操作设计器图表。可以准确保存数据、图表内容、背景图像和格式。

### **在模板文件中操作设计器图表**

要在模板文件中操作设计器图表，请使用所有与图表相关的 API 调用。例如，使用[**工作表.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts)属性以获取模板文件中的现有图表集合。

#### **创建图表**

以下示例显示了如何创建饼图。稍后我们将操作此图表。以下输出由代码生成。

**输入饼图** 

![待办事项：图像_替代_文本](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **操纵图表**

以下示例显示如何操作现有图表。在这个例子中，我们修改上面创建的图表。以下输出由代码生成。请注意，图表标题的颜色已从蓝色变为黑色，并且“England 30000”已更改为“United Kingdom, 30K”。

**饼图已修改** 

![待办事项：图像_替代_文本](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **在设计器模板中操作折线图**

在这个例子中，我们将操作一个折线图。我们将向现有图表添加一些数据系列并更改它们的线条颜色。

首先，看一下设计器折线图。

**输入折线图** 

![待办事项：图像_替代_文本](chart-formatting_11.png)

现在我们操作折线图（包含在**折线图.xls**文件）使用以下代码。以下输出由代码生成。

**操纵的折线图** 

![待办事项：图像_替代_文本](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **使用迷你图**

Microsoft Excel 2010 可以以比以往更多的方式分析信息。它允许用户使用新的数据分析和可视化工具跟踪和突出重要的数据趋势。迷你图是可以放置在单元格内的迷你图表，以便您可以在同一个表格中查看数据和图表。当正确使用迷你图时，数据分析会更快、更切题。它们还提供了一个简单的信息视图，避免了带有大量繁忙图表的过度拥挤的工作表。

Aspose.Cells 提供了一个 API 用于在电子表格中操作迷你图。

### **Microsoft Excel 中的迷你图**

要在 Microsoft Excel 2010 中插入迷你图：

1. 选择要显示迷你图的单元格。为了便于查看，请选择数据旁边的单元格。
1. 点击**插入**在功能区上，然后选择**柱子**在里面**迷你图**团体。

![待办事项：图像_替代_文本](chart-formatting_13.png)

1. 选择或输入工作表中包含源数据的单元格范围。
图表出现。

例如，迷你图可帮助您查看趋势或垒球联赛的输赢记录。迷你图甚至可以总结联盟中每支球队的整个赛季。

![待办事项：图像_替代_文本](chart-formatting_14.png)

### **使用 Aspose.Cells 的迷你图**

开发人员可以使用 API 提供的 API 创建、删除或读取迷你图（在模板文件中）。通过为给定数据范围添加自定义图形，开发人员可以自由地将不同类型的微型图表添加到选定的单元格区域。

下面的示例演示了迷你图功能。该示例显示了如何：

1. 打开一个简单的模板文件。
1. 阅读工作表的迷你图信息。
1. 将给定数据范围的新迷你图添加到单元格区域。
1. 将 Excel 文件保存到磁盘。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **将 3D 格式应用于图表**

您可能需要 3D 图表样式，以便您可以只获得场景的结果。 Aspose.Cells API 提供相关 API 以应用 Microsoft Excel 2007 3D 格式，如本文中所演示。

### **为图表设置 3D 格式**

下面给出了一个完整的示例来演示如何创建图表和应用 Microsoft Excel 2007 3D 格式。执行上述示例代码后，工作表中将添加一个柱形图（具有 3D 效果），如下所示。

**具有 3D 格式的柱形图**

![待办事项：图像_替代_文本](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

有关支持的 2D 和 3D 图表的完整列表，请参阅[支持的渲染图表类型](/cells/zh/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **推进主题**
- [将图片设置为背景填充图表](/cells/zh/java/set-picture-as-background-fill-in-the-chart/)
