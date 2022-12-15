---
title: Riordina i fogli all'interno della cartella di lavoro
type: docs
weight: 50
url: /it/java/re-order-sheets-within-workbook/
---
## **Aspose.Cells - Riordina i fogli all'interno della cartella di lavoro**
Aspose.Cells fornisce un metodo, Worksheet.moveTo(), utilizzato per spostare un foglio di lavoro in un'altra posizione nello stesso foglio di calcolo.

**Giava**

{{< highlight "java" >}}

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

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Riordina i fogli all'interno della cartella di lavoro**
Apache POI fornisce il metodo Workbook.setSheetOrder() per impostare i fogli di lavoro nell'ordine richiesto.

**Giava**

{{< highlight "java" >}}

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

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/reordersheets)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Copiare e spostare fogli di lavoro](/cells/it/java/copying-and-moving-worksheets).

{{% /alert %}}
