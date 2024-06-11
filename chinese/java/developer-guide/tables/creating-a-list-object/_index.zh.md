---
title: 创建一个表
type: docs
weight: 40
url: /zh/java/creating-a-list-object/
---

{{% alert color="primary" %}}

电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债列表。多个用户可以共同使用、创建和维护各种列表。

Aspose.Cells支持创建和管理列表。

{{% /alert %}}

## **表格的优势**

将数据列表转换为实际的列表对象时，有一些很明显的优势：

- 新行和列会自动包括在内。
- 列表底部可以轻松添加总计行来显示求和、平均、计数等信息。
- 添加在右侧的列会自动并入列表对象中。
- 基于行和列的图表会自动扩展。
- 分配给行和列的命名范围将自动扩展。
列表受到意外行和列删除的保护。

## **使用Microsoft Excel创建一个表**

选取数据范围以创建一个列表对象 

![todo:image_alt_text](creating-a-list-object_1.png)

这会显示创建列表对话框。

创建列表对话框 

![todo:image_alt_text](creating-a-list-object_2.png)

实现列表对象并指定总行（选择**数据**，然后**列表**，接着**总行**）。

创建一个列表对象 

![todo:image_alt_text](creating-a-list-object_3.png)

## **使用Aspose.Cells API创建表**

Aspose.Cells提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)，请使用[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)集合属性。每个[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)实际上是[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)类的对象，后者还提供添加列表对象和指定列表对象的单元格范围的add方法。

根据指定的单元格范围，Aspose.Cells在工作表中创建了列表对象。使用[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)类的属性（例如ShowTotals、ListColumns等）来控制列表。

在下面的示例中，我们使用Aspose.Cells API创建了与前面在Microsoft Excel中创建相同的[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
