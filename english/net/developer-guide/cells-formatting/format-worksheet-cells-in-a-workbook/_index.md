---
title: Format Worksheet Cells in a Workbook
description: Aspose.Cells is a .NET library for working with spreadsheet files. It supports formatting worksheet cells in workbooks, allowing users to customize the appearance and style of the cells. This article will introduce how to format worksheet cells using the Aspose.Cells library.
keywords: Aspose.Cells, Workbook, Worksheet, Cell, Formatting, Appearance, Style
type: docs
weight: 2000
url: /net/format-worksheet-cells-in-a-workbook/
---

{{% alert color="primary" %}}

This article shows how to:

1. Use styles to quickly format data.
1. Format cells in rows and columns.
1. Use borders and colors to emphasize data.
1. Apply number formats to emphasize data.
1. Use fonts and attributes to highlight data.
1. Format data in a named range.
1. Change data alignment and orientation.
1. Set row height and column width.

The example project performs all of these tasks and provides developers with a detailed description of how to create a workbook, add data into and apply formatting using [Aspose.Cells](https://products.aspose.com/cells/net/).

{{% /alert %}}

## **Data Formatting**

Formatting is used to distinguish between different types of information and to display data clearly.

A format represents a style and is defined as a set of characteristics, such as fonts and font sizes, number formats, cell borders, cell shading, indentation, alignment and text orientation. Borders provide further ways to highlight information. A border is a line drawn around a cell or a group of cells.

Number formats also make data more meaningful. By applying different number formats, you can change the appearance of numbers without changing the number behind the appearance.

Aspose.Cells provides lets you draw borders around cells and ranges easily. It also lets you apply fonts and shade cells. The component is efficient enough that you can format a complete row or column, set alignments, wrap and rotate text in cells. Aspose.Cells further supports all number formats supported by Microsoft Excel.

This article shows how to create a console application in Visual Studio.Net that generates an annual sales report. The workbook is created from scratch, then data is inserted and the worksheet is formatted. We show how to create a simple console application which creates an Excel workbook (you can also use a template file), insert sales data into the first worksheet, format the data and save an Excel file.

### **Process**

Below are the steps involved how to create a spreadsheet and format different cells in different rows and columns of a worksheet.

1. Download and install Aspose.Cells:
   1. [Download](https://downloads.aspose.com/cells/net) Aspose.Cells for .NET.
   1. Install it on your development computer.
1. Create a project and add references:
   1. Start Visual Studio.Net.
   1. Create a new console application.
   1. Add a reference to Aspose.Cells, for example …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Add the following code to the project:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FormatWorksheetCells-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}