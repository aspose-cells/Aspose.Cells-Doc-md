---  
title: Ersätt text i smart art med Node.js via C++  
linktitle: Ersätt text i Smart Art  
type: docs  
weight: 1200  
url: /sv/nodejs-cpp/replace-text-in-smart-art/  
description: Lär dig hur du ersätter text i smart art med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Smart art är en av de viktigaste objekten i en arbetsbok. Ofta finns det ett behov av att uppdatera texten i smart art. Aspose.Cells for Node.js via C++ tillhandahåller denna funktion genom att sätta [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) egenskapen.  

Den provkällfilen kan laddas ner från följande länk:  

[SmartArt.xlsx](77496338.xlsx)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SmartArt.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(sourceFilePath);

const worksheets = wb.getWorksheets();
for (let i = 0; i < worksheets.getCount(); i++) 
{
const worksheet = worksheets.get(i);
const shapes = worksheet.getShapes();
for (let j = 0; j < shapes.getCount(); j++) 
{
const shape = shapes.get(j);
shape.setAlternativeText("ReplacedAlternativeText"); // This works fine just as the normal Shape objects do.
if (shape.isSmartArt()) 
{
const smartArtShapes = shape.getResultOfSmartArt().getGroupedShapes();
for (let k = 0; k < smartArtShapes.length; k++) 
{
const smartart = smartArtShapes[k];
smartart.setText("ReplacedText"); // This doesn't update the text in Workbook which I save to the another file.
}
}
}
}

const options = new AsposeCells.OoxmlSaveOptions();
options.setUpdateSmartArt(true);
const outputFilePath = path.join(dataDir, "outputSmartArt.xlsx");
wb.save(outputFilePath, options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
