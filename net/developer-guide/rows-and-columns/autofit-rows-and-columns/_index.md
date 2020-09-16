---
title: AutoFit Rows and Columns
type: docs
weight: 20
url: /net/autofit-rows-and-columns/
---

{{% alert color="primary" %}}

Microsoft Excel lets users auto size the width and height of cells according to its content. This feature is also available through Aspose.Cells so developers can auto size the dimensions of a cell at runtime.

{{% /alert %}}

## **Auto Fitting**

Aspose.Cells provides a [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class provides a wide range of properties and methods for managing a worksheet. This article looks at using the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class to autofit rows or columns.

### **AutoFit Row - Simple**

The most straight-forward approach to auto-sizing the width and height of a row is to call the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class [**AutoFitRow**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) method. The [**AutoFitRow**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) method takes a row index (of the row to be resized) as a parameter.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **AutoFit Row in a Range of Cells**

A row is composed of many columns. Aspose.Cells allows developers to auto-fit a row based on the content in a range of cells within the row by calling an overloaded version of the [**AutoFitRow**](apireference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) method. It takes the following parameters:

- **Row index**, the index of the row about to be auto-fitted.
- **First column index**, the index of the row's first column.
- **Last column index**, the index of the row's last column.

The [**AutoFitRow**](apireference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) method checks the contents of all the columns in the row and then auto-fits the row.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **AutoFit Column in a Range of Cells**

A column is composed of many rows. It is possible to auto-fit a column based on the content in a range of cells in the column by calling an overloaded version of [**AutoFitColumn**](https://apireference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) method that takes the following parameters:

- **Column index**, the index of the column about to be auto-fitted.
- **First row index**, the index of the column's first row.
- **Last row index**, the index of the column's last row.

The [**AutoFitColumn**](https://apireference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) method checks the contents of all rows in the column and then auto-fits the column.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **AutoFit Rows for Merged Cells**

With Aspose.Cells it is possible to autofit rows even for cells that have been merged using the [**AutoFitterOptions**](https://apireference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://apireference.aspose.com/cells/net/aspose.cells/autofitteroptions) class provides [**AutoFitMergedCellsType**](https://apireference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) property that can be used to autofit rows for merged cells. [**AutoFitMergedCellsType**](https://apireference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) accepts [**AutoFitMergedCellsType**](https://apireference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) enumerable which has the following members.

- None: Ignore merged cells.
- FirstLine: Only expands the height of the first row.
- LastLine: Only expands the height of the last row.
- EachLine: Only expands the height of each row.

{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

You may also try to use the overloaded versions of [**AutoFitRows**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**AutoFitColumns**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) methods accepting a range of rows/columns and an instance of [**AutoFitterOptions**](https://apireference.aspose.com/cells/net/aspose.cells/autofitteroptions) to auto-fit the selected rows/columns with your desired  [**AutoFitterOptions**](https://apireference.aspose.com/cells/net/aspose.cells/autofitteroptions) accordingly.

The signatures of the aforesaid methods are as follow:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://apireference.aspose.com/cells/net/aspose.cells/autofitteroptions) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://apireference.aspose.com/cells/net/aspose.cells/autofitteroptions) options)

{{% /alert %}}

## **Important to Know**

{{% alert color="primary" %}}

If a cell is merged then the AutoFit methods will not be applied, which is the same behavior as in Microsoft Excel. You can get around this by using the auto filter API. Moreover, if the text in a cell is wrapped, the [**AutoFitColumn**](https://apireference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) method will not be applied either. Another thing you need to know is that the *AutoFit* methods are time-consuming. So, you should call these methods as seldom as possible to ensure the efficiency of your application.

{{% /alert %}}
