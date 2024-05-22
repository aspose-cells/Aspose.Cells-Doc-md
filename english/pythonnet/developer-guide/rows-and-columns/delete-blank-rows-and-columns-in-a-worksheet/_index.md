---
title: Delete Blank Rows and Columns in a Worksheet
type: docs
weight: 300
url: /python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: This article describes how to delete blank rows and columns in a worksheet with Aspose.Cells for Python via .NET library.
keywords: Python Excel Library, Python delete Blank Rows, Python remove Blank Rows, Python delete Blank columns, Python remove Blank columns, Python delete or remove blank rows and columns.
---

{{% alert color="primary" %}}

It is possible to delete all blank rows and columns from a worksheet. This is useful when, for example, generating a PDF file from a Microsoft Excel file and want to convert only rows and columns that contain data or related object.

Use the following Aspose.Cells methods to delete empty rows and columns:

1. To delete blank rows, use the [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows) method. Please note, for blank rows that will be deleted, it is not only required that [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) should be true, but also there should be no visible comment defined for any cell in those rows, and no pivot table whose range intersects with them.
1. To delete blank columns, use the [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns) method.

{{% /alert %}}

## C# code to delete Blank Rows

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## C# code to Delete Blank Columns

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
