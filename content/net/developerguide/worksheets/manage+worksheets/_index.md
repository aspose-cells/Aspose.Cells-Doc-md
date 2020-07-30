---
title : "Manage Worksheets" 
description : "" 
weight : 12145 
toc : false
type: docs
url: /net/developerguide/worksheets/manage+worksheets/
---

# Aspose.Cells for .NET : Manage Worksheets


Developers can easily create and manage worksheets in Microsoft Excel files programmatically using Aspose.Cells' flexible API. This topic describes approaches for adding and removing worksheets in Microsoft Excel files.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding Worksheets to a New Excel File](#adding-worksheets-to-a-new-excel-file)
*   2 [Adding Worksheets to a Designer Spreadsheet](#adding-worksheets-to-a-designer-spreadsheet)
*   3 [Accessing Worksheets using Sheet Name](#accessing-worksheets-using-sheet-name)
*   4 [Removing Worksheets using Sheet Name](#removing-worksheets-using-sheet-name)
*   5 [Removing Worksheets using Sheet Index](#removing-worksheets-using-sheet-index)
{{< /panel >}}
 

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents an Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a wide range of properties and methods for managing worksheets.

## Adding Worksheets to a New Excel File

To create a new Excel file programmatically:

1.  Create an object of the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class.
2.  Call the [Add](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection/methods/add) method of the [WorksheetCollection](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection) class. An empty worksheet is added to the Excel file automatically. It can be referenced by passing the sheet index of the new worksheet to the [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection.
3.  Obtain a worksheet reference.
4.  Perform work on the worksheets.
5.  Save the new Excel file with new worksheets by calling the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class' [Save](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/save/index) method.

## Adding Worksheets to a Designer Spreadsheet

The process of adding worksheets to a designer spreadsheet is the same as that of adding a new worksheet, except that the Excel file already exists so should be opened before worksheets are added. A designer spreadsheet can be opened by the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class.

## Accessing Worksheets using Sheet Name

Access any worksheet by specifying its name or index.

## Removing Worksheets using Sheet Name

To remove worksheets from a file, call the [RemoveAt](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection/methods/removeat/index) method of [WorksheetCollection](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection) class. Pass the sheet name to the [RemoveAt](https://apireference.aspose.com/net/cells/aspose.cells.worksheetcollection/removeat/methods/1) method to remove a specific worksheet.

## Removing Worksheets using Sheet Index

Removing worksheets by name works well when the name of the worksheet is known. If you don't know the worksheet's name, use an overloaded version of the [RemoveAt](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection/methods/removeat) method that takes the sheet index of the worksheet instead of its sheet name.

