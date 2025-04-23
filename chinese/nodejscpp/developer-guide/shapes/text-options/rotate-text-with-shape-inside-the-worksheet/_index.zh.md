---
title: 使用Node.js通过C++在工作表内旋转带有形状的文本
linktitle: 在工作表内旋转文本与形状
type: docs
weight: 1300
url: /zh/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: 了解如何使用Aspose.Cells for Node.js via C++在Excel工作表内旋转带有形状的文本。
---

## **可能的使用场景**

您可以在任何形状中添加文本，使用Microsoft Excel。如果使用非常旧的Microsoft Excel 2003添加形状，则文本不会随形状旋转。但如果使用较新的Microsoft Excel版本（如2007、2010、2013或2016等）添加形状，文本将随形状旋转。您可以通过[**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--)属性控制文本是否随形状旋转。默认值是**true**，表示文本将随形状旋转；如果设置为**false**，文本将不随形状旋转。

## **在工作表内旋转文本与形状**

以下示例加载包含三角形和其文本旋转的示例Excel文件（64716896.xlsx）。如果在Microsoft Excel中打开样本文件并旋转三角形，文本也会旋转。然后代码将[**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--)属性设置为**false**并保存为输出Excel文件（64716897.xlsx）。如果在Microsoft Excel中再次打开输出文件并旋转三角形，文本将不再旋转。请参考以下截图，显示代码对示例Excel文件的影响。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
