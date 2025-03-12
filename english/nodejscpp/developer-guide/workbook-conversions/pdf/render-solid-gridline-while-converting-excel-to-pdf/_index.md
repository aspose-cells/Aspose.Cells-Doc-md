---
title: Render Solid Gridline while converting Excel to PDF with Node.js via C++
linktitle: Render Solid Gridline while converting Excel to PDF
type: docs
weight: 390
url: /nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Learn how to render solid gridlines while converting Excel to PDF using Aspose.Cells for Node.js via C++. 
keywords: Render solid gridline to PDF Node.js via C++, Convert Excel to PDF with solid gridline Node.js via C++, PdfSaveOptions for solid gridline Node.js via C++ 
---

For compatibility with older versions, Aspose.Cells renders gridlines as dotted lines by default while converting Excel to PDF. However, modern Excel renders gridlines as solid lines today.

With option [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) , Aspose.Cells for Node.js via C++ can also render gridlines as solid lines.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an empty Workbook
const wb = new AsposeCells.Workbook();

// Prepare data
wb.getWorksheets().get(0).getCells().get("D9").putValue("gridline");

// Enable to print gridline
wb.getWorksheets().get(0).getPageSetup().setPrintGridlines(true);

// Set to render gridline as solid line
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setGridlineType(AsposeCells.GridlineType.Hair);

// Save the pdf file with PdfSaveOptions
wb.save(path.join(dataDir, "test_Cs.pdf"), pdfSaveOptions);
```

![solid-gridline.png](solid-gridline.png)

