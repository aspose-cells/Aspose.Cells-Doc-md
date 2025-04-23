---
title: Calcola il fattore di scala della configurazione pagina con Node.js tramite C++
linktitle: Calcola il fattore di scala della pagina di impostazione
type: docs
weight: 300
url: /it/nodejs-cpp/calculate-page-setup-scaling-factor/
description: Questo articolo fornisce codice di esempio che spiega come usare l API Node.js con C++ per calcolare il fattore di scala della configurazione pagina utilizzando l opzione Adatta a n pagina(i) in larghezza per m in altezza del foglio di lavoro di Excel programmaticamente.
keywords: Adatta a n pagine in larghezza per m in altezza excel Node.js tramite C++, calcola il fattore di scala della configurazione pagina con Node.js tramite C++
---

{{% alert color="primary" %}}

Quando imposti la scalabilità della configurazione pagina usando l'opzione **Adatta a n pagina(i) in larghezza per m in altezza**, Microsoft Excel calcola il Fattore di Scala della Configurazione Pagina. Puoi calcolare la stessa cosa usando la proprietà [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--). Questa proprietà restituisce un valore double che può essere convertito in percentuale. Ad esempio, se restituisce 0.5, significa che il fattore di scala è il 50%.

{{% /alert %}}

Il seguente codice di esempio illustra come calcolare il fattore di scala dell'impostazione della pagina utilizzando la proprietà [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
