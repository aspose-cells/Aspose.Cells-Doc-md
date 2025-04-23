---  
title: البيانات في شكل غير بدائي باستخدام Node.js عبر C++  
linktitle: البيانات في شكل غير الذي يتميز ببساطة  
type: docs  
weight: 300  
url: /ar/nodejs-cpp/data-in-non-primitive-shape/  
description: تعلم كيفية الوصول والتلاعب بالأشكال غير البدائية في Aspose.Cells for Node.js via C++.  
---  

## **الوصول إلى بيانات الشكل غير الذي يتميز ببساطة**  

في بعض الأحيان، تحتاج إلى الوصول إلى البيانات من شكل ليس مدمجًا. يطلق على الأشكال المدمجة ، الأشكال الأساسية ، ويطلق على الأشكال التي ليست كذلك ، الأشكال غير الأساسية. على سبيل المثال، يمكنك تحديد أشكالك الخاصة باستخدام خطوط متصلة مختلفة.  

## **الشكل غير الأساسي**  

في Aspose.Cells for Node.js via C++، يتم تعيين الأشكال غير البدائية على أنها من النوع [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/). يمكنك التحقق من نوعها باستخدام خاصية [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--).  

الوصول إلى بيانات الشكل باستخدام خاصية [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--). وتُرجع كافة المسارات المرتبطة التي تتكون منها الشكل غير البدائي. هذه المسارات من النوع [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath) وتحتوي على قائمة بجميع القطاعات التي تحتوي بدورها على النقاط في كل قطاع.  

|**يظهر مثالًا على شكل غير أساسي**|  
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

