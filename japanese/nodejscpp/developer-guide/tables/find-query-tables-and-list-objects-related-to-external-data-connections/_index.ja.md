---
title: 外部データ接続に関連したクエリテーブルとリストオブジェクトをNode.jsをC++経由で検索する
linktitle: 外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける
type: docs
weight: 20
url: /ja/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Aspose.Cells for Node.js via C++を使用して、外部データ接続に関するクエリテーブルやリストオブジェクトを見つける方法を学びます。
---

{{% alert color="primary" %}} 

時々、外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける必要があります。 クエリテーブルは、接続IDを持つ外部データ接続オブジェクトと関連しており、リストオブジェクトはクエリテーブルに関連しています。

{{% /alert %}} 
## **外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける**
[サンプルエクセルファイル](5115493.xlsm)を使用して、外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける方法について説明する以下のサンプルコードを参照してください。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

function printTables(workbook, externalConnection) {
// Iterate all the worksheets
for (let j = 0; j < workbook.getWorksheets().getCount(); j++) {
const worksheet = workbook.getWorksheets().get(j);

// Check all the query tables in a worksheet
for (let k = 0; k < worksheet.getQueryTables().getCount(); k++) {
const qt = worksheet.getQueryTables().get(k);

// Check if query table is related to this external connection
if (externalConnection.getId() === qt.getConnectionId() && qt.getConnectionId() >= 0) {
// Print the query table name and print its refersto range
console.log("querytable " + qt.getName());
const n = qt.getName().replace(/\+/g, '_').replace(/=/g, '_');
const names = workbook.getWorksheets().getNames();
const name = names.get("'" + worksheet.getName() + "'!" + n);

if (!name.isNull()) {
const range = name.getRange();
if (!range.isNull()) {
console.log("refersto: " + range.getRefersTo());
}
}
}
}

// Iterate all the list objects in this worksheet
for (let k = 0; k < worksheet.getListObjects().getCount(); k++) {
const table = worksheet.getListObjects().get(k);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
// Access the query table related to list object
const qt = table.getQueryTable();

// Check if query table is related to this external connection
if (externalConnection.getId() === qt.getConnectionId() && qt.getConnectionId() >= 0) {
// Print the query table name and print its refersto range
console.log("querytable " + qt.getName());
console.log("Table " + table.getDisplayName());
console.log("refersto: " + worksheet.getName() + "!" + AsposeCells.CellsHelper.cellIndexToName(table.getStartRow(), table.getStartColumn()) + ":" + AsposeCells.CellsHelper.cellIndexToName(table.getEndRow(), table.getEndColumn()));
}
}
}
}
}
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsm");
// Load workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Check all the connections inside the workbook
for (let i = 0; i < workbook.getDataConnections().getCount(); i++) {
const externalConnection = workbook.getDataConnections().get(i);
console.log("connection: " + externalConnection.getName());
printTables(workbook, externalConnection);
console.log();
}
```


上記のサンプルコードをこの[サンプルエクセルファイル](5115493.xlsm)で実行した場合のコンソール出力は次のとおりです。

{{< highlight java >}}

 connection: AAPL Connection

querytable hp?s=AAPL+Historical+Prices

refersto: =Sheet1!$Q$1:$W$69

connection: BOSL066360W7_SQLEXPRESS Test

querytable BOSL066360W7_SQLEXPRESS Test

Table Table_BOSL066360W7_SQLEXPRESS_Test

refersto: Sheet1!A1:B3

connection: BOSL066360W7_SQLEXPRESS Test1

querytable BOSL066360W7_SQLEXPRESS Test_1

Table Table_BOSL066360W7_SQLEXPRESS_Test_1

refersto: Sheet1!D1:E2

connection: UWTI Connection

querytable hp?s=UWTI+Historical+Prices

refersto: =Sheet1!$H$1:$N$69

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
