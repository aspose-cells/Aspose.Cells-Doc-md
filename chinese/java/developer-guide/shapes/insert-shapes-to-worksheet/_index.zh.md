---
title: 将形状插入到工作表中 Aspose.Cells
type: docs
weight: 5
url: /zh/java/insert-shapes-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

有时您需要在工作表中插入一些必要的形状。您可能需要在工作表的不同位置插入相同的形状。或者您需要在工作表中批量插入形状。

不用担心！[Aspose.Cells](https://products.aspose.com/cells/)支持所有这些操作。

{{% /alert %}}

excel中的形状主要分为以下几种：
- **线条**
- **矩形**
- **基本形状**
- **块箭头**
- **方程形状**
- **流程图**
- **星星和横幅**
- **标注**

本指南文档将从每种类型中选择一个或两个形状来制作示例。通过这些示例，您将学习如何使用[Aspose.Cells](https://products.aspose.com/cells/)将指定的形状插入到工作表中。



## **在工作表中插入一行**

线条的形状属于**线条**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入行的单元格
- 单击插入菜单，然后单击形状。
- 然后，从“最近使用的形状”或“线条”中选择线条

![](line.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入一行。

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何向工作表插入行。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

执行上面的代码，你会得到如下结果：

![](line2.png)



## **向工作表插入线箭头**

线箭头的形状属于**线条**category.It 是 line 的特例。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入直线箭头的单元格
- 单击插入菜单，然后单击形状。
- 然后，从“最近使用的形状”或“线条”中选择线条箭头

![](line_arrow1.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入线箭头。

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何将线箭头插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

执行上面的代码，你会得到如下结果：

![](line_arrow2.png)



## **在工作表中插入一个矩形**

矩形的形状属于**矩形**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入矩形的单元格
- 单击插入菜单，然后单击形状。
- 然后，从“最近使用的形状”或“矩形”中选择矩形

![](rectangle.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入一个矩形。

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何将矩形插入到工作表中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

执行上面的代码，你会得到如下结果：

![](rectangle2.png)



## **将多维数据集插入工作表**

立方体的形状属于**基本形状**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入立方体的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择多维数据集**基本形状**

![](cube.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入一个立方体。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何将多维数据集插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

执行上面的代码，你会得到如下结果：

![](cube2.png)



## **将标注四箭头插入工作表**

标注四箭头的形状属于**块箭头**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入标注四箭头的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择标注四箭头**块箭头**

![](callout_quad_arrow.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入标注四箭头。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何将标注四箭头插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

执行上面的代码，你会得到如下结果：

![](callout_quad_arrow2.png)



## **在工作表中插入乘号**

乘号的形状属于**方程形状**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入乘号的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择乘号**方程形状**

![](multiplication_sign.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入乘号。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何将乘号插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

执行上面的代码，你会得到如下结果：

![](multiplication_sign2.png)



## **将多文档插入工作表**

多文档的形状属于**流程图**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入多文档的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择多文档**流程图**

![](multidocument.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入多文档。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何将多文档插入到工作表中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

执行上面的代码，你会得到如下结果：

![](multidocument2.png)



## **在工作表中插入一个五角星**

五角星的形状属于**星星和横幅**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入五角星的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择五角星**星星和横幅**

![](star_5_points.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入一个五角星。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何将五角星插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

执行上面的代码，你会得到如下结果：

![](star_5_points2.png)



## **将思想气泡云插入工作表**

思想气泡云的形状属于**标注**类别。

***在 Microsoft Excel 中（例如 2007）：***

- 选择要插入思想气泡云的单元格
- 单击插入菜单，然后单击形状。
- 然后，从中选择思想气泡云**标注**

![](thought_bubble_cloud.png)

***使用 Aspose.Cells***

您可以使用以下方法在工作表中插入思想泡泡云。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

该方法返回一个[形状](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)目的。

{{% /alert %}}

以下示例显示如何将思想泡泡云插入到工作表中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

执行上面的代码，你会得到如下结果：

![](thought_bubble_cloud2.png)
