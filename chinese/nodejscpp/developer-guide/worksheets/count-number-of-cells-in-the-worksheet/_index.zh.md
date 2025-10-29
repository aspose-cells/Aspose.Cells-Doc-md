---
title: 用C++在Node.js中计数工作表中的单元格数量
linktitle: 计算工作表中单元格的数量
type: docs
weight: 110
url: /zh/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: 学习如何通过Aspose.Cells for Node.js via C++以编程方式统计Excel工作表中的单元格数。
keywords: 用C++在Node.js中统计Excel工作表单元格数
---

您可以使用下面给出的代码示例中所示的[**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--)或[**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--)属性来计算工作表中的单元格数量。

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
