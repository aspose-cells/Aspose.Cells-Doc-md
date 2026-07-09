---
title: Sparkline in Bild und HTML konvertieren in Aspose.Cells for C++
linktitle: Convert Sparkline to Image and HTML
description: Erfahren Sie, wie Sie Aspose.Cells-Sparklines als eigenständige Bilder für die Zelleneinbettung rendern und sparkline-reiche Arbeitsblätter mit HtmlSaveOptions als HTML exportieren.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, Sparkline rendern, Sparkline in Bild konvertieren, Sparkline nach HTML exportieren
type: docs
weight: 120
url: /de/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die innerhalb von Arbeitsblattzellen platziert werden. Aspose.Cells ermöglicht es Ihnen, jede Sparkline als eigenständiges Bild zu extrahieren (zum Einbetten in eine andere Zelle oder einen externen Bericht) und das gesamte sparkline-reiche Arbeitsblatt zur browserbasierten Verteilung als HTML zu exportieren. Die in diesem Artikel verwendete Eigenschaft `Cell.EmbeddedImage` ist ab **Aspose.Cells 26.5 und höher** verfügbar.
{{% /alert %}}

## **Einführung**

Sparklines sind eine kompakte Möglichkeit, Trends direkt innerhalb eines Arbeitsblatts zu visualisieren. Während Excel-Benutzer sie an Ort und Stelle sehen, erfordern viele reale Szenarien, dass eine Sparkline die Zelle verlässt – beispielsweise um als statisches Bild in eine andere Zelle eingebettet, an eine automatisierte E-Mail angehängt oder als Teil eines HTML-Berichts für das Web gerendert zu werden.

Aspose.Cells unterstützt beide dieser Operationen. Die Methode `Sparkline.ToImage` rendert eine einzelne Sparkline in einen Stream, und die resultierenden Bytes können `Cell.EmbeddedImage` zugewiesen werden, sodass das Bild innerhalb einer einzelnen Zelle der Arbeitsmappe gespeichert wird. Separat ermöglicht es `HtmlSaveOptions`, die gesamte Arbeitsmappe – einschließlich Sparklines – in eine in sich geschlossene HTML-Datei zu konvertieren. Dieser Artikel führt Sie Schritt für Schritt durch beide Arbeitsabläufe.

## **Arbeitsablauf 1 – Sparklines als Bilder rendern und in Zellen einbetten**

In diesem Arbeitsablauf erstellen Sie ein Arbeitsblatt, das einen kleinen Bereich mit Quellwerten enthält, fügen drei verschiedene Sparkline-Gruppen (Linie, Spalte und Gestapelt/Gewinn-Verlust) an diesen Bereich an, rendern jede Gruppe als PNG und schreiben diese PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die aktiven Sparklines als auch ihre gerenderten Bildentsprechungen enthält.

### **Schritt-für-Schritt-Anleitung**

1. Definieren Sie ein Arbeitsverzeichnis und stellen Sie sicher, dass es auf der Festplatte vorhanden ist.
2. Erstellen Sie eine neue `Workbook` und holen Sie sich eine Referenz auf das erste `Worksheet`.
3. Befüllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispielwerten (z. B. tägliche Verkaufszahlen oder Temperaturmessungen).
4. Fügen Sie dem Arbeitsblatt drei `SparklineGroup`-Objekte hinzu, indem Sie `worksheet.SparklineGroups.Add(...)` aufrufen:
   - Eine `SparklineType.Line`-Gruppe verankert bei `F1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.Column`-Gruppe verankert bei `G1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.Stacked` (Gewinn/Verlust)-Gruppe verankert bei `H1`, mit Datenbereich `A1:E1`.
