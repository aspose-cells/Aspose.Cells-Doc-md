---
title: Sparklines in Aspose.Cells for C++ in Bild und HTML konvertieren
linktitle: Sparklines
description: Erfahren Sie, wie Sie Aspose.Cells-Sparklines als eigenständige Bilder zum Einbetten in Zellen rendern und sparkline-reiche Arbeitsblätter mit HtmlSaveOptions nach HTML exportieren.
keywords: Aspose.Cells, C++, Sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, Sparkline rendern, Sparkline in Bild konvertieren, Sparkline nach HTML exportieren
type: docs
weight: 120
url: /de/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die innerhalb von Arbeitsblattzellen platziert werden. Aspose.Cells ermöglicht es Ihnen, jede Sparkline als eigenständiges Bild zu extrahieren (zum Einbetten in eine andere Zelle oder einen externen Bericht) und das gesamte sparkline-reiche Arbeitsblatt für die browserbasierte Verteilung nach HTML zu exportieren. Die in diesem Artikel verwendete Eigenschaft `Cell.EmbeddedImage` ist ab **Aspose.Cells 26.5 und höher** verfügbar.

## **Einführung**
Sparklines sind eine kompakte Möglichkeit, Trends direkt in einem Arbeitsblatt zu visualisieren. Während Excel-Benutzer sie an Ort und Stelle sehen, erfordern viele reale Szenarien, dass eine Sparkline die Zelle verlässt — beispielsweise, um als statisches Bild in eine andere Zelle eingebettet, an eine automatisierte E-Mail angehängt oder als Teil eines im Web veröffentlichten HTML-Berichts gerendert zu werden.
Aspose.Cells unterstützt beide dieser Vorgänge. Die Methode `Sparkline.ToImage` rendert eine einzelne Sparkline in ein `Vector<uint8_t>`-Byte-Array, und die resultierenden Bytes können `Cell.EmbeddedImage` zugewiesen werden, sodass das Bild in einer einzelnen Zelle der Arbeitsmappe gespeichert wird. Separat ermöglicht es `HtmlSaveOptions`, die gesamte Arbeitsmappe — einschließlich der Sparklines — in eine in sich geschlossene HTML-Datei zu konvertieren. Dieser Artikel führt Sie Schritt für Schritt durch beide Workflows.

## **Workflow 1 — Sparklines als Bilder rendern und in Zellen einbetten**
In diesem Workflow erstellen Sie ein Arbeitsblatt, das einen kleinen Bereich mit Quellwerten enthält, hängen drei verschiedene Sparkline-Gruppen (Linie, Spalte und Gestapelt/Gewinn-Verlust) an diesen Bereich an, rendern jede Gruppe als PNG und schreiben diese PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die Live-Sparklines als auch ihre gerenderten Bildgegenstücke enthält.

### **Schritt-für-Schritt-Anleitung**
1. Definieren Sie ein Arbeitsverzeichnis und stellen Sie sicher, dass es auf der Festplatte vorhanden ist.
2. Erstellen Sie eine neue `Workbook` und erhalten Sie eine Referenz auf das erste `Worksheet`.
3. Füllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispielwerten (zum Beispiel tägliche Verkaufszahlen oder Temperaturmessungen).
4. Fügen Sie dem Arbeitsblatt drei `SparklineGroup`-Objekte hinzu, indem Sie `worksheet.SparklineGroups.Add(...)` aufrufen:
   - Eine `SparklineType.Line`-Gruppe verankert bei `F1` mit dem Datenbereich `A1:E1`.
   - Eine `SparklineType.Column`-Gruppe verankert bei `G1` mit dem Datenbereich `A1:E1`.
   - Eine `SparklineType.Stacked`-Gruppe (Gewinn/Verlust) verankert bei `H1` mit dem Datenbereich `A1:E1`.
