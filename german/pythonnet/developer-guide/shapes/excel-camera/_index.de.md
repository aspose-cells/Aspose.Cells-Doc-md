---
title: Excel-Kamera in Aspose.Cells for Python via .NET
linktitle: Excel-Kamera
description: Erfahren Sie, wie Sie die Excel-Kamera in Aspose.Cells for Python via .NET verwenden, um ein dynamisches Bild zu erstellen, das mit einem Zellbereich verknüpft ist, sich mit den Quelldaten aktualisiert und die gesamte Quellformatierung beibehält.
keywords: Aspose.Cells, Python, Excel-Kamera, dynamisches Bild, verknüpftes Bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /de/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Die Excel-Kamera ist ein Arbeitsblattobjekt, das ein Live-Bild eines Zellbereichs rendert und wie ein gewöhnliches Bild auf der Zeichenebene schwebt. Aspose.Cells unterstützt zwei Erstellungsmodi: ein dynamisches Bild, das sich automatisch aktualisiert, sobald sich die Quelldaten ändern, und ein statisches Bild, das einen einmaligen Schnappschuss eines Bereichs aufnimmt. Dieser Artikel führt Sie durch beide Vorgehensweisen, damit Sie diejenige auswählen können, die zu Ihrem Layout passt.

## Was ist die Excel-Kamera?
Die Excel-Kamera ist im Wesentlichen ein Bildobjekt, das an einer bestimmten Zeile und Spalte auf der Zeichenebene des Arbeitsblatts verankert ist. Im Gegensatz zu einem normal eingefügten Bild ist die Kamera über eine Formel im A1-Stil wie `"A1:F10"` mit einem Quellbereich verknüpft. Sobald sich eine Zelle innerhalb dieses Bereichs ändert, wird das Bild der Kamera automatisch aktualisiert, um den neuen Inhalt widerzuspiegeln. Die Kamera bewahrt die vollständige Formatierung des Quellbereichs – Rahmen, Hintergrundfarben, Schriftarten und Zahlenformate –, sodass alles, was innerhalb der Zellen sichtbar ist, auch im Bild der Kamera erscheint. Dadurch ist die Kamera besonders nützlich für Dashboards, Zusammenfassungen, Seitenleisten und Berichtslayouts, in denen Sie eine sichtbare Vorschau eines entfernten Bereichs anzeigen möchten, ohne zu scrollen oder Daten zu wiederholen. Zwei Einschränkungen gelten: Sie müssen `update_selected_value()` vor dem Speichern der Arbeitsmappe aufrufen, und die Datei wird als HTML oder PDF exportiert, da diese Formate auf den eingebetteten Bilddaten basieren und nicht auf einer Live-Neuberechnung.

