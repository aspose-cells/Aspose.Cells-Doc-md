---  
title: Dati in forma non primitiva con Node.js tramite C++  
linktitle: Dati in Forma Non Primitiva  
type: docs  
weight: 300  
url: /it/nodejs-cpp/data-in-non-primitive-shape/  
description: Scopri come accedere e manipolare forme non primitive in Aspose.Cells for Node.js via C++.  
---  

## **Accesso ai Dati di Forma Non-Primitiva**  

A volte, è necessario accedere ai dati da una forma non incorporata. Le forme incorporate sono chiamate forme primitive; quelle che non lo sono vengono chiamate non primitive. Ad esempio, è possibile definire le proprie forme utilizzando diverse linee collegate da curve.  

## **Una Forma Non-Primitiva**  

In Aspose.Cells for Node.js via C++, le forme non primitive sono assegnate al tipo [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/). Puoi verificare il loro tipo utilizzando la proprietà [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--).  

Accedi ai dati della forma usando la proprietà [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--). Ritorna tutti i percorsi collegati che compongono la forma non primitiva. Questi percorsi sono di tipo [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath) che contiene un elenco di tutti i segmenti che a loro volta contengono i punti in ciascun segmento.  

|**Mostra un esempio di una forma non primitiva**|  
| :- |  
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "NonPrimitiveShape.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Accessing the user defined shape
const shape = worksheet.getShapes().get(0);

if (shape.getAutoShapeType() === AsposeCells.AutoShapeType.NotPrimitive) 
{
// Access shape's data
const shapePathCollection = shape.getPaths();

// Access information of individual path
for (let i = 0; i < shapePathCollection.getCount(); i++) 
{
const shapePath = shapePathCollection.get(i);
// Access path segment list
const pathSegments = shapePath.getPathSegementList();

// Access individual path segment
for (let j = 0; j < pathSegments.getCount(); j++)
{
const pathSegment = pathSegments.get(j);
// Gets the points in path segment
const segmentPoints = pathSegment.getPoints();

for (let k = 0; k < segmentPoints.getCount(); k++) 
{
const pathPoint = segmentPoints.get(k);
console.log("X: " + pathPoint.getX() + ", Y: " + pathPoint.getY());
}
}
}
}
```  

