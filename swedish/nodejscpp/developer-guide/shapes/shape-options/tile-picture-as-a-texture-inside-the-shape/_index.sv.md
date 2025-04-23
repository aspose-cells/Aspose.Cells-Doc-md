---  
title: Tile Picture som textur inuti shape med Node.js via C++  
linktitle: Använda bild som texture i en form  
type: docs  
weight: 1700  
url: /sv/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Lär dig hur du kaklar en liten bild som textur inuti en form med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

När bilden är liten och täcker inte hela ytan av formen utan att förlora kvalitet, har du möjlighet att använda den som texture. Texturen fyller formens yta med en liten bild genom att upprepa dem som om de är kakel.  

## **Använda bild som texture i en form**  

Du kan fylla shape's yta med en bild och kakla den med hjälp av [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--)-egenskapen och sätta den till **true**. Se följande exempel, dess [sample Excel-fil](46465050.xlsx) samt skärmdump för referens.  

## **Skärmdump**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

