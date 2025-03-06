---
title: Autofit Rows and Columns
type: docs
weight: 20
url: /java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel provides a good feature to Auto Size the width and height of a cell according to its content. This feature is also available to Aspose.Cells users with the power of auto-sizing the dimensions of a cell at runtime.

{{% /alert %}} 
## **Auto Fitting**
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a wide range of properties and methods for managing a worksheet. This article looks at using the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class to autofit rows or columns.
### **AutoFit Row - Simple**
The most straight-forward approach to auto-sizing the width and height of a row is to call the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class' [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) method. The [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) method takes a row index (of the row to be resized) as a parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit Row in a Range of Cells**
A row is composed of many columns. Aspose.Cells allows developers to auto-fit a row based on the content in a range of cells within the row by calling an overloaded version of the [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) method. It takes the following parameters:

- **Row index**, the index of the row about to be auto-fitted.
- **First column index**, the index of the row's first column.
- **Last column index**, the index of the row's last column.

The [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) method checks the contents of all the columns in the row and then auto-fits the row.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **AutoFit Column - Simple**
The easiest way to auto-size the width and height of a column is to call the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class' [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) method. The [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) method takes the column index (of the column about to be resized) as a parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit Column in a Range of Cells**
A column is composed of many rows. It is possible to auto-fit a column based on the content in a range of cells in the column by calling an overloaded version of [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) method that takes the following parameters:

- **Column index**, represents the index of the column whose contents need to auto-fit
- **First row index**, represents the index of the first row of the column
- **Last row index**, represents the index of the last row of the column

The [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) method checks the contents of all rows in the column and then auto-fits the column.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **AutoFit Rows for Merged Cells**
With Aspose.Cells it is possible to autofit rows even for cells that have been merged using the [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) class provides [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) property that can be used to autofit rows for merged cells. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) accepts [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) enumerable which has the following members.

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Ignore merged cells.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE): Only expands the height of the first row.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE): Only expands the height of the last row.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE): Only expands the height of each row.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

You may also use the overloaded versions of [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--) methods accepting a range of rows/columns and an instance of [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) to auto-fit the selected rows/columns with the desired [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) accordingly.

The signatures of aforesaid methods are as follow:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Important to Know**
{{% alert color="primary" %}} 

If a cell is merged then the *AutoFit* methods will not be applied, which is the same behavior as in Microsoft Excel. Moreover, if the text in a cell is wrapped, the [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) method will not be applied either. Another thing you need to know is that the *AutoFit* methods are time-consuming. So, you should call these methods as seldom as possible to ensure the efficiency of your application.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}