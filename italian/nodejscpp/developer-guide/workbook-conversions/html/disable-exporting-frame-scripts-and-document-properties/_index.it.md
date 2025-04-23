---
title: Disabilitare l esportazione di Frame Scripts e Proprietà del Documento con Node.js tramite C++
linktitle: Disabilita l Esportazione degli Script Frame e delle Proprietà del Documento
type: docs
weight: 310
url: /it/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Impara come disabilitare l esportazione di frame script e proprietà del documento durante la conversione di un workbook in HTML usando Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells esporta frame script e proprietà del documento durante la conversione di un workbook in HTML. La versione 8.6.0 di Aspose.Cells for Node.js via C++ introduce un'opzione che consente opzionalmente di disabilitare l'esportazione di frame script e proprietà del documento. Usa la proprietà `HtmlSaveOptions.exportFrameScriptsAndProperties` per disabilitarla.

{{% /alert %}}

## **Disabilita l'esportazione degli script frame e delle proprietà del documento**

Il seguente codice di esempio ti permette di disabilitare l'esportazione degli script frame e delle proprietà del documento. Una volta convertito un workbook in HTML, il file di output non conterrà alcuno script frame o proprietà del documento.

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
