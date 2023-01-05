---
title: Arbeiten mit Farben in Apache POI und Aspose.Cells
type: docs
weight: 20
url: /de/java/working-with-colors-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Arbeiten mit Farben**
Aspose.Cells bietet eine Klasse,[Arbeitsmappe](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)Klasse. Die Worksheet-Klasse stellt eine Cells-Sammlung bereit. Jeder Artikel in der Sammlung Cells repräsentiert ein Objekt der[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)Klasse.

Aspose.Cells stellt die setStyle-Methode in der Cell-Klasse bereit, die verwendet wird, um die Formatierung einer Zelle festzulegen. Außerdem kann das Style-Objekt der Style-Klasse verwendet werden, um Schrifteinstellungen zu konfigurieren.

**Java**

{{< highlight "java" >}}

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
Die CellStyle-Klasse ist verfügbar, um Hintergrund- und Füllmustereinstellungen festzulegen.

**Java**

{{< highlight "java" >}}

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
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Farben und Hintergrundmuster](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}
