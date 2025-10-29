---  
title: 使用 Node.js via C++ 在非原始形状的数据  
linktitle: 非基本形状中的数据  
type: docs  
weight: 300  
url: /zh/nodejs-cpp/data-in-non-primitive-shape/  
description: 了解如何在 Aspose.Cells for Node.js via C++ 中访问和操作非原始形状。  
---  

## **访问非基本形状的数据**  

有时，您需要访问非内置形状的形状的数据。内置形状称为基本形状；而不是内置形状的称为非基本形状。例如，您可以使用不同的曲线连接线定义自己的形状。  

## **非基本形状**  

在 Aspose.Cells for Node.js via C++ 中，非原始形状被赋予类型 [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/)。你可以通过 [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--) 属性检查它们的类型。  

使用 [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--) 属性访问形状数据。它返回构成非原始形状的所有连接路径。这些路径的类型是 [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath)，包含一个段落列表，每个段落包含该段中的点。  

|**显示了非原始形状的示例**|  
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