5. Erstellen Sie eine Instanz von `ImageOrPrintOptions` und setzen Sie deren `ImageType` auf `ImageType.Png`, damit jede Sparkline als transparentes PNG gerendert wird.
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

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen dupliziert ist: die native Live-Sparkline, verankert in Zeile 1, und ein statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder innerhalb der Datei selbst gespeichert sind, bleibt die Arbeitsmappe ein einzelnes in sich geschlossenes Artefakt, das per E-Mail gesendet oder archiviert werden kann, ohne dass die eingebetteten Bildreferenzen beschädigt werden. Rendern Sie jede Sparkline-Gruppe als PNG — `Sparkline.ToImage(ImageOrPrintOptions)` gibt die Bildbytes direkt als `Vector<uint8_t>` zurück — und weisen Sie das Array der Eigenschaft `EmbeddedImage` der Zielzelle zu — die Zuweisung macht das Bild zum Teil der gespeicherten Inhalte der Zelle.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe in einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.Sparklines[0]` adressieren, anstatt sie mit `foreach` zu durchlaufen. Dies hält den Rendering-Code kurz und entspricht dem typischen Muster „eine Sparkline pro Ankerzelle". Das Speichern der Bildbytes über `Cell.EmbeddedImage` erfordert Aspose.Cells 26.5 oder höher.

## **Workflow 2 — Sparkline-Arbeitsblatt nach HTML exportieren**
Sobald die Arbeitsmappe Live-Sparklines (und optional eingebettete Bildgegenstücke) enthält, kann das gesamte Arbeitsblatt im Web veröffentlicht werden, indem es als HTML gespeichert wird. Die Klasse `HtmlSaveOptions` stellt die Schalter bereit, die Sie zur Steuerung dieses Exports benötigen; in diesem Workflow verwenden Sie die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` wieder und konvertieren sie in ein sauberes, einseitiges HTML-Dokument.

### **Schritt-für-Schritt-Anleitung**
1. Stellen Sie sicher, dass die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` in Ihrem Arbeitsverzeichnis auf der Festplatte verfügbar ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und setzen Sie die Eigenschaft `ExportActiveWorksheetOnly` auf `true`, sodass die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
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

Der obige Code nimmt die sparkline-reiche Arbeitsmappe aus Workflow 1 und verwandelt sie in eine portable HTML-Datei. Sparklines werden je nach Exportmodus als Inline-SVG- oder PNG-Renderings im generierten HTML bewahrt, sodass Endbenutzer die Trends in jedem modernen Browser anzeigen können, ohne dass Excel installiert sein muss. Durch das Setzen von `ExportActiveWorksheetOnly` auf `true` vermeiden Sie es, versehentlich versteckte Blätter oder Hilfsdaten zu veröffentlichen — nur das dem Benutzer aktuell sichtbare Arbeitsblatt wird exportiert.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, wie `ExportHiddenWorksheet`, `ExportImagesAsBase64` und `Encoding`. Passen Sie diese nach Bedarf für Ihr Bereitstellungsziel an.

## **API-Zusammenfassung**
Die oben beschriebenen Workflows basieren auf einer kleinen Reihe von Aspose.Cells-APIs, die zusammenarbeiten.
- `SparklineGroup` und der Sammlungs-Accessor `worksheet.SparklineGroups` werden verwendet, um den Typ (Linie, Spalte, Gestapelt), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe zu deklarieren. In diesem Artikel ist jede Gruppe in einer einzelnen Zelle verankert, sodass die Gruppe über `worksheet.SparklineGroups[i]` erreicht wird.
- `Sparkline` und der Indexer `group.Sparklines[0]` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine `foreach`-Schleife erforderlich.
- `Sparkline.ToImage(ImageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline direkt als `Vector<uint8_t>`-Byte-Array zurückgibt.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (ein `bool`) beschränkt den HTML-Export auf das aktive Arbeitsblatt. Es ist eine der am häufigsten verwendeten Eigenschaften auf `HtmlSaveOptions` beim Erstellen einseitiger Berichte.
- `ImageOrPrintOptions.ImageType` befindet sich im Namespace `Aspose.Cells.Drawing` und wählt das Bildformat (zum Beispiel `ImageType.Png`) aus, das beim Rendern mit `ToImage` und beim Drucken von Arbeitsblättern als Bilder verwendet wird.

## **Verwandte Artikel**
- [Sparklines in Aspose.Cells for C++](/cells/de/cpp/sparkline/)
- [Bild in eine Zelle einfügen](/cells/de/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker-Einzelzellen-Array-Rendering | Aspose.Cells for C++](/cells/de/cpp/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}