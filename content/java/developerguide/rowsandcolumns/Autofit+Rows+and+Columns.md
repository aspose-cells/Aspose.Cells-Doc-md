+++
title = "Autofit Rows and Columns" 
description = "" 
weight = 12153 
+++

Aspose.Cells for Java : Autofit Rows and Columns  

# Aspose.Cells for Java : Autofit Rows and Columns



Microsoft Excel provides a good feature to Auto Size the width and height of a cell according to its content. This feature is also available to Aspose.Cells users with the power of auto-sizing the dimensions of a cell at runtime.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Auto Fitting](#AutofitRowsandColumns-AutoFitting)
    *   1.1 [AutoFit Row - Simple](#AutofitRowsandColumns-AutoFitRow-Simple)
    *   1.2 [AutoFit Row in a Range of Cells](#AutofitRowsandColumns-AutoFitRowinaRangeofCells)
    *   1.3 [AutoFit Column - Simple](#AutofitRowsandColumns-AutoFitColumn-Simple)
    *   1.4 [AutoFit Column in a Range of Cells](#AutofitRowsandColumns-AutoFitColumninaRangeofCells)
    *   1.5 [AutoFit Rows for Merged Cells](#AutofitRowsandColumns-AutoFitRowsforMergedCells)
*   2 [Important to Know](#AutofitRowsandColumns-ImportanttoKnow)
{{< /panel >}}
 

### Auto Fitting

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#Worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class provides a wide range of properties and methods for managing a worksheet. This article looks at using the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class to autofit rows or columns.

#### AutoFit Row - Simple

The most straight-forward approach to auto-sizing the width and height of a row is to call the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class' [autoFitRow](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitRow(int)) method. The [autoFitRow](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitRow(int)) method takes a row index (of the row to be resized) as a parameter.

#### AutoFit Row in a Range of Cells

A row is composed of many columns. Aspose.Cells allows developers to auto-fit a row based on the content in a range of cells within the row by calling an overloaded version of the [autoFitRow](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitRow(int,%20int,%20int)) method. It takes the following parameters:

*   **Row index**, the index of the row about to be auto-fitted.
*   **First column index**, the index of the row's first column.
*   **Last column index**, the index of the row's last column.

The [autoFitRow](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitRow(int,%20int,%20int)) method checks the contents of all the columns in the row and then auto-fits the row.

#### AutoFit Column - Simple

The easiest way to auto-size the width and height of a column is to call the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class' [autoFitColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitColumn(int)) method. The [autoFitColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitColumn(int)) method takes the column index (of the column about to be resized) as a parameter.

#### AutoFit Column in a Range of Cells

A column is composed of many rows. It is possible to auto-fit a column based on the content in a range of cells in the column by calling an overloaded version of [autoFitColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitColumn(int,%20int,%20int)) method that takes the following parameters:

*   **Column index**, represents the index of the column whose contents need to auto-fit
*   **First row index**, represents the index of the first row of the column
*   **Last row index**, represents the index of the last row of the column

The [autoFitColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitColumn(int,%20int,%20int)) method checks the contents of all rows in the column and then auto-fits the column.

#### AutoFit Rows for Merged Cells

With Aspose.Cells it is possible to autofit rows even for cells that have been merged using the [AutoFitterOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/AutoFitterOptions) class provides [AutoFitMergedCellsType](https://apireference.aspose.com/java/cells/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) property that can be used to autofit rows for merged cells. [AutoFitMergedCellsType](https://apireference.aspose.com/java/cells/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)accepts [AutoFitMergedCellsType](https://apireference.aspose.com/java/cells/com.aspose.cells/AutoFitMergedCellsType) enumerable which has the following members.

*   [NONE](https://apireference.aspose.com/java/cells/com.aspose.cells/autofitmergedcellstype#NONE): Ignore merged cells.
*   [FIRST\_LINE](https://apireference.aspose.com/java/cells/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Only expands the height of the first row.
*   [LAST\_LINE](https://apireference.aspose.com/java/cells/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Only expands the height of the last row.
*   [EACH\_LINE](https://apireference.aspose.com/java/cells/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Only expands the height of each row.

You may also use the overloaded versions of [autoFitRows](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitRows()) & [autoFitColumns](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitColumns()) methods accepting a range of rows/columns and an instance of [AutoFitterOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/AutoFitterOptions) to auto-fit the selected rows/columns with the desired [AutoFitterOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/AutoFitterOptions) accordingly.

The signatures of aforesaid methods are as follow:

1.  autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/AutoFitterOptions) options)
2.  autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/AutoFitterOptions) options)

### Important to Know

If a cell is merged then the *AutoFit *methods will not be applied, which is the same behavior as in Microsoft Excel. Moreover, if the text in a cell is wrapped, the [autoFitColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#autoFitColumn(int)) method will not be applied either. Another thing you need to know is that the *AutoFit *methods are time-consuming. So, you should call these methods as seldom as possible to ensure the efficiency of your application.

