---
title: 在工作表中删除空行和空列
type: docs
weight: 300
url: /zh/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: 本文介绍了如何使用 Aspose.Cells for Python via .NET 库删除工作表中的空行和列。
keywords: Python Excel Library，Python 删除空行，Python 移除空行，Python 删除空列，Python 移除空列，Python 删除或移除空行和列。
---

{{% alert color="primary" %}}

可以删除工作表中的所有空行和空列。例如，从 Microsoft Excel 文件生成 PDF 文件并且只要转换包含数据或相关对象的行和列时，这很有用。

使用以下Aspose.Cells方法来删除空行和空列:

1. 要删除空行，请使用[**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows)方法。请注意，对于将要被删除的空行，不仅需要[**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/)为true，还必须在这些行中的任何单元格没有可见的注释定义，也不应该和任何数据透视表的范围相交。
1. 要删除空列，请使用[**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns)方法。

{{% /alert %}}

## 删除空行的C#代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## 删除空列的C#代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
