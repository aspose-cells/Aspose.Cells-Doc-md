---
title: Downlevel Comments mit Revealed beim Speichern in HTML mit Node.js via C++ deaktivieren
linktitle: Deaktivieren von Downlevel Revealed Kommentaren beim Speichern als HTML
type: docs
weight: 20
url: /de/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Lernen Sie, wie Sie die Downlevel Comments beim Speichern einer Excel Datei als HTML mit Aspose.Cells for Node.js via C++ deaktivieren.
---

## **Mögliche Verwendungsszenarien**

Beim Speichern Ihrer Excel-Datei als HTML zeigt Aspose.Cells Downlevel-Conditional-Comments an. Diese bedingten Kommentare sind hauptsächlich für ältere Versionen von Internet Explorer relevant und für moderne Webbrowser irrelevant. Sie können sie im Detail unter folgendem Link lesen.

- [Bedingter Kommentar - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++ ermöglicht es, diese Downlevel-Revealed-Comments zu entfernen, indem die Eigenschaft [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) auf **true** gesetzt wird.

## **Beim Speichern als HTML-Wrap Kommentare ausblenden**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--). Das Bild zeigt die Wirkung dieser Eigenschaft, wenn sie nicht auf true gesetzt ist. Bitte laden Sie die [Beispiel-Excel-Datei](50528257.xlsx) herunter, die in diesem Code verwendet wird, sowie die [generierte HTML-Ausgabe](50528258.zip) zur Referenz.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
