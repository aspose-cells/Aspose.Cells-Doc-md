---
title: 插入Excel文件的图片和形状。
linktitle: 形状
type: docs
weight: 140
url: /zh/python-net/insert-shapes/
description: 将图片、OLE对象、形状管理到Excel文件中。
---

{{% alert color="primary" %}}

有时候，您需要在工作表中插入一些必要的形状。您可能需要在工作表的不同位置插入相同的形状。或者您需要批量在工作表中插入形状。

不用担心！[Aspose.Cells](https://products.aspose.com/cells/)支持所有这些操作。

{{% /alert %}}

Excel中的形状主要分为以下类型:
- **图片**
- **Ole对象**
- **线条**
- **矩形**
- **基本形状**
- **方块箭头**
- **方程式形状**
- **流程图**
- **星星和横幅**
- **标注**

这份指南将从每个类型中选择一个或两个形状来制作示例。通过这些示例，您将学习如何使用[Aspose.Cells](https://products.aspose.com/cells/)将指定的形状插入工作表中。

## **在C#中在Excel工作表中添加图片**

向电子表格中添加图片非常简单。只需几行代码：
只需调用[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)中封装的[**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)集合的[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)方法。[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) 方法接受以下参数：

- **upper_left_row**，左上角行的索引。
- **upper_left_column**，左上角列的索引。
- **file_name**，图像文件的名称，含路径。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-Pictures-AddingPictures-1.py" >}}


## **在C#中向Excel工作表插入OLE对象**

Aspose.Cells for Python via .NET 支持在工作表中添加、提取和操作OLE对象。因此，Aspose.Cells for Python via .NET 具有 [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection) 类，用于向集合列表添加新的OLE对象。另一类 [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject)，代表OLE对象。它有一些重要成员：

- [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data)属性指定图像（图标）数据为字节数组类型。将显示该图像以显示工作表中的OLE对象。
- [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data)属性指定对象数据的字节数组形式。当您双击OLE对象图标时，将在其关联的程序中显示此数据。

下面的示例演示了如何将一个或多个OLE对象添加到工作表中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-OLE-InsertingOLEObjects-1.py" >}}

## **在C#中向Excel工作表插入线条**

线形状属于**线条**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入线条的单元格
- 点击“插入”菜单，然后点击“形状”
- 接着，从“最近使用的形状”或“线条”中选择线条

![](line.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入线条。

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

该方法返回一个 [LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) 对象。

{{% /alert %}}

下面的示例显示如何将线条插入工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Line.py" >}}

执行上述代码，您将获得以下结果：

![](line2.png)



## **在C#中向Excel工作表插入线箭头**

箭头线的形状属于**线**类别。它是线的特殊情况。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入箭头线的单元格
- 点击“插入”菜单，然后点击“形状”
- 接着，从“最近使用的形状”或“线”中选择箭头线

![](line_arrow1.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入箭头线。

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

该方法返回一个 [LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) 对象。

{{% /alert %}}

以下示例显示了如何向工作表插入箭头线。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-LineArrow.py" >}}

执行上述代码，您将获得以下结果：

![](line_arrow2.png)



## **在 C# 中向 Excel 工作表插入矩形**

矩形的形状属于**矩形**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入矩形的单元格
- 点击“插入”菜单，然后点击“形状”
- 接着，从“最近使用的形状”或“矩形”中选择矩形

![](rectangle.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入矩形。

{{% alert color="primary" %}}

[**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle)

该方法返回一个 [RectangleShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) 对象。

{{% /alert %}}

以下示例显示了如何向工作表中插入矩形。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Rectangle.py" >}}

执行上述代码，您将获得以下结果：

![](rectangle2.png)



## **在 C# 中向 Excel 工作表插入立方体**

立方体的形状属于**基本形状**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入立方体的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**基本形状**中选择立方体

![](cube.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入立方体。

{{% alert color="primary" %}}

[**public Shape add_auto_shape(type, upper_left_row, top, upper_left_column, left, height, width)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

该方法返回一个 [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) 对象。

{{% /alert %}}

以下示例显示了如何向工作表中插入立方体。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Cube.py" >}}

执行上述代码，您将获得以下结果：

![](cube2.png)



## **在C#中向Excel工作表中插入标注四方箭头**

呼叫四向箭头的形状属于**块箭头**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入标注四箭头的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**块箭头**中选择标注四箭头

![](callout_quad_arrow.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入标注四箭头

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

该方法返回一个 [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) 对象。

{{% /alert %}}

以下示例显示了如何将标注四箭头插入工作表

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.py" >}}

执行上述代码，您将获得以下结果：

![](callout_quad_arrow2.png)



## **在C#中向Excel工作表插入乘号的形状**

乘法符号的形状属于**方程形状**类别

***在Microsoft Excel中(例如2007年)：***

- 选择要插入乘法符号的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**方程形状**中选择乘法符号

![](multiplication_sign.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入乘法符号

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

该方法返回一个 [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) 对象。

{{% /alert %}}

以下示例显示如何将乘法符号插入工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.py" >}}

执行上述代码，您将获得以下结果：

![](multiplication_sign2.png)



## **在C#中向Excel工作表插入多文档的形状**

多文档的形状属于**流程图**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入多文档的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**流程图**中选择多文档

![](multidocument.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入多文档。

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

该方法返回一个 [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) 对象。

{{% /alert %}}

以下示例显示如何向工作表中插入多文档。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Multidocument.py" >}}

执行上述代码，您将获得以下结果：

![](multidocument2.png)



## **在C#中向Excel工作表插入五角星**

五角星的形状属于**星形图案**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入五角星的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**星形和横幅**中选择五角星

![](star_5_points.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入五角星

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

该方法返回一个 [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) 对象。

{{% /alert %}}

以下示例显示了如何向工作表中插入五角星。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-FivePointedStar.py" >}}

执行上述代码，您将获得以下结果：

![](star_5_points2.png)



## **在C#中向Excel工作表插入一个思维气泡云**

思维气泡云的形状属于**标注**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入思维气泡云的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**标注**中选择思维气泡云

![](thought_bubble_cloud.png)

***使用Aspose.Cells for Python via .NET***

您可以使用以下方法在工作表中插入思维气泡云。

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

该方法返回一个 [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) 对象。

{{% /alert %}}

以下示例演示了如何向工作表中插入思维气泡云。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.py" >}}

执行上述代码，您将获得以下结果：

![](thought_bubble_cloud2.png)

## **高级主题**
- [改变形状的调整值](/cells/zh/python-net/change-adjustment-values-of-the-shape/)
- [在工作表之间复制形状](/cells/zh/python-net/copy-shapes-between-worksheets/)
- [非原始形状中的数据](/cells/zh/python-net/data-in-non-primitive-shape/)
- [查找工作表内形状的绝对位置](/cells/zh/python-net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [从形状获取连接点](/cells/zh/python-net/get-connection-points-from-shape/)
- [管理控件](/cells/zh/python-net/managing-controls/)
- [向工作表添加图标](/cells/zh/python-net/insert-svg-to-excel/)
- [管理OLE对象](/cells/zh/python-net/managing-ole-objects/)
- [管理图片](/cells/zh/python-net/managing-pictures/)
- [管理智能图形](/cells/zh/python-net/managing-smartart/)
- [管理文本框](/cells/zh/python-net/managing-textbox-of-excel/)
- [在工作表中添加艺术字水印](/cells/zh/python-net/add-wordart-watermark-to-worksheet/)
- [刷新链接形状的值](/cells/zh/python-net/refresh-values-of-linked-shapes/)
- [在工作表内发送形状到最前或最后](/cells/zh/python-net/send-shape-front-or-back-inside-the-worksheet/)
- [管理形状选项](/cells/zh/python-net/managing-shape-options/)
- [管理形状文本选项](/cells/zh/python-net/managing-shape-text-options/)
- [Web扩展 - 办公室加载项](/cells/zh/python-net/web-extensions-office-add-ins/)

