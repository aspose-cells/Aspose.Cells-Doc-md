---
title: Working with the Reflection Effect of Shape or Chart with Node.js via C++
linktitle: Working with the Reflection Effect of Shape or Chart
type: docs
weight: 210
url: /nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Learn how to work with the reflection effect of shapes or charts using Aspose.Cells for Node.js via C++. Set various reflection properties to achieve desired results.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells for Node.js via C++ provides the [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) property along with the [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) class to work with the reflection effect of shape or chart. The [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) class contains the following properties which can be set to achieve different results as per application requirements.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **Working with the Reflection Effect of Shape or Chart**
The following sample code loads the [source excel file](5115424.xlsx) and accesses the first shape in the default worksheet. It sets different properties of the [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) class and then saves the workbook in the [output excel file](5115423.xlsx).

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
{{< app/cells/assistant language="nodejs-cpp" >}}
