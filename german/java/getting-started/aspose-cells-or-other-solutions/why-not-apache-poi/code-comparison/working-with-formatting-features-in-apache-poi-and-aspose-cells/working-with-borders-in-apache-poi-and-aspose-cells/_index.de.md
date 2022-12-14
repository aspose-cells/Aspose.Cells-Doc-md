---
title: Arbeiten mit Grenzen in Apache POI und Aspose.Cells
type: docs
weight: 10
url: /de/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Arbeiten mit Grenzen**
Aspose.Cells bietet eine Klasse,[Arbeitsmappe](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)das stellt eine Microsoft Excel-Datei dar. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)Klasse. Die Worksheet-Klasse stellt eine Cells-Sammlung bereit. Jeder Artikel in der Sammlung Cells repräsentiert ein Objekt der[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)Klasse.

Aspose.Cells stellt die setStyle-Methode in der[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)Klasse zum Festlegen des Formatierungsstils einer Zelle. Auch das Style-Objekt der[Stil](http://docs.aspose.com:8082/docs/display/cellsjava/Style)-Klasse wird verwendet und stellt Eigenschaften zum Konfigurieren von Schriftarteinstellungen bereit.

**Java**

{{< highlight "java" >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Arbeiten mit Grenzen**
Die CellStyle-Klasse bietet Funktionen zum Festlegen von Rahmeneinstellungen mithilfe von Apache POI SS - HSSF und XSSF.

**Java**

{{< highlight "java" >}}

 //Setting the line of the top border

style.setBorder(BorderType.TOP_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the bottom border

style.setBorder(BorderType.BOTTOM_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the left border

style.setBorder(BorderType.LEFT_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the right border

style.setBorder(BorderType.RIGHT_BORDER,CellBorderType.THICK,Color.getBlack());

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Grenzen zu Cells hinzufügen](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
