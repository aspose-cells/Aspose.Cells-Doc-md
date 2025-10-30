---
title: Autoadatta colonne e righe durante il caricamento di HTML in Workbook con Node.js tramite C++
linktitle: Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook
type: docs
weight: 120
url: /it/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Scopri come autoadattare colonne e righe durante il caricamento di file HTML in un Workbook usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

Puoi autoadattare colonne e righe mentre carichi il tuo file HTML all'interno dell'oggetto Workbook. Imposta la proprietà [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) a **true** a questo scopo.

## **Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook**

Il seguente esempio di codice carica prima il campione HTML in un Workbook senza opzioni di caricamento e lo salva in formato XLSX. Successivamente, carica di nuovo il campione HTML nel Workbook, questa volta impostando la proprietà [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) a **true**, e lo salva in formato XLSX. Scarica entrambi i file excel generati, cioè [Output Excel senza AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) e [Output Excel con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). La schermata seguente mostra l'effetto della proprietà [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) su entrambi i file Excel di output.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
