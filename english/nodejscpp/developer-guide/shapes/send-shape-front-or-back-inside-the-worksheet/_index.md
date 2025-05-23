---
title: Send Shape Front or Back inside the Worksheet with Node.js via C++
linktitle: Send Shape Front or Back inside the Worksheet
type: docs
weight: 3400
url: /nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Learn how to send a shape to the front or back in a worksheet using Aspose.Cells for Node.js via C++. 
---

## **Possible Usage Scenarios**

When there are multiple shapes present in the same location, their visibility is determined by their z-order positions. Aspose.Cells provides [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-) method, which changes the z-order position of the shape. To send a shape to the back, you will use a negative number like -1, -2, -3, etc., and to bring a shape to the front, you will use a positive number like 1, 2, 3, etc.

## **Send Shape Front or Back inside the Worksheet**

The following sample code explains the usage of [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-) method. Please see the [sample Excel file](50528330.xlsx) used inside the code and the [output Excel file](50528331.xlsx) generated by it. The screenshot shows the effect of the code on the sample Excel file upon execution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleToFrontOrBack.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first and fourth shape
const shape1 = worksheet.getShapes().get(0);
const shape4 = worksheet.getShapes().get(3);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 1: " + shape1.getZOrderPosition());

// Send this shape to front
shape1.toFrontOrBack(2);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 4: " + shape4.getZOrderPosition());

// Send this shape to back
shape4.toFrontOrBack(-2);

// Save the output Excel file
const outputFilePath = path.join(dataDir, "outputToFrontOrBack.xlsx");
workbook.save(outputFilePath);
```
