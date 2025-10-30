---  
title: Converti Excel in immagine ad alta risoluzione con Node.js tramite C++  
linktitle: Convertire Excel in immagine ad alta risoluzione  
type: docs  
weight: 100  
url: /it/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: Scopri come convertire i file Excel in immagini ad alta risoluzione usando Aspose.Cells for Node.js via C++.  
---  

 Con la crescente diffusione di schermi ad alta risoluzione, le immagini generate a 96 DPI risultano spesso sfocate e poco chiare. Per garantire chiarezza su schermi ad alta risoluzione, è essenziale generare immagini a DPI superiori. Aspose.Cells for Node.js via C++ offre la funzionalità di impostare [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) e [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--), permettendoti di creare immagini di alta qualità da file Excel che appaiono nitide su display ad alta risoluzione.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of ImageOrPrintOptions
const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(300);
options.setVerticalResolution(300);
options.setImageType(AsposeCells.ImageType.Png);

// Get the worksheet
const sheet = workbook.getWorksheets().get(0);

// Create a SheetRender instance
const render = new AsposeCells.SheetRender(sheet, options);

// Generate and save the image
render.toImage(0, "output.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
