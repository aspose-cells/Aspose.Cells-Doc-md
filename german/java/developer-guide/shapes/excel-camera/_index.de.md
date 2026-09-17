---
title: Excel-Kamera in Aspose.Cells for Java
description: Erfahren Sie, wie Sie die Excel-Kamera in Aspose.Cells for Java verwenden, um ein dynamisches Bild zu erstellen, das mit einem Zellbereich verknüpft ist, sich mit den Quelldaten aktualisiert und die gesamte Quellformatierung beibehält.
linktitle: Excel-Kamera
keywords: Aspose.Cells, Java, Excel-Kamera, dynamisches Bild, verknüpftes Bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, ByteArrayInputStream
type: docs
weight: 90
url: /de/java/excel-camera/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Die Excel-Kamera ist ein Arbeitsblattobjekt, das ein Live-Bild eines Zellbereichs rendert und wie ein gewöhnliches Bild auf der Zeichnungsebene schwebt. Aspose.Cells unterstützt zwei Erstellungsmodi: ein dynamisches Bild, das sich automatisch aktualisiert, sobald sich die Quelldaten ändern, und ein statisches Bild, das eine einmalige Momentaufnahme eines Bereichs erfasst. Dieser Artikel führt Sie durch beide Ansätze, damit Sie denjenigen auswählen können, der zu Ihrem Layout passt.

## Was ist die Excel-Kamera?
Die Excel-Kamera ist im Wesentlichen ein Bildobjekt, das an einer bestimmten Zeile und Spalte auf der Zeichnungsebene des Arbeitsblatts verankert ist. Anders als ein normal eingefügtes Bild ist die Kamera über eine Formel im A1-Stil wie `"A1:F10"` mit einem Quellbereich verknüpft. Sobald sich eine Zelle innerhalb dieses Bereichs ändert, wird das Bild der Kamera automatisch aktualisiert, um den neuen Inhalt wiederzugeben. Die Kamera erhält die vollständige Formatierung des Quellbereichs — Rahmen, Hintergrundfarben, Schriftarten und Zahlenformate — sodass alles, was in den Zellen sichtbar ist, auch im Bild der Kamera erscheint. Dies macht die Kamera besonders nützlich für Dashboards, Zusammenfassungen, Seitenleisten und Berichtslayouts, in denen Sie eine sichtbare Vorschau eines entfernten Bereichs anzeigen möchten, ohne zu scrollen oder Daten zu wiederholen. Zwei Einschränkungen gelten: Sie müssen `updateSelectedValue()` vor dem Speichern der Arbeitsmappe aufrufen, und die Datei wird nach HTML oder PDF exportiert, da diese Formate auf den eingebetteten Bilddaten basieren und nicht auf einer Live-Neuberechnung.

## Methode 1 — Hinzufügen eines dynamischen Kamerabilds
Die dynamische Kamera ist der häufigste Ansatz und kommt dem in Excel integrierten Kamerawerkzeug am nächsten. Sie funktioniert, indem ein Bild ohne anfänglichen Bildinhalt hinzugefügt und ihm anschließend eine `Formula` zugewiesen wird, die auf den Quellbereich verweist. Nachdem die Formel zugewiesen wurde, aktualisiert der Aufruf von `updateSelectedValue()` die eingebetteten Bilddaten, sodass sie mit den Zellen synchronisiert sind, die sie spiegeln. Die Kamera wird nicht über eine dedizierte Klasse implementiert — sie wird vollständig auf dem Standardtyp `Picture` aufgebaut.
Die wichtigsten APIs sind:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — fügt ein an der angegebenen Zeile und Spalte verankertes Bild hinzu. Die Übergabe von `null` für den Parameter `stream` erstellt ein leeres Bild, das als Platzhalter für eine dynamische Kamera dient. Die Methode gibt den Index des neuen Bildes zurück.
- `worksheet.getPictures().get(index)` — Indexer-Zugriff, um ein bestimmtes `Picture` aus der Sammlung abzurufen.
- `Picture.setFormula(String value)` — legt den Verweis im A1-Stil auf den Quellbereich fest, den die Kamera spiegelt, z. B. `"A1:F10"`.
- `Picture.updateSelectedValue()` — eine Void-Methode, die die eingebetteten Bilddaten aus den Zellen aktualisiert, auf die `Formula` verweist.

