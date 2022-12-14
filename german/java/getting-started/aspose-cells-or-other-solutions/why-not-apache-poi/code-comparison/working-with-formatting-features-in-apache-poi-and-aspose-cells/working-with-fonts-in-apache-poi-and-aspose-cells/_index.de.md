---
title: Arbeiten mit Schriftarten in Apache POI und Aspose.Cells
type: docs
weight: 30
url: /de/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells – Arbeiten mit Schriftarten**
Aspose.Cells bietet eine Klasse,[Arbeitsmappe](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)das stellt eine Microsoft Excel-Datei dar. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)Klasse. Die Worksheet-Klasse stellt eine Cells-Sammlung bereit. Jeder Artikel in der Sammlung Cells repräsentiert ein Objekt der[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)Klasse.

**Java**

{{< highlight "java" >}}

 //Adding some value to cell

Cell cell = cells.get("A1");

cell.setValue("This is Aspose test of fonts!");

//Setting the font name to "Courier New"

Style style = cell.getStyle();

Font font = style.getFont();

font.setName("Courier New");

font.setSize(24);

font.setBold(true);

font.setUnderline(FontUnderlineType.SINGLE);

font.setColor(Color.getBlue());

font.setStrikeout(true);

//font.setSubscript(true);

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Arbeiten mit Schriftarten**
Apache POI SS stellt eine Font-Klasse bereit, um verschiedene Font-Einstellungen festzulegen.

**Java**

{{< highlight "java" >}}

 // Create a new font and alter it.

Font font = wb.createFont();

font.setFontHeightInPoints((short)24);

font.setFontName("Courier New");

font.setItalic(true);

font.setStrikeout(true);

// Fonts are set into a style so create a new one to use.

CellStyle style = wb.createCellStyle();

style.setFont(font);

// Create a cell and put a value in it.

Cell cell = row.createCell(1);

cell.setCellValue("This is a test of fonts");

cell.setCellStyle(style);

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Umgang mit Schrifteinstellungen](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
