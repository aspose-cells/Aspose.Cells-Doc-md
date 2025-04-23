---
title: Zellenkommentare einfügen
type: docs
weight: 40
url: /de/java/insert-cell-comments/
---

## **Aspose.Cells - Zellenkommentare einfügen**

Fügen Sie einen Kommentar zu einer Zelle hinzu, indem Sie die addComments-Methode der Shapes-Sammlung aufrufen (die im Worksheet-Objekt gekapselt ist). Das neue Comment-Objekt kann aus der Comments-Sammlung durch Übergabe des Kommentarindexes abgerufen werden. Nach dem Zugriff auf das Comment-Objekt passen Sie die Kommentarnotiz an, indem Sie die setNote-Methode des Comment-Objekts verwenden.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = worksheet.getComments().add("F5");

Comment comment = worksheet.getComments().get(commentIndex);

//Setting the comment note

comment.setNote("Hello Aspose!");

{{< /highlight >}}

## **Apache POI SS - HSSF & XSSF - Zellenkommentare einfügen**

Die folgenden Beispiele zeigen, wie Kommentare mit der Apache POI-API eingefügt werden können.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook(); //or new HSSFWorkbook();

CreationHelper factory = wb.getCreationHelper();

Sheet sheet = wb.createSheet();

Row row   = sheet.createRow(3);

Cell cell = row.createCell(5);

cell.setCellValue("F4");

Drawing drawing = sheet.createDrawingPatriarch();

// When the comment box is visible, have it show in a 1x3 space

ClientAnchor anchor = factory.createClientAnchor();

anchor.setCol1(cell.getColumnIndex());

anchor.setCol2(cell.getColumnIndex()+1);

anchor.setRow1(row.getRowNum());

anchor.setRow2(row.getRowNum()+3);

// Create the comment and set the text+author

Comment comment = drawing.createCellComment(anchor);

RichTextString str = factory.createRichTextString("Hello, World!");

comment.setString(str);

comment.setAuthor("Apache POI");

// Assign the comment to the cell

cell.setCellComment(comment);

{{< /highlight >}}

## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/addcomments)

{{< app/cells/assistant language="java" >}}
