---
title: Modifier une connexion de données SQL existante en utilisant Aspose.Cells for JavaScript via C++
linktitle: Modifier une connexion de données SQL existante à l aide d Aspose.Cells
type: docs
weight: 20
url: /fr/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Apprenez comment modifier les propriétés de connexion de données SQL existantes en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la modification de connexions de données SQL existantes. L'article expliquera comment utiliser Aspose.Cells pour modifier différentes propriétés de la connexion de données SQL.  
Vous pouvez ajouter ou consulter des connexions de données dans Microsoft Excel en suivant la commande de menu **Données > Connexions**.  
De même, Aspose.Cells offre des moyens d'accéder et de modifier les connexions de données en utilisant la collection Workbook.dataConnections.
{{% /alert %}}

## Modifier une connexion de données SQL existante à l'aide d'Aspose.Cells

L'échantillon suivant illustre l'utilisation de Aspose.Cells for JavaScript via C++ pour modifier la connexion de données SQL du classeur. Vous pouvez télécharger le fichier Excel source utilisé dans ce code et le fichier Excel de sortie généré par le code à partir des liens suivants.

- [Fichier Excel Source](5112357.xlsx)  
- [Fichier Excel de Sortie](5112356.xlsx)  

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
