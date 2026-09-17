---
title: Sparkline in Aspose.Cells for .NET in Bild und HTML konvertieren
linktitle: Sparkline
description: Erfahren Sie, wie Sie Aspose.Cells-Sparklines als eigenständige Bilder zum Einbetten in Zellen rendern und sparklinereiche Arbeitsblätter mit HtmlSaveOptions nach HTML exportieren.
keywords: Aspose.Cells, .NET, Sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, Sparkline rendern, Sparkline in Bild konvertieren, Sparkline nach HTML exportieren
type: docs
weight: 120
url: /de/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Aspose.Cells ermöglicht es Ihnen, jede Sparkline als eigenständiges Bild zu extrahieren (zum Einbetten in eine andere Zelle oder einen externen Bericht) und das gesamte sparklinereiche Arbeitsblatt für die browserbasierte Verteilung nach HTML zu exportieren. Die in diesem Artikel verwendete Eigenschaft `Cell.EmbeddedImage` ist in **Aspose.Cells 26.5 und höher** verfügbar.

## **Einführung**
Sparklines sind eine kompakte Möglichkeit, Trends direkt in einem Arbeitsblatt zu visualisieren. Während Excel-Benutzer sie an Ort und Stelle sehen, erfordern viele reale Szenarien, dass eine Sparkline die Zelle verlässt — zum Beispiel, um als statisches Bild in eine andere Zelle eingebettet, an eine automatisierte E-Mail angehängt oder als Teil eines im Web veröffentlichten HTML-Berichts gerendert zu werden.
Aspose.Cells unterstützt beide dieser Operationen. Die Methode `Sparkline.ToImage` rendert eine einzelne Sparkline in einen Stream, und die resultierenden Bytes können `Cell.EmbeddedImage` zugewiesen werden, sodass das Bild in einer einzelnen Zelle der Arbeitsmappe gespeichert wird. Separat ermöglicht `HtmlSaveOptions` die Konvertierung der gesamten Arbeitsmappe — einschließlich aller Sparklines — in eine in sich geschlossene HTML-Datei. Dieser Artikel führt Sie durch beide Workflows von Anfang bis Ende.

## **Workflow 1 — Sparklines als Bilder rendern und in Zellen einbetten**
In diesem Workflow erstellen Sie ein Arbeitsblatt, das einen kleinen Bereich mit Quellwerten enthält, fügen drei verschiedene Sparkline-Gruppen (Linie, Spalte und Gestapelt/Gewinn-Verlust) an diesen Bereich an, rendern jede Gruppe als PNG und schreiben diese PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die aktiven Sparklines als auch ihre gerenderten Bildgegenstücke enthält.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` und holen Sie sich eine Referenz auf das erste `Worksheet`.
2. Befüllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispielwerten (zum Beispiel tägliche Verkaufszahlen oder Temperaturmessungen).
3. Fügen Sie drei `SparklineGroup`-Objekte zum Arbeitsblatt hinzu, indem Sie `worksheet.SparklineGroups.Add(...)` aufrufen:
   - Eine `SparklineType.Line`-Gruppe verankert an `F1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.Column`-Gruppe verankert an `G1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.Stacked`-Gruppe (Gewinn/Verlust) verankert an `H1`, mit Datenbereich `A1:E1`.
4. Erstellen Sie eine `ImageOrPrintOptions`-Instanz und setzen Sie deren `ImageType` auf `ImageType.Png`, damit jede Sparkline als PNG-Bild gerendert wird.
6. Speichern Sie die Arbeitsmappe als `output_with_sparklines.xlsx`.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;
// Erstellen Sie eine neue Arbeitsmappe und greifen Sie auf das erste Arbeitsblatt zu
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Beispieldaten in die Zellen A1:E1 einfügen
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Fügen Sie eine Linien-Sparkline-Gruppe hinzu, verankert bei F1 (Spalte 5, Zeile 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
// Fügen Sie eine Säulen-Sparkline-Gruppe hinzu, verankert bei G1 (Spalte 6, Zeile 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
// Fügen Sie eine Gewinn/Verlust (gestapelte) Sparkline-Gruppe hinzu, verankert bei H1 (Spalte 7, Zeile 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
// Bildoptionen für die PNG-Ausgabe konfigurieren
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;
// Konvertieren Sie die Linien-Sparkline in ein Bild und betten Sie es in Zelle F2 ein
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}
// Konvertieren Sie die Säulen-Sparkline in ein Bild und betten Sie es in Zelle G2 ein
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}
// Konvertieren Sie die Gewinn/Verlust-Sparkline in ein Bild und betten Sie es in Zelle H2 ein
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}
// Speichern Sie die Arbeitsmappe auf der Festplatte
workbook.Save("output_with_sparklines.xlsx");
```

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen existiert: die aktive, native Sparkline, die an Zeile 1 verankert ist, und ein statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder innerhalb der Datei selbst leben, bleibt die Arbeitsmappe ein einzelnes in sich geschlossenes Artefakt, das per E-Mail versendet oder archiviert werden kann, ohne dass die eingebetteten Bildreferenzen verloren gehen.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe an einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.Sparklines[0]` ansprechen, anstatt mit `foreach` zu enumerieren. Dies hält den Rendering-Code kurz und entspricht dem typischen Muster „eine Sparkline pro Ankerzelle". Das Speichern der Bildbytes über `Cell.EmbeddedImage` erfordert Aspose.Cells 26.5 oder höher.

## **Workflow 2 — Das Sparkline-Arbeitsblatt nach HTML exportieren**
Sobald die Arbeitsmappe aktive Sparklines (und optional eingebettete Bildgegenstücke) enthält, kann das gesamte Arbeitsblatt im Web veröffentlicht werden, indem es als HTML gespeichert wird. Die Klasse `HtmlSaveOptions` bietet die Optionen, die Sie zur Steuerung dieses Exports benötigen; in diesem Workflow verwenden Sie die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` wieder und konvertieren sie in ein sauberes, einseitiges HTML-Dokument.

