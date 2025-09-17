##Printing Workbooks
How print worksheets and workbook using Java. This article provides the Java code to print worksheets and workbook using Aspose.Cells for Java API.
This document is designed to provide the developers with understanding (in a compact manner) on how to print spreadsheets.
## Usage Scenario
After you finish creating your spreadsheet, you will probably want to print a hard copy of the sheet for your need. When you are printing, MS Excel assumes you want to print the entire worksheet area unless you specify your selection. The following screenshot shows the dialog box for printing workbook with Excel.
![todo:image_alt_text](printing-workbooks_1.png)
**Figure:** Print Dialog Box
## Printing Workbooks using Aspose.Cells
Aspose.Cells for Java provides a [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) method of the [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) class. By using the [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) method, you can provide the printer name as well as the print job name.
## Sample Code
### Print Selected Worksheet
The following code snippet demonstrates the use of the [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) method to print your selected worksheet.
### Print Whole Workbook
You can also use the [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) method to print the whole workbook. The following code snippet demonstrates the use of the [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) method to print the whole workbook.
## Related Articles
- [Specify Job or Document Name while printing with Aspose.Cells](https://docs.aspose.com/cells/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
