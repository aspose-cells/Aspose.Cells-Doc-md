---
title: 隐藏和显示行和列
type: docs
weight: 60
url: /zh/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

有时，隐藏工作表中的某些行或列，稍后再显示它们是有意义的。Microsoft Excel提供了此功能，Aspose.Cells也是。

{{% /alert %}}

## **控制行和列的可见性**

Aspose.Cells提供了一个代表Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含了一个[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)，允许开发人员访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合，表示工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合提供了几种管理工作表中的行或列的方法。以下介绍了其中的一些。

### **隐藏行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合的[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)和[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)方法，分别隐藏行或列。两种方法都以行索引或列索引作为参数，以隐藏特定的行或列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

还可以通过将行高或列宽设置为0来隐藏行或列。

{{% /alert %}}

### **显示行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合的[**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)和[**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)方法，分别显示任何隐藏的行或列。两种方法都需要两个参数：

- 行或列索引 - 用于显示特定行或列的索引。
- 行高或列宽 - 在取消隐藏后分配给行或列的行高或列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

在使隐藏的列可见时，如果需要恢复其先前分配的宽度或其原始宽度，请使用负宽度取消隐藏列。例如：worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **隐藏多行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合的[**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)和[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)方法，分别一次隐藏多行或列。两种方法都需要起始行或列索引和应该隐藏的行数或列数作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

还可以使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类的[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)和[**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)方法来显示多行和列。

{{% /alert %}}
