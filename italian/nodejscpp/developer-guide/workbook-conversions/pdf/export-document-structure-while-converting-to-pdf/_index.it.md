---
title: Esporta la struttura del documento durante la conversione in PDF con Node.js tramite C++
linktitle: Esportare la Struttura del Documento Durante la Conversione in PDF
type: docs
weight: 360
url: /it/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Impara come esportare la struttura del documento durante la conversione di un file Excel in PDF contrassegnato usando Aspose.Cells for Node.js via C++. 
---

Le strutture logiche PDF forniscono un meccanismo per incorporare informazioni sulla struttura del contenuto del documento in un file PDF. Aspose.Cells for Node.js via C++ preserva le informazioni sulla struttura di un documento Microsoft Excel, come celle, righe, tabelle, fogli di lavoro, immagini, forme, intestazione/piedipagina, ecc.

Con l’opzione [PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--) puoi salvare in un PDF con tag con la struttura del documento esportata.

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
