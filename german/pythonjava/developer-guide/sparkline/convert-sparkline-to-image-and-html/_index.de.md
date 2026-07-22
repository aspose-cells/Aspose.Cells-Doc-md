---
title: Sparkline in Aspose.Cells for Python via Java in Bild und HTML konvertieren
linktitle: Convert Sparkline to Image and HTML
description: Erfahren Sie, wie Sie Aspose.Cells-Sparklines als eigenständige Bilder für die Zelleneinbettung rendern und Sparkline-reiche Arbeitsblätter mit HtmlSaveOptions in HTML exportieren.
keywords: Aspose.Cells, Python via Java, Sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, Sparkline rendern, Sparkline in Bild konvertieren, Sparkline nach HTML exportieren
type: docs
weight: 120
url: /de/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die innerhalb von Arbeitsblattzellen platziert werden. Aspose.Cells ermöglicht es Ihnen, jede Sparkline als eigenständiges Bild zu extrahieren (zum Einbetten in eine andere Zelle oder einen externen Bericht) und außerdem das gesamte Sparkline-reiche Arbeitsblatt für die browserbasierte Verteilung nach HTML zu exportieren. Die in diesem Artikel verwendete Eigenschaft `Cell.embedded_image` ist in **Aspose.Cells 26.5 und höher** verfügbar.
{{% /alert %}}

## **Einführung**

Sparklines sind eine kompakte Möglichkeit, Trends direkt innerhalb eines Arbeitsblatts zu visualisieren. Während Excel-Benutzer sie an Ort und Stelle sehen, erfordern viele reale Szenarien, dass eine Sparkline die Zelle verlässt – beispielsweise um als statisches Bild in eine andere Zelle eingebettet, an eine automatisierte E-Mail angehängt oder als Teil eines HTML-Berichts im Web veröffentlicht zu werden.

Aspose.Cells unterstützt diese beiden Vorgänge. Die Methode `Sparkline.to_image` rendert eine einzelne Sparkline in einen Stream, und die resultierenden Bytes können `Cell.embedded_image` zugewiesen werden, sodass das Bild in einer einzelnen Zelle der Arbeitsmappe gespeichert wird. Separat ermöglicht es `HtmlSaveOptions`, die gesamte Arbeitsmappe – einschließlich der Sparklines – in eine in sich geschlossene HTML-Datei zu konvertieren. Dieser Artikel führt Sie Schritt für Schritt durch beide Workflows.

## **Workflow 1 – Sparklines als Bilder rendern und in Zellen einbetten**

In diesem Workflow erstellen Sie ein Arbeitsblatt, das einen kleinen Bereich mit Quellwerten enthält, fügen drei verschiedene Sparkline-Gruppen (Linie, Spalte und Gestapelt/Gewinn-Verlust) an diesen Bereich an, rendern jede Gruppe als PNG und schreiben diese PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die Live-Sparklines als auch deren gerenderte Bildentsprechungen enthält.

### **Schritt-für-Schritt-Anleitung**

1. Definieren Sie ein Arbeitsverzeichnis und stellen Sie sicher, dass es auf der Festplatte vorhanden ist.
2. Erstellen Sie eine neue `Workbook` und holen Sie sich eine Referenz auf das erste `Worksheet`.
3. Befüllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispieldatenwerten (zum Beispiel tägliche Verkaufszahlen oder Temperaturmessungen).
4. Fügen Sie dem Arbeitsblatt drei `SparklineGroup`-Objekte hinzu, indem Sie `worksheet.sparkline_groups.add(...)` aufrufen:
   - Eine `SparklineType.LINE`-Gruppe, verankert bei `F1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.COLUMN`-Gruppe, verankert bei `G1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.STACKED`-Gruppe (Gewinn/Verlust), verankert bei `H1`, mit Datenbereich `A1:E1`.
5. Erstellen Sie eine `ImageOrPrintOptions`-Instanz und setzen Sie deren `image_type` auf `ImageType.PNG`, sodass jede Sparkline als transparentes PNG gerendert wird.
6. Rendern Sie für jede der drei Gruppen deren einzelne Sparkline mit `group.sparklines[0].to_image(byte_array_output_stream, image_options)`, konvertieren Sie den `ByteArrayOutputStream` in ein `byte[]` (oder lesen Sie dessen `to_byte_array()` in Python-`bytes`) und weisen Sie die Bytes jeweils `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` und `worksheet.cells["H2"].embedded_image` zu.
7. Speichern Sie die Arbeitsmappe als `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# Erstellen Sie eine neue Arbeitsmappe und greifen Sie auf das erste Arbeitsblatt zu
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Beispieldaten in den Zellen A1:E1 einfügen
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Fügen Sie eine Liniendiagramm-Sparkline-Gruppe hinzu, die bei F1 verankert ist (Spalte 5, Zeile 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# Fügen Sie eine Spaltendiagramm-Sparkline-Gruppe hinzu, die bei G1 verankert ist (Spalte 6, Zeile 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# Fügen Sie eine Win/Loss (Gestapelt) Sparkline-Gruppe hinzu, die bei H1 verankert ist (Spalte 7, Zeile 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# Bildoptionen für die PNG-Ausgabe konfigurieren
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# Konvertieren Sie die Liniendiagramm-Sparkline in ein Bild und betten Sie es in Zelle F2 ein
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# Konvertieren Sie die Spaltendiagramm-Sparkline in ein Bild und betten Sie es in Zelle G2 ein
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# Konvertieren Sie die Win/Loss-Sparkline in ein Bild und betten Sie es in Zelle H2 ein
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# Speichern Sie die Arbeitsmappe auf der Festplatte
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen dupliziert wird: die Live-, native Sparkline, verankert in Zeile 1, und ein statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder innerhalb der Datei selbst leben, bleibt die Arbeitsmappe ein einzelnes in sich geschlossenes Artefakt, das per E-Mail versendet oder archiviert werden kann, ohne dass die eingebetteten Bildreferenzen verloren gehen. Rendern Sie jede Sparkline-Gruppe als PNG, konvertieren Sie den `ByteArrayOutputStream` in ein `byte[]` (oder verwenden Sie `to_byte_array()`, um ein Python-`bytes`-Objekt zu erhalten), und weisen Sie das Array der Eigenschaft `embedded_image` der Zielzelle zu – die Zuweisung ist es, die das Bild zum gespeicherten Inhalt der Zelle macht.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe an einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.sparklines[0]` ansprechen, anstatt mit einer `for`-Schleife zu enumerieren. Dies hält den Rendering-Code kurz und entspricht dem typischen Muster "eine Sparkline pro Ankerzelle". Das Speichern der Bildbytes über `Cell.embedded_image` erfordert Aspose.Cells 26.5 oder höher.
{{% /alert %}}

