---
title: Show and Hide Gridlines and Row Column Headers
type: docs
weight: 30
url: /python-net/show-and-hide-gridlines-and-row-column-headers/
description: This article provides sample code for using the Aspose.Cells for Python via .NET API to programmatically hide or show gridlines, row and column headers of an Excel worksheet.
keywords: Python Excel Library, Python Show and Hide Gridlines, How to Show and Hide Row Column Headers in Python, How to Show and Hide Gridlines and Row Column Headers in Python.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET supports hiding and showing Gridlines of the worksheet which are visible by default. It also provides controlling visibility of Row Column Headers of the worksheet.

{{% /alert %}}

## **Show and Hide Gridlines**

All Excel worksheets have gridlines by default. They help delineate cells so that it is easy to enter data into particular cells. Gridlines enable us to view a worksheet as a collection of cells, where each cell is easily identifiable.

### **Controlling the Visibility of the Gridlines**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of gridlines, use the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) class [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) property. [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) is a Boolean property, which means that it can only store a **true** or **false** value.

#### **Making Gridlines Visible**

Make the gridlines visible by setting the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) property to **true**.

#### **Hiding Gridlines**

Hide gridlines by setting the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) property to **false**.

A complete example is given below that demonstrates the use of the [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) property by opening an excel file(book1.xls), hiding the gridlines on the first worksheet and saving the modified file as output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Show and Hide Row Column Headers**

All worksheets in an Excel file are composed of cells that are arranged in rows and columns. All rows and columns have unique values that are used to identify them and to identify individual cells. For example, rows are numbered – 1, 2, 3, 4, etc. – and columns are ordered alphabetically – A, B, C, D, etc. The row and column values are displayed in the headers. Using Aspose.Cells for Python via .NET, developers can control the visibility of these row and column headers.

### **Controlling the Visibility of the Worksheets**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of row and column headers, use the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) class [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) property. [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) is a Boolean property, which means that it can only store a **true** or **false** value.

#### **Making Row/Column Headers Visible**

Make row and column headers visible by setting the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) property to **true**.

#### **Hiding Row/Column Headers**

Hide row and column headers by setting the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) property to **false**.

A complete example is given below that shows how to use the [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) property by opening an excel file(book1.xls), hiding the row and column headers on the first worksheet and saving the modified file as output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

It is also possible to use the [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) and [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) methods of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) class to make multiple rows and columns visible.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}