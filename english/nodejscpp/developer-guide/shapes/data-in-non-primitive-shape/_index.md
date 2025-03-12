---  
title: Data in Non-Primitive Shape with Node.js via C++  
linktitle: Data in Non-Primitive Shape  
type: docs  
weight: 300  
url: /nodejs-cpp/data-in-non-primitive-shape/  
description: Learn how to access and manipulate non-primitive shapes in Aspose.Cells for Node.js via C++.  
---  

## **Accessing Data of Non-Primitive Shape**  

Sometimes, you need to access data from a shape that is not built-in. Built-in shapes are called primitive shapes; ones that aren't are called non-primitive. For example, you can define your own shapes using different curve connected lines.  

## **A Non-Primitive Shape**  

In Aspose.Cells for Node.js via C++, non-primitive shapes are assigned the type [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/nodejs-cpp/autoshapetype/). You can check their type using the [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getAutoShapeType--) property.  

Access the shape data using the [**Shape.getPaths()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getPaths--) property. It returns all the connected paths that comprise the non-primitive shape. These paths are of the type [**ShapePath**](https://reference.aspose.com/cells/nodejs-cpp/shapepath) that holds a list of all the segments which in turn contain the points in each segment.  

|**Shows an example of a non-primitive shape**|  
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

if (shape.getAutoShapeType() === AsposeCells.AutoShapeType.NotPrimitive) {
    // Access shape's data
    const shapePathCollection = shape.getPaths();

    // Access information of individual path
    for (let i = 0; i < shapePathCollection.getCount(); i++) {
        const shapePath = shapePathCollection.get(i);
        // Access path segment list
        const pathSegments = shapePath.getPathSegementList();

        // Access individual path segment
        for (let j = 0; j < pathSegments.getCount(); j++) {
            const pathSegment = pathSegments.get(j);
            // Gets the points in path segment
            const segmentPoints = pathSegment.getPoints();

            for (let k = 0; k < segmentPoints.getCount(); k++) {
                const pathPoint = segmentPoints.get(k);
                console.log("X: " + pathPoint.getX() + ", Y: " + pathPoint.getY());
            }
        }
    }
}
```  
  