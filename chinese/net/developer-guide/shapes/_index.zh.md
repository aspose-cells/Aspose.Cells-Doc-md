---
title: 插入 Excel 文件的图片和形状
linktitle: 形状
type: docs
weight: 140
url: /zh/net/insert-shapes/
description: 管理 Excel 文件中的图片、oleobject、形状。
---

{{% alert color="primary" %}}

有时您需要在工作表中插入一些必要的形状。您可能需要将相同形状插入工作表的不同位置。或者您需要批量插入工作表中的形状。

不要担心！[Aspose.Cells](https://products.aspose.com/cells/) 支持所有这些操作。

{{% /alert %}}

Excel 中的形状主要分为以下类型：
- **图片**
- **OleObjects**
- **直线**
- **矩形**
- **基本形状**
- **块状箭头**
- **等式形状**
- **流程图**
- **星星和旗帜**
- **标记**

本指南文档将从每种类型中选择一个或两个形状来制作样本。通过这些示例，您将学会如何使用[Aspose.Cells](https://products.aspose.com/cells/)将指定的形状插入工作表中。

## **在C#中为Excel工作表添加图片**

在电子表格中添加图片非常简单。只需要几行代码：
只需调用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)对象中封装的[**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)集合的[**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)方法。[**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)方法接受以下参数：

- **左上角行索引**，左上角行的索引。
- **左上角列索引**，左上角列的索引。
- **图片文件名**，包含路径的图片文件名。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **在C#中将OLE对象插入Excel工作表**

Aspose.Cells支持在工作表中添加、提取和操作OLE对象。因此，Aspose.Cells具有[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)类，用于向集合列表添加新的OLE对象。另一个类[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)代表一个OLE对象。它有一些重要成员：

- [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)属性指定字节数组类型的图像(图标)数据。图像将显示在工作表中以显示OLE对象。
- [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)属性指定字节数组形式的对象数据。当您双击OLE对象图标时，将在其相关程序中显示此数据。

以下示例显示如何将OLE对象插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **在C#中向Excel工作表插入线**

线的形状属于**线条**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入线条的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后，从“最近使用的形状”或“线条”中选择线条

![](line.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入线条。

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

该方法返回一个[LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入线条。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

执行上述代码，您将获得以下结果：

![](line2.png)



## **在C#中向Excel工作表插入一条线箭头**

线箭头的形状属于**线条**类别。它是线条的一个特例。

***在Microsoft Excel（例如2007）中：***

- 选择要插入线箭头的单元格
- 单击“插入”菜单，然后单击“形状”
- 接着，从“最近使用的形状”或“线条”中选择线箭头

![](line_arrow1.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入线箭头。

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn,	int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

该方法返回一个[LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入线箭头。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

执行上述代码，您将获得以下结果：

![](line_arrow2.png)



## **在C#中向Excel工作表插入一个矩形**

矩形的形状属于**矩形**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入矩形的单元格
- 单击“插入”菜单，然后单击“形状”
- 接着，从“最近使用的形状”或“矩形”中选择矩形。

![](rectangle.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入一个矩形。

{{% alert color="primary" %}}

[**public RectangleShape AddRectangle(int upperLeftRow,	int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

该方法返回一个[RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)对象。

{{% /alert %}}

以下示例显示如何向工作表插入矩形。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

执行上述代码，您将获得以下结果：

![](rectangle2.png)



## **在C#中向Excel工作表插入立方体**

立方体的形状属于**基本形状**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入立方体的单元格
- 单击“插入”菜单，然后单击“形状”
- 接着，从**基本形状**中选择立方体

![](cube.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入一个立方体。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)对象。

{{% /alert %}}

以下示例展示了如何将立方体插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

执行上述代码，您将获得以下结果：

!\[](cube2.png)



## **在C#中将一个标注四向箭头插入Excel工作表**

标注四向箭头的形状属于**块箭头**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入标注四向箭头的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后，从**块箭头**中选择标注四向箭头

!\[](callout_quad_arrow.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入一个标注四向箭头。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)对象。

{{% /alert %}}

以下示例展示了如何将标注四向箭头插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

执行上述代码，您将获得以下结果：

![](callout_quad_arrow2.png)



## **在C#中向Excel工作表插入乘法符号**

乘法符号的形状属于**方程形状**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入乘法符号的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后从**方程形状**中选择乘法符号

![](multiplication_sign.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入乘法符号。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)对象。

{{% /alert %}}

以下示例显示如何将乘法符号插入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

执行上述代码，您将获得以下结果：

![](multiplication_sign2.png)



## **在C#中向Excel工作表插入多文档**

多文档的形状属于**流程图**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入多文档的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后从**流程图**中选择多文档

![](multidocument.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入一个多文档。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)对象。

{{% /alert %}}

下面的示例显示如何向工作表插入多文档。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

执行上述代码，您将获得以下结果：

![](multidocument2.png)



## **在 C# 中向 Excel 工作表插入五角星**

五角星形状属于**星形和横幅**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入五角星的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后，在**星形和横幅**中选择五角星

![](star_5_points.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入五角星。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入五角星。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

执行上述代码，您将获得以下结果：

![](star_5_points2.png)



## **在C#中向Excel工作表插入一个思维气泡云**

思维气泡云的形状属于**标注**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入思维气泡云的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后从**标注**中选择思维气泡云

![](thought_bubble_cloud.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入思维气泡云。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

该方法返回一个[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入思维气泡云。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

执行上述代码，您将获得以下结果：

![](thought_bubble_cloud2.png)

## **高级主题**
- [更改形状的调整值](/cells/zh/net/change-adjustment-values-of-the-shape/)
- [在工作表之间复制形状](/cells/zh/net/copy-shapes-between-worksheets/)
- [非原始形状中的数据](/cells/zh/net/data-in-non-primitive-shape/)
- [在工作表内部查找形状的绝对位置](/cells/zh/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [从形状获取连接点](/cells/zh/net/get-connection-points-from-shape/)
- [管理控件](/cells/zh/net/managing-controls/)
- [将图标添加到工作表](/cells/zh/net/insert-svg-to-excel/)
- [管理OLE对象](/cells/zh/net/managing-ole-objects/)
- [管理图片](/cells/zh/net/managing-pictures/)
- [管理智能图形](/cells/zh/net/managing-smartart/)
- [管理文本框](/cells/zh/net/managing-textbox-of-excel/)
- [在工作表添加艺术字水印](/cells/zh/net/add-wordart-watermark-to-worksheet/)
- [刷新链接形状的值](/cells/zh/net/refresh-values-of-linked-shapes/)
- [将形状发送到工作表内的前面或后面](/cells/zh/net/send-shape-front-or-back-inside-the-worksheet/)
- [管理形状选项](/cells/zh/net/managing-shape-options/)
- [管理形状文本选项](/cells/zh/net/managing-shape-text-options/)
- [Web扩展 - Office加载项](/cells/zh/net/web-extensions-office-add-ins/)

