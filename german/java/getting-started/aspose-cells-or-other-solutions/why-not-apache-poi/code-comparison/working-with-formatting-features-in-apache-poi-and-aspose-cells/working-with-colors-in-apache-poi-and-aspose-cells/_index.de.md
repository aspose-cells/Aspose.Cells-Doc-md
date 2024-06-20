---
title: Arbeiten mit Farben in Apache POI und Aspose.Cells
type: docs
weight: 20
url: /de/java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Arbeiten mit Farben**
Aspose.Cells bietet eine Klasse, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse Workbook enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) dargestellt. Die Klasse Worksheet stellt eine Cellscollection bereit. Jedes Element in der Cells-Sammlung repräsentiert ein Objekt der Klasse [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)

Aspose.Cells bietet die setStyle-Methode in der Cell-Klasse, die verwendet wird, um die Formatierung einer Zelle festzulegen. Außerdem kann das Style-Objekt der Style-Klasse verwendet werden, um Schriftart-Einstellungen zu konfigurieren.

**Java**

{{< highlight java >}}

 //Accessing cell from the worksheet

Cell cell = cells.get("B2");

Style style = cell.getStyle();

//Setting the foreground color to yellow

style.setBackgroundColor(Color.getYellow());

//Setting the background pattern to vertical stripe

style.setPattern(BackgroundType.VERTICAL_STRIPE);

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

// === Setting Foreground ===

//Adding custom color to the palette at 55th index

Color color = Color.fromArgb(212,213,0);

workbook.changePalette(color,55);

//Accessing cell from the worksheet

cell = cells.get("B3");

//Adding some value to the cell

cell.setValue("Hello Aspose!");

//Setting the custom color to the font

style = cell.getStyle();

Font font = style.getFont();

font.setColor(color);

cell.setStyle(style);


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Arbeiten mit Farben**
Die CellStyle-Klasse steht zur Verfügung, um Hintergrund- und Fillpattern-Einstellungen festzulegen.

**Java**

{{< highlight java >}}

 // Aqua background

CellStyle style = wb.createCellStyle();

style.setFillBackgroundColor(IndexedColors.AQUA.getIndex());

style.setFillPattern(CellStyle.BIG_SPOTS);

Cell cell = row.createCell((short) 1);

cell.setCellValue("X");

cell.setCellStyle(style);

// Orange "foreground", foreground being the fill foreground not the font color.

style = wb.createCellStyle();

style.setFillForegroundColor(IndexedColors.ORANGE.getIndex());

style.setFillPattern(CellStyle.SOLID_FOREGROUND);

cell = row.createCell((short) 2);

cell.setCellValue("X");

cell.setCellStyle(style);

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Farben und Hintergrundmuster](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}