5. Erstellen Sie eine Instanz von `ImageOrPrintOptions` und setzen Sie deren `ImageType` auf `ImageType.Png`, damit jede Sparkline als transparentes PNG gerendert wird.
6. Rendern Sie für jede der drei Gruppen deren einzelne Sparkline mit `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, konvertieren Sie den `MemoryStream` in einen `Vector<uint8_t>` und weisen Sie das Array jeweils `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` und `worksheet.Cells["H2"].EmbeddedImage` zu.
7. Speichern Sie die Arbeitsmappe als `output_with_sparklines.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);

    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);

    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);

    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);

    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);

    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);

    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);

    workbook.Save(u"output_with_sparklines.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen dupliziert wird: die aktive, native Sparkline, verankert in Zeile 1, und ein statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder innerhalb der Datei selbst leben, bleibt die Arbeitsmappe ein einzelnes in sich geschlossenes Artefakt, das per E-Mail versendet oder archiviert werden kann, ohne dass die Verweise auf eingebettete Bilder verloren gehen. Rendern Sie jede Sparkline-Gruppe als PNG, konvertieren Sie den `MemoryStream` in einen `Vector<uint8_t>` und weisen Sie das Array der Eigenschaft `EmbeddedImage` der Zielzelle zu – die Zuweisung ist das, was das Bild Teil des gespeicherten Inhalts der Zelle werden lässt.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe in einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.Sparklines[0]` ansprechen, anstatt mit `foreach` zu enumerieren. Dies hält den Rendering-Code kurz und entspricht dem typischen Muster „eine Sparkline pro Ankerzelle". Das Speichern der Bildbytes über `Cell.EmbeddedImage` erfordert Aspose.Cells 26.5 oder höher.
{{% /alert %}}

## **Arbeitsablauf 2 – Das Sparkline-Arbeitsblatt nach HTML exportieren**

Sobald die Arbeitsmappe aktive Sparklines (und optional eingebettete Bildentsprechungen) enthält, kann das gesamte Arbeitsblatt ins Web veröffentlicht werden, indem es als HTML gespeichert wird. Die Klasse `HtmlSaveOptions` bietet die Einstellungen, die Sie zur Steuerung dieses Exports benötigen; in diesem Arbeitsablauf verwenden Sie die in Arbeitsablauf 1 erzeugte Datei `output_with_sparklines.xlsx` erneut und konvertieren sie in ein sauberes, einseitiges HTML-Dokument.

### **Schritt-für-Schritt-Anleitung**

1. Stellen Sie sicher, dass die in Arbeitsablauf 1 erzeugte Datei `output_with_sparklines.xlsx` in Ihrem Arbeitsverzeichnis auf der Festplatte verfügbar ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und setzen Sie die Eigenschaft `ExportActiveWorksheetOnly` auf `true`, damit die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
4. Rufen Sie `workbook.Save("sparklines.html", htmlOptions)` auf, um die HTML-Ausgabe auf die Festplatte zu schreiben.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Der obige Code nimmt die sparkline-reiche Arbeitsmappe aus Arbeitsablauf 1 und verwandelt sie in eine portable HTML-Datei. Sparklines werden je nach Exportmodus als Inline-SVG- oder PNG-Renderings innerhalb des generierten HTML beibehalten, sodass Endbenutzer die Trends in jedem modernen Browser anzeigen können, ohne Excel installiert zu haben. Durch das Setzen von `ExportActiveWorksheetOnly` auf `true` vermeiden Sie es, versehentlich versteckte Blätter oder Hilfsdaten zu veröffentlichen – es wird nur das aktuell für den Benutzer sichtbare Arbeitsblatt exportiert.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, wie z. B. `ExportHiddenWorksheet`, `ExportImagesAsBase64` und `Encoding`. Passen Sie diese nach Bedarf für Ihr Bereitstellungsziel an.
{{% /alert %}}

## **API-Zusammenfassung**

Die oben beschriebenen Arbeitsabläufe beruhen auf einer kleinen Reihe von Aspose.Cells-APIs, die zusammenarbeiten.

- `SparklineGroup` und der Sammlungs-Accessor `worksheet.SparklineGroups` werden verwendet, um den Typ (Linie, Spalte, Gestapelt), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe zu deklarieren. In diesem Artikel ist jede Gruppe in einer einzelnen Zelle verankert, sodass die Gruppe über `worksheet.SparklineGroups[i]` erreicht wird.
- `Sparkline` und der Indexer `group.Sparklines[0]` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine `foreach`-Schleife erforderlich.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline in einen bereitgestellten `Stream` schreibt. Die Methode gibt `void` zurück; Sie lesen die Bytes nach dem Aufruf aus dem Stream.
- `Cell.EmbeddedImage` ist eine Eigenschaft vom Typ `Vector<uint8_t>`, die ein Bild innerhalb einer einzelnen Zelle speichert. Sie ist ab **Aspose.Cells 26.5 und höher** verfügbar und ist die empfohlene Methode, um eine mit `ToImage` gerenderte Sparkline zurück in dieselbe Arbeitsmappe zu übertragen.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (ein `bool`) beschränkt den HTML-Export auf das aktive Arbeitsblatt. Es ist eine der am häufigsten verwendeten Eigenschaften von `HtmlSaveOptions` bei der Erstellung von einseitigen Berichten.
- `ImageOrPrintOptions.ImageType` befindet sich im Namespace `Aspose.Cells.Drawing` und wählt das Bildformat (z. B. `ImageType.Png`), das beim Rendern mit `ToImage` und beim Drucken von Arbeitsblättern als Bilder verwendet wird.

## **Verwandte Artikel**

- [Sparklines in Aspose.Cells for Aspose.Cells for C++](/cells/de/cpp/sparkline/)
- [Bild in eine Zelle einfügen](/cells/de/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells for C++](/cells/de/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}