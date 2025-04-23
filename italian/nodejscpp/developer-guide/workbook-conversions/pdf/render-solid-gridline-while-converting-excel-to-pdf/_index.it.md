---
title: Renderizza linee di griglia solide durante la conversione di Excel in PDF con Node.js tramite C++
linktitle: Renderizza linee di griglia solide durante la conversione di Excel in PDF
type: docs
weight: 390
url: /it/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Impara come rendere le linee di griglia solide durante la conversione di Excel in PDF usando Aspose.Cells for Node.js via C++. 
keywords: Renderizza linee di griglia solide su PDF Node.js tramite C++, converte Excel in PDF con linee di griglia solide Node.js tramite C++, PdfSaveOptions per linee di griglia solide Node.js tramite C++ 
---

Per compatibilità con versioni più vecchie, Aspose.Cells rende le linee di griglia come linee tratteggiate di default durante la conversione di Excel in PDF. Tuttavia, Excel moderno rende le linee di griglia come linee solide oggi.

Con l'opzione [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) , Aspose.Cells for Node.js via C++ può anche rendere le linee di griglia come linee solide.

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

