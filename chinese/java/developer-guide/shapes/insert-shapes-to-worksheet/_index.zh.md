---
title: 在Aspose.Cells中插入形状到工作表
type: docs
weight: 5
url: /zh/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

有时候，您需要在工作表中插入一些必要的形状。您可能需要在工作表的不同位置插入相同的形状。或者您需要批量在工作表中插入形状。

不用担心！[Aspose.Cells](https://products.aspose.com/cells/)支持所有这些操作。

{{% /alert %}}

Excel中的形状主要分为以下类型:
- **线条**
- **矩形**
- **基本形状**
- **方块箭头**
- **方程式形状**
- **流程图**
- **星星和横幅**
- **标注**

这份指南将从每个类型中选择一个或两个形状来制作示例。通过这些示例，您将学习如何使用[Aspose.Cells](https://products.aspose.com/cells/)将指定的形状插入工作表中。



## **向工作表插入一条线**

线形状属于**线条**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入线条的单元格
- 点击“插入”菜单，然后点击“形状”
- 接着，从“最近使用的形状”或“线条”中选择线条

![](line.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入线条。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

下面的示例显示如何将线条插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

执行上述代码，您将获得以下结果：

![](line2.png)



## **向工作表插入带箭头的线**

箭头线的形状属于**线**类别。它是线的特殊情况。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入箭头线的单元格
- 点击“插入”菜单，然后点击“形状”
- 接着，从“最近使用的形状”或“线”中选择箭头线

![](line_arrow1.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入箭头线。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表插入箭头线。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

执行上述代码，您将获得以下结果：

![](line_arrow2.png)



## **向工作表插入矩形**

矩形的形状属于**矩形**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入矩形的单元格
- 点击“插入”菜单，然后点击“形状”
- 接着，从“最近使用的形状”或“矩形”中选择矩形

![](rectangle.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入矩形。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表中插入矩形。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

执行上述代码，您将获得以下结果：

![](rectangle2.png)



## **向工作表插入立体图**

立方体的形状属于**基本形状**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入立方体的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**基本形状**中选择立方体

![](cube.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入立方体。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表中插入立方体。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

执行上述代码，您将获得以下结果：

![](cube2.png)



## **在工作表中插入箭头标签**

呼叫四向箭头的形状属于**块箭头**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入标注四箭头的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**块箭头**中选择标注四箭头

![](callout_quad_arrow.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入标注四箭头

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何将标注四箭头插入工作表

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

执行上述代码，您将获得以下结果：

![](callout_quad_arrow2.png)



## **在工作表中插入乘号**

乘法符号的形状属于**方程形状**类别

***在Microsoft Excel中(例如2007年)：***

- 选择要插入乘法符号的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**方程形状**中选择乘法符号

![](multiplication_sign.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入乘法符号

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示如何将乘法符号插入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

执行上述代码，您将获得以下结果：

![](multiplication_sign2.png)



## **在工作表中插入多文档**

多文档的形状属于**流程图**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入多文档的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**流程图**中选择多文档

![](multidocument.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入多文档。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示如何向工作表中插入多文档。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

执行上述代码，您将获得以下结果：

![](multidocument2.png)



## **在工作表中插入五角星**

五角星的形状属于**星形图案**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入五角星的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**星形和横幅**中选择五角星

![](star_5_points.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入五角星

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例显示了如何向工作表中插入五角星。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

执行上述代码，您将获得以下结果：

![](star_5_points2.png)



## **在工作表中插入思维气泡云**

思维气泡云的形状属于**标注**类别。

***在Microsoft Excel中(例如2007年)：***

- 选择要插入思维气泡云的单元格
- 点击“插入”菜单，然后点击“形状”
- 然后，从**标注**中选择思维气泡云

![](thought_bubble_cloud.png)

***使用Aspose.Cells***

您可以使用以下方法在工作表中插入思维气泡云。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

该方法返回一个[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)对象。

{{% /alert %}}

以下示例演示了如何向工作表中插入思维气泡云。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

执行上述代码，您将获得以下结果：

![](thought_bubble_cloud2.png)
{{< app/cells/assistant language="java" >}}
