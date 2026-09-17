---
title: Excel-Kamera in Aspose.Cells for .NET
description: Erfahren Sie, wie Sie die Excel-Kamera in Aspose.Cells for .NET verwenden, um ein dynamisches Bild zu erstellen, das mit einem Zellbereich verknüpft ist, sich mit den Quelldaten aktualisiert und die gesamte Quellformatierung beibehält.
linktitle: Excel-Kamera
keywords: Aspose.Cells, .NET, Excel-Kamera, dynamisches Bild, verknüpftes Bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /de/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Die Excel-Kamera ist ein Arbeitsblatt-Objekt, das ein Live-Bild eines Zellbereichs rendert und wie eine gewöhnliche Grafik auf der Zeichnungsebene schwebt. Aspose.Cells unterstützt zwei Erstellungsmodi: ein dynamisches Bild, das sich automatisch aktualisiert, sobald sich die Quelldaten ändern, und ein statisches Bild, das eine einmalige Momentaufnahme eines Bereichs erfasst. Dieser Artikel führt durch beide Ansätze, damit Sie denjenigen auswählen können, der zu Ihrem Layout passt.

## Was ist die Excel-Kamera?
Die Excel-Kamera ist im Wesentlichen ein Bildobjekt, das an einer bestimmten Zeile und Spalte auf der Zeichnungsebene des Arbeitsblatts verankert ist. Im Gegensatz zu einer normal eingefügten Grafik ist die Kamera über eine A1-Formel wie `"A1:F10"` mit einem Quellbereich verknüpft. Sobald sich eine Zelle innerhalb dieses Bereichs ändert, wird das Bild der Kamera automatisch aktualisiert, um den neuen Inhalt wiederzugeben. Die Kamera bewahrt die vollständige Formatierung des Quellbereichs — Rahmen, Hintergrundfarben, Schriftarten und Zahlenformate — sodass alles, was innerhalb der Zellen sichtbar ist, auch im Bild der Kamera erscheint. Dies macht die Kamera besonders nützlich für Dashboards, Zusammenfassungen, Seitenleisten und Berichtslayouts, bei denen Sie eine sichtbare Vorschau eines entfernten Bereichs wünschen, ohne zu scrollen oder Daten zu wiederholen. Zwei Einschränkungen gelten: Sie müssen `UpdateSelectedValue()` vor dem Speichern der Arbeitsmappe aufrufen, und die Datei wird nach HTML oder PDF exportiert, da diese Formate auf den eingebetteten Bilddaten beruhen und nicht auf einer Live-Neuberechnung.

