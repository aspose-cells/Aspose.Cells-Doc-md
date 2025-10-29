---  
title: دمج مرفق في PDF باستخدام Node.js عبر C++  
linktitle: تضمين مرفق في ملف PDF  
type: docs  
weight: 380  
url: /ar/nodejs-cpp/embed-attachment-to-pdf/  
description: تعلم كيف يمكنك دمج كائن Ole كمرفق في PDF باستخدام Aspose.Cells for Node.js via C++.  
---  

في Excel، يمكنك إدراج كائن Ole بمصدر البيانات ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). انقر نقرًا مزدوجًا على كائن Ole، وسيتم فتح الملف المضمن.

عمومًا، أثناء التحويل إلى PDF، سيتم عرض كائن Ole كرمز أو صورة مصغرة بدون بيانات مصدر كائن Ole. باستخدام خيار [PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--)، يمكنك دمج بيانات مصدر كائن Ole كمرفق في PDF. يمكنك النقر المزدوج على الرمز أو الصورة المصغرة في PDF لفتح الملف المصدر لكائن Ole.

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
