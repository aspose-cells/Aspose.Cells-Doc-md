---  
title: Text in Smart Art mit Node.js via C++ ersetzen  
linktitle: Ersetzen Sie Text in SmartArt  
type: docs  
weight: 1200  
url: /de/nodejs-cpp/replace-text-in-smart-art/  
description: Lernen Sie, wie man Text in Smart Art mit Aspose.Cells for Node.js via C++ ersetzt.  
---  

## **Mögliche Verwendungsszenarien**  

Smart Art ist eines der wichtigsten Objekte in einer Arbeitsmappe. Häufig besteht die Notwendigkeit, den Text in Smart Art zu aktualisieren. Aspose.Cells for Node.js via C++ bietet diese Funktion, indem es die [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--)-Eigenschaft setzt.  

Die Beispielquelle kann von folgendem Link heruntergeladen werden:  

[SmartArt.xlsx](77496338.xlsx)  

## **Beispielcode**  

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