### **Schritt-für-Schritt-Anleitung**
1. Stellen Sie sicher, dass die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` in Ihrem Arbeitsverzeichnis auf der Festplatte verfügbar ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und setzen Sie deren Eigenschaft `ExportActiveWorksheetOnly` auf `true`, damit die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
4. Rufen Sie `workbook.Save("sparklines.html", htmlOptions)` auf, um die HTML-Ausgabe auf die Festplatte zu schreiben.

```csharp
using System;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

Der obige Code nimmt die sparklinereiche Arbeitsmappe aus Workflow 1 und verwandelt sie in eine portable HTML-Datei. Die Sparkline-Gruppen werden als Inline-Bilder in der generierten HTML-Tabelle gerendert, sodass Endbenutzer die Trends in jedem modernen Browser anzeigen können, ohne dass Excel installiert sein muss. Durch Setzen von `ExportActiveWorksheetOnly` auf `true` vermeiden Sie versehentliches Veröffentlichen versteckter Blätter oder Hilfsdaten — nur das aktuell für den Benutzer sichtbare Arbeitsblatt wird exportiert.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, wie z. B. `ExportHiddenWorksheet`, `ExportImagesAsBase64` und `Encoding`. Passen Sie diese nach Bedarf für Ihr Bereitstellungsziel an.

## **API-Zusammenfassung**
Die obigen Workflows stützen sich auf einen kleinen Satz von Aspose.Cells-APIs, die zusammenarbeiten.
- `SparklineGroup` und der Sammlungs-Accessor `worksheet.SparklineGroups` werden verwendet, um den Typ (Linie, Spalte, Gestapelt), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe zu deklarieren. In diesem Artikel ist jede Gruppe an einer einzelnen Zelle verankert, sodass die Gruppe über `worksheet.SparklineGroups[i]` erreicht wird.
- `Sparkline` und der Indexer `group.Sparklines[0]` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine `foreach`-Schleife erforderlich.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline in einen bereitgestellten `Stream` schreibt. Die Methode gibt `void` zurück; Sie lesen die Bytes nach dem Aufruf aus dem Stream.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (ein `bool`) beschränkt den HTML-Export auf das aktive Arbeitsblatt. Es ist eine der am häufigsten verwendeten Eigenschaften von `HtmlSaveOptions` bei der Erstellung einseitiger Berichte.
- `ImageOrPrintOptions.ImageType` befindet sich im Namespace `Aspose.Cells.Drawing` und wählt das Bildformat (zum Beispiel `ImageType.Png`) aus, das beim Rendern mit `ToImage` und beim Drucken von Arbeitsblättern in Bilder verwendet wird.

## **Verwandte Artikel**
- [Erstellen von Sparklines in Aspose.Cells for .NET](/de/net/creating-sparklines/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}