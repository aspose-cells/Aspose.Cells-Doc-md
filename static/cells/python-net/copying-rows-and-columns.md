##Copying Rows and Columns
This article shows how to Copy Rows and Columns through the Aspose.Cells for Python via .NET API.
## **Introduction**
Sometimes, you need to copy rows and columns in a worksheet without copying the entire worksheet. With Aspose.Cells, it is possible to copy rows and columns within or between workbooks.
When a row (or column) is copied, the data contained in it, including formulas - with updated references - and values, comments, formatting, hidden cells, images, and other drawing objects are copied too.
## **How to Copy Rows and Columns with Microsoft Excel**
1. Select the row or column that you want to copy.
1. To copy rows or columns, click **Copy** on the **Standard** toolbar, or press **CTRL**+**C**.
1. Select a row or column below or to the right of where you want to copy your selection.
1. When you are copying rows or columns, click **Copied Cells** on the **Insert** menu.
If you click **Paste** on the **Standard** toolbar or press **CTRL**+**V** instead of clicking a command on the **Insert** menu, any contents of the destination cells are replaced.
## **How to Paste Rows and Columns using Paste Options with Microsoft Excel**
1. Select the cells that contain the data or other attributes that you want to copy.
1. On the Home tab, click **Copy**.
1. Click the first cell in the area where you want to **paste** what you copied.
1. On the Home tab, click the arrow next to **Paste**, and then select **Paste** Special.
1. Select the **options** you want.
## **How to Copy Rows and Columns Using Aspose.Cells for .NET**
## **How to Copy Single Rows**
Aspose.Cells provides the [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) method of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) class. This method copies all types of data including formulas, values, comments, cell formats, hidden cells, images and other drawing objects from the source row to the destination row.
The [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) method takes the following parameters:
- the source [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) object,
- source row index, and
- destination row index.
Use this method to copy a row within a sheet, or to another sheet. The [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) method works in a similar way to Microsoft Excel. So, for example, you don't need to set the height of the destination row explicitly, that value is copied too.
The following example shows how to copy a row in a worksheet. It uses a template Microsoft Excel file and copies the second row (complete with data, formatting, comments, images and so on) and paste it to the 12th row in the same worksheet.
You can skip the step that gets the source row height using the [**Cells.get_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/get_row_height/#int) method and then sets the destination row height using the [**Cells.set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) method as the [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) method automatically takes care of the row height.
When copying rows, it is important to note related images, charts or other drawing objects as this is the same with Microsoft Excel:
1. If the source row index is 5, the image, chart, etc., is copied if it is contained in the three rows (the starting row index is 4 and the ending row index is 6).
1. The existing images, charts, etc. in the destination row will not be removed.
## **How to Copy Multiple Rows**
You can also copy multiple rows onto a new destination while using the [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int) method which takes an additional parameter of type integer to specify the number of source rows to be copied.
## **How to Copy Columns**
Aspose.Cells provides the [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) method of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) class, this method copies all types of data, including formulas - with updated references - and values, comments, cell formats, hidden cells, images and other drawing objects from the source column to the destination column.
The [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) method takes the following parameters:
- the source [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) object,
- source column index, and
- the destination column index.
Use the [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) method to copy a column within a sheet or to another sheet.
This example copies a column from a worksheet and pastes it into a worksheet in another workbook.
## **How to Copy Multiple Columns**
Similar to [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int) method, the Aspose.Cells APIs also provide the [**Cells.copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/) method in order to copy multiple source columns to a new location.
## **How to Paste Rows and Columns with Paste Options**
Aspose.Cells now provides [**PasteOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions) while using functions [**copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int-aspose.cells.CopyOptions-aspose.cells.PasteOptions) and [**copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/#aspose.cells.Cells-int-int-int-aspose.cells.PasteOptions). It allows to set appropriate paste option similar to Excel.
