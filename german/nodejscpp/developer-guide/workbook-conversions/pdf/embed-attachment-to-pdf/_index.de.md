---  
title: Anhang in PDF einbetten mit Node.js via C++  
linktitle: Anhang in PDF einbetten  
type: docs  
weight: 380  
url: /de/nodejs-cpp/embed-attachment-to-pdf/  
description: Erfahren Sie, wie Sie ein Ole Objekt als Anhang in einer PDF mit Aspose.Cells for Node.js via C++ einbetten.  
---  

In Excel können Sie ein Ole-Objekt mit Quelldaten einfügen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Klicken Sie doppelt auf das Ole-Objekt, und die eingebettete Datei wird geöffnet.

Im Allgemeinen wird das Ole-Objekt beim Konvertieren in PDF als Symbol oder Miniaturansicht ohne Quelldaten des Ole-Objekts dargestellt. Mit der Option [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) können Sie die Quelldaten des Ole-Objekts als Anhang in das PDF einbetten. Sie können im PDF mit einem Doppelklick auf das Symbol oder die Miniaturansicht die Quelldatei des Ole-Objekts öffnen.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "embedded-attachments-example.xlsx");

// Open the template file
const wb = new AsposeCells.Workbook(filePath);

// Set to embed Ole Object attachment.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setEmbedAttachments(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

![embedded-attachment.png](embedded-attachment.png)  

{{< app/cells/assistant language="nodejs-cpp" >}}
