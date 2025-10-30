---
title: Automatisches Anpassen von Spalten und Zeilen beim Laden von HTML in Workbook mit Node.js über C++
linktitle: Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe
type: docs
weight: 120
url: /de/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Erfahren Sie, wie Sie Spalten und Zeilen automatisch anpassen, während Sie HTML Dateien in ein Workbook mit Aspose.Cells for Node.js via C++ laden.
---

## **Mögliche Verwendungsszenarien**

 Sie können Spalten und Zeilen automatisch anpassen, während Sie Ihre HTML-Datei innerhalb des Workbook-Objekts laden. Setzen Sie dazu die Eigenschaft [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) auf **true**.

## **Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe**

Der folgende Beispielcode lädt zuerst eine Beispiel-HTML-Datei in ein Workbook ohne Ladeoptionen und speichert es im XLSX-Format. Anschließend lädt er wieder die HTML-Datei, setzt dabei die Eigenschaft [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) auf **true** und speichert erneut im XLSX-Format. Bitte laden Sie beide Ausgabedateien herunter: [Ausgabedatei ohne AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) und [Ausgabedatei mit AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Das folgende Screenshot zeigt die Auswirkung der [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--)-Eigenschaft beider Dateien.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
