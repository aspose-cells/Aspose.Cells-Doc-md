---
title: 图表中的形状
description: 学习如何使用 Aspose.Cells for Python via .NET 添加控件和自定义 Microsoft Excel 图表。我们的指南将演示如何操作图表元素、调整格式，以及提升图表的整体外观和易用性。
keywords: Aspose.Cells for Python via .NET，图表控件，图表定制，Microsoft Excel，图表元素，格式设置。
type: docs
weight: 70
url: /zh/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

有时你需要在图表中插入绘图对象，例如标签、文本框、图片等。Aspose.Cells for Python via .NET 可以在运行时向图表添加控件。

{{% /alert %}}

## **向图表添加标签控件**

标签提供了一种向用户提供有关电子表格内容信息的方式。
Aspose.Cells for Python via .NET 允许你向图表中添加和操作标签。

[**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)类提供了一个名为[**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart)的方法，用于向图表添加标签控件。以下是该方法使用的参数列表：

- **top** – 以图表区域的1/4000单位为垂直偏移的标签。
- **left** – 以图表区域的1/4000单位为水平偏移的标签。
- **height** – 标签的高度，以图表区域的1/4000单位为单位。
- **width** – 标签的宽度，单位为图表区域的1/4000。

该方法返回[**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label)对象。[**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label)类代表图表中的标签，具有一些重要成员：

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)（属性）– 指定标签的标题字符串。
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill)（属性）– 指定填充颜色属性。

以下示例演示如何向图表添加标签。示例使用了一个设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用此文件向图表插入标签。以下是添加标签到图表的原始代码。执行该代码时生成以下输出。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **将文本框控件添加到图表**

在报告中突出显示重要信息的一种方法是使用文本框。例如，输入文本以突出显示公司名称或指示销售额最高的地理区域。[**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)类提供了一个名为[**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart)的方法，用于向图表添加文本框控件。以下是该方法使用的参数列表：

- **top** – 文本框与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 文本框距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **height** – 文本框的高度，单位为图表区域的1/4000。
- **width** – 文本框的宽度，单位为图表区域的1/4000。

该方法返回一个 [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) 对象。[**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) 类表示图表中的文本框。

以下示例显示了如何向图表添加文本框。该示例使用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入文本框以显示图表标题。以下是添加文本框到图表的原始代码。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **向图表添加图片**

Aspose.Cells for Python via .NET 允许你在图表中插入图片。例如，添加图片以强调或赋予图表内容更多意义，或插入品牌图像文件。

[**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart) 的方法，用于向图表添加图片对象。以下是该方法使用的参数列表。

- **top** – 图片与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 图片与图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **stream** - 一个包含图像数据的流对象。
- **widthScale** - 图像宽度的比例值，以百分比表示。
- **heightScale** - 图像高度的比例值，以百分比表示。

该方法返回一个 [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) 对象。[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) 类表示图表中的图片对象。

以下示例显示了如何向图表添加图片。该示例利用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入图片。以下是添加图片到图表的原始代码。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **在图表中添加复选框**

Aspose.Cells for Python via .NET 允许你通过 [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype) 枚举在图表工作表中插入复选框。以下示例演示如何为图表工作表添加复选框。

以下图像显示了输出文件中带有复选框的图表工作表。

![todo:image_alt_text](controls-in-charts_1.jpg)

以下代码片段生成的[输出文件](101089316.xlsx)已附上，供您参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **高级主题**
- [向图表添加艺术字水印](/cells/zh/python-net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="python-net" >}}
