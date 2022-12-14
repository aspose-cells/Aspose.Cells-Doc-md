---
title: 隐藏和显示行和列
type: docs
weight: 60
url: /zh/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

有时，隐藏工作表中的某些行或列并稍后显示它们是有意义的。 Microsoft Excel 提供此功能，Aspose.Cells 也提供此功能。

{{% /alert %}}

## **控制行和列的可见性**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)允许开发人员访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)代表工作表中所有单元格的集合。这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection 提供了多种方法来管理工作表中的行或列。下面讨论其中的一些。

### **隐藏行和列**

开发人员可以通过调用[**隐藏行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)和[**隐藏列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)分别收藏。这两种方法都将行和列索引作为参数来隐藏特定的行或列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

也可以通过将行高或列宽分别设置为 0 来隐藏行或列。

{{% /alert %}}

### **显示行和列**

开发人员可以通过调用[**取消隐藏行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)和[**取消隐藏列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)分别收藏。两种方法都有两个参数：

- **行或列索引** 用于显示特定行或列的行或列的索引。
- **行高或列宽** 取消隐藏后分配给行或列的行高或列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

在使隐藏的列可见时，如果您需要将其恢复到先前分配的宽度或原始宽度，请取消隐藏宽度为负的列。例如：worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **隐藏多行多列**

开发人员可以通过调用[**隐藏行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)和[**隐藏列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)分别收藏。这两种方法都将起始行或列索引以及应隐藏的行数或列数作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

也可以使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)班级'[**取消隐藏行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)和[**取消隐藏列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)使多行和多列可见的方法。

{{% /alert %}}
