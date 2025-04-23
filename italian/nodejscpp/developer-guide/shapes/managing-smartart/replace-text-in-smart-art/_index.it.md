---  
title: Sostituisci il testo in smart art con Node.js tramite C++  
linktitle: Sostituire il testo nella forma di arte intelligente  
type: docs  
weight: 1200  
url: /it/nodejs-cpp/replace-text-in-smart-art/  
description: Impara come sostituire il testo in smart art usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Lo smart art è uno degli oggetti principali in una cartella di lavoro. Spesso è necessario aggiornare il testo nello smart art. Aspose.Cells for Node.js via C++ fornisce questa funzionalità impostando la proprietà [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).  

Il file di origine di esempio può essere scaricato dal seguente link:  

[SmartArt.xlsx](77496338.xlsx)  

## **Codice di Esempio**  

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

