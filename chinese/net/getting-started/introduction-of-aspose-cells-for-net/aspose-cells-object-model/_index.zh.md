---
title: Aspose.Cells对象模型
type: docs
weight: 20
url: /zh/net/aspose-cells-object-model/
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


## **PivotTableCollection/PivotTable**
每个Worksheet对象包含一个PivotTableCollection对象，表示工作表中所有数据透视表对象的集合，如下所示：

|**数据透视表和数据透视表对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_10.png)|
PivotTable对象表示工作表中的数据透视表。开发人员可以使用PivotTable对象设置数据透视表的样式和其他相关属性。

## **TimelineCollection/Timeline**
每个Worksheet对象包含一个TimelineCollection对象，表示工作表中所有时间轴对象的集合，如下所示：

|**时间轴和时间轴对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_11.png)|
Timeline对象表示工作表中的时间轴。开发人员可以使用Timeline对象设置时间轴的样式和其他相关属性。

## **SlicerCollection/Slicer**
每个工作表对象都包含一个 SlicerCollection 对象，该对象表示工作表中所有 Slicer 对象的集合，如下所示：

|**Slicers & Slicer 对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_12.png)|
Slicer 对象表示工作表中的切片器。开发人员可以使用 Slicer 对象设置切片器的样式和其他相关属性。

## **ListObjectCollection/ListObject**
每个工作表对象都包含一个 ListObjectCollection 对象，该对象表示工作表中所有 ListObject 对象的集合，如下所示：

|**ListObjects & ListObject 对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_13.png)|
ListObject 对象表示工作表中的表格。开发人员可以使用 ListObject 对象设置表格的样式和其他相关属性。

## **ShapeCollection/Shape**
每个工作表对象都包含一个 ShapeCollection 对象，该对象表示工作表中所有 Shape 对象的集合，如下所示：

|**Shapes & Shape 对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_14.png)|
Shape 对象表示工作表中的形状。开发人员可以使用 Shape 对象设置形状的样式和其他相关属性。

## **SparklineGroupCollection/SparklineGroup**
每个工作表对象都包含一个 SparklineGroupCollection 对象，该对象表示工作表中所有 SparklineGroup 对象的集合，如下所示：

|**SparklineGroups & SparklineGroup 对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_15.png)|
SparklineGroup 对象表示工作表中的迷你图组。开发人员可以使用 SparklineGroup 对象设置迷你图组的样式和其他相关属性。