{{% alert color="primary" %}}
`updateSelectedValue()` MUSS vor dem Speichern aufgerufen werden, wenn die Ausgabe HTML oder PDF ist; andernfalls enthält die exportierte Datei keine Bilddaten und die Kamera wird im gerenderten Output leer angezeigt.
{{% /alert %}}

Der folgende Code erstellt eine Arbeitsmappe, fügt ein leeres Bild verankert an Zeile 10, Spalte 6 hinzu, verknüpft es über `setFormula` mit dem Quellbereich `A1:F10`, aktualisiert die eingebetteten Bilddaten und speichert die Arbeitsmappe.

```java
import java.io.InputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamische Kamera: Fügen Sie ein leeres Bild hinzu, verknüpfen Sie es über eine Formel mit A1:F10 und aktualisieren Sie es dann
PictureCollection pictures = worksheet.getPictures();
int index = pictures.add(10, 6, (InputStream) null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX);
```

## Methode 2 — Hinzufügen eines statischen Kamerabilds
Die statische Kamera ist im Wesentlichen eine einmal gerenderte Vorschau eines Zellbereichs. Anstatt eine Live-Verknüpfung aufrechtzuerhalten, rendern Sie den Bereich einmal in Bildbytes, wickeln diese Bytes in einen `ByteArrayInputStream` und fügen sie als gewöhnliches Bild hinzu. Der Bildinhalt ist dann zum Zeitpunkt der Erstellung festgelegt und wird nicht automatisch aktualisiert, wenn sich Quellzellen ändern.
Die wichtigsten APIs sind:
- `Cells.createRange(String address)` — erstellt ein `Range`-Objekt aus einer Adresse im A1-Stil wie `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — rendert den Bereich in Bildbytes. Die Übergabe von `null` verwendet die Standard-Renderingoptionen; es gibt Überladungen für eine feinere Steuerung der Ausgabe.
- `new ByteArrayInputStream(byte[] buffer)` — wickelt die gerenderten Bildbytes in einen `ByteArrayInputStream`, der an `PictureCollection.add` übergeben werden kann.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — fügt das an der angegebenen Zeile und Spalte verankerte Bild hinzu, wobei dieses Mal der durch das Rendering erzeugte `ByteArrayInputStream` übergeben wird.
Der folgende Code erstellt eine Arbeitsmappe, baut einen `Range` für `A1:F10`, rendert ihn über `Range.toImage(null)` in Bildbytes, wickelt die Bytes in einen `ByteArrayInputStream`, fügt das an Zeile 10, Spalte 6 verankerte Bild hinzu und speichert die Arbeitsmappe.

```java
import java.io.ByteArrayInputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.Range;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Statische Kamera: Bereich erstellen, in Bytes rendern, in ByteArrayInputStream verpacken, als Bild hinzufügen
Range range = worksheet.getCells().createRange("A1:F10");
PictureCollection pictures = worksheet.getPictures();
pictures.add(10, 6, new ByteArrayInputStream(range.toImage(null)));
workbook.save("output_static.xlsx", SaveFormat.XLSX);
```

## Wahl zwischen dynamisch und statisch
- **Dynamische Kamera:** aktualisiert sich bei jeder Neuberechnung, unterstützt den HTML- und PDF-Export nach `updateSelectedValue()` und erhält das Verhalten der Live-Verknüpfung über die gesamte Lebensdauer der Datei.
- **Statische Kamera:** ein einmaliges Rendering, das nie aktualisiert wird, nützlich, wenn Sie eine feste visuelle Momentaufnahme zur Erstellungszeit einbetten möchten, anstelle einer Live-Spiegelung der Daten.
Aspose.Cells unterstützt sowohl eine dynamische, sich automatisch aktualisierende Kamera, die auf `Picture.Formula` plus `updateSelectedValue()` aufbaut, als auch eine statische Einmalkamera, die auf `Range.toImage` plus einem `ByteArrayInputStream` basiert. Wählen Sie den dynamischen Ansatz, wenn Ihre Ausgabe mit den Quellzellen synchron bleiben muss, und wählen Sie den statischen Ansatz, wenn Sie nur eine feste visuelle Momentaufnahme zur Erstellungszeit benötigen.

## Verwandte Artikel
- [Sparkline in Bild und HTML konvertieren in Aspose.Cells for Java](/cells/de/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}