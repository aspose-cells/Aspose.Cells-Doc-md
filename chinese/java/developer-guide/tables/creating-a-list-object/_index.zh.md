---
title: 创建表
type: docs
weight: 40
url: /zh/java/creating-a-list-object/
---
{{% alert color="primary" %}}

电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债。多个用户可以一起使用、创建和维护各种列表。

Aspose.Cells 支持创建和管理列表。

{{% /alert %}}

## **一张桌子的好处**

将数据列表转换为实际列表对象时有很多优点：

- 自动包含新行和新列。
- 列表底部的总计行可以轻松添加以显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到 List 对象中。
- 基于行和列的图表将自动展开。
- 分配给行和列的命名范围将自动扩展。
- 该列表受到保护，不会意外删除行和列。

## **使用 Microsoft Excel 创建表格**

**选择用于创建列表对象的数据范围** 

![待办事项：图片_替代_文本](creating-a-list-object_1.png)

这将显示“创建列表”对话框。

**创建列表对话框** 

![待办事项：图片_替代_文本](creating-a-list-object_2.png)

实施列表对象并指定总行（选择**数据**， 然后**列表**， 其次是**总行数**).

**创建列表对象** 

![待办事项：图片_替代_文本](creating-a-list-object_3.png)

## **使用 Using Aspose.Cells API 创建表**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。创建一个[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)在工作表中，使用[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)Worksheet 类的集合属性。每个[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)实际上是[**列表对象集合**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)类，它进一步提供了用于添加 List 对象并为列表指定单元格范围的 add 方法。

Aspose.Cells根据指定范围的单元格在工作表中创建List对象。使用属性（例如ShowTotals、ListColumns等）[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)控制列表的类。

在下面给出的示例中，我们创建了相同的[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)使用我们在上一节中使用 Microsoft Excel 创建的 Aspose.Cells API。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
