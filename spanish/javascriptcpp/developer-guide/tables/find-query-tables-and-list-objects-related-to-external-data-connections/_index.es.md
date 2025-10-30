---
title: Encontrar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externos con JavaScript vía C++
linktitle: Encuentra Tablas de Consulta y Objetos Lista relacionados con Conexiones de Datos Externos
type: docs
weight: 20
url: /es/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Aprenda cómo encontrar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externos usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}} 

A veces, necesitas descubrir las Tablas de Consulta y Objetos Lista relacionados con alguna Conexión de Datos Externos. Las Tablas de Consulta están relacionadas con el objeto Conexión de Datos Externos con el Id de Conexión, mientras que los Objetos Lista están relacionados con una Tabla de Consulta.

{{% /alert %}} 
## **Buscar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externos**
Los siguientes códigos de ejemplo con [archivo de Excel de muestra](5115493.xlsm) explican cómo encontrar Tablas y Objetos de Lista relacionados con la Conexión de Datos Externos.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>List Query Tables and Connections</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, CellsHelper, TableDataSourceType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        function printTables(workbook, externalConnection) {
            // Iterate all the worksheets
            for (let j = 0; j < workbook.worksheets.count; j++) {
                const worksheet = workbook.worksheets.get(j);

                // Check all the query tables in a worksheet
                for (let k = 0; k < worksheet.queryTables.count; k++) {
                    const qt = worksheet.queryTables.get(k);

                    // Check if query table is related to this external connection
                    if (externalConnection.id === qt.connectionId && qt.connectionId >= 0) {
                        // Print the query table name and print its refersto range
                        console.log("querytable " + qt.name);
                        const n = qt.name.replace(/\+/g, '_').replace(/=/g, '_');
                        const names = workbook.worksheets.names;
                        const name = names.get("'" + worksheet.name + "'!" + n);

                        if (!name.isNull()) {
                            const range = name.range;
                            if (!range.isNull()) {
                                console.log("refersto: " + range.refersTo);
                            }
                        }
                    }
                }

                // Iterate all the list objects in this worksheet
                for (let k = 0; k < worksheet.listObjects.count; k++) {
                    const table = worksheet.listObjects.get(k);

                    // Check the data source type if it is query table
                    if (table.dataSourceType === TableDataSourceType.QueryTable) {
                        // Access the query table related to list object
                        const qt = table.queryTable;

                        // Check if query table is related to this external connection
                        if (externalConnection.id === qt.connectionId && qt.connectionId >= 0) {
                            // Print the query table name and print its refersto range
                            console.log("querytable " + qt.name);
                            console.log("Table " + table.displayName);
                            console.log("refersto: " + worksheet.name + "!" + CellsHelper.cellIndexToName(table.startRow, table.startColumn) + ":" + CellsHelper.cellIndexToName(table.endRow, table.endColumn));
                        }
                    }
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Check all the connections inside the workbook
            for (let i = 0; i < workbook.dataConnections.count; i++) {
                const externalConnection = workbook.dataConnections.get(i);
                console.log("connection: " + externalConnection.name);
                printTables(workbook, externalConnection);
                console.log();
            }

            resultDiv.innerHTML = '<p style="color: green;">Operation completed. See console for connection and query table details.</p>';
        });
    </script>
</html>
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
