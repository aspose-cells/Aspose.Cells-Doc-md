---
title: تصدير هيكل المستند أثناء التحويل إلى PDF باستخدام Node.js عبر C++
linktitle: تصدير هيكل الوثيقة أثناء التحويل إلى PDF
type: docs
weight: 360
url: /ar/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: تعلم كيفية تصدير هيكل المستند أثناء تحويل ملف Excel إلى PDF موسوم باستخدام Aspose.Cells for Node.js via C++. 
---

توفر تسهيلات الهيكل المنطقي لـ PDF وسيلة لإضافة معلومات حول هيكل محتوى المستند إلى ملف PDF. يحفظ Aspose.Cells for Node.js via C++ المعلومات حول الهيكل من مستند Microsoft Excel، مثل الخلايا، الصفوف، الجداول، أوراق العمل، الصور، الأشكال، الرأس والتذييل، وغيرها.

باستخدام خيار [PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--)، يمكنك حفظ ملف PDF موسوم مع تصدير هيكل المستند.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "document-structure-example.xlsx");
// Open the excel file with image, shape, chart, etc.
const wb = new AsposeCells.Workbook(filePath);

// Set to export document structure.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setExportDocumentStructure(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

