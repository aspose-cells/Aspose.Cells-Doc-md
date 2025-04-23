---
title: 获取范围的单元格地址、计数、偏移量、整个列和整个行，使用 C++ 在 Node.js 中
linktitle: 获取范围的地址、单元格计数、偏移、整列和整行
type: docs
weight: 330
url: /zh/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **可能的使用场景**
Aspose.Cells for Node.js via C++ 提供了 Range 对象，具有多种实用方法，方便用户轻松操作 Excel 范围。本文介绍了 Range 对象的以下方法或属性的用法。

- **地址**

获取范围的地址。

- **单元格计数**

获取范围中的所有单元格数。

- **偏移**

通过偏移获取范围。

- **整列**

获取代表包含指定范围的整列（或多列）的 Range 对象。

- **整行**

获取代表包含指定范围的整行（或多行）的 Range 对象。

## **获取范围的地址、单元格计数、偏移、整列和整行**
下面的示例代码解释了上述方法和属性的用法。请参考以下给出的代码的控制台输出。

## **示例代码**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Create range A1:B3.
console.log("Creating Range A1:B3\n");
let rng = ws.getCells().createRange("A1:B3");

// Print range address and cell count.
console.log("Range Address: " + rng.getAddress());
console.log("Range row Count: " + rng.getRowCount());
console.log("Range column Count: " + rng.getColumnCount());

// Formatting console output.
console.log("----------------------");
console.log("");

// Create range A1.
console.log("Creating Range A1\n");
rng = ws.getCells().createRange("A1");

// Print range offset, entire column and entire row.
console.log("Offset: " + rng.getOffset(2, 2).getAddress());
console.log("Entire Column: " + rng.getEntireColumn().getAddress());
console.log("Entire Row: " + rng.getEntireRow().getAddress());

// Formatting console output.
console.log("----------------------");
console.log("");
```

## **控制台输出**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
