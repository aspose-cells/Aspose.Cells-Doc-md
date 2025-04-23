---
title: 使用 Node.js + C++ 在 Excel 文件中自动填充区域
linktitle: 自动填充范围
type: docs
weight: 105
url: /zh/nodejs-cpp/autofill-ranges/
description: 学习如何在Excel文件的指定范围内执行自动填充操作，使用 Aspose.Cells for Node.js via C++。
---

## **在Excel中指定范围执行自动填充**

在Excel中，选择一个范围，将鼠标移动到右下角，然后拖动“加号”以自动填充数据。

## ** 使用 Aspose.Cells for Node.js via C++ 自动填充范围**

以下示例演示如何在范围内执行自动填充操作，这里有可供测试该功能的示例文件（可下载）：

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

