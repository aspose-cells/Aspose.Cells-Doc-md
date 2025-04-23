---  
title: Rendering Slicer con Node.js tramite C++  
linktitle: Rendering del filtro  
type: docs  
weight: 40  
url: /it/nodejs-cpp/rendering-slicer/  
---  

## **Possibili Scenari di Utilizzo**  
Aspose.Cells for Node.js via C++ supporta il rendering delle forme dello slicer. Se converti il tuo foglio di lavoro in un'immagine o salvi il tuo workbook in formato PDF o HTML, vedrai che gli slicer vengono resi correttamente.  

## **Rendering dello slicer**  
Il seguente esempio di codice carica il [file Excel di esempio](67338479.xlsx) che contiene uno slicer esistente. Converte il foglio di lavoro in un'immagine impostando l'area di stampa che copre solo lo slicer. L'immagine risultante è l'[immagine di output](67338480.png) che mostra lo slicer reso. Come puoi vedere, lo slicer è stato renderizzato correttamente e appare come nel file Excel di esempio.  

![todo:image_alt_text](rendering-slicer_1)  
## **Codice di Esempio**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  

