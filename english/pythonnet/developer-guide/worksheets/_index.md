---
title: Manage Worksheets of Microsoft Excel files.
linktitle: Worksheets
type: docs
weight: 90
url: /python-net/manage-worksheets/
description: This article shows how to Manage Worksheets of Microsoft Excel files by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Manage Worksheets of Microsoft Excel files, Add worksheet in Python, Python remove worksheet, Python How to Add Worksheets to a New Excel File, Python How to Add Worksheets to a Designer Spreadsheet, Python How to Access Worksheets using Sheet Name, Python How to Remove Worksheets using Sheet Name, Python How to Remove Worksheets using Sheet Index, Python How to Activate Sheets and Making a Cell Active.
---


{{% alert color="primary" %}}

Developers can easily create and manage worksheets in Microsoft Excel files programmatically using Aspose.Cells' flexible API. This topic describes approaches for adding and removing worksheets in Microsoft Excel files.

{{% /alert %}}

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a wide range of properties and methods for managing worksheets.

## **How to Add Worksheets to a New Excel File**

To create a new Excel file programmatically:

1. Create an object of the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class.
1. Call the [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) method of the [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) class. An empty worksheet is added to the Excel file automatically. It can be referenced by passing the sheet index of the new worksheet to the [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) collection.
1. Obtain a worksheet reference.
1. Perform work on the worksheets.
1. Save the new Excel file with new worksheets by calling the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) method.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **How to Add Worksheets to a Designer Spreadsheet**

The process of adding worksheets to a designer spreadsheet is the same as that of adding a new worksheet, except that the Excel file already exists so should be opened before worksheets are added. A designer spreadsheet can be opened by the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **How to Access Worksheets using Sheet Name**

Access any worksheet by specifying its name or index.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **How to Remove Worksheets using Sheet Name**

To remove worksheets from a file, call the [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) method of [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) class. Pass the sheet name to the [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) method to remove a specific worksheet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **How to Remove Worksheets using Sheet Index**

Removing worksheets by name works well when the name of the worksheet is known. If you don't know the worksheet's name, use the [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int) method that takes the sheet index of the worksheet instead of its sheet name.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **How to Activate Sheets and Make an Active Cell in the Worksheet**

Sometimes, you need a specific worksheet to be active and displayed when a user opens a Microsoft Excel file in Excel. Similarly, you might want to activate a specific cell and set the scrollbars to show the active cell.
Aspose.Cells is capable of doing all these tasks.

An **active sheet** is a sheet you're working on: the active sheet's name on the tab is bold by default.

An **active cell** is a selected cell, the cell into which data is entered when you begin typing. Only one cell is active at a time. The active cell is highlighted by a heavy border.

### **How to Activate Sheets and Make a Cell Active**

Aspose.Cells provides specific API calls for activating a sheet and a cell. For Example, the [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) property is useful for setting the active sheet in a workbook.
Similarly, [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) property is used to set and get an active cell in the worksheet.

To make sure that the horizontal or vertical scrollbars are at the row and column index position you want to show specific data, use the [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) and [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/) properties.

The following example shows how to activate a worksheet and make an active cell in it. In the generated output, the scrollbars will be scrolled to make the 2nd row and 2nd column as their first visible row and column.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

