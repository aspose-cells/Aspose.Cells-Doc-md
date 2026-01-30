---
title: Delete Blank Rows and Columns in a Worksheet with Go
linktitle: Delete Blank Rows and Columns in a Worksheet
type: docs
weight: 300
url: /gocpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Delete empty rows and columns in a worksheet using Aspose.Cells with Go.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

It is possible to delete all blank rows and columns from a worksheet. This is useful when, for example, generating a PDF file from a Microsoft Excel file and you want to convert only rows and columns that contain data or related objects.

Use the following Aspose.Cells methods to delete empty rows and columns:

1. To delete blank rows, use the [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/gocpp/aspose.cells/cells/deleteblankrows/) method. Please note, for blank rows that will be deleted, it is not only required that [**Row.IsBlank**](https://reference.aspose.com/cells/gocpp/aspose.cells/row/isblank/) should be true, but also that there should be no visible comment defined for any cell in those rows, and no pivot tables whose range intersects with them.
2. To delete blank columns, use the [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/gocpp/aspose.cells/cells/deleteblankcolumns/) method.

{{% /alert %}}

## Go code to delete Blank Rows

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteBlankRowsAndColumnsInAWorksheet01.go" >}}

## Go code to Delete Blank Columns

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteBlankRowsAndColumnsInAWorksheet02.go" >}}

{{< app/cells/assistant language="go" >}}