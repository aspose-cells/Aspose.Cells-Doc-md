---  
title: Node.jsとC++を使用した非プリミティブシェイプのデータ操作  
linktitle: 非原始の形のデータ  
type: docs  
weight: 300  
url: /ja/nodejs-cpp/data-in-non-primitive-shape/  
description: Aspose.Cells for Node.js via C++で非プリミティブシェイプにアクセスし操作する方法を学びます。  
---  

## **非原始の形のデータへのアクセス**  

時々、ビルトインでない形状からデータにアクセスする必要があります。ビルトインの形状は原始形状と呼ばれ、そうでないものは非原始形状と呼ばれます。例えば、異なる曲線接続線を使用して独自の形状を定義することができます。  

## **非原始の形状**  

Aspose.Cells for Node.js via C++では、非プリミティブシェイプはタイプ[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/)に割り当てられています。[**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--)プロパティを使って型を確認できます。  

[**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--)プロパティを使用してシェイプデータにアクセスします。これにより、非プリミティブシェイプを構成するすべての接続されたパスが取得できます。これらのパスは[**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath)タイプであり、すべてのセグメントのリストを保持し、それぞれのセグメントにはポイントが含まれています。  

|**非原始の形状の例を示す**|  
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
