---
title: 使用 Node.js 通过 C++ 搜索和替换范围内的数据
linktitle: 在 Excel 中使用 C# 代码搜索和替换范围内的数据
type: docs
weight: 170
url: /zh/nodejs-cpp/search-and-replace-data-in-a-range/
description: 本文展示了如何使用 Node.js 通过 C++ 代码在 Excel 的范围内搜索和替换数据。
keywords: Node.js 在 Excel 中搜索和替换数据，Node.js 在 Excel 中搜索数据，Node.js 在范围内搜索和替换数据，Node.js 搜索范围内的数据，Node.js 在范围内搜索数据，Node.js 搜索 Excel 中的数据，Node.js 搜索范围内的数据，Node.js 使用搜索和替换在 Excel 中的数据，使用 Node.js 在范围内搜索和替换数据，使用 Node.js 在范围内搜索和替换数据，Node.js 在范围内搜索和替换数据
---

{{% alert color="primary" %}}

 有时需要在范围内搜索并替换特定数据，而忽略范围外的单元格值。Aspose.Cells for Node.js via C++ 允许你将搜索限制在特定范围内。本文解释了如何操作。

{{% /alert %}}

 Aspose.Cells for Node.js via C++ 提供了 [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) 方法，用于在搜索数据时指定范围。下面的代码示例在范围内搜索并替换数据。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

const area = AsposeCells.CellArea.createCellArea("E9", "H15");

const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);
opts.setRange(area);

let cell = null;

do {
cell = worksheet.getCells().find("search", cell, opts);
if (cell === null || cell.isNull()) {
break;
}
cell.putValue("replace");
} while (true);

workbook.save(path.join(dataDir, "output.out.xlsx"));
```
