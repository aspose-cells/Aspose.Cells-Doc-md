---
title: Sparklines in Bild und HTML konvertieren in Aspose.Cells for Python via .NET
linktitle: Convert Sparkline to Image and HTML
description: Erfahren Sie, wie Sie Aspose.Cells-Sparklines als eigenständige Bilder zum Einbetten in Zellen rendern und Sparkline-reiche Arbeitsblätter mithilfe von HtmlSaveOptions in Python via .NET nach HTML exportieren.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, sparkline rendern, sparkline in Bild konvertieren, sparkline nach HTML exportieren
type: docs
weight: 120
url: /de/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die in Arbeitsblattzellen platziert werden. Aspose.Cells ermöglicht es Ihnen, jede Sparkline als eigenständiges Bild zu extrahieren (zur Einbettung in eine andere Zelle oder einen externen Bericht) und das gesamte Sparkline-reiche Arbeitsblatt nach HTML zu exportieren, um es browserbasiert zu verteilen. Die in diesem Artikel verwendete Eigenschaft `cell.embedded_image` ist in **Aspose.Cells 26.5 und höher** verfügbar.
{{% /alert %}}

## **Einführung**

Sparklines sind eine kompakte Möglichkeit, Trends direkt in einem Arbeitsblatt zu visualisieren. Während Excel-Benutzer sie an Ort und Stelle sehen, erfordern viele reale Szenarien, dass eine Sparkline die Zelle verlässt – zum Beispiel, um als statisches Bild in eine andere Zelle eingebettet, an eine automatisierte E-Mail angehängt oder als Teil eines HTML-Berichts gerendert zu werden, der im Web veröffentlicht wird.

Aspose.Cells unterstützt diese beiden Operationen. Die Methode `sparkline.to_image` rendert eine einzelne Sparkline in einen Stream, und die resultierenden Bytes können `cell.embedded_image` zugewiesen werden, sodass das Bild in einer einzelnen Zelle der Arbeitsmappe gespeichert wird. Separat ermöglicht es `HtmlSaveOptions`, die gesamte Arbeitsmappe – einschließlich der Sparklines – in eine in sich geschlossene HTML-Datei zu konvertieren. Dieser Artikel führt Sie Schritt für Schritt durch beide Workflows.

## **Workflow 1 – Sparklines als Bilder rendern und in Zellen einbetten**

In diesem Workflow erstellen Sie ein Arbeitsblatt, das einen kleinen Bereich mit Quellwerten enthält, hängen drei verschiedene Sparkline-Gruppen (Linie, Spalte und Gestapelt/Gewinn-Verlust) an diesen Bereich an, rendern jede Gruppe als PNG und schreiben diese PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die Live-Sparklines als auch ihre gerenderten Bildgegenstücke enthält.

### **Schritt-für-Schritt-Anleitung**

1. Definieren Sie ein Arbeitsverzeichnis und stellen Sie sicher, dass es auf der Festplatte existiert.
2. Erstellen Sie eine neue `Workbook` und holen Sie sich eine Referenz auf das erste `Worksheet`.
3. Füllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispielwerten (zum Beispiel tägliche Verkaufszahlen oder Temperaturmessungen).
4. Fügen Sie dem Arbeitsblatt drei `SparklineGroup`-Objekte hinzu, indem Sie `worksheet.sparkline_groups.add(...)` aufrufen:
   - Eine `SparklineType.LINE`-Gruppe verankert bei `F1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.COLUMN`-Gruppe verankert bei `G1`, mit Datenbereich `A1:E1`.
   - Eine `SparklineType.STACKED`-Gruppe (Gewinn/Verlust) verankert bei `H1`, mit Datenbereich `A1:E1`.
5. Erstellen Sie eine `ImageOrPrintOptions`-Instanz und setzen Sie deren `image_type` auf `ImageType.PNG`, damit jede Sparkline als transparentes PNG gerendert wird.
6. Rendern Sie für jede der drei Gruppen ihre einzelne Sparkline mit `group.sparklines[0].to_image(memory_stream, image_options)`, konvertieren Sie den `BytesIO`-Stream in ein `bytes`-Objekt und weisen Sie das Array jeweils `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` und `worksheet.cells["H2"].embedded_image` zu.
7. Speichern Sie die Arbeitsmappe als `output_with_sparklines.xlsx`.

