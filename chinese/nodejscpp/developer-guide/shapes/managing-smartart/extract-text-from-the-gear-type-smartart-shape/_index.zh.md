---
title: 用Node.js通过C++从Gear类型智能艺术形状中提取文本
linktitle: 从齿轮型智能图形中提取文本
type: docs
weight: 500
url: /zh/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: 学习如何使用Aspose.Cells for Node.js via C++从Gear类型智能艺术形状中提取文本。
---

## **可能的使用场景**

Aspose.Cells可以从Gear类型智能艺术形状中提取文本。为此，首先应使用[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--)方法将智能艺术形状转换为群组形状。然后使用[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--)方法获取构成群组形状的所有单独形状的数组。最后，可以在循环中逐一迭代每个单独形状并提取它们的文本，使用[**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--)属性。

## **从齿轮型智能图形中提取文本**

以下示例代码加载包含齿轮型智能图形的[sample Excel文件](67338483.xlsx)。然后按上述步骤从其各个形状中提取文本。请参阅下面提供的代码的控制台输出以供参考。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **控制台输出**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
