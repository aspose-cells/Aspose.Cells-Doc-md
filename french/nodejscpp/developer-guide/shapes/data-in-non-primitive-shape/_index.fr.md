---  
title: Données dans une forme non primitive avec Node.js via C++  
linktitle: Données dans une forme non primitive  
type: docs  
weight: 300  
url: /fr/nodejs-cpp/data-in-non-primitive-shape/  
description: Apprenez à accéder et à manipuler les formes non primitives dans Aspose.Cells for Node.js via C++.  
---  

## **Accès aux données d'une forme non primitive**  

Parfois, vous avez besoin d'accéder aux données d'une forme qui n'est pas intégrée. Les formes intégrées sont appelées formes primitives; celles qui ne le sont pas sont appelées non primitives. Par exemple, vous pouvez définir vos propres formes en utilisant différentes lignes connectées par courbe.  

## **Une forme non primitive**  

Dans Aspose.Cells for Node.js via C++, les formes non primitives se voient attribuer le type [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/). Vous pouvez vérifier leur type en utilisant la propriété [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--).  

Accédez aux données de la forme en utilisant la propriété [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--). Elle renvoie tous les chemins connectés qui composent la forme non primitive. Ces chemins sont de type [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath) qui contient une liste de tous les segments, lesquels contiennent à leur tour les points dans chaque segment.  

|**Montre un exemple d'une forme non primitive**|  
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
