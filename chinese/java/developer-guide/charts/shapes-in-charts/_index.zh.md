---
title: 图表中的控件
linktitle: 图表中的形状
type: docs
weight: 60
url: /zh/java/controls-in-charts/
---
{{% alert color="primary" %}}

有时您需要将标签、文本框、图片等绘图对象插入到图表中。 Aspose.Cells 可以在运行时将控件添加到图表中。

{{% /alert %}}

## **向图表添加标签控件**

标签提供了一种向用户提供有关电子表格内容的信息的方法。 Aspose.Cells 允许您甚至在图表中添加和操作标签。

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)类提供了一个名为[**在图表中添加标签**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), 用于向图表添加标签控件。下面是用于该方法的参数列表：

- **最佳**– 标签距左上角的垂直偏移量，以图表区域的 1/4000 为单位。
- **剩下**– 标签距左上角的垂直偏移量，以图表区域的 1/4000 为单位。
- **高度**– 标签的高度，以图表区域的 1/4000 为单位。
- **宽度** – 标签的宽度，以图表区域的 1/4000 为单位。

该方法返回一个对象[**标签**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)类，其中[**标签**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)类代表图表中的标签。它有一些重要的成员，详述如下：

- [**文本**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)属性指定标签的标题字符串。
- [**充满**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill)属性指定填充颜色属性。

以下示例显示如何向图表添加标签。该示例使用其中包含图表的设计器文件。我们使用此文件将标签插入图表中。

下面是设计器文件的屏幕截图。

**设计师图表**

![待办事项：图片_替代_文本](controls-in-charts_1.png)

下面是向图表添加标签的原始代码。执行代码时会生成以下输出。

**图表中添加了标签**

![待办事项：图片_替代_文本](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **将文本框控件添加到图表**

在报告中突出显示重要信息的一种方法是使用文本框。例如，输入文本以突出显示公司名称或指示销售额最高的地理区域。这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)类提供了一个名为[**添加文本框图表**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int))，用于向图表添加文本框控件。以下是该方法使用的参数列表：

- **最佳** – 文本框距左上角的垂直偏移量，以图表区域的 1/4000 为单位。
- **剩下** – 文本框距左上角的垂直偏移量，以图表区域的 1/4000 为单位。
- **高度**– 文本框的高度，以图表区域的 1/4000 为单位。
- **宽度** – 文本框的宽度，以图表区域的 1/4000 为单位。

该方法返回一个对象[**文本框**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)上课的地方[**文本框**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)类表示图表中的文本框。

以下示例显示如何向图表添加文本框。该示例使用以前的设计器文件，其中包含一个图表。我们使用此文件在图表中插入一个文本框以显示图表标题。

下面是向图表添加文本框的原始代码。执行代码时会生成以下输出。

**图表中添加了一个文本框**

![待办事项：图片_替代_文本](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **添加图片到图表**

Aspose.Cells 允许您将图像插入图表。例如，添加图片以强调或赋予图表或其内容更多含义，或插入品牌图像文件。

这[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)类提供了一个名为[**添加画中画**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), 用于向图表添加图片对象。以下是该方法使用的参数列表：

- **最佳**– 图片距左上角的垂直偏移量，以图表区域的 1/4000 为单位。
- **剩下**– 图片距左上角的垂直偏移量，以图表区域的 1/4000 为单位。
- **溪流**– 包含图像数据的流对象。
- **宽度比例**– 图像宽度的比例，一个百分比值。
- **高度比例**– 图像高度的比例，一个百分比值。

该方法返回一个对象[**图片**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)上课的地方[**图片**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)类代表图表中的图片对象。

下面的示例演示如何将图片添加到图表中。该示例使用以前的设计器文件，其中包含一个图表。我们使用此文件将图像插入图表中。

下面是向图表添加图片的原始代码。执行代码时产生如下输出

**图表中插入了一张图片**

![待办事项：图片_替代_文本](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **在图表中添加复选框**

Aspose.Cells 允许您使用[**Mso绘图类型**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType)枚举。以下示例演示了向图表工作表添加复选框。

下图显示了输出文件中带有复选框的图表工作表。

![待办事项：图片_替代_文本](controls-in-charts_5.jpg)

这[输出文件](InsertCheckboxInChartSheet_out.xlsx)附上由以下代码片段生成的代码供您参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
