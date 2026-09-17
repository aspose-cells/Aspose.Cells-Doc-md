---
title: Excel-Kamera in Aspose.Cells for Node.js via Java
linktitle: Excel-Kamera
description: Lernen Sie, wie Sie die Excel-Kamera in Aspose.Cells for Node.js via Java verwenden, um ein dynamisches Bild zu erstellen, das mit einem Zellbereich verknüpft ist und sich mit den Quelldaten aktualisiert, wobei die gesamte Quellformatierung erhalten bleibt.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Excel-Kamera, dynamisches Bild, verknüpftes Bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /de/nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Die Excel-Kamera ist ein Arbeitsblattobjekt, das ein Live-Bild eines Zellbereichs rendert und wie ein gewöhnliches Bild auf der Zeichnungsebene schwebt. Aspose.Cells unterstützt zwei Erstellungsmodi: ein dynamisches Bild, das sich automatisch aktualisiert, sobald sich die Quelldaten ändern, und ein statisches Bild, das eine einmalige Momentaufnahme eines Bereichs erfasst. Dieser Artikel führt Sie durch beide Ansätze, damit Sie denjenigen auswählen können, der zu Ihrem Layout passt.

## Was ist die Excel-Kamera?
Die Excel-Kamera ist im Wesentlichen ein Bildobjekt, das an einer bestimmten Zeile und Spalte auf der Zeichnungsebene des Arbeitsblatts verankert ist. Im Gegensatz zu einem normal eingefügten Bild ist die Kamera über eine A1-Formel wie `"A1:F10"` mit einem Quellbereich verknüpft. Sobald sich eine Zelle innerhalb dieses Bereichs ändert, wird das Bild der Kamera automatisch aktualisiert, um den neuen Inhalt widerzuspiegeln. Die Kamera bewahrt die vollständige Formatierung des Quellbereichs – Rahmen, Hintergrundfarben, Schriftarten und Zahlenformate – sodass alles, was innerhalb der Zellen sichtbar ist, auch im Bild der Kamera erscheint. Dies macht die Kamera besonders nützlich für Dashboards, Zusammenfassungen, Seitenleisten und Berichtslayouts, in denen Sie eine sichtbare Vorschau eines entfernten Bereichs anzeigen möchten, ohne zu scrollen oder Daten zu wiederholen. Es gelten zwei Einschränkungen: Sie müssen `updateSelectedValue()` vor dem Speichern der Arbeitsmappe aufrufen, und die Datei wird in HTML oder PDF exportiert, da diese Formate auf den eingebetteten Bilddaten basieren und nicht auf einer Live-Neuberechnung.

