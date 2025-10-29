---  
title: Встроить вложение в PDF с помощью Node.js через C++  
linktitle: Встроить вложение в PDF  
type: docs  
weight: 380  
url: /ru/nodejs-cpp/embed-attachment-to-pdf/  
description: Узнайте, как встроить Ole Object как вложение в PDF с помощью Aspose.Cells for Node.js via C++.  
---  

В Excel можно вставлять Ole Object с исходными данными ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Дважды щелкните по Ole Object, и вложенный файл откроется.

Образовательно, при преобразовании в PDF Ole Object будет отображаться как значок или миниатюра без исходных данных Ole Object. С помощью опции [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) вы можете встроить исходные данные Ole Object как вложение в PDF. Двойной клик по значку или миниатюре в PDF откроет исходный файл Ole Object.

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
