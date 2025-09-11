---
title: Save Specified Worksheets to PDF with Node.js via C++
linktitle: Save Specified Worksheets to PDF
type: docs
weight: 140
url: /nodejs-cpp/save-specified-worksheets-to-pdf/
description: Learn how to save specified worksheets to PDF using Aspose.Cells for Node.js via C++. 
---


By default, Aspose.Cells saves all **visible** worksheets in a workbook to a PDF file. With [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) option, you can save specified worksheets to a PDF file. e.g. you can save the active worksheet to PDF, save all worksheets (both visible and hidden worksheets) to PDF, save custom multiple worksheets to PDF.

## **Save Active Worksheet to PDF**

If you want to only export the active sheet to PDF, you can achieve this by passing [**SheetSet.getActive()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getActive--) to [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) option.

The sheet `Sheet2` is the active sheet of the source file [sheetset-example.xlsx](sheetset-example.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set active sheet to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getActive());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **Save All Worksheets to PDF**

[**SheetSet.getVisible()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getVisible--) indicates visible sheets in a workbook, and [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) indicates all sheets including both visible sheets and hidden/invisible sheets in a workbook. If you want to export all sheets to PDF, you can just pass  [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) to [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) option.

The source file [sheetset-example.xlsx](sheetset-example.xlsx) contains all four sheets with hidden sheet `Sheet3`.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set all sheets to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getAll());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **Save Specified Worksheets to PDF**

If you want to export desired/custom multiple sheets to PDF, you can achieve this by passing multiple sheet indices to [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) option.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set custom multiple sheets(Sheet1, Sheet3) to output
const sheetSet = new AsposeCells.SheetSet([0, 2]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **Reorder Worksheets to PDF**

If you want to reorder sheets (e.g. in reverse order) to PDF without modifying the source file, you can achieve this by passing reordered sheet indices to [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) option.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");
// Open the template excel file
const wb = new AsposeCells.Workbook(filePath);

// Reorder sheets(Sheet1, Sheet2, Sheet3, Sheet4) to sheets(Sheet4, Sheet3, Sheet2, Sheet1)
const sheetSet = new AsposeCells.SheetSet([3, 2, 1, 0]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}