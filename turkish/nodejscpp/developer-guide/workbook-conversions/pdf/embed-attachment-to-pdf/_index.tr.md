---  
title: Electronik Posta ile PDF e Ek Olarak Ekleme (Node.js C++) ile  
linktitle: Ekli Dosya Ekle PDF ye  
type: docs  
weight: 380  
url: /tr/nodejs-cpp/embed-attachment-to-pdf/  
description: Aspose.Cells for Node.js via C++ kullanarak bir Ole Nesnesini ek olarak nasıl gömeceğinizi öğrenin.  
---  

Excel'de, kaynak verileriyle bir Ole Nesnesi ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) ekleyebilirsiniz. Ole Nesnesine çift tıklayın, gömülü dosya açılır.

Genellikle, PDF'ye dönüştürürken, Ole Nesnesi bir ikon veya küçük resim olarak gösterilir ve kaynak verileri gösterilmez. [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) seçeneği ile, Ole Nesnesinin kaynak verisini ek olarak gömebilirsiniz. PDF’de ikona veya küçük resme çift tıklayarak Ole Nesnesinin kaynak dosyasını açabilirsiniz.

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

