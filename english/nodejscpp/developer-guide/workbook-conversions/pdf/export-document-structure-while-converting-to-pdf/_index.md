---
title: Export Document Structure While Converting to PDF with Node.js via C++
linktitle: Export Document Structure While Converting to PDF
type: docs
weight: 360
url: /nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Learn how to export document structure while converting an Excel file to a tagged PDF using Aspose.Cells for Node.js via C++. 
---

PDF logical structure facilities provide a mechanism for incorporating information regarding the document content structure into a PDF file. Aspose.Cells for Node.js via C++ preserves information about the structure from a Microsoft Excel document, such as cell, row, table, worksheet, image, shape, header/footer, etc.

With option [PdfSaveOptions.exportDocumentStructure](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#exportDocumentStructure) you can save to a tagged PDF with the document structure exported.

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

