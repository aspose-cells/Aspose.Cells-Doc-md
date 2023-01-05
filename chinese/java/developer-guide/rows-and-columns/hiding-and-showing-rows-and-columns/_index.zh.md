---
title: 隐藏和显示行和列
type: docs
weight: 50
url: /zh/java/hiding-and-showing-rows-and-columns/
---
## **介绍**
有时，用户可能还需要隐藏工作表的某些行或列，然后再显示。 Microsoft Excel 提供此功能，因此为 Aspose.Cells。
## **控制行和列的可见性**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)代表工作表中所有单元格的集合。这[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection 提供了多种方法来管理工作表中的行或列。下面讨论其中一些。
### **隐藏行或列**
开发人员可以通过调用[隐藏行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\)） 和[隐藏列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)分别收藏。这两种方法都将行/列索引作为参数来隐藏特定的行或列。

{{% alert color="primary" %}} 

注意：如果我们将行高或列宽分别设置为 0，也可以隐藏行或列。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **显示行和列**
开发人员可以通过调用[取消隐藏行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\)） 和[取消隐藏列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)分别收藏。两种方法都有两个参数：

- **行或列索引** 用于显示特定行或列的行或列的索引。
- **行高或列宽** 显示后分配给行或列的行高或列宽。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

在使隐藏的列/行可见的同时，如果需要将其恢复到之前分配的宽度或高度，或原来的宽度或高度，请取消隐藏宽度或高度为负的列或行。例如，worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
