---
title: Limita il Numero di Pagine Generate  Conversione da Excel a PDF con Node.js tramite C++
linktitle: Limita il numero di pagine generate  Conversione di Excel in PDF
type: docs
weight: 180
url: /it/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Impara a limitare il numero di pagine generate quando converti un foglio di calcolo Excel in PDF usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

A volte, vuoi stampare un intervallo di pagine in un file PDF di output. Aspose.Cells for Node.js via C++ ha la capacità di impostare un limite su quante pagine vengono generate durante la conversione di un foglio di calcolo Excel nel formato PDF.

{{% /alert %}}

## **Limitazione del numero di pagine generate**

L'esempio seguente mostra come rendere un intervallo di pagine (3 e 4) in un file Microsoft Excel in PDF.

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

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) subito prima di renderizzarlo in PDF. Questo garantisce che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti siano presenti nel file di output.

{{% /alert %}}
