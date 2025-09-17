##Re-Order Sheets Within Workbook
## **Aspose.Cells - Re-Order Sheets Within Workbook**
Aspose.Cells provides a method, Worksheet.moveTo(), used to move a worksheet to another location in the same spreadsheet.
**Java**
//Create a new Workbook.
Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();
Worksheet worksheet1 = worksheets.get(0);
Worksheet worksheet2 = worksheets.add("Sheet2");
Worksheet worksheet3 = worksheets.add("Sheet3");
//Move Sheets with in Workbook.
worksheet2.moveTo(0);
worksheet1.moveTo(1);
worksheet3.moveTo(2);
//Save the excel file.
workbook.save(dataDir + "AsposeMoveSheet.xls");
## **Apache POI SS - HSSF XSSF - Re-Order Sheets Within Workbook**
Apache POI provides Workbook.setSheetOrder() method to set worksheets in required order.
**Java**
Workbook wb = new HSSFWorkbook();
wb.createSheet("new sheet");
wb.createSheet("second sheet");
wb.createSheet("third sheet");
wb.setSheetOrder("second sheet", 0);
wb.setSheetOrder("new sheet", 1);
wb.setSheetOrder("third sheet", 2);
FileOutputStream fileOut = new FileOutputStream(dataDir + "Apache_Reordered.xls");
wb.write(fileOut);
fileOut.close();
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/reordersheets)
For more details, visit [Copying and Moving Worksheets](https://docs.aspose.com/cells/java/copying-and-moving-worksheets).
