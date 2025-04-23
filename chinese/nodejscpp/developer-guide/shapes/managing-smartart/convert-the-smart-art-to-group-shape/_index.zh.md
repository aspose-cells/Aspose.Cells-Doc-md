---
title: 使用Node.js通过C++将智能艺术转换为组合形状
linktitle: 将智能图转为组合形状
type: docs
weight: 200
url: /zh/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **可能的使用场景**

你可以使用[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--)方法将智能艺术形状转换为群组形状。这将使你能像处理组合形状一样处理智能艺术形状。这样，你就可以访问该组合形状的各个部分或形状。

## **将智能图转换为组合形状**

以下示例代码加载包含智能艺术形状的[示例Excel文件](55541793.xlsx)，如截图所示。然后它将智能艺术形状转换为群组形状，并打印Shape.isGroup属性。请查看下面的示例代码控制台输出。

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **控制台输出**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
