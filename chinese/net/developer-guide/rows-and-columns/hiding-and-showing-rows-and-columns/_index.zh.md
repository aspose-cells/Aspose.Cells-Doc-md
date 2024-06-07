---
title: 隐藏和显示行和列
type: docs
weight: 60
url: /zh/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

有时，在工作表中隐藏某些行或列并稍后显示它们是有意义的。Microsoft Excel提供了这个功能，Aspose.Cells也提供了这个功能。

{{% /alert %}}

## **控制行和列的可见性**

Aspose.Cells提供了一个代表Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)，允许开发人员访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合，代表工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合提供了几种用于管理工作表中行或列的方法。以下将讨论其中一些。

### **隐藏行和列**

开发人员可以通过调用 [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) 和 [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) 方法来隐藏 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合中的行或列。这两种方法都将行和列索引作为参数，以隐藏特定的行或列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

还可以将行高或列宽分别设置为 0 来隐藏行或列。

{{% /alert %}}

### **显示行和列**

开发人员可以通过调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合的 [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) 和 [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) 方法来显示任何隐藏的行或列。这两种方法都有两个参数:

- **行或列索引** - 用于显示特定行或列的行或列索引。
- **行高或列宽** - 在取消隐藏后分配给行或列的行高或列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

将隐藏的列显示出来时，如果需要将其恢复为先前分配的宽度或其原始宽度，请以负宽度取消隐藏列。例如：worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **隐藏多行和列**

开发人员可以通过调用 [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) 和 [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) 方法一次隐藏多行或列，分别将起始行或列索引和应该隐藏的行或列数作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

也可以使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类的[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)和[**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)方法使多行和列可见。

{{% /alert %}}
