---  
title: Infoga bilaga i PDF med Node.js via C++  
linktitle: Inbädda bilaga till PDF  
type: docs  
weight: 380  
url: /sv/nodejs-cpp/embed-attachment-to-pdf/  
description: Lär dig hur du infogar ett Ole objekt som en bilaga i en PDF med Aspose.Cells for Node.js via C++.  
---  

I Excel kan du infoga ett Ole-objekt med källdata ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Dubbelklicka på Ole-objektet, och den inbäddade filen öppnas.

Generellt, när du konverterar till PDF, kommer Ole-objektet att renderas som en ikon eller miniatyrbild utan Ole-objektets källdata. Med alternativet [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) kan du bädda in Ole-Objektets källdata som en bilaga i PDF:en. Du kan dubbelklicka på ikonen eller miniatyrbilden i PDF:n för att öppna källfilen för Ole-objektet.

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
