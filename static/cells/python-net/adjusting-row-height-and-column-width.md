##Format Rows and Columns
Aspose.Cells for Python via .NET can support change row height or column width, as well as apply formatting on rows or columns.
When working with spreadsheets and adding data to rows or columns, you might need to change the height of rows or width of columns. Sometimes, applying formatting on rows or columns means that the current height or width needs to change to show the data. Normally, users adjust row heights and column widths in a WYSIWYG environment using Microsoft Excel. But, with Aspose.Cells for Python via .NET developers can perform these operations at runtime.
## **Working with Rows**
### **How to Adjust Row Height**
Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection that represents all cells in the worksheet.
The [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection provides several methods to manage rows or columns in a worksheet. Some of these are discussed below in more detail.
### **How to Set the Height of a Row**
It is possible to set the height of a single row by calling the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection's [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) method. The [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) method takes the following parameters as follows:
- **row**, the index of the row that you're changing the height of.
- **height**, the row height to apply on the row.
### **How to Set the Height of All Rows in a Worksheet**
If developers need to set the same row height for all rows in the worksheet, they can do it by using the [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) property of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection.
**Example:**
## **Working with Columns**
### **How to Set the Width of a Column**
Set the width of a column by calling the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection's [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) method. The [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) method takes the following parameters:
- **column**, the index of the column that you're changing the width of.
- **width**, the desired column width.
### **How to Set Column Width in Pixels**
Set the width of a column by calling the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection's [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) method. The [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) method takes the following parameters:
- **column**, the index of the column that you're changing the width of.
- **pixels**, the desired column width in pixels.
### **How to Set the Width of All Columns in a Worksheet**
To set the same column width for all columns in the worksheet, use the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection's [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) property.
## **Advance topics**
- [AutoFit Rows and Columns](https://docs.aspose.com/cells/python-net/autofit-rows-and-columns/)
- [Convert Text to Columns using Aspose.Cells](https://docs.aspose.com/cells/python-net/convert-text-to-columns-using-aspose-cells/)
- [Copying Rows and Columns](https://docs.aspose.com/cells/python-net/copying-rows-and-columns/)
- [Delete Blank Rows and Columns in a Worksheet](https://docs.aspose.com/cells/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Grouping and Ungrouping Rows and Columns](https://docs.aspose.com/cells/python-net/grouping-and-ungrouping-rows-and-columns/)
- [Hiding and Showing Rows and Columns](https://docs.aspose.com/cells/python-net/hiding-and-showing-rows-and-columns/)
- [Insert or Delete Rows in an Excel Worksheet](https://docs.aspose.com/cells/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Inserting and Deleting Rows and Columns of Excel file](https://docs.aspose.com/cells/python-net/inserting-and-deleting-rows-and-columns/)
- [Remove duplicate rows in a Worksheet](https://docs.aspose.com/cells/python-net/remove-duplicate-rows-in-a-worksheet/)
- [Update references in other worksheets while deleting blank columns and rows in a worksheet](https://docs.aspose.com/cells/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
