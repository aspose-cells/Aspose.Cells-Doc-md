##Manage Worksheets of Microsoft Excel files.
Add worksheet, remove worksheet and active Sheet using Aspose.Cells.
Developers can easily create and manage worksheets in Microsoft Excel files programmatically using Aspose.Cells' flexible API. This topic describes approaches for adding and removing worksheets in Microsoft Excel files.
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file.
A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a wide range of properties and methods for managing worksheets.
## **Adding Worksheets to a New Excel File**
To create a new Excel file programmatically:
1. Create an object of the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class.
1. Call the [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) method of the [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) class. An empty worksheet is added to the Excel file automatically. It can be referenced by passing the sheet index of the new worksheet to the [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection.
1. Obtain a worksheet reference.
1. Perform work on the worksheets.
1. Save the new Excel file with new worksheets by calling the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class' [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method.
## **Adding Worksheets to a Designer Spreadsheet**
The process of adding worksheets to a designer spreadsheet is the same as that of adding a new worksheet, except that the Excel file already exists so should be opened before worksheets are added. A designer spreadsheet can be opened by the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class.
## **Accessing Worksheets using Sheet Name**
Access any worksheet by specifying its name or index.
## **Removing Worksheets using Sheet Name**
To remove worksheets from a file, call the [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) method of [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) class. Pass the sheet name to the [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) method to remove a specific worksheet.
## **Removing Worksheets using Sheet Index**
Removing worksheets by name works well when the name of the worksheet is known. If you don't know the worksheet's name, use an overloaded version of the [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) method that takes the sheet index of the worksheet instead of its sheet name.
## **Activating Sheets and Making an Active Cell in the Worksheet**
Sometimes, you need a specific worksheet to be active and displayed when a user opens a Microsoft Excel file in Excel. Similarly, you might want to activate a specific cell and set the scrollbars to show the active cell.
Aspose.Cells is capable of doing all these tasks.
An **active sheet** is a sheet you're working on: the active sheet's name on the tab is bold by default.
An **active cell** is a selected cell, the cell into which data is entered when you begin typing. Only one cell is active at a time. The active cell is highlighted by a heavy border.
### **Activating Sheets and Making a Cell Active**
Aspose.Cells provides specific API calls for activating a sheet and a cell. For Example, the [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) property is useful for setting the active sheet in a workbook.
Similarly, [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) property is used to set and get an active cell in the worksheet.
To make sure that the horizontal or vertical scrollbars are at the row and column index position you want to show specific data, use the [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) and [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn) properties.
The following example shows how to activate a worksheet and make an active cell in it. In the generated output, the scrollbars will be scrolled to make the 2nd row and 2nd column as their first visible row and column.
## **Advance topics**
- [Copying and Moving Worksheets](https://docs.aspose.com/cells/net/copying-and-moving-worksheets/)
- [Count number of cells in the Worksheet](https://docs.aspose.com/cells/net/count-number-of-cells-in-the-worksheet/)
- [Detecting Empty Worksheets](https://docs.aspose.com/cells/net/detecting-empty-worksheets/)
- [Find if the Worksheet is Dialog Sheet](https://docs.aspose.com/cells/net/find-if-the-worksheet-is-dialog-sheet/)
- [Get worksheet unique id](https://docs.aspose.com/cells/net/get-worksheet-unique-id/)
- [Create, Manipulate or Remove Scenarios from Worksheets](https://docs.aspose.com/cells/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Managing Page Breaks](https://docs.aspose.com/cells/net/managing-page-breaks/)
- [Page Setup Features](https://docs.aspose.com/cells/net/page-setup-features/)
- [Print multiple copies of a worksheet](https://docs.aspose.com/cells/net/print-multiple-copies-of-a-worksheet/)
- [Utilize Sheet.SheetId property of OpenXml using Aspose.Cells](https://docs.aspose.com/cells/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Worksheet Views](https://docs.aspose.com/cells/net/worksheet-views/)
