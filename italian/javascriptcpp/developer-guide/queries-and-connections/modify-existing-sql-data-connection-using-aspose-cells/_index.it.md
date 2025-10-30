---
title: Modifica la connessione dati SQL esistente usando Aspose.Cells for JavaScript tramite C++
linktitle: Modificare la connessione dati SQL esistente utilizzando Aspose.Cells
type: docs
weight: 20
url: /it/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Impara come modificare le proprietà della connessione dati SQL esistente usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}
Aspose.Cells supporta la modifica di una connessione dati SQL esistente. L'articolo spiegherà come utilizzare Aspose.Cells per modificare diverse proprietà di una connessione dati SQL.  
È possibile aggiungere o visualizzare le connessioni dati all'interno di Microsoft Excel seguendo il comando di menu **Dati > Connessioni**.  
Analogamente, Aspose.Cells offre strumenti per accedere e modificare le connessioni dati utilizzando la collezione Workbook.dataConnections.
{{% /alert %}}

## Modificare la connessione dati SQL esistente usando Aspose.Cells

Il seguente esempio illustra l'uso di Aspose.Cells for JavaScript tramite C++ per modificare la connessione dati SQL del workbook. Puoi scaricare il file Excel di origine usato in questo codice e il file Excel di output generato dal codice dai seguenti link.

- [File Excel di Origine](5112357.xlsx)  
- [File Excel di Output](5112356.xlsx)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Data Connection Example</title>
    </head>
    <body>
        <h1>Data Connection Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first Data Connection
            const conn = workbook.dataConnections.get(0);

            // Change the Data Connection Name and Odc file
            conn.name = "MyConnectionName";
            conn.odcFile = "C:\\Users\\MyDefaulConnection.odc";

            // Change the Command Type, Command and Connection String
            const dbConn = conn;
            dbConn.commandType = AsposeCells.OLEDBCommandType.SqlStatement;
            dbConn.command = "Select * from AdminTable";
            dbConn.connectionString = "Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Data connection updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
