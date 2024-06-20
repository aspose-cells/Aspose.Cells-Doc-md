---
title: Daten in Zellen hinzufügen
type: docs
weight: 10
url: /de/java/add-data-in-cells/
---

## **Aspose.Cells - Daten in Zellen hinzufügen**
Aspose.Cells bietet eine Klasse Workbook, die eine Microsoft Excel-Datei darstellt. Die Klasse Workbook enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse Worksheet dargestellt. Die Klasse Worksheet bietet eine Cells-Sammlung. Jedes Element in der Cells-Sammlung repräsentiert ein Objekt der Klasse Cell.

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
## **Apache POI SS - HSSF XSSF - Daten in Zellen hinzufügen**
In Apache POI SS kann row.createCell(1).setCellValue verwendet werden, um Daten in Zellen hinzuzufügen.

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/adddataincells)

{{% alert color="primary" %}} 

Weitere Details finden Sie unter [Daten zu Zellen hinzufügen](/java/adding-data-to-cells).

{{% /alert %}}
