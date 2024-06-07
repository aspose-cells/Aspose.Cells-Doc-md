---
title: Aspose.Cells对象模型
type: docs
weight: 20
url: /zh/python-java/aspose-cells-object-model/
---

{{% alert color="primary" %}}

Aspose.Cells对象模型提供了有关Aspose.Cells类库对象之间结构关系的信息。

{{% /alert %}}

Aspose.Cells对象模型的顶层结构如下所示，采用分层方式展示。

|**Aspose.Cells对象模型的顶层结构**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
从以上图中可以看到，对象模型的根是Workbook对象。下面提供了以下几个对象的简要描述，供入门参考。

## **WorksheetCollection/Worksheet**

Workbook对象包含WorksheetCollection，表示电子表格中所有Worksheet对象的集合，如下所示：

|**工作表和工作表对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|

## **Cells/Cell**

每个Worksheet对象包含一个Cells对象，表示工作表中所有Cell对象的集合，如下所示：

|**单元格和单元格对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
你可以使用Cell对象来获取和设置单个单元格的值，样式，公式和其他属性。

## **ChartCollection/Chart**

Charts对象表示工作表中所有图表对象的集合。每个图表对象由几个其他对象组成，这些对象共同创建和管理图表。 Aspose.Cells中的Chart结构如下图所示：

|**图表的对象模型**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|

## **CommentCollection/Comment**

每个Worksheet对象还包含一个Comments对象，表示工作表中所有评论对象的集合，如下所示：

|**评论和评论对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
Comment对象用于在工作表中的任意指定单元格添加评论。

## **HorizontalPageBreakCollection/HorizontalPageBreak**

每个Worksheet对象包含一个HorizontalPageBreakCollection，表示工作表中所有水平分页符对象的集合，如下所示：

|**水平分页和水平分页对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
HorizontalPageBreak对象用于在工作表中创建水平分页。

## **HyperlinkCollection/Hyperlink**

Worksheet对象还包含一个HyperlinkCollection，表示工作表中所有超链接对象的集合，如下所示：

|**超链接和超链接对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
超链接对象表示工作表中的超链接。 开发人员可以使用超链接对象设置超链接地址和其他相关属性。

## **PictureCollection/Picture**

每个Worksheet对象包含一个PictureCollection对象，表示工作表中所有图片对象的集合，如下所示：

|**图片和图片对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
图片对象表示工作表中的图片。使用图片对象，开发人员不仅可以将图片添加到他们的工作表中，还可以将这些图片定位在任何位置。 还可以设置图片框线或其他属性。

## **VerticalPageBreakCollection/VerticalPageBreak**

每个Worksheet对象包含一个VerticalPageBreakCollection对象，表示工作表中所有垂直分页符对象的集合，如下所示：

|**垂直分页和垂直分页对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
VerticalPageBreak对象用于在工作表中创建垂直分页。