## Methode 1 — Dynamisches Kamerabild hinzufügen
Die dynamische Kamera ist der häufigste Ansatz und kommt dem in Excel integrierten Kamerawerkzeug am nächsten. Sie funktioniert, indem eine Grafik ohne anfänglichen Bildinhalt hinzugefügt und ihr dann eine `Formula` zugewiesen wird, die auf den Quellbereich verweist. Nachdem die Formel zugewiesen wurde, aktualisiert der Aufruf von `UpdateSelectedValue()` die eingebetteten Bilddaten, sodass sie mit den gespiegelten Zellen synchron sind. Die Kamera wird nicht durch eine dedizierte Klasse implementiert — sie basiert vollständig auf dem Standardtyp `Picture`.
Die wichtigsten APIs sind:
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — fügt eine Grafik hinzu, die an der angegebenen Zeile und Spalte verankert ist. Die Übergabe von `null` für den Parameter `stream` erstellt eine leere Grafik, die als Platzhalter für eine dynamische Kamera dient. Die Methode gibt den Index der neuen Grafik zurück.
- `worksheet.Pictures[index]` — Indexer-Zugriff, um eine bestimmte `Picture` aus der Sammlung abzurufen.
- `Picture.Formula` — eine String-Eigenschaft (get/set), die die A1-Referenz auf den Quellbereich enthält, den die Kamera spiegelt, z. B. `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — eine Void-Methode, die die eingebetteten Bilddaten aus den von `Formula` referenzierten Zellen aktualisiert.

{{% alert color="primary" %}}
`UpdateSelectedValue()` MUSS vor dem Speichern aufgerufen werden, wenn die Ausgabe HTML oder PDF ist; andernfalls enthält die exportierte Datei keine Bilddaten und die Kamera erscheint in der gerenderten Ausgabe leer.
{{% /alert %}}

Der folgende Code erstellt eine Arbeitsmappe, fügt eine leere Grafik verankert an Zeile 10 Spalte 6 hinzu, verknüpft sie über die Eigenschaft `Formula` mit dem Quellbereich `A1:F10`, aktualisiert die eingebetteten Bilddaten und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Dynamische Kamera: ein leeres Bild hinzufügen, über eine Formel mit A1:F10 verknüpfen und dann aktualisieren
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Methode 2 — Statisches Kamerabild hinzufügen
Die statische Kamera ist im Wesentlichen eine einmal gerenderte Vorschau eines Zellbereichs. Anstatt eine Live-Verknüpfung aufrechtzuerhalten, rendern Sie den Bereich einmal in Bildbytes, umschließen diese Bytes in einem `MemoryStream` und fügen sie als gewöhnliche Grafik hinzu. Der Bildinhalt ist dann zum Zeitpunkt der Erstellung festgelegt und wird nicht automatisch aktualisiert, wenn sich die Quellzellen ändern.
Die wichtigsten APIs sind:
- `Cells.CreateRange(string address)` — erstellt ein `Range`-Objekt aus einer A1-Adresse wie `"A1:F10"`.
- `Range.ToImage(ImageOrPrintOptions options)` — rendert den Bereich in Bildbytes. Die Übergabe von `null` verwendet die Standard-Rendering-Optionen; es existieren Überladungen für eine feinere Steuerung der Ausgabe.
- `new MemoryStream(byte[] buffer)` — umschließt die gerenderten Bildbytes in einem `MemoryStream`, der in `PictureCollection.Add` eingespeist werden kann.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — fügt die Grafik verankert an der angegebenen Zeile und Spalte hinzu, diesmal unter Übergabe des durch das Rendering erzeugten `MemoryStream`.
Der folgende Code erstellt eine Arbeitsmappe, erstellt einen `Range` für `A1:F10`, rendert ihn durch `Range.ToImage(null)` in Bildbytes, umschließt die Bytes in einem `MemoryStream`, fügt die Grafik verankert an Zeile 10 Spalte 6 hinzu und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Statische Kamera: Bereich erstellen, in Bytes rendern, in MemoryStream einwickeln, als Bild hinzufügen
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Wahl zwischen dynamisch und statisch
- **Dynamische Kamera:** aktualisiert sich bei jeder Neuberechnung, unterstützt den Export nach HTML und PDF nach `UpdateSelectedValue()` und bewahrt das Live-Link-Verhalten über die gesamte Lebensdauer der Datei.
- **Statische Kamera:** ein einmaliges Rendering, das nie aktualisiert wird, nützlich, wenn Sie eine feste visuelle Momentaufnahme eingebettet zur Build-Zeit wünschen, anstelle einer Live-Spiegelung der Daten.
Aspose.Cells unterstützt sowohl eine dynamische, sich automatisch aktualisierende Kamera, die auf `Picture.Formula` plus `UpdateSelectedValue()` basiert, als auch eine statische Einmal-Kamera, die auf `Range.ToImage` plus einem `MemoryStream` basiert. Wählen Sie den dynamischen Ansatz, wenn Ihre Ausgabe mit den Quellzellen synchron bleiben muss, und wählen Sie den statischen Ansatz, wenn Sie nur eine feste visuelle Momentaufnahme zur Build-Zeit benötigen.

## Verwandte Artikel
- [Sparkline in Bild und HTML in Aspose.Cells for .NET konvertieren](/cells/de/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}