## Methode 1 – Dynamisches Kamerabild hinzufügen
Die dynamische Kamera ist der häufigste Ansatz und entspricht am ehesten dem in Excel integrierten Kameratool. Sie funktioniert, indem ein Bild ohne anfänglichen Bildinhalt hinzugefügt und anschließend eine `Formula` zugewiesen wird, die auf den Quellbereich verweist. Nachdem die Formel zugewiesen wurde, aktualisiert der Aufruf von `updateSelectedValue()` die eingebetteten Bilddaten, sodass sie mit den gespiegelten Zellen synchron sind. Die Kamera wird nicht über eine eigene Klasse implementiert – sie wird vollständig auf dem Standardtyp `Picture` aufgebaut.
Die wichtigsten APIs sind:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` – fügt ein Bild hinzu, das an der angegebenen Zeile und Spalte verankert ist. Durch Übergeben von `null` für den Parameter `stream` wird ein leeres Bild erstellt, das als Platzhalter für eine dynamische Kamera dient. Die Methode gibt den Index des neuen Bildes zurück.
- `worksheet.getPictures().get(index)` – Indexerzugriff zum Abrufen eines bestimmten `Picture` aus der Sammlung.
- `Picture.Formula` – eine Zeichenfolgeneigenschaft (`getFormula()`/`setFormula()`), die den A1-Verweis auf den Quellbereich enthält, den die Kamera spiegelt, z. B. `"A1:F10"`.
- `Picture.updateSelectedValue()` – eine void-Methode, die die eingebetteten Bilddaten aus den durch `Formula` referenzierten Zellen aktualisiert.

{{% alert color="primary" %}}
`updateSelectedValue()` MUSS vor dem Speichern aufgerufen werden, wenn die Ausgabe HTML oder PDF ist; andernfalls enthält die exportierte Datei keine Bilddaten und die Kamera erscheint in der gerenderten Ausgabe leer.
{{% /alert %}}

Der folgende Code erstellt eine Arbeitsmappe, fügt ein leeres Bild verankert an Zeile 10, Spalte 6 hinzu, verknüpft es über die Eigenschaft `Formula` mit dem Quellbereich `A1:F10`, aktualisiert die eingebetteten Bilddaten und speichert die Arbeitsmappe.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamische Kamera: Ein leeres Bild hinzufügen, es über eine Formel mit A1:F10 verknüpfen und dann aktualisieren
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## Methode 2 – Statisches Kamerabild hinzufügen
Die statische Kamera ist im Wesentlichen eine einmal gerenderte Vorschau eines Zellbereichs. Anstatt eine Live-Verknüpfung aufrechtzuerhalten, rendern Sie den Bereich einmalig in Bildbytes, wickeln diese Bytes in einen `ByteArrayInputStream` und fügen sie als gewöhnliches Bild hinzu. Der Bildinhalt wird zum Zeitpunkt der Erstellung festgelegt und aktualisiert sich nicht automatisch, wenn sich die Quellzellen ändern.
Die wichtigsten APIs sind:
- `Cells.createRange(String address)` – erstellt ein `Range`-Objekt aus einer A1-Adresse wie `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` – rendert den Bereich in Bildbytes. Durch Übergeben von `null` werden die Standard-Renderingoptionen verwendet; es existieren Überladungen für eine feinere Steuerung der Ausgabe.
- `new ByteArrayInputStream(byte[] buffer)` – wickelt die gerenderten Bildbytes in einen `ByteArrayInputStream`, der in `PictureCollection.add` eingespeist werden kann.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` – fügt das Bild verankert an der angegebenen Zeile und Spalte hinzu, wobei dieses Mal der durch das Rendern erzeugte `ByteArrayInputStream` übergeben wird.
Der folgende Code erstellt eine Arbeitsmappe, erstellt einen `Range` für `A1:F10`, rendert ihn über `range.toImage(null)` in Bildbytes, wickelt die Bytes in einen `ByteArrayInputStream`, fügt das Bild verankert an Zeile 10, Spalte 6 hinzu und speichert die Arbeitsmappe.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Statische Kamera: Bereich erstellen, in Bytes rendern, in ByteArrayInputStream einwickeln, als Bild hinzufügen
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## Auswahl zwischen dynamisch und statisch
- **Dynamische Kamera:** aktualisiert sich bei jeder Neuberechnung, unterstützt den HTML- und PDF-Export nach `updateSelectedValue()` und bewahrt das Verhalten der Live-Verknüpfung über die gesamte Lebensdauer der Datei hinweg.
- **Statische Kamera:** ein einmaliges Rendern, das nie aktualisiert wird – nützlich, wenn Sie eine feste visuelle Momentaufnahme einbetten möchten, die zur Erstellungszeit aufgenommen wird, anstelle einer Live-Spiegelung der Daten.
Aspose.Cells unterstützt sowohl eine dynamische, sich automatisch aktualisierende Kamera, die auf `Picture.Formula` plus `updateSelectedValue()` aufbaut, als auch eine statische Einmalkamera, die auf `Range.toImage` plus einen `ByteArrayInputStream` aufbaut. Wählen Sie den dynamischen Ansatz, wenn Ihre Ausgabe mit den Quellzellen synchron bleiben muss, und wählen Sie den statischen Ansatz, wenn Sie nur eine feste visuelle Momentaufnahme zur Erstellungszeit benötigen.

{{< app/cells/assistant language="nodejs-java" >}}