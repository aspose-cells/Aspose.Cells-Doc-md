---
title: Rifacimento Immagini Aggiunte  Conversione da Excel a PDF con Node.js tramite C++
linktitle: Rifacimento Immagini Aggiunte
type: docs
weight: 150
url: /it/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Impara come comprimere le immagini aggiunte nei file Excel per ridurre la dimensione del PDF e migliorare le prestazioni di conversione usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Durante il lavoro con grandi file Microsoft Excel con molte immagini, potresti aver bisogno di comprimere le immagini aggiunte per ridurre la dimensione del file PDF di output e migliorare le prestazioni complessive di conversione. Aspose.Cells for Node.js via C++ supporta il risampling delle immagini aggiunte per ridurre un po' la dimensione del file PDF di output e migliorare le prestazioni.

{{% /alert %}}

Si prega di consultare il codice di esempio seguente che descrive come eseguire il compito utilizzando l'API Aspose.Cells. L'esempio converte un file Microsoft Excel in un file PDF comprimendo le immagini nel file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

Utilizzare l'opzione [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) minimizza la dimensione del PDF di output, ma potrebbe influire leggermente sulla qualità dell'immagine.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
