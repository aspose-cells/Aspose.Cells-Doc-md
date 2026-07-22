---
title: Sparkline in Bild und HTML in Aspose.Cells for Java konvertieren
linktitle: Convert Sparkline to Image and HTML
description: Erfahren Sie, wie Sie Aspose.Cells-Sparklines als eigenständige Bilder für die Zelleneinbettung rendern und sparkline-reiche Arbeitsblätter mit HtmlSaveOptions nach HTML exportieren.
keywords: Aspose.Cells, Java, Sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, Sparkline rendern, Sparkline in Bild konvertieren, Sparkline nach HTML exportieren
type: docs
weight: 120
url: /de/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Aspose.Cells ermöglicht es Ihnen, jede Sparkline als eigenständiges Bild zu extrahieren (zum Einbetten in eine andere Zelle oder einen externen Bericht) und das gesamte sparkline-reiche Arbeitsblatt zur browserbasierten Verteilung nach HTML zu exportieren. Die in diesem Artikel verwendete Eigenschaft `Cell.EmbeddedImage` ist in **Aspose.Cells 26.5 und höher** verfügbar.
{{% /alert %}}

## **Einführung**

Sparklines sind eine kompakte Möglichkeit, Trends direkt innerhalb eines Arbeitsblatts zu visualisieren. Während Excel-Benutzer sie an Ort und Stelle sehen, erfordern viele reale Szenarien, dass eine Sparkline die Zelle verlässt – zum Beispiel, um als statisches Bild in eine andere Zelle eingebettet, an eine automatisierte E-Mail angehängt oder als Teil eines HTML-Berichts für das Web gerendert zu werden.

Aspose.Cells unterstützt beide dieser Vorgänge. Die Methode `Sparkline.toImage` rendert eine einzelne Sparkline in einen Stream, und die resultierenden Bytes können `Cell.EmbeddedImage` (über `setEmbeddedImage`) zugewiesen werden, sodass das Bild in einer einzelnen Zelle der Arbeitsmappe gespeichert wird. Separat ermöglicht `HtmlSaveOptions` das Konvertieren der gesamten Arbeitsmappe – einschließlich Sparklines – in eine in sich geschlossene HTML-Datei. Dieser Artikel führt Sie von Anfang bis Ende durch beide Workflows.

## **Workflow 1 – Sparklines als Bilder rendern und in Zellen einbetten**

In diesem Workflow erstellen Sie ein Arbeitsblatt, das einen kleinen Bereich mit Quellwerten enthält, fügen diesem Bereich drei verschiedene Sparkline-Gruppen (Linie, Spalte und Gestapelt/Gewinn-Verlust) hinzu, rendern jede Gruppe als PNG und schreiben diese PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die aktiven Sparklines als auch ihre gerenderten Bildgegenstücke enthält.

### **Schritt-für-Schritt-Anleitung**

1. Definieren Sie ein Arbeitsverzeichnis und stellen Sie sicher, dass es auf der Festplatte vorhanden ist.
2. Erstellen Sie eine neue `Workbook` und holen Sie sich eine Referenz auf das erste `Worksheet`.
3. Befüllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispielwerten (zum Beispiel tägliche Verkaufszahlen oder Temperaturmessungen).
4. Fügen Sie drei `SparklineGroup`-Objekte zum Arbeitsblatt hinzu, indem Sie `worksheet.getSparklineGroups().add(...)` aufrufen:
   - Eine `SparklineType.LINE`-Gruppe verankert bei `F1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.COLUMN`-Gruppe verankert bei `G1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.STACKED`-Gruppe (Gewinn/Verlust) verankert bei `H1`, mit Datenbereich `A1:E1`.
5. Erstellen Sie eine `ImageOrPrintOptions`-Instanz und rufen Sie `setImageType(ImageType.PNG)` auf, damit jede Sparkline als transparentes PNG gerendert wird.
6. Rendern Sie für jede der drei Gruppen ihre einzelne Sparkline mit `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)`, konvertieren Sie den `ByteArrayOutputStream` in ein `byte[]` und weisen Sie das Array jeweils über `worksheet.getCells().get("F2").setEmbeddedImage(...)`, `worksheet.getCells().get("G2").setEmbeddedImage(...)` und `worksheet.getCells().get("H2").setEmbeddedImage(...)` zu.
7. Rufen Sie `workbook.save("output_with_sparklines.xlsx")` auf, um die Arbeitsmappe auf der Festplatte zu speichern.

