---
title: Delete Blank Rows and Columns in a Worksheet
type: docs
weight: 300
url: /net/delete-blank-rows-and-columns-in-a-worksheet/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

It is possible to delete all blank rows and columns from a worksheet. This is useful when, for example, generating a PDF file from a Microsoft Excel file and want to convert only rows and columns that contain data or related object.

Use the following Aspose.Cells methods to delete empty rows and columns:

1. To delete blank rows, use the [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) method. Please note, for blank rows that will be deleted, it is not only required that [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) should be true, but also there should be no visible comment defined for any cell in those rows, and no pivot table whose range intersects with them.
1. To delete blank columns, use the [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) method.

{{% /alert %}}

## C# code to delete Blank Rows

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## C# code to Delete Blank Columns

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
