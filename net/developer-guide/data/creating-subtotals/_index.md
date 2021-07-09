---
title: Creating Subtotals
type: docs
weight: 80
url: /net/creating-subtotals/
---

{{% alert color="primary" %}}

You can automatically create subtotals for any repeating values in a spreadsheet. Aspose.Cells provides API features that help you add subtotals to spreadsheets programmatically.

{{% /alert %}}

## **Using Microsoft Excel**

To add subtotals in Microsoft Excel:

1. Create a simple data list in the first worksheet of the workbook (as shown in the figure below) and save the file as Book1.xls.
1. Select any cell within your list.
1. From the **Data** menu, select **Subtotals**. The Subtotals dialog will be displayed. Define what function to use and where to place the subtotals.

## **Using the Aspose.Cells API**

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class. The class provides a wide range of properties and methods for managing worksheets and other objects. Each worksheet consists of a [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/cells) collection. To add subtotals to a worksheet, use the [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/cells) class' [**Subtotal**](https://apireference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) method. Provide parameter values to the method to specify how the subtotal should be calculated and placed.

In the examples below, we have added subtotals to the first worksheet of the template file (Book1.xls) using the Aspose.Cells API. When the code is executed, a worksheet with subtotals is created.

The code snippets that follow show how to add subtotals to a worksheet with Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}
