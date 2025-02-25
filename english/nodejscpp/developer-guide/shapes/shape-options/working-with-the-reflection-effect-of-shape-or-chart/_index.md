---
title: Working with the Reflection Effect of Shape or Chart with Node.js via C++
linktitle: Working with the Reflection Effect of Shape or Chart
type: docs
weight: 210
url: /nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Learn how to work with the reflection effect of shapes or charts using Aspose.Cells for Node.js via C++. Set various reflection properties to achieve desired results.
---

## **Possible Usage Scenarios**
Aspose.Cells for Node.js via C++ provides the [Shape.Reflection](https://reference.aspose.com/cells/nodejs-cpp/shape/#reflection) property along with the [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) class to work with the reflection effect of shape or chart. The [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) class contains the following properties which can be set to achieve different results as per application requirements.

- [Blur](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#blur)
- [Direction](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#direction)
- [Distance](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#distance)
- [FadeDirection](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#fadeDirection)
- [RotWithShape](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#rotWithShape)
- [Size](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#size)
- [Transparency](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#transparency)
- [Type](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#type)

## **Working with the Reflection Effect of Shape or Chart**
The following sample code loads the [source excel file](5115424.xlsx) and accesses the first shape in the default worksheet. It sets different properties of the [Shape.Reflection](https://reference.aspose.com/cells/nodejs-cpp/shape/#reflection) class and then saves the workbook in the [output excel file](5115423.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
const reflectionEffect = shape.getReflection();
reflectionEffect.setBlur(30);
reflectionEffect.setSize(90);
reflectionEffect.setTransparency(0);
reflectionEffect.setDistance(80);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
