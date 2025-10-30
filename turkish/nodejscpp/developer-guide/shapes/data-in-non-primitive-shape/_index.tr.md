---  
title: Node.js ve C++ kullanarak Non Primitive Shape Verisi  
linktitle: Non Primitive Şekildeki Veri  
type: docs  
weight: 300  
url: /tr/nodejs-cpp/data-in-non-primitive-shape/  
description: Aspose.Cells for Node.js via C++ kullanarak non primitif şekilleri nasıl erişip işleyeceğinizi öğrenin.  
---  

## **Basit olmayan Şeklin Verilerine Erişmek**  

Bazı durumlarda, yerleşik olmayan bir şekilden veriye erişmeniz gerekebilir. Yerleşik şekiller basit şekiller olarak adlandırılırken, diğerleri basit olmayan şekiller olarak adlandırılır. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.  

## **Basit Olmayan Bir Şekil**  

Aspose.Cells for Node.js via C++'te, non-primitif şekillere [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/) tipi atanmıştır. Türlerini [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--) özelliğini kullanarak kontrol edebilirsiniz.  

Non-primitif şekil verilerine [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--) özelliğini kullanarak erişin. Bu, non-primitif şekli oluşturan tüm bağlantılı yolları döndürür. Bu yollar, her biri noktaları içeren segmentlerin listesini tutan [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath) tipiyle temsil edilir.  

|**Primitif Olmayan Bir Şeklin Örneğini Gösterir**|  
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
