---
title: Manage Worksheets
type: docs
weight: 20
url: /cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

Developers can easily create and manage worksheets in Microsoft Excel files programmatically using Aspose.Cells flexible API. This topic describes approaches for adding and removing worksheets in Microsoft Excel files.

{{% /alert %}} 

Aspose.Cells provides a class [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) that represents an Excel file. The [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) class contains a [Worksheets](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class. The [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class provides a wide range of methods for managing worksheets.
## **Adding Worksheets to a New Excel File**
To create a new Excel file programmatically:

1. Create an object of the [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class.
1. Call the [Add](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/#aa2bb166f57a4d8eba8e25ce1f99d0c55) method of the [IWorksheetCollection](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/) collection. An empty worksheet is added to the Excel file automatically. It can be referenced by passing the sheet index of the new worksheet to the [IWorksheetCollection](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/) collection.
1. Obtain a worksheet reference.
1. Perform work on the worksheets.
1. Save the new Excel file with new worksheets by calling the [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) class [Save](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/#a77072cfb929787df9ad1f38b02f58349) method.



{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **Accessing Worksheets using Sheet Index**
The following sample code shows how to access or get any worksheet by specifying its index.

{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **Removing Worksheets using Sheet Index**
Removing worksheets by name works well when the name of the worksheet is known. If you don't know the worksheet's name, use an overloaded version of the [RemoveAt](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/#addabcc7d7d76874694018fb3ba37b72c) method that takes the sheet index of the worksheet instead of its sheet name.

{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
