---
title: Aspose.Cells 对象模型
type: docs
weight: 20
url: /zh/python-net/aspose-cells-object-model/
---

{{% alert color="primary" %}}

Aspose.Cells 对象模型提供了有关 Aspose.Cells 类库对象之间结构关系的信息。

{{% /alert %}}

Aspose.Cells对象模型的顶层结构如下所示，以分层方式呈现。

|**Aspose.Cells对象模型的顶层结构**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
如您从上图所见，对象模型的根是Workbook对象。以下提供了一些对象的简要描述，供初学者参考。

## **WorksheetCollection/Worksheet**

Workbook对象包含WorksheetCollection，表示电子表格中所有Worksheet对象的集合，如下所示：

|**Worksheets & Worksheet对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|

## **Cells/Cell**

每个Worksheet对象包含一个Cells对象，表示工作表中所有Cell对象的集合，如下所示：

|**Cells & Cell对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
您可以使用Cell对象来获取和设置单个单元格的值、样式、公式和其他属性。

## **ChartCollection/Chart**

Charts对象表示工作表中所有Chart对象的集合。每个Chart对象由多个协同工作的对象组成，用于创建和管理图表。Aspose.Cells中的Chart结构如下图所示：

|**Chart对象模型**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|

## **CommentCollection/Comment**

每个Worksheet对象还包含一个Comments对象，表示工作表中所有Comment对象的集合，如下所示：

|**Comments & Comment对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
Comment对象用于向工作表中的任何指定单元格添加评论。

## **HorizontalPageBreakCollection/HorizontalPageBreak**

每个Worksheet对象包含HorizontalPageBreakCollection，表示工作表中所有HorizontalPageBreak对象的集合，如下所示：

|**HPageBreaks & HPageBreak对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
HorizontalPageBreak 对象用于在工作表中创建水平分页符。

## **HyperlinkCollection/Hyperlink**

Worksheet 对象还包含一个 HyperlinkCollection，表示工作表中所有超链接对象的集合，如下所示：

|**超链接和超链接对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
Hyperlink 对象表示工作表中的超链接。开发人员可以使用 Hyperlink 对象设置超链接地址和其他相关属性。

## **PictureCollection/Picture**

每个 Worksheet 对象包含一个 PictureCollection 对象，表示工作表中所有图片对象的集合，如下所示：

|**图片和图片对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
Picture 对象表示工作表中的图片。使用 Picture 对象，开发人员不仅可以向其工作表添加图片，还可以将这些图片放置在任何位置。还可以设置图片的边框或其他属性。

## **VerticalPageBreakCollection/VerticalPageBreak**

每个 Worksheet 对象包含一个 VerticalPageBreakCollection 对象，表示工作表中所有垂直分页符对象的集合，如下所示：

|**垂直分页和垂直分页对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
VerticalPageBreak 对象用于在工作表中创建垂直分页符。
{{< app/cells/assistant language="python-net" >}}
