---
title: Begrenzung der Anzahl der erzeugten Seiten  Excel zu PDF Konvertierung mit Node.js via C++
linktitle: Begrenzen der Anzahl der generierten Seiten  Umsetzung von Excel in PDF
type: docs
weight: 180
url: /de/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie die Anzahl der beim Konvertieren eines Excel Tabellendokuments in PDF erzeugten Seiten mit Aspose.Cells for Node.js via C++ beschränken. 
---

{{% alert color="primary" %}}

Manchmal möchten Sie einen Seitenbereich in eine Ausgabedatei PDF drucken. Aspose.Cells for Node.js via C++ bietet die Möglichkeit, eine Begrenzung vorzunehmen, wie viele Seiten beim Konvertieren eines Excel-Tabellendokuments in das PDF-Format erzeugt werden.

{{% /alert %}}

## **Begrenzen der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Bereich von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF umgesetzt wird.

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

Wenn die Tabelle Formeln enthält, ist es am besten, kurz vor dem Rendern in PDF [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) aufzurufen. Dies stellt sicher, dass formelabhängige Werte neu berechnet werden und die korrekten Werte in der Ausgabedatei angezeigt werden.

{{% /alert %}}
