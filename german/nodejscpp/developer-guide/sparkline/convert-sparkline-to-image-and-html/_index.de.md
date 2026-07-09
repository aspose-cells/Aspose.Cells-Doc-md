---
title: Sparkline in Bild und HTML konvertieren in Aspose.Cells for Node.js via C++
linktitle: Convert Sparkline to Image and HTML
description: Erfahren Sie, wie Sie Aspose.Cells-Sparklines als eigenständige Bilder für die Zelleneinbettung rendern und sparkline-reiche Arbeitsblätter mit HtmlSaveOptions nach HTML exportieren.
keywords: Aspose.Cells, Node.js via C++, Sparkline, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, Sparkline rendern, Sparkline in Bild konvertieren, Sparkline nach HTML exportieren
type: docs
weight: 120
url: /de/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Aspose.Cells ermöglicht es Ihnen, jede Sparkline als eigenständiges Bild zu extrahieren (zum Einbetten in eine andere Zelle oder einen externen Bericht) und auch das gesamte sparkline-reiche Arbeitsblatt nach HTML für die browserbasierte Verteilung zu exportieren. Die in diesem Artikel verwendete Eigenschaft `cell.embeddedImage` ist in **Aspose.Cells 26.5 und höher** verfügbar.
{{% /alert %}}

## **Einführung**

Sparklines sind eine kompakte Möglichkeit, Trends direkt in einem Arbeitsblatt zu visualisieren. Während Excel-Benutzer sie an Ort und Stelle sehen, erfordern viele reale Szenarien, dass eine Sparkline die Zelle verlässt — zum Beispiel, um als statisches Bild in eine andere Zelle eingebettet, an eine automatisierte E-Mail angehängt oder als Teil eines HTML-Berichts gerendert zu werden, der im Web veröffentlicht wird.

Aspose.Cells unterstützt beide dieser Operationen. Die Methode `Sparkline.toImage` rendert eine einzelne Sparkline in einen Stream, und die resultierenden Bytes können `cell.embeddedImage` zugewiesen werden, sodass das Bild in einer einzelnen Zelle der Arbeitsmappe gespeichert wird. Separat ermöglicht es `HtmlSaveOptions`, die gesamte Arbeitsmappe — einschließlich Sparklines — in eine in sich geschlossene HTML-Datei zu konvertieren. Dieser Artikel führt Sie Schritt für Schritt durch beide Workflows.

## **Workflow 1 — Sparklines als Bilder rendern und in Zellen einbetten**

In diesem Workflow erstellen Sie ein Arbeitsblatt, das einen kleinen Bereich von Quellwerten enthält, fügen drei verschiedene Sparkline-Gruppen (Linie, Spalte und Gestapelt/Gewinn-Verlust) an diesen Bereich an, rendern jede Gruppe als PNG und schreiben diese PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die Live-Sparklines als auch ihre gerenderten Bildentsprechungen enthält.

### **Schritt-für-Schritt-Anleitung**

1. Definieren Sie ein Arbeitsverzeichnis und stellen Sie sicher, dass es auf der Festplatte vorhanden ist.
2. Erstellen Sie eine neue `Workbook` und holen Sie sich eine Referenz auf das erste `Worksheet`.
3. Befüllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispieldaten (zum Beispiel tägliche Verkaufszahlen oder Temperaturmessungen).
4. Fügen Sie dem Arbeitsblatt drei `SparklineGroup`-Objekte hinzu, indem Sie `worksheet.sparklineGroups.add(...)` aufrufen:
   - Eine `SparklineType.Line`-Gruppe, verankert bei `F1`, mit dem Datenbereich `A1:E1`.
   - Eine `SparklineType.Column`-Gruppe, verankert bei `G1`, mit dem Datenbereich `A1:E1`.
   - Eine `SparklineType.Stacked` (Gewinn/Verlust)-Gruppe, verankert bei `H1`, mit dem Datenbereich `A1:E1`.
5. Erstellen Sie eine `ImageOrPrintOptions`-Instanz und setzen Sie deren `ImageType` auf `ImageType.Png`, damit jede Sparkline als transparentes PNG gerendert wird.
6. Rendern Sie für jede der drei Gruppen ihre einzelne Sparkline mit `group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)`, konvertieren Sie den Stream in einen `Buffer` (oder `Uint8Array`) und weisen Sie die Bytes jeweils `worksheet.cells["F2"].embeddedImage`, `worksheet.cells["G2"].embeddedImage` und `worksheet.cells["H2"].embeddedImage` zu.
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

