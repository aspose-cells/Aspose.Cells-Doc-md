---  
title: Esporta foglio di lavoro o grafico in immagine con larghezza e altezza desiderate tramite Node.js  
linktitle: Esporta un foglio di lavoro o un grafico in un immagine con larghezza e altezza desiderate  
type: docs  
weight: 290  
url: /it/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: Scopri come esportare un foglio di lavoro o grafico in un immagine con larghezza e altezza specificate usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Puoi usare Aspose.Cells for Node.js via C++ per esportare il tuo foglio di lavoro o grafico in un'immagine con la larghezza e altezza desiderate. Fornisce il metodo [**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-) per impostare la larghezza e altezza desiderate dell'immagine esportata. Le dimensioni sono specificate in pixel.  
{{% /alert %}}  

Il seguente codice esporta il foglio di lavoro in un'immagine delle dimensioni 400x400.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const filePath = path.join(sourceDir, "sampleWorksheetToImageDesiredSize.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set image or print options we want one page per sheet. The image format is in png and desired dimensions are 400x400
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);
opts.setDesiredSize(400, 400, false);

// Render sheet into image
const sr = new AsposeCells.SheetRender(worksheet, opts);
sr.toImage(0, path.join(outputDir, "outputWorksheetToImageDesiredSize.png"));
```  

