---
title: 在 Node.js via C++ 中查找工作表内元素的绝对位置
linktitle: 查找工作表内形状的绝对位置
type: docs
weight: 8000
url: /zh/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: 了解如何使用 Aspose.Cells for Node.js via C++ 在工作表中查找形状的绝对位置。 
---

{{% alert color="primary" %}}

有时，您需要知道工作表中的形状的绝对位置。Aspose.Cells for Node.js via C++ 提供了 [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeftToCorner--) 和 [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTopToCorner--) 属性来实现此目的。这些属性返回形状在工作表中的绝对位置（以像素为单位）。

{{% /alert %}}

以下示例代码显示了工作表中第一个形状的绝对位置（以像素为单位）。示例代码显示了以下控制台输出：

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Displays the absolute position of the shape
console.log(`Absolute Position of this Shape is (${shape.getLeftToCorner()} , ${shape.getTopToCorner()})`);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
