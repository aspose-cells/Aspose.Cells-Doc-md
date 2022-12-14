---
title: 插入 Excel 文件的图片和形状。
linktitle: 形状
type: docs
weight: 140
url: /zh/net/insert-shapes/
description: 将图片、oleobject、形状管理到 Excel 文件中。
---
{{% alert color="primary" %}}

有时您需要在工作表中插入一些必要的形状。您可能需要在工作表的不同位置插入相同的形状。或者您需要在工作表中批量插入形状。

不用担心！[Aspose.Cells](https://products.aspose.com/cells/)支持所有这些操作。

{{% /alert %}}

excel中的形状主要分为以下几种：
- **图片**
- **对象**
- **线条**
- **矩形**
- **基本形状**
- **块箭头**
- **方程形状**
- **流程图**
- **星星和横幅**
- **标注**

本指南文档将从每种类型中选择一个或两个形状来制作示例。通过这些示例，您将学习如何使用[Aspose.Cells](https://products.aspose.com/cells/)将指定的形状插入到工作表中。

## **Excel工作表中添加图片C#**

将图片添加到电子表格非常容易。它只需要几行代码：
只需调用[**添加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)的方法[**图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)集合（封装在[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)目的）。这[**添加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)方法采用以下参数：

- **左上行索引**左上行的索引。
- **左上列索引**左上列的索引。
- **图像文件名**，图像文件的名称，完整的路径。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **在 C# 中将 OLE 对象插入 Excel 工作表**

Aspose.Cells 支持在工作表中添加、提取和操作 OLE 对象。因此，Aspose.Cells 具有[**OleObject集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)类，用于将新的 OLE 对象添加到集合列表中。另一个班级，[**对象**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)代表一个 OLE 对象。它有一些重要的成员：

- 这[**图像数据**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)属性指定字节数组类型的图像（图标）数据。将显示图像以显示工作表中的 OLE 对象。
- 这[**对象数据**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)属性以字节数组的形式指定对象数据。当您双击 OLE 对象图标时，该数据将显示在其相关程序中。

以下示例显示如何将 OLE 对象添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **在 C# 中向 Excel 工作表插入一行**

线条的形状属于**线条**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入行的单元格
- 单击插入菜单，然后单击形状。
- 然后，从“最近使用的形状”或“线条”中选择线条

![](line.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入一行。

{{% alert color="primary" %}}

[公共线形添加线（
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

该方法返回一个[线型](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)目的。

{{% /alert %}}

以下示例显示如何向工作表插入行。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

执行上面的代码，你会得到如下结果：

![](line2.png)



## **在 C# 中向 Excel 工作表插入直线箭头**

线箭头的形状属于**线条**category.It 是 line 的特例。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入直线箭头的单元格
- 单击插入菜单，然后单击形状。
- 然后，从“最近使用的形状”或“线条”中选择线条箭头

![](line_arrow1.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入线箭头。

{{% alert color="primary" %}}

[公共线形添加线（
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

该方法返回一个[线型](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)目的。

{{% /alert %}}

以下示例显示如何将线箭头插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

执行上面的代码，你会得到如下结果：

![](line_arrow2.png)



## **在 C# 中将矩形插入 Excel 工作表**

矩形的形状属于**矩形**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入矩形的单元格
- 单击插入菜单，然后单击形状。
- 然后，从“最近使用的形状”或“矩形”中选择矩形

![](rectangle.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入一个矩形。

{{% alert color="primary" %}}

[公共矩形形状添加矩形（
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

该方法返回一个[长方形](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)目的。

{{% /alert %}}

以下示例显示如何将矩形插入到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

执行上面的代码，你会得到如下结果：

![](rectangle2.png)



## **在 C# 中将立方体插入 Excel 工作表**

立方体的形状属于**基本形状**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入立方体的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择多维数据集**基本形状**

![](cube.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入一个立方体。

{{% alert color="primary" %}}

[公共形状 AddAutoShape(
自选图形类型，
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[形状](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)目的。

{{% /alert %}}

以下示例显示如何将多维数据集插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

执行上面的代码，你会得到如下结果：

![](cube2.png)



## **在 C# 中将标注四箭头插入 Excel 工作表**

标注四箭头的形状属于**块箭头**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入标注四箭头的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择标注四箭头**块箭头**

![](callout_quad_arrow.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入标注四箭头。

{{% alert color="primary" %}}

[公共形状 AddAutoShape(
自选图形类型，
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[形状](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)目的。

{{% /alert %}}

以下示例显示如何将标注四箭头插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

执行上面的代码，你会得到如下结果：

![](callout_quad_arrow2.png)



## **在 C# 中向 Excel 工作表插入乘号**

乘号的形状属于**方程形状**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入乘号的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择乘号**方程形状**

![](multiplication_sign.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入乘号。

{{% alert color="primary" %}}

[公共形状 AddAutoShape(
自选图形类型，
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[形状](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)目的。

{{% /alert %}}

以下示例显示如何将乘号插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

执行上面的代码，你会得到如下结果：

![](multiplication_sign2.png)



## **在 C# 中将多文档插入 Excel 工作表**

多文档的形状属于**流程图**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入多文档的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择多文档**流程图**

![](multidocument.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入多文档。

{{% alert color="primary" %}}

[公共形状 AddAutoShape(
自选图形类型，
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[形状](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)目的。

{{% /alert %}}

以下示例显示如何将多文档插入到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

执行上面的代码，你会得到如下结果：

![](multidocument2.png)



## **在 C# 中向 Excel 工作表插入五角星**

五角星的形状属于**星星和横幅**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入五角星的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择五角星**星星和横幅**

![](star_5_points.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入一个五角星。

{{% alert color="primary" %}}

[公共形状 AddAutoShape(
自选图形类型，
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[形状](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)目的。

{{% /alert %}}

以下示例显示如何将五角星插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

执行上面的代码，你会得到如下结果：

![](star_5_points2.png)



## **在 C# 中将思想气泡云插入 Excel 工作表**

思想气泡云的形状属于**标注**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入思想气泡云的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择思想气泡云**标注**

![](thought_bubble_cloud.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入思想泡泡云。

{{% alert color="primary" %}}

[公共形状 AddAutoShape(
自选图形类型，
 int upperLeftRow,
国际顶级，
 int upperLeftColumn,
剩下的，
整数高度，
整数宽度
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[形状](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)目的。

{{% /alert %}}

以下示例显示如何将思想泡泡云插入到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

执行上面的代码，你会得到如下结果：

![](thought_bubble_cloud2.png)

## **推进主题**
- [更改形状的调整值](/cells/zh/net/change-adjustment-values-of-the-shape/)
- [在工作表之间复制形状](/cells/zh/net/copy-shapes-between-worksheets/)
- [非原始形状的数据](/cells/zh/net/data-in-non-primitive-shape/)
- [在工作表中查找形状的绝对位置](/cells/zh/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [从形状中获取连接点](/cells/zh/net/get-connection-points-from-shape/)
- [管理控制](/cells/zh/net/managing-controls/)
- [将图标添加到工作表](/cells/zh/net/insert-svg-to-excel/)
- [管理 OLE 对象](/cells/zh/net/managing-ole-objects/)
- [管理图片](/cells/zh/net/managing-pictures/)
- [管理智能艺术](/cells/zh/net/managing-smartart/)
- [管理文本框](/cells/zh/net/managing-textbox-of-excel/)
- [将艺术字水印添加到工作表](/cells/zh/net/add-wordart-watermark-to-worksheet/)
- [刷新链接形状的值](/cells/zh/net/refresh-values-of-linked-shapes/)
- [在工作表内发送形状前面或后面](/cells/zh/net/send-shape-front-or-back-inside-the-worksheet/)
- [管理形状选项](/cells/zh/net/managing-shape-options/)
- [管理形状文本选项](/cells/zh/net/managing-shape-text-options/)
- [Web 扩展 - Office 加载项](/cells/zh/net/web-extensions-office-add-ins/)