## Methode 1 – Hinzufügen eines dynamischen Kamerabilds
Die dynamische Kamera ist der häufigste Ansatz und kommt dem in Excel integrierten Kameratool am nächsten. Sie funktioniert, indem ein Bild ohne anfänglichen Bildinhalt hinzugefügt und ihm dann eine `formula` zugewiesen wird, die auf den Quellbereich verweist. Nachdem die Formel zugewiesen wurde, aktualisiert der Aufruf von `update_selected_value()` die eingebetteten Bilddaten, sodass sie mit den Zellen synchronisiert sind, die sie spiegeln. Die Kamera wird nicht durch eine eigene Klasse implementiert – sie wird vollständig auf dem Standardtyp `Picture` aufgebaut.
Die wichtigsten APIs sind:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` – fügt ein Bild hinzu, das an der angegebenen Zeile und Spalte verankert ist. Die Übergabe von `None` für den `stream`-Parameter erstellt ein leeres Bild, das als Platzhalter für eine dynamische Kamera dient. Die Methode gibt den Index des neuen Bildes zurück.
- `worksheet.pictures[index]` – Indexerzugriff, um ein bestimmtes `Picture` aus der Sammlung abzurufen.
- `picture.formula` – eine Zeichenfolgeneigenschaft (get/set), die die Referenz im A1-Stil auf den Quellbereich enthält, den die Kamera spiegelt, z. B. `"A1:F10"`.
- `picture.update_selected_value()` – eine void-Methode, die die eingebetteten Bilddaten aus den durch `formula` referenzierten Zellen aktualisiert.

{{% alert color="primary" %}}
`update_selected_value()` MUSS vor dem Speichern aufgerufen werden, wenn die Ausgabe HTML oder PDF ist; andernfalls enthält die exportierte Datei keine Bilddaten und die Kamera erscheint in der gerenderten Ausgabe leer.
{{% /alert %}}

Der folgende Code erstellt eine Arbeitsmappe, fügt ein leeres Bild verankert in Zeile 10, Spalte 6 hinzu, verknüpft es über die Eigenschaft `formula` mit dem Quellbereich `A1:F10`, aktualisiert die eingebetteten Bilddaten und speichert die Arbeitsmappe.

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Dynamische Kamera: ein leeres Bild hinzufügen, es über eine Formel mit A1:F10 verknüpfen und dann aktualisieren
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Methode 2 – Hinzufügen eines statischen Kamerabilds
Die statische Kamera ist im Wesentlichen eine einmal gerenderte Vorschau eines Zellbereichs. Anstatt eine Live-Verknüpfung aufrechtzuerhalten, rendern Sie den Bereich einmal in Bildbytes, umschließen diese Bytes in einem `BytesIO` und fügen sie als normales Bild hinzu. Der Bildinhalt ist dann zum Zeitpunkt der Erstellung festgelegt und wird nicht automatisch aktualisiert, wenn sich Quellzellen ändern.
Die wichtigsten APIs sind:
- `Cells.create_range(string address)` – erstellt ein `Range`-Objekt aus einer Adresse im A1-Stil wie `"A1:F10"`.
- `Range.to_image(ImageOrPrintOptions options)` – rendert den Bereich in Bildbytes. Die Übergabe von `None` verwendet die Standard-Renderingoptionen; es existieren Überladungen für eine feinere Steuerung der Ausgabe.
- `BytesIO(byte[] buffer)` – umschließt die gerenderten Bildbytes in einem `BytesIO`, das in `PictureCollection.add` eingespeist werden kann.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` – fügt das Bild verankert an der angegebenen Zeile und Spalte hinzu, wobei dieses Mal das durch das Rendering erzeugte `BytesIO` übergeben wird.
Der folgende Code erstellt eine Arbeitsmappe, erstellt einen `Range` für `A1:F10`, rendert ihn über `Range.to_image(null)` in Bildbytes, umschließt die Bytes in einem `BytesIO`, fügt das Bild verankert in Zeile 10, Spalte 6 hinzu und speichert die Arbeitsmappe.

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Statische Kamera: Bereich erstellen, in Bytes rendern, in BytesIO einwickeln, als Bild hinzufügen
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Auswahl zwischen dynamisch und statisch
- **Dynamische Kamera:** aktualisiert sich bei jeder Neuberechnung, unterstützt den HTML- und PDF-Export nach `update_selected_value()` und bewahrt das Verhalten der Live-Verknüpfung über die gesamte Lebensdauer der Datei hinweg.
- **Statische Kamera:** ein einmaliges Rendering, das nie aktualisiert wird, nützlich, wenn Sie einen festen visuellen Schnappschuss zur Erstellungszeit einbetten möchten, anstatt einer Live-Spiegelung der Daten.
Aspose.Cells unterstützt sowohl eine dynamische, sich automatisch aktualisierende Kamera, die auf `picture.formula` plus `update_selected_value()` aufbaut, als auch eine statische, einmalige Kamera, die auf `Range.to_image` plus einem `BytesIO` aufbaut. Wählen Sie den dynamischen Ansatz, wenn Ihre Ausgabe mit den Quellzellen synchron bleiben muss, und wählen Sie den statischen Ansatz, wenn Sie nur einen festen visuellen Schnappschuss zur Erstellungszeit benötigen.

{{< app/cells/assistant language="python-net" >}}