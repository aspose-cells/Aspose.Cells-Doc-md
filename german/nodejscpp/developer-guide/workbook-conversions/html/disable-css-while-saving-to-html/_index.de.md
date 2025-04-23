---
title: CSS beim Speichern als HTML mit Node.js via C++ deaktivieren
linktitle: CSS beim Speichern in HTML deaktivieren
type: docs
weight: 320
url: /de/nodejs-cpp/disable-css-while-saving-to-html/
description: Lernen Sie, wie Sie CSS beim Speichern von Excel Dateien als HTML mit Aspose.Cells for Node.js via C++ deaktivieren. 
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei als einseitiges HTML speichern, werden die CSS-Elemente normalerweise im HTML-Dokument eingebettet und befinden sich im HEAD-Bereich. Wenn Sie diese Datei als Inhalt/Body einer E-Mail anhängen, werden die CSS-Elemente von den meisten E-Mail-Clients entfernt, was zu einer fehlerhaften Darstellung führt. Die Version 24.12 von Aspose.Cells führt eine Option ein, mit der Sie CSS optional deaktivieren können, sodass Stile direkt in den HTML-Elementen angewendet werden. Wenn Sie das HTML als Inhalt/Body der E-Mail setzen möchten, verwenden Sie bitte die Eigenschaft [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) und setzen Sie sie auf **true**.

## **CSS beim Speichern in HTML deaktivieren**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--). 

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
