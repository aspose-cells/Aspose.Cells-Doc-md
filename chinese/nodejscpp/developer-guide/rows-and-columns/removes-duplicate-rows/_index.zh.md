---
title: 使用 C++ 通过 Node.js 移除工作表中的重复行
linktitle: 在工作表中删除重复行
type: docs
weight: 370
url: /zh/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 移除工作表中的重复行，并选择特定列进行重复检测。
---


移除重复行是 Microsoft Excel 的许多实用功能之一。它允许用户删除工作表中的重复行，你可以选择检查哪些列是否存在重复信息。

Aspose.Cells for Node.js via C++ 提供了 `Cells.removeDuplicates()` 方法来实现这一功能。你还可以设置 `startRow`、`startColumn`、`endRow` 和 `endColumn` 来指定要检测重复的范围。

以下是可以下载以进行此功能测试的样本文件：

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
