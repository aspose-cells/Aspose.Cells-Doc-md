---
title: Excel-Kamera in Aspose.Cells for Node.js via C++
linktitle: Excel-Kamera
description: Erfahren Sie, wie Sie die Excel-Kamera in Aspose.Cells for Node.js via C++ verwenden, um ein dynamisches Bild zu erstellen, das mit einem Zellbereich verknüpft ist und sich mit den Quelldaten aktualisiert sowie die gesamte Quellformatierung beibehält.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Excel-Kamera, dynamisches Bild, verknüpftes Bild, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /de/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Die Excel-Kamera ist ein Arbeitsblattobjekt, das ein Live-Bild eines Zellbereichs rendert und wie ein normales Bild auf der Zeichnungsebene schwebt. Aspose.Cells unterstützt zwei Erstellungsmodi: ein dynamisches Bild, das sich automatisch aktualisiert, sobald sich die Quelldaten ändern, und ein statisches Bild, das eine einmalige Momentaufnahme eines Bereichs erfasst. Dieser Artikel führt durch beide Ansätze, damit Sie denjenigen auswählen können, der zu Ihrem Layout passt.

## Was ist die Excel-Kamera?
Die Excel-Kamera ist im Wesentlichen ein Bildobjekt, das an einer bestimmten Zeile und Spalte auf der Zeichnungsebene des Arbeitsblatts verankert ist. Im Gegensatz zu einem normal eingefügten Bild ist die Kamera über eine A1-Formel wie `"A1:F10"` mit einem Quellbereich verknüpft. Sobald sich eine Zelle innerhalb dieses Bereichs ändert, wird das Bild der Kamera automatisch aktualisiert, um den neuen Inhalt widerzuspiegeln. Die Kamera behält die vollständige Formatierung des Quellbereichs bei — Rahmen, Hintergrundfarben, Schriftarten und Zahlenformate — sodass alles, was in den Zellen sichtbar ist, auch im Bild der Kamera erscheint. Dies macht die Kamera besonders nützlich für Dashboards, Zusammenfassungen, Seitenleisten und Berichtslayouts, in denen Sie eine sichtbare Vorschau eines entfernten Bereichs anzeigen möchten, ohne zu scrollen oder Daten zu wiederholen. Zwei Einschränkungen gelten: Sie müssen `updateSelectedValue()` vor dem Speichern der Arbeitsmappe aufrufen, und die Datei wird nach HTML oder PDF exportiert, da diese Formate auf den eingebetteten Bilddaten basieren und nicht auf einer Live-Neuberechnung.

## Methode 1 — Hinzufügen eines dynamischen Kamerabildes
Die dynamische Kamera ist der häufigste Ansatz und entspricht am ehesten dem in Excel eingebauten Kamera-Tool. Sie funktioniert, indem ein Bild ohne anfänglichen Bildinhalt hinzugefügt und anschließend eine `Formula` zugewiesen wird, die auf den Quellbereich verweist. Nachdem die Formel zugewiesen wurde, aktualisiert der Aufruf von `updateSelectedValue()` die eingebetteten Bilddaten, sodass sie mit den Zellen, die sie spiegeln, synchron sind. Die Kamera wird nicht durch eine dedizierte Klasse implementiert — sie wird vollständig auf dem Standardtyp `Picture` aufgebaut.
Die wichtigsten APIs sind:
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — fügt ein Bild hinzu, das an der angegebenen Zeile und Spalte verankert ist. Die Übergabe von `null` für den Parameter `stream` erstellt ein leeres Bild, das als Platzhalter für eine dynamische Kamera dient. Die Methode gibt den Index des neuen Bildes zurück.
- `pictures.get(index)` — ruft ein bestimmtes `Picture` aus der Sammlung anhand des Index ab.
- `Picture.formula` — eine String-Eigenschaft (get/set), die die A1-Referenz auf den Quellbereich enthält, den die Kamera spiegelt, z. B. `"A1:F10"`.
- `Picture.updateSelectedValue()` — eine void-Methode, die die eingebetteten Bilddaten aus den Zellen aktualisiert, auf die `formula` verweist.

