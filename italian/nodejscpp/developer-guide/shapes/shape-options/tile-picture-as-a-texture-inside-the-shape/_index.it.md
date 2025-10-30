---  
title: Immagine a piastrelle come texture all’interno della forma con Node.js tramite C++  
linktitle: Immagine del piastrella come texture all interno della forma  
type: docs  
weight: 1700  
url: /it/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Impara come tiled una piccola immagine come texture all’interno di una forma usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Quando l'immagine è piccola e non copre l'intera superficie della forma senza perdere la sua qualità, hai l'opzione di piastrellarla. La piastrellatura riempie la superficie della forma con un'immagine piccola ripetendola come se fossero piastrelle.  

## **Immagine del piastrella come texture all'interno della forma**  

Puoi riempire la superficie della forma con un’immagine e tile usando la proprietà [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) e impostandola su **true**. Vedi il codice di esempio sottostante, il file Excel di esempio e lo screenshot per riferimento.  

## **Screenshot**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Codice di Esempio**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
