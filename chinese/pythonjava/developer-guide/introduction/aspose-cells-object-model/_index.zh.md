---
title: Aspose.Cells 对象模型
type: docs
weight: 20
url: /zh/python-java/aspose-cells-object-model/
---
{{% alert color="primary" %}}

Aspose.Cells 对象模型提供有关 Aspose.Cells 类库对象之间结构关系的信息。

{{% /alert %}}

Aspose.Cells 对象模型的顶层结构如下图所示。

|**Aspose.Cells对象模型的顶层结构**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_1.png)|
从上图可以看出，对象模型的根是Workbook对象。为了介绍的目的，下面提供了一些对象的简要描述。

## **WorksheetCollection/工作表**

Workbook 对象包含 WorksheetCollection，它表示电子表格中所有 Worksheet 对象的集合，如下所示：

|**工作表和工作表对象**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_2.png)|

## **Cells/Cell**

每个 Worksheet 对象都包含一个 Cells 对象，代表工作表中所有 Cell 对象的集合，如下所示：

|**Cells & Cell 对象**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_3.png)|
您可以使用 Cell 对象获取和设置单个单元格的值、样式、公式和其他属性。

## **ChartCollection/图表**

Charts 对象表示 Worksheet 中所有 Chart 对象的集合。每个 Chart 对象都由多个其他对象组成，这些对象协同工作以创建和管理图表。 Aspose.Cells中的Chart结构如下图所示：

|**图表的对象模型**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_4.png)|

## **评论收藏/评论**

每个 Worksheet 对象还包含一个 Comments 对象，代表工作表中所有 Comment 对象的集合，如下所示：

|**评论和评论对象**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_5.png)|
Comment 对象用于向工作表中的任何指定单元格添加注释。

## **HorizontalPageBreakCollection/HorizontalPageBreak**

每个 Worksheet 对象都包含一个 HorizontalPageBreakCollection，它表示工作表中所有 HorizontalPageBreak 对象的集合，如下所示：

|**HPageBreaks & HPageBreak 对象**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_6.png)|
HorizontalPageBreak 对象用于在工作表中创建水平分页符。

## **HyperlinkCollection/超链接**

Worksheet 对象还包含一个 HyperlinkCollection，它表示工作表中所有 Hyperlink 对象的集合，如下所示：

|**超链接和超链接对象**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_7.png)|
超链接对象表示工作表中的超链接。开发者可以使用 Hyperlink 对象设置超链接地址和其他相关属性。

## **图片集/图片**

每个 Worksheet 对象都包含一个 PictureCollection 对象，该对象表示工作表中所有 Picture 对象的集合，如下所示：

|**图片和图片对象**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_8.png)|
Picture 对象表示工作表中的图片。使用 Picture 对象，开发人员不仅可以将图片添加到他们的工作表中，还可以将这些图片放置在任何位置。还可以设置图片的边框或其他属性。

## **VerticalPageBreakCollection/VerticalPageBreak**

每个 Worksheet 对象都包含一个 VerticalPageBreakCollection 对象，它表示工作表中所有 VerticalPageBreak 对象的集合，如下所示：

|**VPageBreaks & VPageBreak 对象**|
|:- |
|![待办事项：图像_替代_文本](aspose-cells-object-model_9.png)|
VerticalPageBreak 对象用于在工作表中创建垂直分页符。
