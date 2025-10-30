---
title: Recupero dei Dati di Connessione SQL con JavaScript tramite C++
linktitle: Recupero dei Dati di Connessione SQL
type: docs
weight: 10
url: /it/javascript-cpp/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells può aiutarti a recuperare i dati di connessione SQL. Ciò include tutti i dati necessari per stabilire una connessione con il server SQL, ad esempio, **URL server**, **nome utente**, **nome tabella**, **query SQL completa**, **tipo di query**, **posizione della tabella**, e **nome dell'intervallo con nome** ad esso associato.

{{% /alert %}}

In Microsoft Excel, connettersi a un database tramite:

1. Cliccando sul menu **Dati** e selezionando **Da Altre Origini** seguito da **Da Server SQL**.  
1. Poi selezionare **Dati** seguito da **Connessioni**.  
1. Utilizzare la procedura guidata di connessione per collegarsi al database e creare una query del database.

Aspose.Cells for JavaScript tramite C++ fornisce la proprietà `Workbook.dataConnections` per recuperare le connessioni esterne. Restituisce un array di oggetti ExternalConnection nel workbook.

Se l'oggetto ExternalConnection contiene dati di connessione SQL, può essere convertito al tipo DBConnection e le sue proprietà possono essere usate per recuperare comando del database, tipo di comando, descrizione della connessione, informazioni sulla connessione, credenziali, e altro ancora.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Data Connections Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultEl = document.getElementById('result');
                resultEl.innerHTML = '';

                if (!fileInput.files.length) {
                    resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiate workbook from uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access the external collections
                const connections = workbook.dataConnections;
                const connectionCount = connections.count;

                const out = [];

                let connection = null;

                for (let i = 0; i < connectionCount; i++) {
                    connection = connections.get(i);

                    // Check if the Connection is DBConnection, then retrieve its various properties
                    if (connection.classType === AsposeCells.ExternalConnectionClassType.DBConnection) {

                        const dbConn = connection;

                        // Retrieve DB Connection Command
                        out.push('<p>Command: ' + dbConn.command + '</p>');

                        // Retrieve DB Connection Command Type
                        out.push('<p>Command Type: ' + dbConn.commandType + '</p>');

                        // Retrieve DB Connection Description
                        out.push('<p>Description: ' + dbConn.connectionDescription + '</p>');

                        // Retrieve DB Connection ID
                        out.push('<p>Id: ' + dbConn.id + '</p>');

                        // Retrieve DB Connection Info
                        out.push('<p>Info: ' + dbConn.connectionString + '</p>');

                        // Retrieve DB Connection Credentials
                        out.push('<p>Credentials: ' + dbConn.credentialsMethodType + '</p>');

                        // Retrieve DB Connection Name
                        out.push('<p>Name: ' + dbConn.name + '</p>');

                        // Retrieve DB Connection ODC File
                        out.push('<p>OdcFile: ' + dbConn.odcFile + '</p>');

                        // Retrieve DB Connection Source File
                        out.push('<p>Source file: ' + dbConn.sourceFile + '</p>');

                        // Retrieve DB Connection Type
                        out.push('<p>Type: ' + dbConn.sourceType + '</p>');

                        // Retrieve DB Connection Parameters Collection
                        const paramCollection = dbConn.parameters;
                        const paramCount = paramCollection.count;

                        // Iterate the Parameter Collection
                        if (paramCount > 0) {
                            out.push('<h3>Parameters:</h3>');
                        }
                        for (let j = 0; j < paramCount; j++) {
                            const param = paramCollection.get(j);

                            // Retrieve Parameter Cell Reference
                            out.push('<p>Cell reference: ' + param.cellReference + '</p>');

                            // Retrieve Parameter Name
                            out.push('<p>Parameter name: ' + param.name + '</p>');

                            // Retrieve Parameter Prompt
                            out.push('<p>Prompt: ' + param.prompt + '</p>');

                            // Retrieve Parameter SQL Type
                            out.push('<p>SQL Type: ' + param.sqlType + '</p>');

                            // Retrieve Parameter Type
                            out.push('<p>Param Type: ' + param.type + '</p>');

                            // Retrieve Parameter Value
                            out.push('<p>Param Value: ' + param.value + '</p>');
                        } // End for
                    } // End if
                } // End for

                if (out.length === 0) {
                    resultEl.innerHTML = '<p>No DB connections found in the selected workbook.</p>';
                } else {
                    resultEl.innerHTML = out.join('');
                }
            });
        });
    </script>
</html>
```
