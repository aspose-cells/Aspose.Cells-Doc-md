---
title: Bestehende SQL Datenverbindung mit Aspose.Cells for JavaScript via C++ ändern
linktitle: Bereits bestehende SQL Datenverbindung mithilfe von Aspose.Cells ändern
type: docs
weight: 20
url: /de/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Lernen Sie, wie man bestehende SQL Datenverbindungseigenschaften mit Aspose.Cells for JavaScript via C++ ändert.
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Ändern einer bereits bestehenden SQL-Datenverbindung. Der Artikel erläutert, wie Aspose.Cells verwendet wird, um verschiedene Eigenschaften einer SQL-Datenverbindung zu ändern.  
Sie können Datenverbindungen in Microsoft Excel hinzufügen oder anzeigen, indem Sie den Menübefehl **Daten > Verbindungen** befolgen.  
Ähnlich ermöglicht Aspose.Cells den Zugriff auf und die Änderung der Datenverbindungen mithilfe der Sammlung Workbook.dataConnections.
{{% /alert %}}

## Ändern einer bestehenden SQL-Datenverbindung mit Aspose.Cells

Das folgende Beispiel veranschaulicht die Verwendung von Aspose.Cells for JavaScript über C++, um die SQL-Datenverbindung des Arbeitsbuchs zu ändern. Sie können die ursprüngliche Excel-Datei, die in diesem Code verwendet wird, sowie die vom Code generierte Ausgabedatei aus den folgenden Links herunterladen.

- [Quelldatei](5112357.xlsx)  
- [Ausgabedatei](5112356.xlsx)  

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
