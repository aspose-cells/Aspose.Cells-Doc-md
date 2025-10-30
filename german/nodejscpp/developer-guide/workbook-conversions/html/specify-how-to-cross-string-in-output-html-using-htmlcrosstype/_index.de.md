---
title: Geben Sie an, wie der String in der Ausgabedatei HTML mit HtmlCrossType in Node.js über C++ gekreuzt wird
linktitle: Geben Sie an, wie Zeichenkette in der Ausgabe HTML mit HtmlCrossType geschnitten werden soll
type: docs
weight: 140
url: /de/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Erfahren Sie, wie Sie die Textüberlaufsteuerung in HTML Ausgaben durch die Angabe von HtmlCrossType in Aspose.Cells for Node.js via C++ steuern. 
---

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder eine Zeichenkette enthält, die größer ist als die Breite der Zelle, läuft die Zeichenkette über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie diesen Überlauf steuern, indem Sie den Kreuztyp mit der [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)-Aufzählung angeben. Es hat folgende Werte:

- **HtmlCrossType.Default**: Anzeige wie MS Excel; hängt von der nächsten Zelle ab. Wenn die nächste Zelle null ist, läuft die Zeichenkette über oder wird abgeschnitten.

- **HtmlCrossType.MSExport**: Zeigen Sie den String wie MS Excel, der HTML exportiert.

- **HtmlCrossType.Cross**: HTML-Kreuzzeichen anzeigen; die Leistung beim Erstellen großer HTML-Dateien ist mehr als zehnmal schneller als das Einstellen auf Default oder FitToCell.

- **HtmlCrossType.FitToCell**: Nur innerhalb der Breite der Zelle anzeigen.

## **Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740732.xlsx) und speichert sie im HTML-Format, indem verschiedene [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) angegeben werden. Bitte laden Sie die [Ausgabedateien HTML](51740734.zip) herunter, die mit diesem Code generiert wurden. Die Beispiel-Excel-Datei enthält das Bild mit rotem Rahmen, wie in diesem Screenshot gezeigt, der die Wirkung der [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)-Werte auf das Ausgabe-HTML zeigt.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
