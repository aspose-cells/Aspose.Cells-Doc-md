---  
title: Reemplazar texto en arte inteligente con Node.js vía C++  
linktitle: Reemplazar texto en el arte inteligente  
type: docs  
weight: 1200  
url: /es/nodejs-cpp/replace-text-in-smart-art/  
description: Aprende cómo reemplazar texto en arte inteligente usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

El arte inteligente es uno de los objetos principales en un libro de trabajo. Muchas veces es necesario actualizar el texto en el arte inteligente. Aspose.Cells for Node.js via C++ proporciona esta función configurando la propiedad [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).  

El archivo fuente de muestra se puede descargar desde el siguiente enlace:  

[SmartArt.xlsx](77496338.xlsx)  

## **Código de muestra**  

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

