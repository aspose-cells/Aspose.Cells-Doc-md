---  
title: Daten im Nicht Primitive Shape mit Node.js via C++  
linktitle: Daten in nicht primitiver Form  
type: docs  
weight: 300  
url: /de/nodejs-cpp/data-in-non-primitive-shape/  
description: Erfahren Sie, wie Sie auf nicht primitiven Formen in Aspose.Cells for Node.js via C++ zugreifen und diese manipulieren.  
---  

## **Zugriff auf Daten nicht-primitiver Form**  

Manchmal müssen Sie auf Daten aus einer Form zugreifen, die nicht eingebaut ist. Eingebaute Formen werden primitive Formen genannt; solche, die es nicht sind, werden nicht-primitive genannt. Sie können beispielsweise eigene Formen mit verschiedenen verbundenen Kurvenlinien definieren.  

## **Eine nicht-primitive Form**  

In Aspose.Cells for Node.js via C++ werden nicht-primitiven Formen der Art [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/) zugewiesen. Sie können ihren Typ mit der Eigenschaft [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--) überprüfen.  

Greifen Sie auf die Formdaten mit der Eigenschaft [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--) zu. Diese gibt alle verbundenen Pfade zurück, die die nicht-primitiven Formen bilden. Diese Pfade sind vom Typ [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath), der eine Liste aller Segmente enthält, die wiederum die Punkte in jedem Segment enthalten.  

|**Zeigt ein Beispiel für eine nicht-primitive Form**|  
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

{{< app/cells/assistant language="nodejs-cpp" >}}
