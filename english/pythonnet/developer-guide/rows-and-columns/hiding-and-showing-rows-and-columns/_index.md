---
title: Hiding and Showing Rows and Columns
type: docs
weight: 60
url: /python-net/hiding-and-showing-rows-and-columns/
description: This article shows how to Hide and Show Rows and Columns by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Aspose.Cells Python Hide and Show Rows, Python Hide and Show Columns, Python Hide Rows and Columns, Python Show Rows and Columns.
---

{{% alert color="primary" %}}

Sometimes, it makes sense to hide certain rows or columns in a worksheet and display them later. Microsoft Excel provides this feature and so does Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Controlling the Visibility of Rows and Columns**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection that represents all cells in the worksheet. The [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

## **How to Hide Rows and Columns**

Developers can hide a row or column by calling the [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) and [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) methods of the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection respectively. Both methods take the row and column index as a parameter to hide the specific row or column.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

It is also possible to hide a row or column by setting the row height or column width to 0 respectively.

{{% /alert %}}

## **How to Show Rows and Columns**

Developers can show any hidden row or column by calling the [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) and [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) methods of the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection respectively. Both methods take two parameters:

- **Row or column index** - the index of a row or column that is used to show the specific row or column.
- **Row height or column width** - the row height or column width assigned to the row or column after unhiding.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

While making a hidden column visible, if you need to restore it to previously assigned width or to its original width, please unhide the column with a negative width. For example: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **How to Hide Multiple Rows and Columns**

Developers can hide multiple rows or columns at once by calling the [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) and [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) methods of the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

It is also possible to use the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) class' [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/) and [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/) methods to make multiple rows and columns visible.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}