---
title: 在工作表中删除空白行和列
type: docs
weight: 300
url: /zh/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

可以从工作表中删除所有空白行和列。例如，从 Microsoft Excel 文件生成 PDF 文件并且只希望转换包含数据或相关对象的行和列时，这很有用。

使用以下 Aspose.Cells 方法删除空白行和列：

1. 要删除空白行，请使用 [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) 方法。请注意，对于将要删除的空白行，不仅需要 [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) 为 true，而且这些行中的任何单元格都不能定义可见注释，也不能有与它们交叉的数据透视表。
1. 要删除空白列，请使用 [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) 方法。

{{% /alert %}}

## 用于删除空白行的 C# 代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## 用于删除空白列的 C# 代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