{{% alert color="primary" %}}
`updateSelectedValue()` MUSS vor dem Speichern aufgerufen werden, wenn die Ausgabe HTML oder PDF ist; andernfalls enthält die exportierte Datei keine Bilddaten und die Kamera erscheint in der gerenderten Ausgabe leer.
{{% /alert %}}

Der folgende Code erstellt eine Arbeitsmappe, fügt ein leeres Bild verankert in Zeile 10, Spalte 6 hinzu, verknüpft es über die Eigenschaft `Formula` mit dem Quellbereich `A1:F10`, aktualisiert die eingebetteten Bilddaten und speichert die Arbeitsmappe.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamische Kamera: ein leeres Bild hinzufügen, über eine Formel mit A1:F10 verknüpfen und dann aktualisieren
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## Methode 2 — Hinzufügen eines statischen Kamerabildes
Die statische Kamera ist im Wesentlichen eine einmal gerenderte Vorschau eines Zellbereichs. Anstatt eine Live-Verknüpfung aufrechtzuerhalten, rendern Sie den Bereich einmal in Bildbytes, umschließen diese Bytes in einem `Buffer` und fügen sie als normales Bild hinzu. Der Bildinhalt ist zum Zeitpunkt der Erstellung festgelegt und wird nicht automatisch aktualisiert, wenn sich Quellzellen ändern.
Die wichtigsten APIs sind:
- `Cells.createRange(address)` — erstellt ein `Range`-Objekt aus einer A1-Adresse wie `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — rendert den Bereich in Bildbytes. Die Übergabe von `null` verwendet die Standard-Renderingoptionen; es existieren Überladungen für eine feinere Steuerung der Ausgabe.
- `new Buffer(byte[] buffer)` — umschließt die gerenderten Bildbytes in einem `Buffer`, der in `getPictures().add` eingefügt werden kann.
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — fügt das Bild verankert an der angegebenen Zeile und Spalte hinzu, wobei diesmal der durch das Rendering erzeugte `Buffer` übergeben wird.
Der folgende Code erstellt eine Arbeitsmappe, baut einen `Range` für `A1:F10`, rendert ihn über `range.toImage(null)` in Bildbytes, umschließt die Bytes in einem `Buffer`, fügt das Bild verankert in Zeile 10, Spalte 6 hinzu und speichert die Arbeitsmappe.

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Statische Kamera: Bereich erstellen, in Bytes rendern, in MemoryStream einwickeln, als Bild hinzufügen
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## Wahl zwischen dynamisch und statisch
- **Dynamische Kamera:** aktualisiert sich bei jeder Neuberechnung, unterstützt den HTML- und PDF-Export nach `updateSelectedValue()` und bewahrt das Live-Verknüpfungsverhalten über die gesamte Lebensdauer der Datei.
- **Statische Kamera:** ein einmaliges Rendering, das nie aktualisiert wird, nützlich, wenn Sie eine feste visuelle Momentaufnahme zur Erstellungszeit einbetten möchten, anstatt eines Live-Spiegels der Daten.
Aspose.Cells unterstützt sowohl eine dynamische, sich automatisch aktualisierende Kamera, die auf `Picture.formula` plus `updateSelectedValue()` aufbaut, als auch eine statische, einmalige Kamera, die auf `Range.toImage` plus einem `Buffer` basiert. Wählen Sie den dynamischen Ansatz, wenn Ihre Ausgabe mit den Quellzellen synchron bleiben muss, und wählen Sie den statischen Ansatz, wenn Sie nur eine feste visuelle Momentaufnahme zur Erstellungszeit benötigen.

{{< app/cells/assistant language="nodejs-cpp" >}}