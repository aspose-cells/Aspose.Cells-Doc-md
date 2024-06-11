---
title: 图表格式设置
type: docs
weight: 20
url: /zh/java/chart-formatting/
---

## **设置图表外观**

在[图表类型](/cells/zh/java/chart-types/)中，我们简要介绍了Aspose.Cells提供的各种图表类型和图表对象。

在本文中，我们讨论了如何通过设置多种不同属性来自定义图表的外观：

- [设置图表区域](/cells/zh/java/chart-formatting/#setting-chart-area)。
- [设置图表线条](/cells/zh/java/chart-formatting/#setting-chart-lines)。
- [应用主题](/cells/zh/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts)。
- [设置图表和坐标轴的标题](/cells/zh/java/chart-formatting/#setting-the-titles-of-charts-or-axes)。
- [处理网格线](/cells/zh/java/chart-formatting/#setting-major-gridlines)。
- [为背景和侧面设置边框](/cells/zh/java/chart-formatting/#setting-borders-for-back-and-side-walls)。

### **设置图表区域**

图表中存在不同类型的区域，Aspose.Cells提供了修改每个区域外观的灵活性。开发人员可以通过改变前景色、背景色和填充格式等方式在区域上应用不同的格式设置。

在下面的示例中，我们在图表的不同区域应用了不同的格式设置。这些区域包括：

- 绘图区域
- 图表区域
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 区域
- 单个点的 [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) 区域

执行示例代码后，工作表将添加一个柱形图，如下所示：

**具有填充区域的柱形图** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **设置图表线条**

开发人员还可以在下面的示例中对[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)的线条或数据标记应用不同类型的样式。执行示例代码将在工作表中添加柱形图，如下所示：

**应用线条样式后的柱形图** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **将Microsoft Excel 2007/2010主题应用于图表**

开发人员可以在下面的示例中为[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)或其他图表对象应用不同的Microsoft Excel主题和颜色，如下所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **设置图表或坐标轴的标题**

您可以使用Microsoft Excel在所见即所得的环境中设置图表及其坐标轴的标题，如下所示。

**使用Microsoft Excel设置图表及其坐标轴的标题** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells还允许开发人员在运行时设置图表及其坐标轴的标题。所有图表及其坐标轴都包含一个[**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)方法，可用于设置它们的标题，如下示例所示。执行示例代码后，工作表将添加一个柱形图，如下所示：

**设置标题后的柱形图** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **设置主要网格线**

#### **隐藏主要网格线**

开发人员可以使用[**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)对象的[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible)方法来控制主要网格线的可见性。隐藏主要网格线后，工作表中添加的柱形图将具有以下外观：

**带有隐藏主要网格线的柱形图** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **更改主要网格线设置**

开发人员不仅可以控制主要网格线的可见性，还可以控制其他属性，包括其颜色等。设置主要网格线的颜色后，工作表中添加的柱形图将具有以下外观：

**带有彩色主要网格线的柱形图** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **设置背景和侧壁的边框**

自Microsoft Excel 2007发布以来，3D图表的墙壁分为两部分：侧壁和背壁，因此我们必须使用两个[**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)对象分别表示它们，您可以使用[**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall)和[**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall)访问它们。

下面的示例显示了如何使用不同的属性设置侧壁的边框。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **更改图表位置和大小**

有时，您想要在工作表中改变新图表或现有图表的位置或大小。Aspose.Cells提供**[**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject)**属性来实现这一点。您可以使用其子属性重新调整图表的新**高度**和**宽度**，或者使用新的**X**和**Y**坐标来重新定位它。

### **修改图表的位置和大小**

要更改图表的位置（X、Y坐标）和大小（高度、宽度），请使用以下属性：

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

以下示例解释了上述属性的用法。它加载包含图表的现有工作簿的第一个工作表，然后重新调整大小和重新定位图表，并保存工作簿。

在运行示例代码之前，源文件看起来像这样：

**执行示例代码前的图表大小和位置** 

![todo:image_alt_text](chart-formatting_7.png)

执行后，输出文件如下所示：

**执行示例代码后的图表大小和位置** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **操作设计图表**

有时您可能需要操作或修改设计模板文件中的图表。Aspose.Cells完全支持使用其内容和元素来操作设计图表。数据、图表内容、背景图像和格式可以被准确保存。

### **操作设计模板文件中的设计图表**

要在模板文件中操作设计图表，请使用所有与图表相关的API调用。例如，使用**[**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts)**属性来获取模板文件中的现有图表集合。

#### **创建图表**

以下示例演示了如何创建饼图。稍后我们将操作该图表。代码生成了以下输出。

**输入饼图** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **操作图表**

以下示例展示如何操作现有的图表。在此示例中，我们修改了上面创建的图表。代码生成了以下输出。请注意，图表标题的颜色已从蓝色变为黑色，'England 30000' 已更改为 'United Kingdom, 30K'。

**饼图已被修改** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **在设计师模板中操作折线图**

在这个例子中，我们将操作一个折线图。我们将向现有图表添加一些数据系列，并改变它们的线条颜色。

首先，看看设计师折线图。

**输入折线图** 

![todo:image_alt_text](chart-formatting_11.png)

现在我们使用以下代码操作折线图（包含在 **linechart.xls** 文件中）。代码生成了以下输出。

**操作后的折线图** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **使用迷你图**

Microsoft Excel 2010可以以前所未有的方式分析信息。它允许用户使用新的数据分析和可视化工具跟踪和突出重要的数据趋势。 Sparklines是迷你图，可以放置在单元格内，以便您可以在同一张表格中查看数据和图表。当Sparklines被正确使用时，数据分析更快捷、更简洁。它们还提供信息的简单视图，避免了拥挤的工作表和繁忙的图表。

Aspose.Cells提供了用于操作电子表格中迷你图的API。

### **Microsoft Excel 中的迷你图**

如何在 Microsoft Excel 2010 中插入迷你图：

1. 选择要显示迷你图的单元格。为了方便查看，选择数据旁边的单元格。
1. 在功能区上单击**插入**，然后在**迷你图**组中选择**柱**。

![todo:image_alt_text](chart-formatting_13.png)

1. 选择或输入包含源数据的工作表中的单元格范围。
   图表出现。

Sparklines可帮助您查看趋势，例如，软式联赛的胜利或失败记录。 Sparklines甚至可以总结联赛中每支球队整个赛季的情况。

![todo:image_alt_text](chart-formatting_14.png)

### **使用 Aspose.Cells 创建迷你图**

开发人员可以使用Aspose.Cells提供的API创建、删除或读取电子表格中的迷你图。通过为给定数据范围添加自定义图形，开发人员可以自由地向选定的单元区域添加不同类型的小图。

下面的示例演示了迷你图功能。该示例显示了如何：

1. 打开一个简单的模板文件。
1. 读取工作表的迷你图信息。
1. 为给定的数据范围向单元区域添加新的迷你图。
1. 将Excel文件保存在磁盘中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **应用3D格式到图表**

您可能需要3D图表样式，以便您可以获得与您的情景相符的结果。 Aspose.Cells API提供了相关API，以应用Microsoft Excel 2007 3D格式，正如本文所示。

### **设置图表的3D格式**

下面的完整示例演示了如何创建一个图表并应用Microsoft Excel 2007的3D格式。在执行上述示例代码之后，将向工作表添加一个带有3D效果的柱形图，如下所示。

**使用3D格式设置的柱状图**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

要查看支持的2D和3D图表的完整列表，请参阅[用于呈现的支持的图表类型](/cells/zh/java/chart-rendering/#supported-chart-types-for-rendering)。

{{% /alert %}}

## **高级主题**
- [在图表中将图片设置为背景填充](/cells/zh/java/set-picture-as-background-fill-in-the-chart/)
