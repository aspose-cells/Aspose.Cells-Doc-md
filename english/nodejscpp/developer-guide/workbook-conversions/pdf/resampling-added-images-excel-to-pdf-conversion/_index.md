---
title: Resampling Added Images - Excel to PDF Conversion with Node.js via C++
linktitle: Resampling Added Images
type: docs
weight: 150
url: /nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Learn how to compress images added in Excel files to reduce PDF size and improve conversion performance using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

While working with big Microsoft Excel files with lots of images, you might need to compress images that have been added to reduce the output PDF file size and improve the overall conversion performance. Aspose.Cells for Node.js via C++ supports resampling added images to reduce the output PDF file size and improve the performance somewhat.

{{% /alert %}}

Please see the following sample code that describes how to perform the task using the Aspose.Cells API. The example converts a Microsoft Excel file to a PDF file while compressing the images in the file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

Using the the [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) option minimizes the size of the output PDF but it may affect the image quality a bit.

{{% /alert %}} {{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
