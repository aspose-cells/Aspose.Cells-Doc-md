---  
title: Incrustar adjunto en PDF con Node.js a través de C++  
linktitle: Agregar adjunto a PDF  
type: docs  
weight: 380  
url: /es/nodejs-cpp/embed-attachment-to-pdf/  
description: Aprende cómo incrustar un objeto Ole como adjunto en un PDF usando Aspose.Cells for Node.js via C++.  
---  

En Excel, puedes insertar un objeto Ole con datos fuente ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Haz doble clic en el objeto Ole, y el archivo incrustado se abrirá.

Por lo general, al convertir a PDF, el objeto Ole se renderiza como un icono o vista previa sin los datos fuente del objeto Ole. Con la opción [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) puedes incrustar los datos fuente del objeto Ole como adjunto en el PDF. Puedes hacer doble clic en el icono o vista previa en el PDF para abrir el archivo fuente del objeto Ole.

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

