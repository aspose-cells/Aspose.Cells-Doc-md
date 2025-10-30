---
title: Query Tabellen finden und Objekte auflisten, die mit externen Datenverbindungen verbunden sind, mit Node.js über C++
linktitle: Suchen Sie Abfrage Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen
type: docs
weight: 20
url: /de/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Lernen Sie, wie Sie Abfrage Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen mit Aspose.Cells for Node.js via C++ finden.
---

{{% alert color="primary" %}} 

Manchmal müssen Sie Abfrage-Tabellen und Listenobjekte im Zusammenhang mit einer externen Datenverbindung finden. Abfrage-Tabellen sind mit der Verbindungs-ID des externen Datenverbindungsobjekts verbunden, während Listenobjekte mit einer Abfrage-Tabelle verbunden sind.

{{% /alert %}} 
## **Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden**
Die folgenden Beispielcodes mit der [Beispiel-Excel-Datei](5115493.xlsm) erläutern, wie man Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden kann.

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


Folgendes ist die Konsolenausgabe beim Ausführen der oben genannten Beispielcodes mit dieser [Beispiel-Excel-Datei](5115493.xlsm).

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
