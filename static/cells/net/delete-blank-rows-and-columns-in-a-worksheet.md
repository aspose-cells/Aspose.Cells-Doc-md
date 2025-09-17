##Delete Blank Rows and Columns in a Worksheet
It is possible to delete all blank rows and columns from a worksheet. This is useful when, for example, generating a PDF file from a Microsoft Excel file and want to convert only rows and columns that contain data or related object.
Use the following Aspose.Cells methods to delete empty rows and columns:
1. To delete blank rows, use the [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) method. Please note, for blank rows that will be deleted, it is not only required that [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) should be true, but also there should be no visible comment defined for any cell in those rows, and no pivot table whose range intersects with them.
1. To delete blank columns, use the [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) method.
## C# code to delete Blank Rows
## C# code to Delete Blank Columns
