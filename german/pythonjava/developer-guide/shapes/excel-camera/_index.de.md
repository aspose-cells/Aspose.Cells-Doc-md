---
title: Excel-Kamera in Aspose.Cells for Python via Java
linktitle: Excel-Kamera
description: Erfahren Sie, wie Sie die Excel-Kamera in Aspose.Cells for Python via Java verwenden, um ein dynamisches Bild zu erstellen, das mit einem Zellbereich verknüpft ist, sich mit den Quelldaten aktualisiert und alle Quellformatierungen beibehält.
keywords: Aspose.Cells, Python via Java, Excel-Kamera, dynamisches Bild, verknüpftes Bild, Picture.formula, updateSelectedValue, createRange, toImage, byte[]-Array
type: docs
weight: 90
url: /de/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Die Excel-Kamera ist ein Arbeitsblattobjekt, das ein Live-Bild eines Zellbereichs rendert und wie ein gewöhnliches Bild auf der Zeichnungsebene schwebt. Aspose.Cells for Python via Java unterstützt zwei Erstellungsmodi: ein dynamisches Bild, das sich automatisch aktualisiert, sobald sich die Quelldaten ändern, und ein statisches Bild, das einen einmaligen Schnappschuss eines Bereichs erfasst. Dieser Artikel führt durch beide Ansätze, damit Sie denjenigen auswählen können, der zu Ihrem Layout passt.

## Was ist die Excel-Kamera?
Die Excel-Kamera ist im Wesentlichen ein Bildobjekt, das an einer bestimmten Zeile und Spalte auf der Zeichnungsebene des Arbeitsblatts verankert ist. Anders als ein normal eingefügtes Bild ist die Kamera über eine Formel im A1-Stil wie `"A1:F10"` mit einem Quellbereich verknüpft. Sobald sich eine Zelle innerhalb dieses Bereichs ändert, wird das Bild der Kamera automatisch aktualisiert, um den neuen Inhalt widerzuspiegeln. Die Kamera bewahrt die vollständige Formatierung des Quellbereichs — Rahmen, Hintergrundfarben, Schriftarten und Zahlenformate — sodass alles, was innerhalb der Zellen sichtbar ist, auch im Bild der Kamera erscheint. Dadurch eignet sich die Kamera besonders für Dashboards, Zusammenfassungen, Seitenleisten und Berichtslayouts, in denen Sie eine sichtbare Vorschau eines entfernten Bereichs wünschen, ohne zu scrollen oder Daten zu wiederholen. Zwei Einschränkungen gelten: Sie müssen `updateSelectedValue()` vor dem Speichern der Arbeitsmappe aufrufen, und die Datei wird nach HTML oder PDF exportiert, da diese Formate auf den eingebetteten Bilddaten basieren und nicht auf einer Live-Neuberechnung.

## Methode 1 — Hinzufügen eines dynamischen Kamerabilds
Die dynamische Kamera ist der gängigste Ansatz und entspricht am ehesten dem in Excel eingebauten Kamerawerkzeug. Sie funktioniert, indem ein Bild ohne anfänglichen Bildinhalt hinzugefügt und ihm dann eine Formel zugewiesen wird, die auf den Quellbereich verweist. Nachdem die Formel zugewiesen wurde, aktualisiert der Aufruf von `updateSelectedValue()` die eingebetteten Bilddaten, sodass sie mit den Zellen übereinstimmen, die sie spiegeln. Die Kamera wird nicht über eine dedizierte Klasse implementiert — sie wird vollständig auf dem Standardtyp `Picture` aufgebaut.
Die wichtigsten APIs sind:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — fügt ein Bild hinzu, das an der angegebenen Zeile und Spalte verankert ist. Wenn Sie `None` für den Parameter `stream` übergeben, wird ein leeres Bild erstellt, das als Platzhalter für eine dynamische Kamera dient. Die Methode gibt den Index des neuen Bildes zurück.
- `worksheet.getPictures().get(index)` — Zugriffsfunktion zum Abrufen eines bestimmten `Picture` aus der Sammlung.
- `Picture.getFormula()` / `Picture.setFormula()` — liest oder setzt die Referenz im A1-Stil auf den Quellbereich, den die Kamera spiegelt, z. B. `"A1:F10"`.
- `Picture.updateSelectedValue()` — eine Methode ohne Rückgabewert, die die eingebetteten Bilddaten aus den Zellen aktualisiert, auf die die Formel verweist.

