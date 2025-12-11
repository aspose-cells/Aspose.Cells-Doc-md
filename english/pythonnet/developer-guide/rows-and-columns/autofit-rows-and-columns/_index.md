---
title: AutoFit Rows and Columns
type: docs
weight: 20
url: /python-net/autofit-rows-and-columns/
description: This article shows how to auto-fit rows, columns, rows of merged cells, and rows in a range of cells using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Autofit rows, Python autofit columns, Python autofit rows in a range of cells, Python autofit rows of merged cells.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel lets users auto-size the width and height of cells according to their content. This feature is also available through Aspose.Cells for Python via .NET so developers can auto-size the dimensions of a cell at runtime.

{{% /alert %}}

## **Auto Fitting**

Aspose.Cells for Python via .NET provides a **[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)** class that represents a Microsoft Excel file. The **[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)** class contains a **[Worksheets](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)** collection that allows access to each worksheet in an Excel file. A worksheet is represented by the **[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)** class. The **[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)** class provides a wide range of properties and methods for managing a worksheet. This article looks at using the **[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)** class to autofit rows or columns.

### **AutoFit Row - Simple**

The most straightforward approach to auto-sizing the height of a row is to call the **[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)** class **[auto_fit_row](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int)** method. The **auto_fit_row** method takes a row index (the row to be resized) as a parameter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **How to AutoFit Row in a Range of Cells**

A row is composed of many columns. Aspose.Cells for Python via .NET allows developers to auto-fit a row based on the content in a range of cells within the row by calling an overloaded version of the **[auto_fit_row](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int)** method. It takes the following parameters:

- **Row index** – the index of the row to be auto-fitted.
- **First column index** – the index of the row's first column.
- **Last column index** – the index of the row's last column.

The **auto_fit_row** method checks the contents of all the columns in the row and then auto-fits the row.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **How to AutoFit Column in a Range of Cells**

A column is composed of many rows. It is possible to auto-fit a column based on the content in a range of cells in the column by calling an overloaded version of **[auto_fit_column](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int)** that takes the following parameters:

- **Column index** – the index of the column to be auto-fitted.
- **First row index** – the index of the column's first row.
- **Last row index** – the index of the column's last row.

The **auto_fit_column** method checks the contents of all rows in the column and then auto-fits the column.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **How to AutoFit Rows for Merged Cells**

With Aspose.Cells for Python via .NET it is possible to autofit rows even for cells that have been merged using the **[AutoFitterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions)** API. The **AutoFitterOptions** class provides the **auto_fit_merged_cells_type** property that can be used to autofit rows for merged cells. **auto_fit_merged_cells_type** accepts the **[AutoFitMergedCellsType](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype)** enumeration, which has the following members:

- **NONE** – Ignore merged cells.
- **FIRST_LINE** – Only expands the height of the first row.
- **LAST_LINE** – Only expands the height of the last row.
- **EACH_LINE** – Expands the height of each row.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

You may also try using the overloaded versions of **[auto_fit_rows](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions)** and **[auto_fit_columns](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions)** that accept a range of rows/columns and an instance of **AutoFitterOptions** to auto-fit the selected rows/columns with your desired **AutoFitterOptions** accordingly.

The signatures of the aforesaid methods are as follows:

1. `auto_fit_rows(start_row, end_row, options)`
2. `auto_fit_columns(first_column, last_column, options)`

{{% /alert %}}

## **Important to Know**

{{% alert color="primary" %}}

If a cell is merged, the AutoFit methods will not be applied, which is the same behavior as in Microsoft Excel. You can work around this by using the **AutoFilter** API. Moreover, if the text in a cell is wrapped, the **auto_fit_column** method will not be applied either. Another thing you need to know is that the AutoFit methods are time‑consuming, so you should call these methods as rarely as possible to ensure the efficiency of your application.

{{% /alert %}}

## **Advanced topics**
- [AutoFit Rows for Merged Cells](/cells/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
