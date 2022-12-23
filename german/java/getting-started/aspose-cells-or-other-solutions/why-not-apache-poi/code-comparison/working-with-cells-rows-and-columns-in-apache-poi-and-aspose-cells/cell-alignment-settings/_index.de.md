---
title: Cell Ausrichtungseinstellungen
type: docs
weight: 20
url: /de/java/cell-alignment-settings/
---
## **Aspose.Cells - Cell Ausrichtungseinstellungen**
Aspose.Cells bietet eine Klasse, Workbook, die eine Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Worksheet-Klasse dargestellt.

Die Worksheet-Klasse stellt eine Cells-Sammlung bereit. Jedes Element in der Sammlung Cells repräsentiert ein Objekt der Klasse Cell.

Aspose.Cells stellt die setStyle-Methode in der Cell-Klasse bereit, die zur Formatierung einer Zelle verwendet wird. Die Style-Klasse stellt nützliche Eigenschaften zum Konfigurieren von Schriftarteinstellungen bereit.

Wählen Sie mithilfe der TextAlignmentType-Enumeration einen beliebigen Textausrichtungstyp aus.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

int sheetIndex = workbook.getWorksheets().add();

Worksheet worksheet = workbook.getWorksheets().get(sheetIndex);

Cells cells = worksheet.getCells();

//Adding the current system date to "A1" cell

Cell cell = cells.get("A1");

Style style = cell.getStyle();

//Adding some value to the "A1" cell

cell.setValue("Visit Aspose!");

//Setting the horizontal alignment of the text in the "A1" cell

style.setHorizontalAlignment(TextAlignmentType.CENTER);

//Saved style

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Cell Ausrichtungseinstellungen**
HSSFCellStyle stellt den Stil für die Ausrichtung in Zellen mit Apache POI API bereit.

**Java**

{{< highlight "java" >}}

 public static void main(String[]args) throws IOException

{

 // The path to the documents directory.

 String dataDir = Utils.getDataDir(ApacheCellAlignment.class);

 HSSFWorkbook wb = new HSSFWorkbook();

 HSSFSheet sheet = wb.createSheet("new sheet");

 HSSFRow row = sheet.createRow(2);

 createCell(wb, row, 0, HSSFCellStyle.ALIGN_CENTER);

 createCell(wb, row, 1, HSSFCellStyle.ALIGN_CENTER_SELECTION);

 createCell(wb, row, 2, HSSFCellStyle.ALIGN_FILL);

 createCell(wb, row, 3, HSSFCellStyle.ALIGN_GENERAL);

 createCell(wb, row, 4, HSSFCellStyle.ALIGN_JUSTIFY);

 createCell(wb, row, 5, HSSFCellStyle.ALIGN_LEFT);

 createCell(wb, row, 6, HSSFCellStyle.ALIGN_RIGHT);

 // Write the output to a file

 FileOutputStream fileOut = new FileOutputStream(dataDir + "ApahceAlignment.xls");

 wb.write(fileOut);

 fileOut.close();

 System.out.println("Done.");

}

/**

\* Creates a cell and aligns it a certain way.

\*

\* @param wb        the workbook

\* @param row       the row to create the cell in

\* @param column    the column number to create the cell in

\* @param align     the alignment for the cell.

*/

private static void createCell(HSSFWorkbook wb, HSSFRow row, int column, int align) {

 HSSFCell cell = row.createCell(column);

 cell.setCellValue("Align It");

 HSSFCellStyle cellStyle = wb.createCellStyle();

 cellStyle.setAlignment((short)align);

 cell.setCellStyle(cellStyle);

}

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/cellalignment)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Ausrichtungseinstellungen konfigurieren](/cells/de/java/data-formatting/).

{{% /alert %}}
