---
title: 图表中的控件
linktitle: 图表中的形状
type: docs
weight: 60
url: /zh/java/controls-in-charts/
---

{{% alert color="primary" %}}

有时您需要在图表中插入标签、文本框、图片等绘图对象。Aspose.Cells可以在运行时向图表添加控件。

{{% /alert %}}

## **向图表添加标签控件**

标签提供一种向用户提供关于电子表格内容的信息的方法。Aspose.Cells允许您添加并操作标签，即使是图表中的标签。

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)类提供一个名为[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)的方法，用于向图表中添加标签控件。以下是该方法使用的参数列表：

- **top** - 标签距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** - 标签距离图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **height** - 标签的高度，单位为图表区域的1/4000。
- **宽度** - 标签的宽度，以图表区域的1/4000单位表示。

该方法返回[**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)类的对象，其中[**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)类表示图表中的标签。下面详细介绍了一些重要成员：

- [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)属性指定标签的标题字符串。
- [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill)属性指定填充颜色属性。

以下示例显示如何向图表添加标签。该示例使用一个设计文件，其中包含一个图表。我们使用该文件向图表中插入一个标签。

下面是设计文件的屏幕截图。

**设计图表**

![todo:image_alt_text](controls-in-charts_1.png)

以下是向图表添加标签的原始代码。执行代码会生成以下输出。

**图表中添加了一个标签**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **向图表添加文本框控件**

在报表中突出显示重要信息的一种方式是使用文本框。例如，输入文本以突出显示公司名称或指示具有最高销售额的地理区域。[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)类提供一个名为[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)的方法，用于向图表添加文本框控件。以下是该方法使用的参数列表：

- **top** - 文本框距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **左侧** - 文本框距图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **height** – 文本框的高度，单位为图表区域的1/4000。
- **width** – 文本框的宽度，单位为图表区域的1/4000。

该方法返回[**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)类的对象，其中[**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)类表示图表中的文本框。

以下示例显示如何向图表添加文本框。该示例使用之前具有图表的设计文件。我们使用该文件将文本框插入到图表中以显示图表标题。

以下是向图表添加文本框的原始代码。执行代码会生成以下输出。

**图表中添加了一个文本框**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **向图表添加图片**

Aspose.Cells允许您在图表中插入图片。例如，可以添加图片来强调或赋予图表或其内容更多含义，或者插入品牌图片文件。

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)类提供一个名为[**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)的方法，用于向图表添加图片对象。以下是该方法使用的参数列表：

- **top** – 图片距离图表区域左上角的垂直偏移量，单位为图表区域的1/400。
- **left** – 图片距离图表区域左上角的水平偏移量，单位为图表区域的1/400。
- **stream** – 包含图像数据的流对象。
- **widthScale** – 图像宽度的比例尺，百分比值。
- **heightScale** – 图像高度的比例尺，百分比值。

该方法返回一个 [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) 类的对象，在这里 [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) 类表示图表中的图片对象。

下面的示例展示了如何向图表添加图片。示例利用了先前的设计器文件，其中包含了一个图表。我们使用这个文件将一张图片插入到图表中。

以下是添加图片到图表的原始代码。执行代码时生成以下输出。

**在图表中插入了一张图片**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **向图表中添加复选框**

Aspose.Cells允许您通过使用 [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) 枚举在图表工作表中插入复选框。以下示例演示了向图表工作表添加复选框。

以下图像显示了带有复选框的图表工作表的输出文件。

![todo:image_alt_text](controls-in-charts_5.jpg)

以下代码片段生成的 [输出文件](InsertCheckboxInChartSheet_out.xlsx) 附在此供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
