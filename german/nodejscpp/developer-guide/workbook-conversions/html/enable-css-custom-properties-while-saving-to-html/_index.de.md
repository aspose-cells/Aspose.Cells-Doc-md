---
title: CSS benutzerdefinierte Eigenschaften beim Speichern in HTML mit Node.js via C++ aktivieren
linktitle: CSS Benutzerdefinierte Eigenschaften beim Speichern in HTML aktivieren
type: docs
weight: 320
url: /de/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: Lernen Sie, wie Sie benutzerdefinierte CSS Eigenschaften beim Speichern von Excel Dateien in HTML mit Aspose.Cells for Node.js via C++ aktivieren. 
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei als HTML speichern, wird bei mehreren Vorkommnissen eines Base64-Bildes mit benutzerdefinierten Eigenschaften die Bilddaten nur einmal gespeichert, was die Leistung des resultierenden HTML verbessern kann. Bitte verwenden Sie die Eigenschaft [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) und stellen Sie sie beim Speichern auf **true**.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Aktivieren Sie CSS Standard-Eigenschaften beim Speichern in HTML**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--). Das Screenshot zeigt den Effekt, wenn diese Eigenschaft nicht auf **true** gesetzt ist. Bitte laden Sie die [Beispieldatei Excel](50528260.xlsx) herunter, die in diesem Code verwendet wird, sowie die [generierte HTML-Ausgabe](50528261.zip) zur Referenz.



## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
