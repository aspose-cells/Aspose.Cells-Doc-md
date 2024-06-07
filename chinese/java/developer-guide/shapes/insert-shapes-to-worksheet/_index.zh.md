---
title: 在Aspose.Cells中将形状插入到工作表中
type: docs
weight: 5
url: /zh/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

有时您需要在工作表中插入一些必要的形状。您可能需要将相同形状插入工作表的不同位置。或者您需要批量插入工作表中的形状。

不要担心！[Aspose.Cells](https://products.aspose.com/cells/) 支持所有这些操作。

{{% /alert %}}

Excel 中的形状主要分为以下类型：
- **直线**
- **矩形**
- **基本形状**
- **块状箭头**
- **等式形状**
- **流程图**
- **星星和旗帜**
- **标记**

本指南文档将从每种类型中选择一个或两个形状来制作样本。通过这些示例，您将学会如何使用[Aspose.Cells](https://products.aspose.com/cells/)将指定的形状插入工作表中。



## **向工作表插入线条**

线的形状属于**线条**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入线条的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后，从“最近使用的形状”或“线条”中选择线条

![](line.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入线条。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入线条。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

执行上述代码，您将获得以下结果：

![](line2.png)



## **向工作表插入线箭头**

线箭头的形状属于**线条**类别。它是线条的一个特例。

***在Microsoft Excel（例如2007）中：***

- 选择要插入线箭头的单元格
- 单击“插入”菜单，然后单击“形状”
- 接着，从“最近使用的形状”或“线条”中选择线箭头

![](line_arrow1.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入线箭头。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入线箭头。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

执行上述代码，您将获得以下结果：

![](line_arrow2.png)



## **向工作表插入矩形**

矩形的形状属于**矩形**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入矩形的单元格
- 单击“插入”菜单，然后单击“形状”
- 接着，从“最近使用的形状”或“矩形”中选择矩形。

![](rectangle.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入一个矩形。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示如何向工作表插入矩形。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

执行上述代码，您将获得以下结果：

![](rectangle2.png)



## **向工作表插入立方体**

立方体的形状属于**基本形状**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入立方体的单元格
- 单击“插入”菜单，然后单击“形状”
- 接着，从**基本形状**中选择立方体

![](cube.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入一个立方体。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例展示了如何将立方体插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

执行上述代码，您将获得以下结果：

!\[](cube2.png)



## **向工作表插入标注四角箭头**

标注四向箭头的形状属于**块箭头**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入标注四向箭头的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后，从**块箭头**中选择标注四向箭头

!\[](callout_quad_arrow.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入一个标注四向箭头。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例展示了如何将标注四向箭头插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

执行上述代码，您将获得以下结果：

![](callout_quad_arrow2.png)



## **向工作表插入乘法符号**

乘法符号的形状属于**方程形状**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入乘法符号的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后从**方程形状**中选择乘法符号

![](multiplication_sign.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入乘法符号。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示如何将乘法符号插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

执行上述代码，您将获得以下结果：

![](multiplication_sign2.png)



## **向工作表插入多文档**

多文档的形状属于**流程图**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入多文档的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后从**流程图**中选择多文档

![](multidocument.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入一个多文档。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

下面的示例显示如何向工作表插入多文档。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

执行上述代码，您将获得以下结果：

![](multidocument2.png)



## **向工作表插入五角星**

五角星形状属于**星形和横幅**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入五角星的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后，在**星形和横幅**中选择五角星

![](star_5_points.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入五角星。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入五角星。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

执行上述代码，您将获得以下结果：

![](star_5_points2.png)



## **向工作表插入思维泡泡云**

思维气泡云的形状属于**标注**类别。

***在Microsoft Excel（例如2007）中：***

- 选择要插入思维气泡云的单元格
- 单击“插入”菜单，然后单击“形状”
- 然后从**标注**中选择思维气泡云

![](thought_bubble_cloud.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入思维气泡云。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入思维气泡云。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

执行上述代码，您将获得以下结果：

![](thought_bubble_cloud2.png)
