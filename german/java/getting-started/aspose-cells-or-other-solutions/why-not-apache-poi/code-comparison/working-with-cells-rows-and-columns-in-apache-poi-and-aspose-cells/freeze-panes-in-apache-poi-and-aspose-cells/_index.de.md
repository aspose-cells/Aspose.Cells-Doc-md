---
title: Einfrieren von Fenstern in Apache POI und Aspose.Cells
type: docs
weight: 80
url: /de/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Fenster einfrieren**
Aspose.Cells bietet eine Klasse,[Arbeitsmappe](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)das stellt eine Microsoft Excel-Datei dar. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)Klasse. Die Worksheet-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Rufen Sie zum Konfigurieren von Einfrierfenstern die freezePanes-Methode der Worksheet-Klasse auf. Die FreezePanes-Methode übernimmt die folgenden Parameter:

- **Die Zeile**, der Zeilenindex der Zelle, bei der das Einfrieren beginnt.
- **Spalte**, der Spaltenindex der Zelle, ab der das Einfrieren beginnt.
- **Gefrorene Reihen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Gefrorene Säulen**, die Anzahl der sichtbaren Spalten im linken Bereich

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Fenster einfrieren**
sheet.createFreezePane ist verfügbar, um die FreezePane-Funktionalität zu erreichen, während Apache POI SS - HSSF und XSSF verwendet wird

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Fenster einfrieren](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
