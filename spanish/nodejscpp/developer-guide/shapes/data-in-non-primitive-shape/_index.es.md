---  
title: Datos en Forma No Primitiva con Node.js a través de C++  
linktitle: Datos en forma no primitiva  
type: docs  
weight: 300  
url: /es/nodejs-cpp/data-in-non-primitive-shape/  
description: Aprende cómo acceder y manipular formas no primitivas en Aspose.Cells for Node.js via C++.  
---  

## **Acceso a datos de forma no primitiva**  

A veces, necesitas acceder a datos de una forma que no está incorporada. Las formas incorporadas se llaman formas primitivas; las que no lo son se llaman no primitivas. Por ejemplo, puedes definir tus propias formas usando diferentes líneas conectadas curvas.  

## **Una forma no primitiva**  

En Aspose.Cells for Node.js via C++, las formas no primitivas se asignan al tipo [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/). Puedes verificar su tipo usando la propiedad [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--).  

Accede a los datos de la forma usando la propiedad [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--). Esta devuelve todos los caminos conectados que componen la forma no primitiva. Estos caminos son del tipo [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath) que contiene una lista de todos los segmentos que, a su vez, contienen los puntos en cada segmento.  

|**Muestra un ejemplo de una forma no primitiva**|  
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

