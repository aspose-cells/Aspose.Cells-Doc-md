---
title: Rendera solid rutnätslinje vid konvertering av Excel till PDF med Node.js via C++
linktitle: Rendera Solid Gridline när du konverterar Excel till PDF
type: docs
weight: 390
url: /sv/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Lär dig hur man renderar solid rutnätslinjer vid konvertering av Excel till PDF med Aspose.Cells for Node.js via C++. 
keywords: Rendera solid rutnätslinje till PDF Node.js via C++, Konvertera Excel till PDF med solid rutnätslinje Node.js via C++, PdfSaveOptions för solid rutnätslinje Node.js via C++ 
---

För kompatibilitet med äldre versioner renderar Aspose.Cells rutnätslinjer som prickade linjer som standard vid konvertering av Excel till PDF. Moderna Excel-versioner visar dock rutnätslinjer som solid linje idag.

Med alternativet [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) kan Aspose.Cells for Node.js via C++ också rendera rutnätslinjer som solid linje.

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

{{< app/cells/assistant language="nodejs-cpp" >}}
