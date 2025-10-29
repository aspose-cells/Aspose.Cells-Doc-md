---  
title: Данные в нел primitives форм фигуры с помощью Node.js через C++  
linktitle: Данные в не примитивной форме  
type: docs  
weight: 300  
url: /ru/nodejs-cpp/data-in-non-primitive-shape/  
description: Узнайте, как получать доступ и управлять нел primitives фигурами в Aspose.Cells for Node.js via C++.  
---  

## **Доступ к данным не примитивной формы**  

Иногда вам может потребоваться получить доступ к данным из формы, которая не встроена. Встроенные формы называют примитивными, а те, которых нет, называют не примитивными. Например, вы можете определить свои собственные формы, используя разные кривые соединенные линии.  

## **Форма не примитивной формы**  

В Aspose.Cells for Node.js via C++ нел primitives фигуры имеют тип [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/). Вы можете проверить их тип с помощью свойства [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--).  

Доступ к данным фигуры с помощью свойства [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--). Оно возвращает все связанные пути, составляющие нел primitives фигуру. Эти пути типа [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath), которые содержат список всех сегментов, каждый из которых содержит точки.  

|**Показывает пример нетипичной формы**|  
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