## **Workflow 2 – Das Sparkline-Arbeitsblatt nach HTML exportieren**

Sobald die Arbeitsmappe Live-Sparklines (und optional eingebettete Bildentsprechungen) enthält, kann das gesamte Arbeitsblatt im Web veröffentlicht werden, indem es als HTML gespeichert wird. Die Klasse `HtmlSaveOptions` bietet die Einstellungen, die Sie zur Steuerung dieses Exports benötigen; in diesem Workflow verwenden Sie die in Workflow 1 erstellte Datei `output_with_sparklines.xlsx` erneut und konvertieren sie in ein sauberes, einseitiges HTML-Dokument.

### **Schritt-für-Schritt-Anleitung**

1. Stellen Sie sicher, dass die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` auf der Festplatte in Ihrem Arbeitsverzeichnis verfügbar ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und setzen Sie deren Eigenschaft `export_active_worksheet_only` auf `True`, sodass die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
4. Rufen Sie `workbook.save("sparklines.html", html_options)` auf, um die HTML-Ausgabe auf die Festplatte zu schreiben.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

Der obige Code nimmt die Sparkline-reiche Arbeitsmappe aus Workflow 1 und verwandelt sie in eine portable HTML-Datei. Sparklines werden je nach Exportmodus als Inline-SVG- oder PNG-Renderings innerhalb des erzeugten HTML beibehalten, sodass Endbenutzer die Trends in jedem modernen Browser anzeigen können, ohne dass Excel installiert sein muss. Durch das Setzen von `export_active_worksheet_only` auf `True` vermeiden Sie es, versehentlich versteckte Blätter oder Hilfsdaten zu veröffentlichen – nur das aktuell für den Benutzer sichtbare Arbeitsblatt wird exportiert.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, wie `export_hidden_worksheet`, `export_images_as_base64` und `encoding`. Passen Sie diese nach Bedarf für Ihr Bereitstellungsziel an.
{{% /alert %}}

## **API-Zusammenfassung**

Die oben beschriebenen Workflows beruhen auf einer kleinen Reihe von Aspose.Cells-APIs, die zusammenarbeiten.

- `SparklineGroup` und der Sammlungs-Accessor `worksheet.sparkline_groups` werden verwendet, um den Typ (Linie, Spalte, Gestapelt), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe zu deklarieren. In diesem Artikel ist jede Gruppe an einer einzelnen Zelle verankert, sodass die Gruppe über `worksheet.sparkline_groups[i]` erreicht wird.
- `Sparkline` und der Indexer `group.sparklines[0]` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine `for`-Schleife erforderlich.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline in einen bereitgestellten `OutputStream` (wie einen `ByteArrayOutputStream`) schreibt. Die Methode gibt `void` zurück; Sie lesen die Bytes nach dem Aufruf aus dem Stream.
- `Cell.embedded_image` ist eine `byte[]`-Eigenschaft, die ein Bild in einer einzelnen Zelle speichert. Sie ist in **Aspose.Cells 26.5 und höher** verfügbar und ist die empfohlene Methode, um eine mit `to_image` gerenderte Sparkline zurück in dieselbe Arbeitsmappe zu übertragen.
- `HtmlSaveOptions.export_active_worksheet_only` (ein `bool`) beschränkt den HTML-Export auf das aktive Arbeitsblatt. Es ist eine der am häufigsten verwendeten Eigenschaften von `HtmlSaveOptions`, wenn einseitige Berichte erzeugt werden.
- `ImageOrPrintOptions.image_type` befindet sich im Namespace `com.aspose.cells.drawing` und wählt das Bildformat (zum Beispiel `ImageType.PNG`) aus, das beim Rendern mit `to_image` und beim Drucken von Arbeitsblättern als Bilder verwendet wird.

## **Verwandte Artikel**

- [Sparklines in Aspose.Cells for Python via Java](/cells/de/python-java/sparkline/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}