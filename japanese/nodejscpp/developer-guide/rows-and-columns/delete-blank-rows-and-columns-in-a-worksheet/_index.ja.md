---
title: ノード.js経由のC++でワークシートの空白行と列を削除する
linktitle: ワークシート内の空白の行と列を削除する
type: docs
weight: 300
url: /ja/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Aspose.Cells for Node.js via C++を使用して、ワークシートからすべての空白行と列を削除する方法を学びます。 
---

{{% alert color="primary" %}}

ワークシートからすべての空白行と列を削除することは可能です。たとえば、Microsoft ExcelファイルからPDFを生成する際に、データや関連オブジェクトを含む行や列だけを変換したい場合に便利です。

空の行と列を削除するために以下のAspose.Cellsのメソッドを使用します:

1. 空白の行を削除するには、[**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--)メソッドを使用します。削除される空白の行については、[**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--)がtrueであるだけでなく、それらの行のいかなるセルにも見えるコメントが定義されていないこと、そしてそれらと交差するピボットテーブルがないことも必要です。
2. 空白の列を削除するには、[**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--) メソッドを使用します。

{{% /alert %}}

## 空白行削除用のNode.jsコード

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## 空白列削除用のNode.jsコード

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
