---
title: Trouvez les tableaux de requête et liste d objets liés aux connexions de données externes avec JavaScript via C++
linktitle: Trouver des tables de requête et des objets liste liés aux connexions de données externes
type: docs
weight: 20
url: /fr/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Apprenez comment trouver les tableaux de requête et les objets de liste liés aux connexions de données externes en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

Parfois, vous devez trouver des tables de requête et des objets liste liés à une connexion de données externe. Les tables de requête sont liées à l'objet de connexion de données externe avec l'ID de connexion, tandis que les objets liste sont liés à une table de requête.

{{% /alert %}} 
## **Trouver des Tables de Requête et des Objets Liste liés aux Connexions de Données Externes**
Les exemples de code suivants avec [fichier Excel d'exemple](5115493.xlsm) expliquent comment trouver des tables de requête et des objets de liste liés à une connexion de données externe.

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


Voici la sortie de la console de l'exécution des codes d'exemple ci-dessus avec ce [fichier Excel d'exemple](5115493.xlsm).

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