```python
import aspose.cells as ac

# Erstellen Sie eine neue Arbeitsmappe und greifen Sie auf das erste Arbeitsblatt zu
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Füllen Sie Beispieldaten in die Zellen A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Fügen Sie eine Linien-Sparkline-Gruppe hinzu, die an F1 verankert ist (Spalte 5, Zeile 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# Fügen Sie eine Spalten-Sparkline-Gruppe hinzu, die an G1 verankert ist (Spalte 6, Zeile 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# Fügen Sie eine Gewinn/Verlust (gestapelte) Sparkline-Gruppe hinzu, die an H1 verankert ist (Spalte 7, Zeile 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# Konfigurieren Sie die Bildoptionen für die PNG-Ausgabe
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Konvertieren Sie die Linien-Sparkline in ein Bild und betten Sie es in die Zelle F2 ein
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Konvertieren Sie die Spalten-Sparkline in ein Bild und betten Sie es in die Zelle G2 ein
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Konvertieren Sie die Gewinn/Verlust-Sparkline in ein Bild und betten Sie es in die Zelle H2 ein
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Speichern Sie die Arbeitsmappe auf der Festplatte
workbook.save("output_with_sparklines.xlsx")
```

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen dupliziert wird: die Live-, native Sparkline, verankert in Zeile 1, und ein statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder in der Datei selbst gespeichert sind, bleibt die Arbeitsmappe ein einzelnes, in sich geschlossenes Artefakt, das per E-Mail versendet oder archiviert werden kann, ohne dass die eingebetteten Bildreferenzen ungültig werden. Rendern Sie jede Sparkline-Gruppe als PNG, konvertieren Sie den `BytesIO`-Stream in ein `bytes`-Objekt und weisen Sie die Bytes der Eigenschaft `embedded_image` der Zielzelle zu – die Zuweisung ist das, was das Bild zum gespeicherten Inhalt der Zelle macht.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe in einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.sparklines[0]` ansprechen, anstatt sie mit einer `for`-Schleife zu durchlaufen. Dies hält den Rendering-Code kurz und entspricht dem typischen Muster „eine Sparkline pro Ankerzelle". Das Speichern der Bildbytes über `cell.embedded_image` erfordert Aspose.Cells 26.5 oder höher.
{{% /alert %}}

## **Workflow 2 – Das Sparkline-Arbeitsblatt nach HTML exportieren**

Sobald die Arbeitsmappe Live-Sparklines (und optional eingebettete Bildgegenstücke) enthält, kann das gesamte Arbeitsblatt im Web veröffentlicht werden, indem es als HTML gespeichert wird. Die Klasse `HtmlSaveOptions` bietet die Optionen, die Sie zur Steuerung dieses Exports benötigen; in diesem Workflow verwenden Sie die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` erneut und konvertieren sie in ein sauberes, einseitiges HTML-Dokument.

### **Schritt-für-Schritt-Anleitung**

1. Stellen Sie sicher, dass die in Workflow 1 erzeugte Datei `output_with_sparklines.xlsx` in Ihrem Arbeitsverzeichnis auf der Festplatte verfügbar ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und setzen Sie deren Eigenschaft `export_active_worksheet_only` auf `True`, sodass die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
4. Rufen Sie `workbook.save("sparklines.html", html_options)` auf, um die HTML-Ausgabe auf die Festplatte zu schreiben.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

Der obige Code nimmt die Sparkline-reiche Arbeitsmappe aus Workflow 1 und verwandelt sie in eine portable HTML-Datei. Sparklines werden je nach Exportmodus als Inline-SVG- oder PNG-Renderings im generierten HTML beibehalten, sodass Endbenutzer die Trends in jedem modernen Browser anzeigen können, ohne dass Excel installiert sein muss. Durch Setzen von `export_active_worksheet_only` auf `True` vermeiden Sie es, versehentlich versteckte Arbeitsblätter oder Hilfsdaten zu veröffentlichen – es wird nur das für den Benutzer aktuell sichtbare Arbeitsblatt exportiert.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, wie z. B. `export_hidden_worksheet`, `export_images_as_base64` und `encoding`. Passen Sie diese nach Bedarf für Ihr Bereitstellungsziel an.
{{% /alert %}}

## **API-Zusammenfassung**

Die obigen Workflows stützen sich auf eine kleine Auswahl von Aspose.Cells-APIs, die zusammenarbeiten.

- `SparklineGroup` und der Collection-Accessor `worksheet.sparkline_groups` werden verwendet, um den Typ (Linie, Spalte, Gestapelt), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe zu deklarieren. In diesem Artikel ist jede Gruppe in einer einzelnen Zelle verankert, sodass die Gruppe über `worksheet.sparkline_groups[i]` erreicht wird.
- `Sparkline` und der Indexer `group.sparklines[0]` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine `for`-Schleife erforderlich.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline in einen bereitgestellten Stream schreibt. Die Methode gibt `None` zurück; Sie lesen die Bytes nach dem Aufruf aus dem Stream.
- `cell.embedded_image` ist eine `bytes`-Eigenschaft, die ein Bild in einer einzelnen Zelle speichert. Sie ist in **Aspose.Cells 26.5 und höher** verfügbar und ist die empfohlene Methode, um eine mit `to_image` gerenderte Sparkline wieder in dieselbe Arbeitsmappe einzubinden.
- `html_save_options.export_active_worksheet_only` (ein `bool`) beschränkt den HTML-Export auf das aktive Arbeitsblatt. Es ist eine der am häufigsten verwendeten Eigenschaften von `HtmlSaveOptions` bei der Erstellung von einseitigen Berichten.
- `image_or_print_options.image_type` befindet sich im Namespace `aspose.cells.drawing` und wählt das Bildformat (zum Beispiel `ImageType.PNG`) aus, das beim Rendern mit `to_image` und beim Drucken von Arbeitsblättern als Bilder verwendet wird.

## **Verwandte Artikel**

- [Sparklines in Aspose.Cells for Python via .NET](/cells/de/python-net/sparkline/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells for Python via .NET](/cells/de/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}