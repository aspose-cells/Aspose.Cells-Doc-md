---
title: Exportera dokumentstruktur vid konvertering till PDF med Node.js via C++
linktitle: Exportera dokumentstruktur vid konvertering till PDF
type: docs
weight: 360
url: /sv/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Lär dig hur du exporterar dokumentstruktur vid konvertering av en Excel fil till en märkt PDF med Aspose.Cells for Node.js via C++. 
---

PDF:s logiska strukturfunktioner ger en mekanism för att inkludera information om dokumentets innehållsstruktur i en PDF-fil. Aspose.Cells for Node.js via C++ bevarar information om strukturen från ett Microsoft Excel-dokument, som cell, rad, tabell, arbetsblad, bild, form, sidhuvud/fotdel, etc.

Med alternativet [PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--) kan du spara till en märkt PDF med exporterad dokumentstruktur.

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

{{< app/cells/assistant language="nodejs-cpp" >}}
