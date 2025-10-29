---
title: 在工作表中将形状移到前面或后面，用Node.js通过C++
linktitle: 在工作表内部发送形状到前面或后面
type: docs
weight: 3400
url: /zh/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: 学习如何使用Aspose.Cells for Node.js via C++将形状置于工作表的前面或后面。 
---

## **可能的使用场景**

当同一位置存在多种形状时，它们的可见性由z序位置决定。Aspose.Cells提供[**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-)方法，可以改变形状的z序位置。将形状送到最底层，用负数如-1、-2、-3等，想将形状置于最前面，用正数如1、2、3等。

## **在工作表内发送形状到最前或最后**

以下示例代码解释了[**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-)方法的用法。请查看代码中使用的[示例Excel文件](50528330.xlsx)以及由它生成的[输出Excel文件](50528331.xlsx)。截图显示了代码在执行后对示例Excel文件的效果。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

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
{{< app/cells/assistant language="nodejs-cpp" >}}
