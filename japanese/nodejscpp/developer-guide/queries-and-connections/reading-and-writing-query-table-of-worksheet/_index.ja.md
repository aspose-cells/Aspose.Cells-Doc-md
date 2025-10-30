---
title: Node.js経由でC++を使ってワークシートのクエリテーブルを読み書きする方法
linktitle: ワークシートのクエリテーブルの読み取りと書き込み
type: docs
weight: 40
url: /ja/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Worksheet.QueryTablesコレクションを提供し、インデックスでQueryTable型のオブジェクトを返します。以下に2つのプロパティがあります

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

これらはどちらもBoolean値です。Microsoft ExcelでData > Connections > Propertiesから表示できます。

{{% /alert %}}

ワークシートのクエリテーブルの読み書き

最初のワークシートの最初のQueryTableを読み取り、両方のプロパティを出力します。その後、QueryTable.preserveFormattingをtrueに設定します。

このコードで使用される元のExcelファイルとコードによって生成された出力Excelファイルは、以下のリンクからダウンロードできます。

- [元のExcelファイル](5115533.xlsx)
- [出力Excelファイル](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

コンソール出力

上記のサンプルコードのコンソール出力は次の通りです

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

クエリテーブルの結果範囲を取得

Aspose.Cellsには、クエリテーブルの結果範囲のアドレスを読み取るオプションがあります。次のコードは、クエリテーブルの結果範囲のアドレスを読み取る機能を示しています。サンプルファイルは[こちら](72417290.xlsx)からダウンロードできます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
