---
title: Fensterbereiche in Apache POI und Aspose.Cells einfrieren
type: docs
weight: 80
url: /de/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Spalten einfrieren**
Aspose.Cells bietet eine Klasse, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse Workbook enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) repräsentiert. Die Klasse Worksheet bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um Freeze-Panes zu konfigurieren, rufen Sie die Methode freezePanes der Klasse Worksheet auf. Die FreezePanes-Methode verwendet die folgenden Parameter:

- **Zeile**, der Zeilenindex der Zelle, von der das Einfrieren startet.
- **Spalte**, der Spaltenindex der Zelle, von der das Einfrieren startet.
- **Eingefrorene Zeilen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Eingefrorene Spalten**, die Anzahl der sichtbaren Spalten im linken Bereich

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Einfrieren von Fenstern**
sheet.createFreezePane ist verfügbar, um die Funktion FreezePane unter Verwendung von Apache POI SS - HSSF und XSSF zu erreichen

**Java**

{{< highlight java >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Freeze Panes](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
