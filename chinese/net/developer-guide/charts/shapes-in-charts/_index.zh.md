---
title: 图表中的形状
description: 了解如何使用Aspose.Cells for .NET在Microsoft Excel中添加控件和自定义图表。我们的指南将演示如何操控图表元素，调整格式和增强图表的整体外观和可用性。
keywords: Aspose.Cells for .NET，图表控件，图表自定义，Microsoft Excel，图表元素，格式化。
type: docs
weight: 70
url: /zh/net/controls-in-charts/
---

{{% alert color="primary" %}}

有时您需要在图表中插入标签、文本框、图片等绘图对象。Aspose.Cells可以在运行时向图表添加控件。

{{% /alert %}}

## **向图表添加标签控件**

标签为用户提供关于电子表格内容的信息。
Aspose.Cells允许您即使在图表中也添加和操控标签。

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart)的方法，用于向图表添加一个标签控件。以下是该方法使用的参数列表:

- **top** - 标签距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** - 标签距离图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **height** - 标签的高度，单位为图表区域的1/4000。
- **width** - 标签的宽度，单位为图表区域的1/4000。

该方法返回[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)对象。[**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)类代表图表中的一个标签。它有一些重要成员:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)（属性）- 指定标签的标题字符串。
- [**Fill**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill)（属性）- 指定填充颜色属性。

以下示例显示如何向图表中添加一个标签。该示例使用一个设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用此文件向图表中插入一个标签。以下是添加标签到图表的原始代码。执行代码后生成以下输出。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **向图表添加文本框控件**

在报告中突出显示重要信息的一种方法是使用文本框。例如，输入文本以突出公司名称或指示销售额最高的地理区域。[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)的方法，用于向图表添加文本框控件。以下是该方法使用的参数列表:

- **top** - 文本框距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** - 文本框距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **height** – 文本框的高度，单位为图表区域的1/4000。
- **width** – 文本框的宽度，单位为图表区域的1/4000。

该方法返回 [**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) 对象。 [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) 类表示图表中的文本框。

以下示例显示如何向图表添加文本框。该示例使用先前的设计器文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件将一个文本框插入到图表中以显示图表标题。以下是用于向图表添加文本框的原始代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **向图表添加图片**

Aspose.Cells允许您在图表中插入图片。例如，可以添加图片来强调或赋予图表或其内容更多含义，或者插入品牌图片文件。

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart) 的方法，用于向图表添加图片对象。以下是该方法所用的参数列表。

- **top** – 图片距离图表区域左上角的垂直偏移量，单位为图表区域的1/400。
- **left** – 图片距离图表区域左上角的水平偏移量，单位为图表区域的1/400。
- **stream** – 包含图像数据的流对象。
- **widthScale** – 图像宽度的比例尺，百分比值。
- **heightScale** – 图像高度的比例尺，百分比值。

该方法返回一个 [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) 对象。 [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) 类表示图表中的图片对象。

以下示例显示如何向图表中添加图片。该示例利用先前的设计器文件（**exp_piechart.xls**），该文件中包含一个图表。我们使用该文件向图表中插入图像。以下是用于向图表添加图片的原始代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **向图表中添加复选框**

Aspose.Cells允许您使用 [**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) 枚举将复选框插入到图表工作表中。以下示例演示了向图表工作表添加复选框。

以下图像显示了带有复选框的图表工作表的输出文件。

![todo:image_alt_text](controls-in-charts_1.jpg)

生成的[输出文件](101089316.xlsx)作为以下代码片段的附件供您参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **高级主题**
- [向图表添加文字水印](/cells/zh/net/add-wordart-watermark-to-chart/)
