---
title: 隐藏和显示行和列
type: docs
weight: 50
url: /zh/java/hiding-and-showing-rows-and-columns/
---

## **介绍**
有时，用户可能需要将工作表的某些行或列隐藏，然后稍后显示它们。Microsoft Excel 提供此功能，Aspose.Cells 也提供。
## **控制行和列的可见性**
Aspose.Cells 提供了一个 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类，代表 Microsoft Excel 文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个 [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类提供一个 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合，表示工作表中的所有单元格。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合提供了几种方法来管理工作表中的行或列。一些方法如下所述。
### **隐藏行或列**
开发人员可以通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的 [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\)) 和 [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\)) 方法分别隐藏行或列。这两种方法接受行/列索引作为参数，以隐藏特定的行或列。

{{% alert color="primary" %}} 

注意：如果将行高或列宽设置为 0，则还可以隐藏行或列。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **显示行和列**
开发人员可以分别调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的 [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\)) 和 [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\)) 方法来取消隐藏任何隐藏的行或列。这两种方法各自接受两个参数：

- **行或列索引** - 用于显示特定行或列的行或列索引。
- **行高或列宽** - 显示行或列后分配给行或列的行高或列宽。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

在使隐藏的列/行可见时，如果您需要将其恢复为先前分配的宽度或高度，或其原始宽度或高度，请使用负宽度或高度取消隐藏列或行。例如，worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
