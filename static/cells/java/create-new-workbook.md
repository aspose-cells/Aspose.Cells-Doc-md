##Create New Workbook
## **Aspose.Cells - Create New Workbook**
Workbook class is available for simple use
**Java**
Workbook workbook = new Workbook(); // Creating a Workbook object
workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); //Workbooks can be saved in many formats
## **Apache POI SS - HSSF XSSF - Create New Workbook**
Create new Workbook using Workbook class and save using FileOutputStream.
**Java**
Workbook wb = new HSSFWorkbook();
FileOutputStream fileOut;
fileOut = new FileOutputStream("newWorkbook.xls");
wb.write(fileOut);
fileOut.close();
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)
