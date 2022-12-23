---
title: Regolazione altezza colonna riga in xlsx4j
type: docs
weight: 50
url: /it/java/row-column-height-adjustment-in-xlsx4j/
---
## **Aspose.Cells - Regolazione Altezza Colonna Riga**
È possibile impostare l'altezza di una singola riga chiamando il metodo setRowHeight della raccolta Cells. Il metodo setRowHeight accetta i seguenti parametri:

- **Indice di riga**, l'indice della riga di cui stai modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

Impostare la larghezza di una colonna chiamando il metodo setColumnWidth della raccolta Cells. Il metodo setColumnWidth accetta i seguenti parametri:

- **Indice di colonna**, l'indice della colonna di cui stai modificando la larghezza.
- **Larghezza della colonna**, la larghezza della colonna desiderata.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Setting the height of all rows in the worksheet to 8

worksheet.getCells().setStandardHeight(8f);

//Setting the height of the second row to 40

cells.setRowHeight(1, 40);



//Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5);

{{< /highlight >}}
## **xlsx4j - Regolazione altezza colonna riga**
Row.setHt viene utilizzato per impostare l'altezza personalizzata per le righe utilizzando xlsx4j. setCustomHeight deve essere impostato su TRUE.

**Java**

{{< highlight "java" >}}

 SpreadsheetMLPackage pkg = SpreadsheetMLPackage.createPackage();

WorksheetPart sheet = pkg.createWorksheetPart(new PartName("/sheet1.xml"), "Sheet1", 1);

CTSheetFormatPr format = Context.getsmlObjectFactory().createCTSheetFormatPr();

format.setDefaultRowHeight(5);

format.setCustomHeight(Boolean.TRUE);

sheet.getJaxbElement().setSheetFormatPr(format);

SheetData sheetData = sheet.getJaxbElement().getSheetData();

Row row = Context.getsmlObjectFactory().createRow();

row.setHt(66.0);

row.setCustomHeight(Boolean.TRUE);

row.setR(1L);

Cell cell1 = Context.getsmlObjectFactory().createCell();

cell1.setV("1234");

row.getC().add(cell1);

Cell cell2 = Context.getsmlObjectFactory().createCell();

cell2.setV("56");

row.getC().add(cell2);

sheetData.getRow().add(row);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/worksheet/adjustheight)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Regolazione dell'altezza della riga e della larghezza della colonna](/java/adjusting-row-height-and-volumn-width).

{{% /alert %}}
