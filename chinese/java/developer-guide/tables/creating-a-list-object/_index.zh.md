---
title: 创建表
type: docs
weight: 40
url: /zh/java/creating-a-list-object/
---

{{% alert color="primary" %}}

电子表格的优点之一是它允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债列表。多个用户可以共同使用、创建和维护各种列表。

Aspose.Cells支持创建和管理列表。

{{% /alert %}}

## **表的优势**

将数据列表转换为实际列表对象时有很多优势：

- 新行和列会自动包含其中。
- 可轻松添加位于列表底部的总行，以显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到列表对象中。
- 基于行和列的图表将自动扩展。
- 针对行和列分配的命名范围将自动扩展。
- 列表受到意外删除的保护。

## **使用Microsoft Excel创建表**

选择用于创建列表对象的数据范围 

![todo:image_alt_text](creating-a-list-object_1.png)

这将显示创建列表对话框。

创建列表对话框 

![todo:image_alt_text](creating-a-list-object_2.png)

实现列表对象并指定总计行 (选择 **数据**，然后选择 **列表**，接着选择 **总计行**)。

创建列表对象 

![todo:image_alt_text](creating-a-list-object_3.png)

## **使用Aspose.Cells API创建表**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个微软Excel文件。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供了用于管理工作表的各种属性和方法。要在工作表中创建一个 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)，请使用工作表类的 [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) 集合属性。实际上，每个 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) 都是 [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection) 类的对象，后者还提供了添加列表对象和指定范围单元格的 add 方法。

根据指定的单元格范围，在工作表中创建了Aspose.Cells的列表对象。使用 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) 类的属性 (例如，ShowTotals, ListColumns 等) 控制列表。

在下面给出的示例中，我们使用Aspose.Cells API创建了一个与上述部分中使用Microsoft Excel创建的相同的[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
