---
title: 使用 Golang 通过 C++ 操作图表中的形状
linktitle: 图表中的形状
description: 学习如何使用 Aspose.Cells for C++ 添加控件和自定义 Microsoft Excel 中的图表。我们的指南将演示如何操作图表元素、调整格式以及提升图表的整体外观与易用性。
keywords: Aspose.Cells for C++，图表控件，图表自定义，Microsoft Excel，图表元素，格式化。
type: docs
weight: 70
url: /zh/go-cpp/controls-in-charts/
---

{{% alert color="primary" %}}

有时需要在图表中插入标签、文本框、图片等绘图对象。Aspose.Cells 可以在运行时向图表中添加控件。

{{% /alert %}}

## **向图表添加标签控件**

标签提供了一种向用户提供有关电子表格内容信息的方式。
Aspose.Cells允许您甚至在图表中添加和操作标签。

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) 类提供了一个名为 [**AddLabelInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlabelinchart/) 的方法，用于向图表添加标签控件。以下是该方法所用参数的列表：

- **top** – 以图表区域的1/4000单位为垂直偏移的标签。
- **left** – 以图表区域的1/4000单位为水平偏移的标签。
- **height** – 标签的高度，以图表区域的1/4000单位为单位。
- **width** – 标签的宽度，单位为图表区域的1/4000。

该方法返回 [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/go-cpp/label/) 对象。[**Label**](https://reference.aspose.com/cells/go-cpp/label/) 类代表图表中的标签。它具有一些重要成员：

- [**Text**](https://reference.aspose.com/cells/go-cpp/shape/gettext/)（属性） – 指定标签的标题字符串。
- [**Fill**](https://reference.aspose.com/cells/go-cpp/shape/getfill/)（属性）– 指定填充颜色属性。

以下示例演示如何向图表添加标签。示例使用了一个设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用此文件向图表插入标签。以下是添加标签到图表的原始代码。执行该代码时生成以下输出。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts.go" >}}
## **将文本框控件添加到图表**

突出报告中的重要信息的一种方法是使用文本框。例如，输入文本以突出显示公司名称或指示销售最高的地区。[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) 类提供了一个名为 [**AddTextBoxInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addtextboxinchart/) 的方法，用于向图表添加文本框控件。以下是该方法所用参数的列表：

- **top** – 文本框与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 文本框距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **height** – 文本框的高度，单位为图表区域的1/4000。
- **width** – 文本框的宽度，单位为图表区域的1/4000。

该方法返回 [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/) 对象。[**TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/) 类代表图表中的文本框。

以下示例显示了如何向图表添加文本框。该示例使用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入文本框以显示图表标题。以下是添加文本框到图表的原始代码。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-1.go" >}}
## **向图表添加图片**

Aspose.Cells 允许您将图像插入到图表中。例如，添加一张图片以强调或赋予图表或其内容更多的含义，或者插入一个品牌图片文件。

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) 类提供了一个名为 [**AddPictureInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpictureinchart/) 的方法，用于向图表添加图片对象。以下是该方法所用参数的列表：

- **top** – 图片与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 图片与图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **stream** - 一个包含图像数据的流对象。
- **widthScale** - 图像宽度的比例值，以百分比表示。
- **heightScale** - 图像高度的比例值，以百分比表示。

该方法返回一个 [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/go-cpp/picture/) 对象。[**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) 类代表图表中的图片对象。

以下示例显示了如何向图表添加图片。该示例利用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入图片。以下是添加图片到图表的原始代码。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-2.go" >}}
## **在图表中添加复选框**

Aspose.Cells 允许您通过使用 [**MsoDrawingType**](https://reference.aspose.com/cells/go-cpp/msodrawingtype/) 枚举向图表工作表中插入复选框。以下示例演示了向图表工作表添加复选框。

以下图像显示了输出文件中带有复选框的图表工作表。

![todo:image_alt_text](controls-in-charts_1.jpg)

以下代码片段生成的[输出文件](101089316.xlsx)已附上，供您参考。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-3.go" >}}
## **高级主题**
- [向图表添加艺术字水印](/cells/zh/cpp/add-wordart-watermark-to-chart/)
