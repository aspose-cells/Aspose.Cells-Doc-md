##Adjusting Row Height and Column Width
When working with spreadsheets and adding data to rows or columns, you might need to change the height of rows or the width of columns. Sometimes, applying formatting on rows or columns means that the current height or width needs to change to show the data. Normally, users adjust row heights and column widths in a WYSIWYG environment using Microsoft Excel. But, with Aspose.Cells developers can perform these operations at runtime.
## **Working with Rows**
### **Adjusting Row Height**
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection that represents all cells in the worksheet. The [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection provides several methods to manage rows or columns in a worksheet. Some of these are discussed below in more detail.
#### **Setting the Height of a Row**
It is possible to set the height of a single row by calling the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection's [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) method. The [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) method takes the following parameters as follows:
- **Row index**, the index of the row that you're changing the height of.
- **Row height**, the row height to apply on the row.
#### **Setting the Height of All Rows in a Worksheet**
If developers need to set the same row height for all rows in the worksheet, they can do it by using the [SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/) method of the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection.
## **Working with Columns**
### **Setting the Width of a Column**
Set the width of a column by calling the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection's [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) method. The [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) method takes the following parameters:
- **Column index**, the index of the column that you're changing the width of.
- **Column width**, the desired column width.
### **Setting the Width of All Columns in a Worksheet**
To set the same column width for all columns in the worksheet, use the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection's [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) method.
