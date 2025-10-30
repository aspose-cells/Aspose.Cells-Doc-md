---
title: Solide Rasterlinien beim Konvertieren von Excel in PDF mit Node.js über C++ rendern
linktitle: Solide Rasterlinien beim Konvertieren von Excel in PDF rendern
type: docs
weight: 390
url: /de/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Erfahren Sie, wie man solide Rasterlinien beim Konvertieren von Excel in PDF mit Aspose.Cells for Node.js via C++ rendert. 
keywords: Solide Rasterlinie in PDF mit Node.js über C++ rendern, Excel in PDF mit solider Rasterlinie in Node.js über C++ konvertieren, PdfSaveOptions für solide Rasterlinie in Node.js über C++ 
---

Für Kompatibilität mit älteren Versionen rendert Aspose.Cells Rasterlinien standardmäßig als punktierte Linien bei der Konvertierung von Excel in PDF. Moderne Excel-Versionen rendern Rasterlinien heute jedoch als durchgehende Linien.

Mit der Option [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) kann Aspose.Cells for Node.js via C++ Rasterlinien ebenfalls als durchgehende Linien rendern.

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
