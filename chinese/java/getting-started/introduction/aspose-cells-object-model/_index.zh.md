---
title: Aspose.Cells 对象模型
type: docs
weight: 20
url: /zh/java/aspose-cells-object-model/
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

## **PivotTableCollection/PivotTable**
每个 Worksheet 对象包含一个 PivotTableCollection 对象，表示工作表中所有数据透视表对象的集合，如下所示：

|**数据透视表和数据透视表对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_10.png)|
PivotTable 对象表示工作表中的数据透视表。开发人员可以使用 PivotTable 对象设置数据透视表的样式和其他相关属性。

## **TimelineCollection/Timeline**
每个 Worksheet 对象包含一个 TimelineCollection 对象，表示工作表中所有时间轴对象的集合，如下所示：

|**时间轴和时间轴对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_11.png)|
时间线对象表示工作表中的时间线。开发人员可以使用时间线对象设置时间线的样式和其他相关属性。

## **SlicerCollection/Slicer**
每个工作表对象都包含一个 SlicerCollection 对象，该对象表示工作表中所有切片器对象的集合，如下所示：

|**切片器和切片器对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_12.png)|
切片器对象表示工作表中的切片器。开发人员可以使用切片器对象设置切片器的样式和其他相关属性。

## **ListObjectCollection/ListObject**
每个工作表对象都包含一个 ListObjectCollection 对象，该对象表示工作表中所有列表对象的集合，如下所示：

|**列表对象和列表对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_13.png)|
ListObject 对象表示工作表中的表格。开发人员可以使用 ListObject 对象设置表格的样式和其他相关属性。

## **ShapeCollection/Shape**
每个工作表对象都包含一个 ShapeCollection 对象，该对象表示工作表中所有形状对象的集合，如下所示：

|**形状和形状对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_14.png)|
Shape 对象表示工作表中的形状。开发人员可以使用 Shape 对象设置形状的样式和其他相关属性。

## **SparklineGroupCollection/SparklineGroup**
每个工作表对象都包含一个 SparklineGroupCollection 对象，该对象表示工作表中所有迷你图组对象的集合，如下所示：

|**迷你图组和迷你图组对象**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_15.png)|
SparklineGroup 对象表示工作表中的迷你图组。开发人员可以使用 SparklineGroup 对象设置迷你图组的样式和其他相关属性。
{{< app/cells/assistant language="java" >}}
