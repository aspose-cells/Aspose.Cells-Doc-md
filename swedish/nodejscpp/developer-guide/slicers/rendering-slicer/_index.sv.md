---  
title: Rendering av slicer med Node.js via C++  
linktitle: Rendera slicer  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/rendering-slicer/  
---  

## **Möjliga användningsscenario**  
Aspose.Cells for Node.js via C++ stöder rendering av slicerformer. Om du konverterar ditt kalkylblad till en bild eller sparar det som PDF eller HTML, kommer slicers att renderas ordentligt.  

## **Rendering slicer**  
Följande exempel laddar [exempel-Excel-filen](67338479.xlsx) som innehåller en befintlig slicer. Den konverterar kalkylbladet till en bild genom att sätta utskriftsområdet som endast täcker slicern. Den resulterande bilden är [utdata-bild](67338480.png) som visar den renderade slicern. Som du kan se, har slicern renderats ordentligt och ser likadan ut som i exempel-Excel-filen.  

![todo:image_alt_text](rendering-slicer_1)  
## **Exempelkod**  
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