```java
import com.aspose.cells.*;
import java.io.*;

// Eine neue Arbeitsmappe erstellen und auf das erste Arbeitsblatt zugreifen
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Beispieldaten in die Zellen A1:E1 einfügen
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Eine Linien-Sparkline-Gruppe verankert bei F1 (Spalte 5, Zeile 0) hinzufügen
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// Eine Säulen-Sparkline-Gruppe verankert bei G1 (Spalte 6, Zeile 0) hinzufügen
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// Eine Gewinn/Verlust (Gestapelt) Sparkline-Gruppe verankert bei H1 (Spalte 7, Zeile 0) hinzufügen
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// Bildoptionen für die PNG-Ausgabe konfigurieren
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// Die Linien-Sparkline in ein Bild konvertieren und in Zelle F2 einbetten
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Die Säulen-Sparkline in ein Bild konvertieren und in Zelle G2 einbetten
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Die Gewinn/Verlust-Sparkline in ein Bild konvertieren und in Zelle H2 einbetten
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Die Arbeitsmappe auf der Festplatte speichern
workbook.save("output_with_sparklines.xlsx");
```

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen dupliziert wird: die aktive, native Sparkline verankert in Zeile 1, und ein statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder innerhalb der Datei selbst leben, bleibt die Arbeitsmappe ein einzelnes in sich geschlossenes Artefakt, das per E-Mail versendet oder archiviert werden kann, ohne dass die eingebetteten Bildreferenzen verloren gehen. Rendern Sie jede Sparkline-Gruppe als PNG, konvertieren Sie den `ByteArrayOutputStream` in ein `byte[]` und weisen Sie das Array der Eigenschaft `EmbeddedImage` der Zielzelle über `setEmbeddedImage(byte[])` zu – die Zuweisung ist es, die das Bild zum gespeicherten Inhalt der Zelle macht.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe an einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.getSparklines().get(0)` ansprechen, anstatt mit einer `for`-Schleife zu enumerieren. Dies hält den Rendering-Code kurz und entspricht dem typischen Muster „eine Sparkline pro Ankerzelle". Das Speichern der Bildbytes über `Cell.EmbeddedImage` (gesetzt durch `setEmbeddedImage`) erfordert Aspose.Cells 26.5 oder höher.
{{% /alert %}}

## **Workflow 2 – Das Sparkline-Arbeitsblatt nach HTML exportieren**

Sobald die Arbeitsmappe aktive Sparklines (und optional eingebettete Bildgegenstücke) enthält, kann das gesamte Arbeitsblatt im Web veröffentlicht werden, indem es als HTML gespeichert wird. Die Klasse `HtmlSaveOptions` bietet die Einstellungen, die Sie zur Steuerung dieses Exports benötigen; in diesem Workflow verwenden Sie die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` erneut und konvertieren sie in ein sauberes, einseitiges HTML-Dokument.

### **Schritt-für-Schritt-Anleitung**

1. Stellen Sie sicher, dass die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` in Ihrem Arbeitsverzeichnis auf der Festplatte verfügbar ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und rufen Sie `setExportActiveWorksheetOnly(true)` auf, sodass die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
4. Rufen Sie `workbook.save("sparklines.html", htmlOptions)` auf, um die HTML-Ausgabe auf der Festplatte zu schreiben.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Der obige Code nimmt die sparkline-reiche Arbeitsmappe aus Workflow 1 und wandelt sie in eine portable HTML-Datei um. Sparklines werden je nach Exportmodus als Inline-SVG- oder PNG-Renderings innerhalb des generierten HTML beibehalten, sodass Endbenutzer die Trends in jedem modernen Browser anzeigen können, ohne dass Excel installiert sein muss. Durch das Setzen von `ExportActiveWorksheetOnly` auf `true` über `setExportActiveWorksheetOnly(true)` vermeiden Sie, dass versehentlich versteckte Blätter oder Hilfsdaten veröffentlicht werden – es wird nur das aktuell für den Benutzer sichtbare Arbeitsblatt exportiert.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, wie z. B. `ExportHiddenWorksheet`, `ExportImagesAsBase64` und `Encoding`. Passen Sie diese nach Bedarf für Ihr Bereitstellungsziel an.
{{% /alert %}}

## **API-Zusammenfassung**

Die obigen Workflows basieren auf einer kleinen Gruppe von Aspose.Cells-APIs, die zusammenarbeiten.

- `SparklineGroup` und der Collection-Accessor `worksheet.getSparklineGroups()` werden verwendet, um den Typ (Linie, Spalte, Gestapelt), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe zu deklarieren. In diesem Artikel ist jede Gruppe an einer einzelnen Zelle verankert, sodass die Gruppe über `worksheet.getSparklineGroups().get(i)` erreicht wird.
- `Sparkline` und der Indexer `group.getSparklines().get(0)` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine `for`-Schleife erforderlich.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline in einen bereitgestellten `Stream` schreibt. Die Methode gibt `void` zurück; Sie lesen die Bytes aus dem Stream nach dem Aufruf.
- `Cell.EmbeddedImage` ist eine `byte[]`-Eigenschaft (zugewiesen über `cell.setEmbeddedImage(byte[])`), die ein Bild in einer einzelnen Zelle speichert. Sie ist in **Aspose.Cells 26.5 und höher** verfügbar und ist die empfohlene Methode, um eine mit `toImage` gerenderte Sparkline zurück in dieselbe Arbeitsmappe zu übertragen.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` beschränkt den HTML-Export auf das aktive Arbeitsblatt. Es ist eine der am häufigsten verwendeten Eigenschaften von `HtmlSaveOptions` bei der Erstellung von einseitigen Berichten.
- `ImageOrPrintOptions.setImageType(ImageType)` befindet sich im Paket `com.aspose.cells.drawing` und wählt das Bildformat (zum Beispiel `ImageType.PNG`) aus, das beim Rendern mit `toImage` und beim Drucken von Arbeitsblättern in Bilder verwendet wird.

## **Verwandte Artikel**

- [Sparklines in Aspose.Cells for Java](/cells/de/java/sparkline/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/java/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells Java](/cells/de/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}