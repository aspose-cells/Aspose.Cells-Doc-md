---  
title: Incorpora allegato in PDF con Node.js tramite C++  
linktitle: Incorpora allegato in PDF  
type: docs  
weight: 380  
url: /it/nodejs-cpp/embed-attachment-to-pdf/  
description: Impara come incorporare un oggetto Ole come allegato in un PDF usando Aspose.Cells for Node.js via C++.  
---  

In Excel, puoi inserire un oggetto Ole con dati sorgente ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Fai doppio clic sull’oggetto Ole e il file incorporato si aprirà.

In generale, durante la conversione in PDF, l’oggetto Ole verrà visualizzato come un’icona o una miniatura senza dati sorgente dell’Ole Object. Con l’opzione [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) puoi incorporare i dati sorgente dell’Ole Object come allegato nel PDF. Puoi fare doppio clic sull’icona o sulla miniatura nel PDF per aprire il file di origine dell’Ole Object.

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
