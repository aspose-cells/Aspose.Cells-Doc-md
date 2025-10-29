---
title: 图表中的形状
description: 学习如何使用 Aspose.Cells for .NET 来添加控件并自定义 Microsoft Excel 中的图表。我们的指南将演示如何操纵图表元素，调整格式和增强图表的整体外观和可用性。
keywords: Aspose.Cells for .NET，图表控件，图表自定义，Microsoft Excel，图表元素，格式。
type: docs
weight: 70
url: /zh/net/controls-in-charts/
---

{{% alert color="primary" %}}

有时需要在图表中插入标签、文本框、图片等绘图对象。Aspose.Cells 可以在运行时向图表中添加控件。

{{% /alert %}}

## **向图表添加标签控件**

标签提供了一种向用户提供有关电子表格内容信息的方式。
Aspose.Cells允许您甚至在图表中添加和操作标签。

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart)的方法，用于向图表添加标签控件。以下是该方法使用的参数列表：

- **top** – 以图表区域的1/4000单位为垂直偏移的标签。
- **left** – 以图表区域的1/4000单位为水平偏移的标签。
- **height** – 标签的高度，以图表区域的1/4000单位为单位。
- **width** – 标签的宽度，单位为图表区域的1/4000。

该方法返回[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)对象。[**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)类代表图表中的标签，具有一些重要成员：

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)（属性）– 指定标签的标题字符串。
- [**Fill**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill)（属性）– 指定填充颜色属性。

以下示例演示如何向图表添加标签。示例使用了一个设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用此文件向图表插入标签。以下是添加标签到图表的原始代码。执行该代码时生成以下输出。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

**注意：** 此类型的标签控件仅支持在XLS文件中。如果你想在XLSX文件中实现类似效果，请使用以下替代方案：

1. 使用TextBox控件，XLSX文件中有类似的标签控件替代方案。
- [**Example**](https://docs.aspose.com/cells/net/controls-in-charts/#adding-textbox-control-to-the-chart) 用于TextBox，XLSX文件支持。

2. 添加一个工作表，类型为"SheetType.Chart"，然后在该工作表上添加图表和控件。
- [**Example**](https://docs.aspose.com/cells/net/controls-in-charts/#adding-checkbox-in-the-chart) 用于添加SheetType.Chart。

## **将文本框控件添加到图表**

在报告中突出显示重要信息的一种方法是使用文本框。例如，输入文本以突出显示公司名称或指示销售额最高的地理区域。[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)类提供了一个名为[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)的方法，用于向图表添加文本框控件。以下是该方法使用的参数列表：

- **top** – 文本框与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 文本框距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **height** – 文本框的高度，单位为图表区域的1/4000。
- **width** – 文本框的宽度，单位为图表区域的1/4000。

该方法返回一个 [**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) 对象。[**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) 类表示图表中的文本框。

以下示例显示了如何向图表添加文本框。该示例使用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入文本框以显示图表标题。以下是添加文本框到图表的原始代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **向图表添加图片**

Aspose.Cells 允许您将图像插入到图表中。例如，添加一张图片以强调或赋予图表或其内容更多的含义，或者插入一个品牌图片文件。

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) 类提供了一个名为 [**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart) 的方法，用于向图表添加图片对象。以下是该方法使用的参数列表。

- **top** – 图片与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 图片与图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **stream** - 一个包含图像数据的流对象。
- **widthScale** - 图像宽度的比例值，以百分比表示。
- **heightScale** - 图像高度的比例值，以百分比表示。

该方法返回一个 [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) 对象。[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) 类表示图表中的图片对象。

以下示例显示了如何向图表添加图片。该示例利用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入图片。以下是添加图片到图表的原始代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **在图表中添加复选框**

Aspose.Cells 允许您通过使用 [**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) 枚举向图表工作表中插入复选框。以下示例演示了向图表工作表添加复选框。

以下图像显示了输出文件中带有复选框的图表工作表。

![todo:image_alt_text](controls-in-charts_1.jpg)

以下代码片段生成的[输出文件](101089316.xlsx)已附上，供您参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **高级主题**
- [向图表添加艺术字水印](/cells/zh/net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="csharp" >}}
