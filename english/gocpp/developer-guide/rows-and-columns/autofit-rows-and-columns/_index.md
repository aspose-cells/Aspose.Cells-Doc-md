---
title: AutoFit Rows and Columns with Golang via C++
linktitle: AutoFit Rows and Columns
type: docs
weight: 20
url: /go-cpp/autofit-rows-and-columns/
description: This article shows how to autoFit rows, columns, rows of merged cells, and rows in a range of cells using the Aspose.Cells for Go via Go API.
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---

{{% alert color="primary" %}}

Microsoft Excel lets users auto-size the width and height of cells according to their content. This feature is also available through Aspose.Cells, so developers can auto-size the dimensions of a cell at runtime.

{{% /alert %}}

## **Auto Fitting**

Aspose.Cells provides a [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a wide range of methods for managing a worksheet. This article looks at using the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class to auto-fit rows or columns.

### **AutoFit Row - Simple**

The most straightforward approach to auto-sizing the width and height of a row is to call the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class [**AutoFitRow**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitrow_int_int_int/) method. The [**AutoFitRow**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitrow_int_int_int/) method takes a row index (of the row to be resized) as a parameter.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitRowsAndColumns.go" >}}

### **How to AutoFit Row in a Range of Cells**

A row is composed of many columns. Aspose.Cells allows developers to auto-fit a row based on the content in a range of cells within the row by calling an overloaded version of the [**AutoFitRow**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitrow_int_int_int/) method. It takes the following parameters:

- **Row index**, the index of the row about to be auto-fitted.
- **First column index**, the index of the row's first column.
- **Last column index**, the index of the row's last column.

The [**AutoFitRow**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitrow_int_int_int/) method checks the contents of all the columns in the row and then auto-fits the row.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitRowsAndColumns-1.go" >}}

### **How to AutoFit Column in a Range of Cells**

A column is composed of many rows. It is possible to auto-fit a column based on the content in a range of cells in the column by calling an overloaded version of the [**AutoFitColumn**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitcolumn_int_int_int/) method that takes the following parameters:

- **Column index**, the index of the column about to be auto-fitted.
- **First row index**, the index of the column's first row.
- **Last row index**, the index of the column's last row.

The [**AutoFitColumn**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitcolumn_int_int_int/) method checks the contents of all rows in the column and then auto-fits the column.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitRowsAndColumns-2.go" >}}

### **How to AutoFit Rows for Merged Cells**

With Aspose.Cells, it is possible to auto‑fit rows even for cells that have been merged using the [**AutoFitterOptions**](https://reference.aspose.com/cells/go-cpp/autofitteroptions/) API. The [**AutoFitterOptions**](https://reference.aspose.com/cells/go-cpp/autofitteroptions/) class provides the [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/go-cpp/autofitteroptions/getautofitmergedcellstype/) property that can be used to auto‑fit rows for merged cells. [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/go-cpp/autofitteroptions/getautofitmergedcellstype/) accepts the [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/go-cpp/autofitmergedcellstype/) enumeration, which has the following members:

- None: Ignore merged cells.
- FirstLine: Only expands the height of the first row.
- LastLine: Only expands the height of the last row.
- EachLine: Expands the height of each row.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitRowsAndColumns-3.go" >}}

{{% alert color="primary" %}}

You may also try to use the overloaded versions of [**AutoFitRows**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitrows/) and [**AutoFitColumns**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitcolumns/) methods accepting a range of rows/columns and an instance of [**AutoFitterOptions**](https://reference.aspose.com/cells/go-cpp/autofitteroptions/) to auto‑fit the selected rows/columns with your desired [**AutoFitterOptions**](https://reference.aspose.com/cells/go-cpp/autofitteroptions/) accordingly.

The signatures of the aforesaid methods are as follows:

1. `AutoFitRows(int startRow, int endRow, AutoFitterOptions options)`
2. `AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)`

{{% /alert %}}

## **Important to Know**

{{% alert color="primary" %}}

If a cell is merged, then the AutoFit methods will not be applied, which is the same behavior as in Microsoft Excel. You can get around this by using the AutoFilter API. Moreover, if the text in a cell is wrapped, the [**AutoFitColumn**](https://reference.aspose.com/cells/go-cpp/worksheet/autofitcolumn_int_int_int/) method will not be applied either. Another thing you need to know is that the *AutoFit* methods are time‑consuming. So, you should call these methods as infrequently as possible to ensure the efficiency of your application.

{{% /alert %}}

## **Advanced Topics**
- [AutoFit Rows for Merged Cells](/cells/go-cpp/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="go" >}}
