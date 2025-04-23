---
title: 隐藏和显示行和列
type: docs
weight: 50
url: /zh/java/hiding-and-showing-rows-and-columns/
---

## **介绍**
有时，用户可能需要隐藏工作表的某些行或列，然后稍后再显示它们。Microsoft Excel提供了这个功能，Aspose.Cells也提供了。
## **控制行和列的可见性**
Aspose.Cells提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，表示Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合，表示工作表中的所有单元格。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合提供了几种管理工作表中的行或列的方法，以下是其中的一些。
### **隐藏行或列**
开发者可以通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的 [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow-int-) 和 [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn-int-) 方法隐藏某一行或列。两者都接受行/列索引作为参数，以隐藏特定的行或列。

{{% alert color="primary" %}} 

注意：如果将行高或列宽设置为0，则也可以隐藏行或列。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **显示行和列**
开发者可以通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow-int-double-) 和 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn-int-double-) 方法取消隐藏任何隐藏的行或列。这两个方法都接受两个参数：

- 行或列索引 - 用于显示特定行或列的索引。
- **行高或列宽** - 在显示后分配给行或列的行高或列宽。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

在将隐藏的列/行显示出来时，如果需要将其恢复为先前分配的宽度或高度，或其原始宽度或高度，请使用负宽度或高度取消隐藏列或行。例如，worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
