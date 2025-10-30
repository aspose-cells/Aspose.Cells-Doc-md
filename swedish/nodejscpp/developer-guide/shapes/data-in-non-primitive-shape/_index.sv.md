---  
title: Data i icke primitive shapes med Node.js via C++  
linktitle: data i icke primitiv form  
type: docs  
weight: 300  
url: /sv/nodejs-cpp/data-in-non-primitive-shape/  
description: Lär dig hur du får tillgång till och manipulerar icke primitive former i Aspose.Cells for Node.js via C++.  
---  

## **Åtkomst till data av icke-primitiv form**  

Ibland behöver du få åtkomst till data från en form som inte är inbyggd. Inbyggda former kallas primitiva former; de som inte är det kallas icke-primitiva. Till exempel kan du definiera dina egna former med olika kurvanslutna linjer.  

## **En icke-primitiv form**  

I Aspose.Cells for Node.js via C++ tilldelas icke-primitive former typen [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/). Du kan kontrollera deras typ med egenskapen [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--).  

Få tillgång till formdata med [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--)-egenskapen. Den returnerar alla kopplade vägar som utgör den icke-primitive formen. Dessa vägar är av typen [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath) som innehåller en lista över alla segment som i sin tur innehåller punkterna i varje segment.  

|**Visar ett exempel på en icke-primitiv form**|  
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
