---  
title: Embed Attachment to PDF with Node.js via C++  
linktitle: Embed Attachment to PDF  
type: docs  
weight: 380  
url: /nodejs-cpp/embed-attachment-to-pdf/  
description: Learn how to embed an OLE object as an attachment in a PDF using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

In Excel, you can insert an OLE object with source data ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double‑click the OLE object, and the embedded file will be opened.

Generally, when converting to PDF, the OLE object is rendered as an icon or a thumbnail without the source data. With the option [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) you can embed the OLE object source data as an attachment in the PDF. You can double‑click the icon or the thumbnail in the PDF to open the source file of the OLE object.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "embedded-attachments-example.xlsx");

// Open the template file
const wb = new AsposeCells.Workbook(filePath);

// Set to embed OLE object attachment.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setEmbedAttachments(true);

// Save the PDF file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

![embedded-attachment.png](embedded-attachment.png)  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
