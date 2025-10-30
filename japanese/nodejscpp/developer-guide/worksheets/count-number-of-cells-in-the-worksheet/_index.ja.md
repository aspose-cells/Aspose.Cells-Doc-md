---
title: Node.jsとC++を用いてワークシート内のセル数をカウント
linktitle: ワークシート内のセル数を数える
type: docs
weight: 110
url: /ja/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Aspose.Cells for Node.js via C++を利用して、Excelワークシート内のセルの数をプログラム的にカウントする方法を学びます。
keywords: C++経由のNode.jsでセル数をカウント、ExcelワークシートセルのカウントNode.js via C++
---

以下のコード例に示すように、[**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--)または[**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--)プロパティを使用してワークシート内のセル数をカウントすることができます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "BookWithSomeData.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print number of cells in the Worksheet
console.log("Number of Cells: " + worksheet.getCells().getCount());

// If the number of cells is greater than 2147483647, use CountLarge
console.log("Number of Cells (CountLarge): " + worksheet.getCells().getCountLarge());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