// Eine Liniendiagramm-Sparkline-Gruppe hinzufügen, verankert bei F1 (Spalte 5, Zeile 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Eine Spaltendiagramm-Sparkline-Gruppe hinzufügen, verankert bei G1 (Spalte 6, Zeile 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Eine Win/Loss-(Gestapelte) Sparkline-Gruppe hinzufügen, verankert bei H1 (Spalte 7, Zeile 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Bildoptionen für PNG-Ausgabe konfigurieren
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Die Liniendiagramm-Sparkline in ein Bild konvertieren und in Zelle F2 einbetten
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// Die Spaltendiagramm-Sparkline in ein Bild konvertieren und in Zelle G2 einbetten
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// Die Win/Loss-Sparkline in ein Bild konvertieren und in Zelle H2 einbetten
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// Die Arbeitsmappe auf der Festplatte speichern
workbook.save("output_with_sparklines.xlsx");
```

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen dupliziert wird: die native Live-Sparkline, verankert in Zeile 1, und ein statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder in der Datei selbst leben, bleibt die Arbeitsmappe ein einzelnes in sich geschlossenes Artefakt, das per E-Mail versendet oder archiviert werden kann, ohne dass die eingebetteten Bildreferenzen beschädigt werden. Rendern Sie jede Sparkline-Gruppe als PNG, konvertieren Sie den Stream in einen `Buffer` und weisen Sie das Array der Eigenschaft `embeddedImage` der Zielzelle zu — die Zuweisung ist es, die das Bild zum gespeicherten Inhalt der Zelle macht.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe in einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.sparklines[0]` ansprechen, anstatt mit `forEach` zu enumerieren. Dies hält den Rendering-Code kurz und entspricht dem typischen Muster „eine Sparkline pro Ankerzelle". Das Speichern der Bildbytes über `cell.embeddedImage` erfordert Aspose.Cells 26.5 oder höher.
{{% /alert %}}

## **Workflow 2 — Das Sparkline-Arbeitsblatt nach HTML exportieren**

Sobald die Arbeitsmappe Live-Sparklines (und optional eingebettete Bildentsprechungen) enthält, kann das gesamte Arbeitsblatt im Web veröffentlicht werden, indem es als HTML gespeichert wird. Die Klasse `HtmlSaveOptions` stellt die Regler bereit, die Sie benötigen, um diesen Export zu steuern; in diesem Workflow verwenden Sie die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` wieder und konvertieren sie in ein sauberes, einseitiges HTML-Dokument.

### **Schritt-für-Schritt-Anleitung**

1. Stellen Sie sicher, dass die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` auf der Festplatte in Ihrem Arbeitsverzeichnis verfügbar ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und setzen Sie deren Eigenschaft `exportActiveWorksheetOnly` auf `true`, damit die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
4. Rufen Sie `workbook.save("sparklines.html", htmlOptions)` auf, um die HTML-Ausgabe auf die Festplatte zu schreiben.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Der obige Code nimmt die sparkline-reiche Arbeitsmappe aus Workflow 1 und verwandelt sie in eine portable HTML-Datei. Sparklines werden je nach Exportmodus als Inline-SVG- oder PNG-Renderings innerhalb des generierten HTML beibehalten, sodass Endbenutzer die Trends in jedem modernen Browser anzeigen können, ohne Excel installiert zu haben. Durch das Setzen von `exportActiveWorksheetOnly` auf `true` vermeiden Sie es, versehentlich versteckte Blätter oder Hilfsdaten zu veröffentlichen — es wird nur das für den Benutzer aktuell sichtbare Arbeitsblatt exportiert.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, wie `exportHiddenWorksheet`, `exportImagesAsBase64` und `encoding`. Passen Sie diese nach Bedarf für Ihr Bereitstellungsziel an.
{{% /alert %}}

## **API-Zusammenfassung**

Die obigen Workflows stützen sich auf einen kleinen Satz von Aspose.Cells-APIs, die zusammenarbeiten.

- `SparklineGroup` und der Sammlungs-Accessor `worksheet.sparklineGroups` werden verwendet, um den Typ (Linie, Spalte, Gestapelt), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe zu deklarieren. In diesem Artikel ist jede Gruppe in einer einzelnen Zelle verankert, sodass die Gruppe über `worksheet.sparklineGroups[i]` erreicht wird.
- `Sparkline` und der Indexer `group.sparklines[0]` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine `forEach`-Schleife erforderlich.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline in einen bereitgestellten `Stream` schreibt. Die Methode gibt `void` zurück; Sie lesen die Bytes nach dem Aufruf aus dem Stream.
- `cell.embeddedImage` ist eine `Buffer`- (oder `Uint8Array`-)Eigenschaft, die ein Bild in einer einzelnen Zelle speichert. Sie ist in **Aspose.Cells 26.5 und höher** verfügbar und ist die empfohlene Methode, um eine von `toImage` gerenderte Sparkline zurück in dieselbe Arbeitsmappe zu übertragen.
- `htmlSaveOptions.exportActiveWorksheetOnly` (ein `bool`) beschränkt den HTML-Export auf das aktive Arbeitsblatt. Es ist eine der am häufigsten verwendeten Eigenschaften von `HtmlSaveOptions` bei der Erstellung von einseitigen Berichten.
- `imageOrPrintOptions.imageType` befindet sich im Namespace `Aspose.Cells.Drawing` und wählt das Bildformat (zum Beispiel `ImageType.Png`) aus, das beim Rendern mit `toImage` und beim Drucken von Arbeitsblättern in Bilder verwendet wird.

## **Verwandte Artikel**

- [Sparklines in Aspose.Cells for Aspose.Cells for Node.js via C++](/cells/de/nodejs-cpp/sparkline/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/nodejs-cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Einzelzell-Array-Rendering | Aspose.Cells Node.js via C++](/cells/de/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}