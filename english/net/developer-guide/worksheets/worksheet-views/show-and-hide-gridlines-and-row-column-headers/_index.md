---
title: Show and Hide Gridlines and Row Column Headers
type: docs
weight: 30
url: /net/show-and-hide-gridlines-and-row-column-headers/
description: This article provides sample code for using the C# API or .NET Library to programmatically hide or show gridlines, row and column headers of an Excel worksheet.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supports hiding and showing gridlines of a worksheet, which are visible by default. It also provides control over the visibility of row and column headers of the worksheet.

{{% /alert %}}

## **Show and Hide Gridlines**

All Excel worksheets have gridlines by default. They help delineate cells so that it is easy to enter data into particular cells. Gridlines enable us to view a worksheet as a collection of cells, where each cell is easily identifiable.

### **Controlling the Visibility of the Gridlines**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a **Worksheets** collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of gridlines, use the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class **IsGridlinesVisible** property. **IsGridlinesVisible** is a Boolean property, which means that it can only store a **true** or **false** value.

#### **Making Gridlines Visible**

Make the gridlines visible by setting the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class **IsGridlinesVisible** property to **true**.

#### **Hiding Gridlines**

Hide gridlines by setting the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class **IsGridlinesVisible** property to **false**.

A complete example is given below that demonstrates the use of the **IsGridlinesVisible** property by opening an Excel file (book1.xls), hiding the gridlines on the first worksheet, and saving the modified file as **output.xls**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Show and Hide Row Column Headers**

All worksheets in an Excel file are composed of cells that are arranged in rows and columns. All rows and columns have unique values that are used to identify them and to identify individual cells. For example, rows are numbered – 1, 2, 3, 4, etc. – and columns are ordered alphabetically – A, B, C, D, etc. The row and column values are displayed in the headers. Using Aspose.Cells, developers can control the visibility of these row and column headers.

### **Controlling the Visibility of the Worksheets**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a **Worksheets** collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of row and column headers, use the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class **IsRowColumnHeadersVisible** property. **IsRowColumnHeadersVisible** is a Boolean property, which means that it can only store a **true** or **false** value.

#### **Making Row/Column Headers Visible**

Make row and column headers visible by setting the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class **IsRowColumnHeadersVisible** property to **true**.

#### **Hiding Row/Column Headers**

Hide row and column headers by setting the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class **IsRowColumnHeadersVisible** property to **false**.

A complete example is given below that shows how to use the **IsRowColumnHeadersVisible** property by opening an Excel file (book1.xls), hiding the row and column headers on the first worksheet, and saving the modified file as **output.xls**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

It is also possible to use the **UnhideRows** and **UnhideColumns** methods of the **Cells** class to make multiple rows and columns visible.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
