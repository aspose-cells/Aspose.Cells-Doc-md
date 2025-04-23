---
title: Frame Skripte und Dokumenteigenschaften beim Exportieren mit Node.js via C++ deaktivieren
linktitle: Deaktivieren des Exportierens von Rahmen Skripten und Dokumenteigenschaften
type: docs
weight: 310
url: /de/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Lernen Sie, wie Sie das Exportieren von Frame Skripten und Document Properties beim Konvertieren einer Arbeitsmappe in HTML mit Aspose.Cells for Node.js via C++ deaktivieren.
--- 

{{% alert color="primary" %}}

Aspose.Cells exportiert Frame-Skripte und Dokumenteigenschaften beim Umwandeln einer Arbeitsmappe in HTML. Die Version 8.6.0 von Aspose.Cells for Node.js via C++ führt eine Option ein, mit der Sie das Exportieren von Frame-Skripten und Document Properties optional deaktivieren können. Bitte verwenden Sie die Eigenschaft `HtmlSaveOptions.exportFrameScriptsAndProperties`, um das Exportieren zu deaktivieren.

{{% /alert %}}

## **Deaktivieren des Exports von Rahmen-Skripten und Dokumenteigenschaften**

Der folgende Beispielcode ermöglicht es Ihnen, den Export von Rahmen-Skripten und Dokumenteigenschaften zu deaktivieren. Nach der Konvertierung einer Arbeitsmappe in HTML enthält die Ausgabedatei keine Rahmen-Skripte und Dokumenteigenschaften.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
