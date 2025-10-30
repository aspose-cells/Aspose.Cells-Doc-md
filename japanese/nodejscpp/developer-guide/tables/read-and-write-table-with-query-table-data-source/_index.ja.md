---
title: Node.jsを使用して、クエリテーブルデータソースを持つテーブルの読み書き方法
linktitle: クエリテーブルデータソースを持つテーブルの読み書き
type: docs
weight: 30
url: /ja/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: Aspose.Cells for Node.js via C++を使用して、クエリテーブルをデータソースとするテーブルの読み書き方法を学びます。 
---

## **クエリテーブルデータソースを持つテーブルの読み書き**
Aspose.Cells for Node.js via C++を使えば、クエリテーブルをデータソースとするテーブルの読み書きが可能です。この機能はXLSファイルもサポートしています。以下のコードスニペットは、そのようなテーブルの読み取りと書き込み、最初にテーブルを読み取り、その後合計行を追加する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

ソースエクセルファイルと出力エクセルファイルが添付されています。

[ソースファイル](96928091.xls)

[出力ファイル](96928092.xls)
{{< app/cells/assistant language="nodejs-cpp" >}}