{{% alert color="primary" %}}
`updateSelectedValue()` MUSS vor dem Speichern aufgerufen werden, wenn die Ausgabe HTML oder PDF ist; andernfalls enthält die exportierte Datei keine Bilddaten und die Kamera erscheint in der gerenderten Ausgabe leer.
{{% /alert %}}

Der folgende Code erstellt eine Arbeitsmappe, fügt ein leeres Bild verankert an Zeile 10, Spalte 6 hinzu, verknüpft es über die Methode `setFormula` mit dem Quellbereich `A1:F10`, aktualisiert die eingebetteten Bilddaten und speichert die Arbeitsmappe.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Dynamische Kamera: Fügen Sie ein leeres Bild hinzu, verknüpfen Sie es über eine Formel mit A1:F10 und aktualisieren Sie es dann
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Methode 2 — Hinzufügen eines statischen Kamerabilds
Die statische Kamera ist im Wesentlichen eine einmal gerenderte Vorschau eines Zellbereichs. Anstatt eine Live-Verknüpfung aufrechtzuerhalten, rendern Sie den Bereich einmal in Bildbytes, umschließen diese Bytes in einem `byte[]`-Array und fügen sie als gewöhnliches Bild hinzu. Der Bildinhalt wird zum Zeitpunkt der Erstellung festgelegt und aktualisiert sich nicht automatisch, wenn sich Quellzellen ändern.
Die wichtigsten APIs sind:
- `Cells.createRange(String address)` — erstellt ein `Range`-Objekt aus einer Adresse im A1-Stil wie `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — rendert den Bereich in Bildbytes. Wenn Sie `None` übergeben, werden die Standard-Renderingoptionen verwendet; es existieren Überladungen zur feineren Steuerung der Ausgabe.
- `byte[] array(byte[] buffer)` — umschließt die gerenderten Bildbytes in einem `byte[]`-Array, das in `PictureCollection.add` eingespeist werden kann.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — fügt das Bild verankert an der angegebenen Zeile und Spalte hinzu, dieses Mal unter Übergabe des durch das Rendering erzeugten `byte[]`-Arrays.
Der folgende Code erstellt eine Arbeitsmappe, baut einen `Range` für `A1:F10` auf, rendert ihn über `Range.toImage(None)` in Bildbytes, umschließt die Bytes in einem `byte[]`-Array, fügt das Bild verankert an Zeile 10, Spalte 6 hinzu und speichert die Arbeitsmappe.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Statische Kamera: Bereich erstellen, in Bytes rendern, in ByteArrayInputStream einwickeln, als Bild hinzufügen
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Wahl zwischen dynamisch und statisch
- **Dynamische Kamera:** aktualisiert sich bei jeder Neuberechnung, unterstützt den HTML- und PDF-Export nach `updateSelectedValue()` und bewahrt das Verhalten der Live-Verknüpfung über die gesamte Lebensdauer der Datei hinweg.
- **Statische Kamera:** ein einmaliges Rendering, das sich nie aktualisiert — nützlich, wenn Sie einen festen visuellen Schnappschuss zur Erstellungszeit einbetten möchten, anstatt eines Live-Spiegels der Daten.
Aspose.Cells for Python via Java unterstützt sowohl eine dynamische, sich automatisch aktualisierende Kamera, die auf `setFormula` plus `updateSelectedValue()` aufbaut, als auch eine statische Kamera für einmaliges Rendering, die auf `toImage` plus ein `byte[]`-Array aufbaut. Wählen Sie den dynamischen Ansatz, wenn Ihre Ausgabe mit den Quellzellen synchron bleiben muss, und wählen Sie den statischen Ansatz, wenn Sie lediglich einen festen visuellen Schnappschuss zur Erstellungszeit benötigen.

{{< app/cells/assistant language="python" >}}