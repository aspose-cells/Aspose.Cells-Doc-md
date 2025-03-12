---
title: Limit the Number of Pages Generated - Excel to PDF Conversion with Node.js via C++
linktitle: Limit the Number of Pages Generated - Excel to PDF Conversion
type: docs
weight: 180
url: /nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Learn how to limit the number of pages generated when converting an Excel spreadsheet to PDF using Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Sometimes, you want to print a range of pages to an output PDF file. Aspose.Cells for Node.js via C++ has the ability to set a limit on how many pages are generated when converting an Excel spreadsheet to the PDF file format.

{{% /alert %}}

## **Limiting the Number of Pages Generated**

The following example shows how to render a range of pages (3 and 4) in a Microsoft Excel file to PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Instantiate the PdfSaveOption
const options = new AsposeCells.PdfSaveOptions();

// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.setPageIndex(3);
// Number of pages to be printed
options.setPageCount(2);

// Save the PDF file
workbook.save(path.join(dataDir, "outPDF1.out.pdf"), options);
```

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering it to PDF. Doing so ensures that formula-dependent values are recalculated, and the correct values are rendered in the output file.

{{% /alert %}}
