---
title: Cell Impostazioni allineamento
type: docs
weight: 20
url: /it/java/cell-alignment-settings/
---
## **Aspose.Cells - Cell Impostazioni allineamento**
Aspose.Cells fornisce una classe, Workbook, che rappresenta un file Excel. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe Worksheet.

La classe Worksheet fornisce una raccolta Cells. Ogni elemento nella raccolta Cells rappresenta un oggetto della classe Cell.

Aspose.Cells fornisce il metodo setStyle nella classe Cell che viene utilizzato per la formattazione di una cella. La classe Style fornisce proprietà utili per la configurazione delle impostazioni dei caratteri.

Selezionare qualsiasi tipo di allineamento del testo utilizzando l'enumerazione TextAlignmentType.

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
## **Apache POI SS - HSSF e XSSF - Cell Impostazioni di allineamento**
HSSFCellStyle fornisce lo stile per l'allineamento nelle celle utilizzando Apache POI API.

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/cellalignment)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Configurazione delle impostazioni di allineamento](/cells/it/java/data-formatting/).

{{% /alert %}}
