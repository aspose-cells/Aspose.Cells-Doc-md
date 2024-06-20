---
title: Zoomfaktor mit Apache POI und Aspose.Cells
type: docs
weight: 70
url: /de/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Zoom-Faktor**
Microsoft Excel bietet eine Funktion, die es Benutzern ermöglicht, den Zoom- oder Skalierungsfaktor eines Tabellenblatts festzulegen. Diese Funktion unterstützt Benutzer dabei, den Inhalt des Tabellenblatts in kleineren oder größeren Ansichten zu sehen.

Aspose.Cells bietet eine Klasse, Workbook, die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Tabellenblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Worksheet-Klasse repräsentiert. Die Worksheet-Klasse bietet eine breite Palette von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Verwenden Sie die Methode setZoom der Worksheet-Klasse, um den Zoomfaktor eines Arbeitsblatts festzulegen.

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Zoomfaktor**
Apache POI stellt die Methode Sheet.setZoom() zur Verfügung, um die Zoomfunktion zu nutzen.

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
