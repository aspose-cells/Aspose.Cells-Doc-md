---
title: Justering av radkolumnhöjd i xlsx4j
type: docs
weight: 50
url: /sv/java/row-column-height-adjustment-in-xlsx4j/
---
## **Aspose.Cells - Justering av radkolumnhöjd**
Det är möjligt att ställa in höjden på en enda rad genom att anropa Cells-samlingens setRowHeight-metod. Metoden setRowHeight tar följande parametrar:

- **Radindex**, indexet för raden som du ändrar höjden på.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

Ställ in bredden på en kolumn genom att anropa Cells-samlingens setColumnWidth-metod. Metoden setColumnWidth tar följande parametrar:

- **Kolumnindex**, indexet för kolumnen som du ändrar bredden på.
- **Kolumnbredd**, önskad kolumnbredd.

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
## **xlsx4j - Justering av radkolumnhöjd**
Row.setHt används för att ställa in anpassad höjd för rader med xlsx4j. setCustomHeight ska ställas in på TRUE.

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
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/worksheet/adjustheight)

{{% alert color="primary" %}} 

 För mer information, besök[Justera radhöjd och kolumnbredd](/java/adjusting-row-height-and-volumn-width).

{{% /alert %}}
