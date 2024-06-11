---
title: 在工作表中删除空白行和列
type: docs
weight: 300
url: /zh/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: 本文描述了如何使用 Aspose.Cells for Python 通过 .NET 库删除工作表中的空行和列。
keywords: Python Excel库，Python删除空行，Python删除空列，Python删除空白行和列，Python删除或移除空白行和列。
---

{{% alert color="primary" %}}

可以从工作表中删除所有空白行和列。例如，从 Microsoft Excel 文件生成 PDF 文件并且只希望转换包含数据或相关对象的行和列时，这很有用。

使用以下 Aspose.Cells 方法删除空白行和列：

1. 要删除空白行，请使用 [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows) 方法。请注意，对于将要删除的空白行，不仅需要 [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) 为 true，而且这些行中的任何单元格都不能定义可见注释，也不能有与它们交叉的数据透视表。
1. 要删除空白列，请使用 [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns) 方法。

{{% /alert %}}

## 用于删除空白行的 C# 代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## 用于删除空白列的 C# 代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
