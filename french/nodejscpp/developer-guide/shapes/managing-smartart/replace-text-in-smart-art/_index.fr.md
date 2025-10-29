---  
title: Remplacer le texte dans l art intelligent avec Node.js via C++  
linktitle: Remplacer le texte dans l art intelligent  
type: docs  
weight: 1200  
url: /fr/nodejs-cpp/replace-text-in-smart-art/  
description: Apprenez comment remplacer le texte dans l art intelligent en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

L'art intelligent est l'un des principaux objets dans un classeur. Souvent, il est nécessaire de mettre à jour le texte dans l'art intelligent. Aspose.Cells for Node.js via C++ fournit cette fonctionnalité en fixant la propriété [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).  

Le fichier source d'exemple peut être téléchargé à partir du lien suivant :  

[SmartArt.xlsx](77496338.xlsx)  

## **Code d'exemple**  

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
