---
title: 在工作表中删除空行和空列
type: docs
weight: 300
url: /zh/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

可以删除工作表中的所有空行和空列。例如，从 Microsoft Excel 文件生成 PDF 文件并且只要转换包含数据或相关对象的行和列时，这很有用。

使用以下Aspose.Cells方法来删除空行和空列:

1. 要删除空行，请使用[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows)方法。请注意，对于将要被删除的空行，不仅需要[**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/)为true，还必须在这些行中的任何单元格没有可见的注释定义，也不应该和任何数据透视表的范围相交。
1. 要删除空列，请使用[**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns)方法。

{{% /alert %}}

## 删除空行的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## 删除空列的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
