---
title: Estrazione di immagini dai fogli di lavoro utilizzando ImageOrPrintOptions con Node.js tramite C++
linktitle: Estrai immagini dai fogli di lavoro utilizzando ImageOrPrintOptions
type: docs
weight: 140
url: /it/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Scopri come estrarre immagini dai fogli di lavoro Excel e salvarle usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Gli utenti di Microsoft Excel possono aggiungere immagini ai fogli di calcolo. Con Aspose.Cells for Node.js via C++, è possibile leggere le immagini dai file Excel di Microsoft e salvarle su disco locale. Questo articolo mostra come.

{{% /alert %}} 

Il codice di esempio di seguito mostra come estrarre immagini da un file di Excel e salvarle.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
