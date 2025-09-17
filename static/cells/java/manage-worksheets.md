##Manage Worksheets
Developers can easily create and manage worksheets in their Excel files programmatically using the flexible API of Aspose.Cells. In this topic, we will discuss some approaches to add and remove worksheets in Excel files.
Managing worksheets using Aspose.Cells is as easy as ABC. In this section, we will describe how can we:
1. Create a new Excel file from scratch and add a worksheet to it
1. Add worksheets to designer spreadsheets
1. Accessing Worksheets using Sheet Name
1. Remove a worksheet from an Excel file using its sheet name
1. Remove a worksheet from an Excel file using its sheet index
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) that represents an Excel file. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file.
A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class provides a wide range of properties and methods to manage a worksheet. Let's see how can we make use of these basic set of APIs.
## **Adding Worksheets to a New Excel File**
To create a new Excel file programmatically, developers would need to create an object of [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class that represents an Excel file. Then developers can call [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) method of the [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). When we call [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) method, an empty worksheet is added to the Excel file automatically, which can be referenced by passing the sheet index of the newly added worksheet to the [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). After the worksheet reference is obtained, developers can work on their worksheets according to their requirements. After the work is done on the worksheets, developers can save their newly created Excel file with new worksheets by calling the [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) method of the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class.
## **Adding Worksheets to a Designer Spreadsheet**
The process of adding worksheets to a designer spreadsheet is entirely same as that of the above approach except that the Excel file is already created and we need to open that Excel file first before adding a worksheet to it. A designer spreadsheet can be opened by passing the file path or stream while initializing the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class.
## **Accessing Worksheets using Sheet Name**
Developers may access or get any worksheet by specifying its name or index.
## **Removing Worksheets using Sheet Name**
Sometimes, developers may need to remove worksheets from existing Excel files and that task can be performed by calling the [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-java.lang.String-) method of the [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) collection. We can pass the sheet name to the [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-java.lang.String-) method to remove a specific worksheet.
## **Removing Worksheets using Sheet Index**
The above approach of removing worksheets works well if developers already know the sheet names of the worksheets to be deleted. But, what if you don't know the sheet name of the worksheet that you want to remove from your Excel file?
Well, in such circumstances, developers can use an overloaded version of [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-int-) method that takes the sheet index of the worksheet instead of its sheet name.
## **Advance topics**
- [Activating Sheets and Activating a Cell in Worksheet](https://docs.aspose.com/cells/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Copy and Move Worksheets Within and Between Workbooks](https://docs.aspose.com/cells/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Copying and Moving Worksheets](https://docs.aspose.com/cells/java/copying-and-moving-worksheets/)
- [Count number of cells in the Worksheet](https://docs.aspose.com/cells/java/count-number-of-cells-in-the-worksheet/)
- [Detecting Empty Worksheets](https://docs.aspose.com/cells/java/detecting-empty-worksheets/)
- [Find if the Worksheet is Dialog Sheet](https://docs.aspose.com/cells/java/find-if-the-worksheet-is-dialog-sheet/)
- [Get worksheet unique id](https://docs.aspose.com/cells/java/get-worksheet-unique-id/)
- [Insert Background Image to Excel](https://docs.aspose.com/cells/java/insert-background-image-to-excel/)
- [Create, Manipulate or Remove Scenarios from Worksheets](https://docs.aspose.com/cells/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Managing Page Breaks](https://docs.aspose.com/cells/java/managing-page-breaks/)
- [Page Setup Features](https://docs.aspose.com/cells/java/page-setup-features/)
- [Update references in other worksheets while deleting blank columns and rows in a worksheet](https://docs.aspose.com/cells/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Utilize Sheet.SheetId property of OpenXml using Aspose.Cells](https://docs.aspose.com/cells/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Working with Background in ODS Files](https://docs.aspose.com/cells/java/working-with-background-in-ods-files/)
- [Worksheet Views](https://docs.aspose.com/cells/java/worksheet-views/)
