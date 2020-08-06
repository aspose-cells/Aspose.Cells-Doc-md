---
title: Add Data in Cells
type: docs
weight: 10
url: /java/add-data-in-cells/
---

## **Aspose.Cells - Add Data in Cells**
Aspose.Cells provides a class, Workbook, that represents a Microsoft Excel file. Workbook class contains a WorksheetCollection that allows access to each worksheet in the Excel file. A worksheet is represented by the Worksheet class. The Worksheet class provides a Cellscollection. Each item in the Cells collection represents an object of the Cell class.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.get("A1").setValue("Hello World"); //Adding a string value to the cell

cells.get("A2").setValue(20.5); //Adding a double value to the cell

cells.get("A3").setValue(15); //Adding an integer  value to the cell

cells.get("A4").setValue(true); //Adding a boolean value to the cell

Cell cell = cells.get("A5"); //Adding a date/time value to the cell

cell.setValue(java.util.Calendar.getInstance());

//Setting the display format of the date

Style style = cell.getStyle();

style.setNumber(15);

cell.setStyle(style);

workbook.save(dataDir + "DataInCells_Aspose.xls"); //Saving the Excel file

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Add Data in Cells**
In Apache POI SS row.createCell(1).setCellValue can be used to add data in cells.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

CreationHelper createHelper = wb.getCreationHelper();

Sheet sheet = wb.createSheet("new sheet");

// Create a row and put some cells in it. Rows are 0 based.

Row row = sheet.createRow((short)0);

// Create a cell and put a value in it.

Cell cell = row.createCell(0);

cell.setCellValue(1);

// Or do it on one line.

row.createCell(1).setCellValue(1.2);

row.createCell(2).setCellValue(

createHelper.createRichTextString("This is a string"));

row.createCell(3).setCellValue(true);

// Write the output to a file

FileOutputStream fileOut = new FileOutputStream(dataDir + "DataInCells_Apache.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/workbook/adddataincells/)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/adddataincells)

{{% alert color="primary" %}} 

For more details, visit [Adding Data to Cells](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Data+to+Cells).

{{% /alert %}}
