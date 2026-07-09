---
title: Sparkline in Bild und HTML konvertieren in Aspose.Cells for Node.js via Java
linktitle: Convert Sparkline to Image and HTML
description: Erfahren Sie, wie Sie Aspose.Cells-Sparklines als eigenständige Bilder zur Zelleneinbettung rendern und sparkline-reiche Arbeitsblätter mithilfe von HtmlSaveOptions als HTML exportieren.
keywords: Aspose.Cells, Node.js via Java, Sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, Sparkline rendern, Sparkline in Bild konvertieren, Sparkline nach HTML exportieren
type: docs
weight: 120
url: /de/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Aspose.Cells ermöglicht es Ihnen, jede Sparkline als eigenständiges Bild zu extrahieren (zur Einbettung in eine andere Zelle oder einen externen Bericht) und das gesamte sparkline-reiche Arbeitsblatt zur browserbasierten Verteilung als HTML zu exportieren. Die in diesem Artikel verwendete Eigenschaft `Cell.EmbeddedImage` ist in **Aspose.Cells 26.5 und höher** verfügbar.
{{% /alert %}}

## **Einführung**

Sparklines sind eine kompakte Möglichkeit, Trends direkt in einem Arbeitsblatt zu visualisieren. Während Excel-Benutzer sie an Ort und Stelle sehen, erfordern viele reale Szenarien, dass eine Sparkline die Zelle verlässt — beispielsweise um als statisches Bild in eine andere Zelle eingebettet, an eine automatisierte E-Mail angehängt oder als Teil eines HTML-Berichts im Web veröffentlicht zu werden.

Aspose.Cells unterstützt beide dieser Vorgänge. Die Methode `Sparkline.toImage` rendert eine einzelne Sparkline in einen Stream, und die resultierenden Bytes können `Cell.EmbeddedImage` zugewiesen werden, sodass das Bild in einer einzelnen Zelle der Arbeitsmappe gespeichert wird. Separat ermöglicht es `HtmlSaveOptions`, die gesamte Arbeitsmappe — einschließlich der Sparklines — in eine in sich geschlossene HTML-Datei zu konvertieren. Dieser Artikel führt Sie Schritt für Schritt durch beide Workflows.

## **Workflow 1 — Sparklines als Bilder rendern und in Zellen einbetten**

In diesem Workflow erstellen Sie ein Arbeitsblatt, das einen kleinen Bereich mit Quellwerten enthält, fügen diesem Bereich drei verschiedene Sparkline-Gruppen (Linie, Spalte und Gestapelt/Gewinn-Verlust) hinzu, rendern jede Gruppe als PNG und schreiben diese PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die Live-Sparklines als auch ihre gerenderten Bildgegenstücke enthält.

### **Schritt-für-Schritt-Anleitung**

1. Definieren Sie ein Arbeitsverzeichnis und stellen Sie sicher, dass es auf der Festplatte vorhanden ist.
2. Erstellen Sie eine neue `Workbook` und holen Sie sich eine Referenz auf das erste `Worksheet`.
3. Füllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispielwerten (z. B. tägliche Verkaufszahlen oder Temperaturmessungen).
4. Fügen Sie dem Arbeitsblatt drei `SparklineGroup`-Objekte hinzu, indem Sie `worksheet.sparklineGroups.add(...)` aufrufen:
   - Eine Gruppe vom Typ `SparklineType.Line` verankert bei `F1`, mit Datenbereich `A1:E1`.
   - Eine Gruppe vom Typ `SparklineType.Column` verankert bei `G1`, mit Datenbereich `A1:E1`.
   - Eine Gruppe vom Typ `SparklineType.Stacked` (Gewinn/Verlust) verankert bei `H1`, mit Datenbereich `A1:E1`.
