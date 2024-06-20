---
title: Ajustement de la hauteur de ligne et de colonne dans xlsx4j
type: docs
weight: 50
url: /fr/java/row-column-height-adjustment-in-xlsx4j/
---

## **Aspose.Cells - Ajustement de la hauteur de ligne et de colonne**
Il est possible de définir la hauteur d'une seule ligne en appelant la méthode setRowHeight de la collection Cells. La méthode setRowHeight prend les paramètres suivants :

- **Index de ligne**, l'index de la ligne pour laquelle vous modifiez la hauteur.
- **Hauteur de la ligne**, la hauteur de la ligne à appliquer sur la ligne.

Définissez la largeur d'une colonne en appelant la méthode setColumnWidth de la collection Cells. La méthode setColumnWidth prend les paramètres suivants:

- Index de la colonne, l'index de la colonne dont vous changez la largeur.
- Largeur de colonne, la largeur de colonne souhaitée.

**Java**

{{< highlight java >}}

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
## **xlsx4j - Ajustement de la hauteur de la ligne et de la colonne**
Row.setHt est utilisé pour définir une hauteur personnalisée pour les lignes en utilisant xlsx4j. setCustomHeight doit être défini sur TRUE.

**Java**

{{< highlight java >}}

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
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/worksheet/adjustheight)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Ajustement de la hauteur de la ligne et de la largeur de la colonne](/java/adjusting-row-height-and-volumn-width).

{{% /alert %}}
