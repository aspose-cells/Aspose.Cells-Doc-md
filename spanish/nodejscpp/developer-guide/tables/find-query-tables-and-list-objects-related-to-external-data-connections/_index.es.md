---
title: Encuentre Consultas de Tablas y Objetos de Lista relacionados con Conexiones de Datos Externos con Node.js a través de C++
linktitle: Encuentra Tablas de Consulta y Objetos Lista relacionados con Conexiones de Datos Externos
type: docs
weight: 20
url: /es/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Aprenda cómo encontrar Consultas de Tablas y Objetos de Lista relacionados con Conexiones de Datos Externos usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

A veces, necesitas descubrir las Tablas de Consulta y Objetos Lista relacionados con alguna Conexión de Datos Externos. Las Tablas de Consulta están relacionadas con el objeto Conexión de Datos Externos con el Id de Conexión, mientras que los Objetos Lista están relacionados con una Tabla de Consulta.

{{% /alert %}} 
## **Buscar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externos**
Los siguientes códigos de ejemplo con [archivo de Excel de muestra](5115493.xlsm) explican cómo encontrar Tablas y Objetos de Lista relacionados con la Conexión de Datos Externos.

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


La siguiente es la salida de consola al ejecutar los códigos de ejemplo anteriores con este [archivo de Excel de muestra](5115493.xlsm).

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
