---
title: 图表中的控件
linktitle: 图表中的形状
type: docs
weight: 60
url: /zh/java/controls-in-charts/
---

{{% alert color="primary" %}}

有时需要在图表中插入标签、文本框、图片等绘图对象。Aspose.Cells 可以在运行时向图表中添加控件。

{{% /alert %}}

## **向图表添加标签控件**

标签提供了向用户提供关于电子表格内容的信息的方法。Aspose.Cells 允许您甚至在图表中添加和操作标签。

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)类提供了一个名为[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart-int-int-int-int-)的方法，用于向图表添加标签控件。以下是用于该方法的参数列表：

- **top** – 以图表区域的1/4000单位为垂直偏移的标签。
- **left** – 以图表区域的1/4000单位为水平偏移的标签。
- **height** – 标签的高度，以图表区域的1/4000单位为单位。
- **width** – 标签的宽度，以图表区域的1/4000单位为单位。

该方法返回[**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)类的对象，其中[**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)类表示图表中的标签。它具有以下重要成员：

- [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)属性指定标签的标题字符串。
- [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill)属性指定填充颜色属性。

以下示例显示了如何向图表添加标签。该示例使用一个设计文件，其中包含一个图表。我们使用此文件将一个标签插入到图表中。

以下是设计文件的截图。

**设计师图表**

![todo:image_alt_text](controls-in-charts_1.png)

以下是添加标签到图表的原始代码。执行该代码时会生成以下输出。

**图表中添加了一个标签**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **将文本框控件添加到图表**

在报告中突出显示重要信息的一种方法是使用文本框。例如，输入文本以突出显示公司名称或指示销售额最高的地理区域。[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)类提供了一个名为[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart-int-int-int-int-)的方法，用于向图表添加文本框控件。以下是该方法使用的参数列表：

- **top** – 文本框与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 文本框与图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **height** – 文本框的高度，单位为图表区域的1/4000。
- **width** – 文本框的宽度，单位为图表区域的1/4000。

该方法返回一个 [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) 类的对象，其中 [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) 类代表图表中的一个文本框。

以下示例显示了如何向图表添加一个文本框。该示例使用上述包含图表的设计文件。我们使用该文件将一个文本框插入到图表中以显示图表标题。

以下是向图表添加文本框的原始代码。执行该代码时将生成以下输出。

**图表中添加了一个文本框**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **向图表添加图片**

Aspose.Cells 允许您将图像插入到图表中。例如，添加一张图片以强调或赋予图表或其内容更多的含义，或者插入一个品牌图片文件。

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) 类提供了一个名为 [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart-int-int-java.io.InputStream-int-int-) 的方法，用于向图表添加图片对象。以下是该方法使用的参数列表。

- **top** – 图片与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 图片与图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **stream** - 一个包含图像数据的流对象。
- **widthScale** - 图像宽度的比例值，以百分比表示。
- **heightScale** - 图像高度的比例值，以百分比表示。

该方法返回一个[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)类的对象，其中[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)类表示图表中的图片对象。

以下示例显示如何向图表中添加图片。该示例利用之前包含图表的设计文件。我们使用该文件向图表中插入一幅图像。

以下是向图表中添加图片的原始代码。执行该代码后生成以下输出。

**图片已插入到图表中**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **在图表中添加复选框**

Aspose.Cells允许您通过使用[**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType)枚举向图表工作表插入复选框。以下示例演示如何向图表工作表添加复选框。

以下图像显示了输出文件中带有复选框的图表工作表。

![todo:image_alt_text](controls-in-charts_5.jpg)

附上以下代码片段生成的[输出文件](InsertCheckboxInChartSheet_out.xlsx)供您参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
{{< app/cells/assistant language="java" >}}
