##Adjusting Row Height and Column Width
When working with spreadsheets and adding data to rows or columns, you might need to change the height of rows or width of columns. Sometimes, applying formatting to rows or columns means that the current height or width needs to change to show the data. Normally, users adjust row heights and column widths in a WYSIWYG environment using Microsoft Excel. But, with Aspose.Cells developers can perform these operations at runtime. Indexes of rows and columns will start from 0.
## **Working with Rows**
### **Adjusting Row Height**
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection that represents all cells in the worksheet.
The [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection provides several methods to manage rows or columns in a worksheet. Some of these are discussed below in more detail.
### **Setting the Row Height**
It is possible to set the height of a single row by calling the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection's [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight-int-double-) method. The [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight-int-double-) method takes the following parameters:
- **Row index**, the index of the row that you're changing the height of.
- **Row height**, the row height to apply on the row.
### **Setting the Height of All Rows**
To set the same row height for all rows in a worksheet, use the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection's [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight) method.
## **Working with Columns**
### **Setting the Width of a Column**
Set the width of a column by calling the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection's [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth-int-double-) method. The [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth-int-double-) method takes the following parameters:
- **Column index**, the index of the column that you're changing the width of.
- **Column width**, the desired column width.
### **Setting the Width of All Columns**
To set the same column width for all columns in a worksheet, use the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection's [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth) method.
