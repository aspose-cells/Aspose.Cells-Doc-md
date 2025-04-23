---
title: Inaktivera Export av Frame Scripts och Dokumentegenskaper med Node.js via C++
linktitle: Inaktivera Exportering av Ramskript och Dokumentegenskaper
type: docs
weight: 310
url: /sv/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Lär dig hur du inaktiverar export av frame scripts och dokumentegenskaper när du konverterar en arbetsbok till HTML med Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells exporterar frame scripts och dokumentegenskaper när den konverterar en arbetsbok till HTML. Version 8.6.0 av Aspose.Cells for Node.js via C++ introducerar ett alternativ som gör det möjligt att inaktivera export av frame scripts och dokumentegenskaper. Använd `HtmlSaveOptions.exportFrameScriptsAndProperties`-egenskapen för att stänga av exporten.

{{% /alert %}}

## **Inaktivera export av ramskript och dokumentegenskaper**

Följande exempelkod tillåter dig att inaktivera export av ramskript och dokumentegenskaper. När du konverterar en arbetsbok till HTML kommer utdatafilen inte att innehålla några ramskript eller dokumentegenskaper.

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
