---  
title: Incorporer une pièce jointe dans le PDF avec Node.js via C++  
linktitle: Intégrer la pièce jointe dans le PDF  
type: docs  
weight: 380  
url: /fr/nodejs-cpp/embed-attachment-to-pdf/  
description: Apprenez comment incorporer un objet Ole en tant que pièce jointe dans un PDF en utilisant Aspose.Cells for Node.js via C++.  
---  

Dans Excel, vous pouvez insérer un objet Ole avec des données sources ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double-cliquez sur l'objet Ole, et le fichier intégré s'ouvrira.

Généralement, lors de la conversion en PDF, l'objet Ole sera rendu sous forme d'icône ou de miniature sans les données sources de l'objet Ole. Avec l'option [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) vous pouvez intégrer les données source de l'objet Ole en tant que pièce jointe dans le PDF. Vous pouvez double-cliquer sur l'icône ou la miniature dans le PDF pour ouvrir le fichier source de l'objet Ole.

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
