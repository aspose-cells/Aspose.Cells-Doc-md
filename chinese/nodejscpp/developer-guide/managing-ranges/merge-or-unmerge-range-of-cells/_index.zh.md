---
title: 用 Node.js 通过 C++ 合并或取消合并单元格范围
linktitle: 合并或取消合并单元格范围
type: docs
weight: 190
url: /zh/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: 用 Node.js 通过 C++ 合并和取消合并 Excel 中的单元格范围。
keywords: 在 Node.js 中合并和取消合并单元格，使用 Node.js 合并和取消合并范围中的单元格，使用 Node.js 在 Excel 中合并和取消合并单元格，使用 Node.js 在 Excel 中合并和取消合并单元格，使用 Node.js 在 Excel 中合并和取消合并单元格
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 来合并或拆分一系列单元格。Aspose.Cells 为此提供了 [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) 和 [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) 方法。本文解释了如何将一系列单元格合并为单个单元格。

{{% /alert %}}

## **示例**

以下示例代码首先创建一个范围 — A1:D4 — 然后使用[**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--)方法将该范围中的单元格合并成一个单元格。类似地，你也可以通过创建范围并调用[**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--)方法来拆分单元格。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
