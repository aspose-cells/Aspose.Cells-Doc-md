---
title: Node.jsで範囲のアドレスセル数、オフセット、列全体や行全体を取得する方法（C++経由）
linktitle: 範囲のアドレス、セル数、オフセット、全列、および全行を取得する
type: docs
weight: 330
url: /ja/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **可能な使用シナリオ**
Aspose.Cells for Node.js via C++は、Excel範囲を容易に操作できるさまざまなユーティリティメソッドを備えたRangeオブジェクトを提供します。この記事では、Rangeオブジェクトの以下のメソッドやプロパティの使い方を説明します。

- **アドレス**

範囲のアドレスを取得します。

- **セル数**

範囲内のすべてのセル数を取得します。

- **オフセット**

オフセットによって範囲を取得します。

- **全列**

指定された範囲を含む列全体を表すRangeオブジェクトを取得します。

- **全行**

指定された範囲を含む行全体を表すRangeオブジェクトを取得します。

## **範囲のアドレス、セル数、オフセット、全列および全行を取得する**
以下のサンプルコードは、上記で説明したメソッドとプロパティの使用方法を説明します。参考のために、以下に示すコードのコンソール出力をご覧ください。

## **サンプルコード**
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

## **コンソール出力**
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
