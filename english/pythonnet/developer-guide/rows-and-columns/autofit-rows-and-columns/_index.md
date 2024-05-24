---
title: AutoFit Rows and Columns
type: docs
weight: 20
url: /python-net/autofit-rows-and-columns/
description: This article shows how to autoFit rows, columns, rows of merged cells and row in a range of cells by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Autofit rows, Python autofit columns, Python autofit row in a range of cells, Python autofit rows of merged cells.
---

{{% alert color="primary" %}}

Microsoft Excel lets users auto size the width and height of cells according to its content. This feature is also available through Aspose.Cells for Python via .NET so developers can auto size the dimensions of a cell at runtime.

{{% /alert %}}

## **Auto Fitting**

Aspose.Cells for Python via .NET provides a [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a wide range of properties and methods for managing a worksheet. This article looks at using the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class to autofit rows or columns.

### **AutoFit Row - Simple**

The most straight-forward approach to auto-sizing the width and height of a row is to call the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) method. The [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) method takes a row index (of the row to be resized) as a parameter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **How to AutoFit Row in a Range of Cells**

A row is composed of many columns. Aspose.Cells for Python via .NET allows developers to auto-fit a row based on the content in a range of cells within the row by calling an overloaded version of the [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) method. It takes the following parameters:

- **Row index**, the index of the row about to be auto-fitted.
- **First column index**, the index of the row's first column.
- **Last column index**, the index of the row's last column.

The [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) method checks the contents of all the columns in the row and then auto-fits the row.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **How to AutoFit Column in a Range of Cells**

A column is composed of many rows. It is possible to auto-fit a column based on the content in a range of cells in the column by calling an overloaded version of [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) method that takes the following parameters:

- **Column index**, the index of the column about to be auto-fitted.
- **First row index**, the index of the column's first row.
- **Last row index**, the index of the column's last row.

The [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) method checks the contents of all rows in the column and then auto-fits the column.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **How to AutoFit Rows for Merged Cells**

With Aspose.Cells for Python via .NET it is possible to autofit rows even for cells that have been merged using the [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) class provides [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) property that can be used to autofit rows for merged cells. [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) accepts [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype) enumerable which has the following members.

- NONE: Ignore merged cells.
- FIRST_LINE: Only expands the height of the first row.
- LAST_LINE: Only expands the height of the last row.
- EACH_LINE: Only expands the height of each row.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

You may also try to use the overloaded versions of [**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) & [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions) methods accepting a range of rows/columns and an instance of [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) to auto-fit the selected rows/columns with your desired  [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) accordingly.

The signatures of the aforesaid methods are as follow:

1. auto_fit_rows(start_row, end_row, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) options)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Important to Know**

{{% alert color="primary" %}}

If a cell is merged then the AutoFit methods will not be applied, which is the same behavior as in Microsoft Excel. You can get around this by using the auto filter API. Moreover, if the text in a cell is wrapped, the [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) method will not be applied either. Another thing you need to know is that the *AutoFit* methods are time-consuming. So, you should call these methods as seldom as possible to ensure the efficiency of your application.

{{% /alert %}}

## **Advance topics**
- [AutoFit Rows for Merged Cells](/cells/python-net/autofit-rows-for-merged-cells/)
