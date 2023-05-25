---
title: 删除工作表中的空白行和列
type: docs
weight: 300
url: /zh/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

可以从工作表中删除所有空白行和列。这在例如从 Microsoft Excel 文件生成 PDF 文件并且只想转换包含数据或相关对象的行和列时很有用。

使用以下 Aspose.Cells 方法删除空行和空列：

1. 要删除空白行，请使用[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows)方法。请注意，对于将被删除的空白行，不仅要求[**行.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/)应该是真的，但也不应该为这些行中的任何单元格定义可见的注释，并且不应该有范围与它们相交的数据透视表。
1. 要删除空白列，请使用[**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns)方法。

{{% /alert %}}

##  C# 删除空白行的代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## C# 删除空白列的代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
