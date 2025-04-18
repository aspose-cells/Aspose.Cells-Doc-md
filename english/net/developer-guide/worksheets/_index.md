---
title: Manage Worksheets
type: docs
weight: 90
url: /net/manage-worksheets/
description: Add worksheet, remove worksheet and active Sheet using Aspose.Cells.
---



{{% alert color="primary" %}}

Developers can easily create and manage worksheets in Microsoft Excel files programmatically using Aspose.Cells' flexible API. This topic describes approaches for adding and removing worksheets in Microsoft Excel files.

{{% /alert %}}

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a wide range of properties and methods for managing worksheets.

## **Adding Worksheets to a New Excel File**
To create a new Excel file programmatically:

1. Create an object of the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class.
1. Call the [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) method of the [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) class. An empty worksheet is added to the Excel file automatically. It can be referenced by passing the sheet index of the new worksheet to the [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection.
1. Obtain a worksheet reference.
1. Perform work on the worksheets.
1. Save the new Excel file with new worksheets by calling the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class' [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Accessing Worksheets using Sheet Name**

Access any worksheet by specifying its name or index.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Removing Worksheets using Sheet Index**
Removing worksheets by name works well when the name of the worksheet is known. If you don't know the worksheet's name, use an overloaded version of the [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) method that takes the sheet index of the worksheet instead of its sheet name.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}