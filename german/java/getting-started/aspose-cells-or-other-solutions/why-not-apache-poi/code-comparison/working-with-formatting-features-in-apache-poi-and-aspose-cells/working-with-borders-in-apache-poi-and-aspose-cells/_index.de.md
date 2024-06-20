---
title: Arbeiten mit Rahmen in Apache POI und Aspose.Cells
type: docs
weight: 10
url: /de/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Arbeiten mit Rahmen**
Aspose.Cells bietet eine Klasse, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse Workbook enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) dargestellt. Die Klasse Worksheet stellt eine Cellscollection bereit. Jedes Element in der Cells-Sammlung repräsentiert ein Objekt der Klasse [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)

Aspose.Cells bietet die setStyle-Methode in der Klasse [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) an, um den Formatierungsstil einer Zelle festzulegen. Außerdem wird das Style-Objekt der Klasse [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) verwendet und bietet Eigenschaften zur Konfiguration von Schriftart-Einstellungen.

**Java**

{{< highlight java >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Arbeiten mit Rahmen**
Die CellStyle-Klasse bietet Funktionen zur Festlegung von Rahmen-Einstellungen unter Verwendung von Apache POI SS - HSSF und XSSF.

**Java**

{{< highlight java >}}

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Rahmen zu Zellen hinzufügen](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
