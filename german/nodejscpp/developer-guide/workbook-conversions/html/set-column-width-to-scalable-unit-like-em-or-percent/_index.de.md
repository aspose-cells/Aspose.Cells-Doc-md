---
title: Spaltenbreite in skalierbare Einheiten wie em oder Prozent mit Node.js via C++ einstellen
linktitle: Spaltenbreite in skalierbare Einheiten wie em oder Prozent einstellen
type: docs
weight: 130
url: /de/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Erfahren Sie, wie Sie die Spaltenbreite auf skalierbare Einheiten wie em oder Prozent in Aspose.Cells for Node.js via C++ einstellen. Verbessern Sie die Präsentation der generierten HTML Tabellen.
---

Das Erstellen einer HTML-Datei aus einer Tabelle ist sehr üblich. Die Größe der Spalten wird in "pt" definiert, was in vielen Fällen funktioniert. Es kann jedoch Fälle geben, in denen diese feste Größe nicht erforderlich ist. Zum Beispiel, wenn die Breite eines Container-Panels 600px beträgt, wo diese HTML-Seite angezeigt wird, erhalten Sie möglicherweise eine horizontale Bildlaufleiste, wenn die generierte Tabellengröße größer ist. Es wurde verlangt, dass diese feste Größe in eine skalierbare Einheit wie em oder Prozent geändert wird, um eine bessere Präsentation zu erreichen. Das folgende Beispiel kann verwendet werden, wobei [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) auf **true** gesetzt wird, um eine skalierbare Breite zu erstellen.

Beispiel-Quelldatei und Ausgabedateien können von folgenden Links heruntergeladen werden:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
