---
title: Node.js経由C++を使用してExcelの範囲をコピー
linktitle: 範囲をコピーする
type: docs
weight: 105
url: /ja/nodejs-cpp/copy-ranges-of-Excel/
---

## **紹介**

Excel では、範囲を選択し、範囲をコピーし、その後、同じワークシート、他のワークシート、または他のファイルに特定のオプションで貼り付けることができます。

## **Aspose.Cells for Node.js via C++を使用した範囲のコピー**

Aspose.Cells for Node.js via C++は、範囲をコピーするためのいくつかのオーバーロードされた[Range.copy(Range, PasteOptions)](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-)メソッドを提供します。また、[Range.copyStyle(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyStyle-range-)は範囲のスタイルのみをコピーし、[Range.copyData(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyData-range-)は範囲の値のみをコピーします。

## **範囲をコピー**

2つの範囲を作成します：ソース範囲とターゲット範囲、その後`Range.copy`メソッドを使用してソース範囲をターゲット範囲にコピーします。

以下のコードを参照してください:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
let worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
let worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
let sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
let targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy source range to target range in the same worksheet 
targetRange.copy(sourceRange);

// Create target range of cells.
workbook.getWorksheets().add();
worksheet = workbook.getWorksheets().get(1);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another worksheet 
targetRange.copy(sourceRange);

// Copy to another workbook
const anotherWorkbook = new AsposeCells.Workbook();

worksheet = workbook.getWorksheets().get(0);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another workbook 
targetRange.copy(sourceRange);
```

## **オプションで範囲を貼り付ける**

Aspose.Cells for Node.js via C++は、特定の種類の貼り付けに対応しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Init paste options.
const options = new AsposeCells.PasteOptions();
// Set paste type.
options.setPasteType(AsposeCells.PasteType.ValuesAndFormats);
options.setSkipBlanks(true);
// Copy source range to target range
targetRange.copy(sourceRange, options);
```

## **範囲のデータのみのコピー**

また、以下のコードのように`Range.copyData`メソッドを使ってデータをコピーすることも可能です：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = worksheets.get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy the data of source range to target range
targetRange.copyData(sourceRange);
```

## **高度なトピック**
- [ソース範囲の行の高さを宛先範囲にコピーします。](/cells/ja/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/)

{{< app/cells/assistant language="nodejs-cpp" >}}
