---
title: Arbeiten mit Schriftarten in Apache POI und Aspose.Cells
type: docs
weight: 30
url: /de/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Arbeiten mit Schriftarten**
Aspose.Cells bietet eine Klasse, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse Workbook enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) dargestellt. Die Klasse Worksheet bietet eine Cells-Sammlung. Jedes Element in der Cells-Sammlung repräsentiert ein Objekt der Klasse [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

**Java**

{{< highlight java >}}

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
Apache POI SS bietet die Klasse Font, um verschiedene Schrifteinstellungen festzulegen.

**Java**

{{< highlight java >}}

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Umgang mit Schriftarteinstellungen](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