5. Erstellen Sie eine `ImageOrPrintOptions`-Instanz und setzen Sie deren `ImageType` auf `ImageType.Png`, sodass jede Sparkline als transparentes PNG gerendert wird.
6. Rendern Sie für jede der drei Gruppen ihre einzelne Sparkline mit `group.sparklines[0].toImage(outputStream, imageOptions)`, konvertieren Sie den `ByteArrayOutputStream` in ein `byte[]`, und weisen Sie das Array jeweils `worksheet.cells.get("F2").setEmbeddedImage(...)`, `worksheet.cells.get("G2").setEmbeddedImage(...)` und `worksheet.cells.get("H2").setEmbeddedImage(...)` zu.
7. Speichern Sie die Arbeitsmappe als `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Beispieldaten in die Zellen A1:E1 einfügen
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Füge eine Liniendiagramm-Sparkline-Gruppe hinzu, verankert bei F1 (Spalte 5, Zeile 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Füge eine Spaltendiagramm-Sparkline-Gruppe hinzu, verankert bei G1 (Spalte 6, Zeile 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Füge eine Gewinn/Verlust (Gestapelt) Sparkline-Gruppe hinzu, verankert bei H1 (Spalte 7, Zeile 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Bildoptionen für PNG-Ausgabe konfigurieren
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Konvertiere die Liniendiagramm-Sparkline in ein Bild und bette sie in Zelle F2 ein
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Konvertiere die Spaltendiagramm-Sparkline in ein Bild und bette sie in Zelle G2 ein
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Konvertiere die Gewinn/Verlust-Sparkline in ein Bild und bette sie in Zelle H2 ein
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Speichere die Arbeitsmappe auf der Festplatte
workbook.save("output_with_sparklines.xlsx");
```

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen dupliziert wird: die native Live-Sparkline, verankert in Zeile 1, und ein statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder innerhalb der Datei selbst leben, bleibt die Arbeitsmappe ein einzelnes, in sich geschlossenes Artefakt, das per E-Mail versendet oder archiviert werden kann, ohne dass die eingebetteten Bildverweise verloren gehen. Rendern Sie jede Sparkline-Gruppe als PNG, konvertieren Sie den `ByteArrayOutputStream` in ein `byte[]`, und weisen Sie das Array der Eigenschaft `setEmbeddedImage` der Zielzelle zu — die Zuweisung ist das, was das Bild zum gespeicherten Inhalt der Zelle macht.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe in einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.sparklines[0]` ansprechen, anstatt mit `forEach` zu enumerieren. Dadurch bleibt der Rendering-Code kurz und entspricht dem typischen Muster „eine Sparkline pro Ankerzelle". Das Speichern der Bild-Bytes über `Cell.EmbeddedImage` erfordert Aspose.Cells 26.5 oder höher.
{{% /alert %}}

## **Workflow 2 — Das Sparkline-Arbeitsblatt nach HTML exportieren**

Sobald die Arbeitsmappe Live-Sparklines (und optional eingebettete Bildgegenstücke) enthält, kann das gesamte Arbeitsblatt im Web veröffentlicht werden, indem es als HTML gespeichert wird. Die Klasse `HtmlSaveOptions` bietet die Schalter, die Sie zur Steuerung dieses Exports benötigen; in diesem Workflow verwenden Sie die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` erneut und konvertieren sie in ein sauberes, einseitiges HTML-Dokument.

### **Schritt-für-Schritt-Anleitung**

1. Stellen Sie sicher, dass die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` in Ihrem Arbeitsverzeichnis auf der Festplatte verfügbar ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und setzen Sie die Eigenschaft `ExportActiveWorksheetOnly` auf `true`, sodass die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
4. Rufen Sie `workbook.save("sparklines.html", htmlOptions)` auf, um die HTML-Ausgabe auf die Festplatte zu schreiben.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Der obige Code nimmt die sparkline-reiche Arbeitsmappe aus Workflow 1 und verwandelt sie in eine portable HTML-Datei. Sparklines werden je nach Exportmodus als Inline-SVG- oder PNG-Renderings in der generierten HTML-Datei beibehalten, sodass Endbenutzer die Trends in jedem modernen Browser anzeigen können, ohne dass Excel installiert sein muss. Indem Sie `ExportActiveWorksheetOnly` auf `true` setzen, vermeiden Sie es, versehentlich versteckte Blätter oder Hilfsdaten zu veröffentlichen — es wird nur das aktuell für den Benutzer sichtbare Arbeitsblatt exportiert.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, wie z. B. `ExportHiddenWorksheet`, `ExportImagesAsBase64` und `Encoding`. Passen Sie diese nach Bedarf für Ihr Bereitstellungsziel an.
{{% /alert %}}

## **API-Zusammenfassung**

Die oben beschriebenen Workflows stützen sich auf eine kleine Reihe von Aspose.Cells-APIs, die zusammenarbeiten.

- `SparklineGroup` und der Sammlungs-Accessor `worksheet.sparklineGroups` werden verwendet, um den Typ (Line, Column, Stacked), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe festzulegen. In diesem Artikel ist jede Gruppe in einer einzelnen Zelle verankert, sodass die Gruppe über `worksheet.sparklineGroups[i]` erreicht wird.
- `Sparkline` und der Indexer `group.sparklines[0]` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine `forEach`-Schleife erforderlich.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline in einen bereitgestellten `OutputStream` schreibt. Die Methode gibt `void` zurück; Sie lesen die Bytes aus dem Stream nach dem Aufruf.
- `Cell.EmbeddedImage` ist eine `byte[]`-Eigenschaft, die ein Bild in einer einzelnen Zelle speichert. Sie ist in **Aspose.Cells 26.5 und höher** verfügbar und ist die empfohlene Methode, um eine mit `toImage` gerenderte Sparkline in dieselbe Arbeitsmappe zurückzuführen.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (ein `boolean`) beschränkt den HTML-Export auf das aktive Arbeitsblatt. Es ist eine der am häufigsten verwendeten Eigenschaften von `HtmlSaveOptions` bei der Erstellung von einseitigen Berichten.
- `ImageOrPrintOptions.ImageType` befindet sich im Namespace `com.aspose.cells.drawing` und wählt das Bildformat (zum Beispiel `ImageType.Png`) aus, das beim Rendern mit `toImage` und beim Drucken von Arbeitsblättern als Bilder verwendet wird.

## **Verwandte Artikel**

- [Sparklines in Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/sparkline/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/nodejs-java/inserting-an-image-into-a-cell/)
- [SmartMarker Einzelzell-Array-Rendering | Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}