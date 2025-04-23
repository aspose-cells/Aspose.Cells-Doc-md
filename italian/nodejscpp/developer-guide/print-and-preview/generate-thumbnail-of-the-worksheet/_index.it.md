---
title: Genera anteprima del foglio di lavoro con Node.js tramite C++
linktitle: Generare un anteprima del foglio di lavoro
type: docs
weight: 110
url: /it/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Scopri come generare un immagine miniatura da un foglio di lavoro usando Aspose.Cells for Node.js via C++. Crea piccole immagini per anteprime in documenti e presentazioni.
---

{{% alert color="primary" %}} 

Può essere utile generare anteprime dai fogli di lavoro. Un'anteprima è un'immagine ridotta che può essere incollata in un documento Word o una presentazione PowerPoint per dare un'anteprima di ciò che c'è nel foglio di lavoro. Può essere aggiunta a una pagina Web con un collegamento per scaricare il documento originale e ha una serie di altri utilizzi.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ ti permette di esportare i fogli di lavoro in file immagine, quindi creare una miniatura è facile. Il codice di esempio di seguito mostra come esportare i fogli di lavoro in file immagine.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
