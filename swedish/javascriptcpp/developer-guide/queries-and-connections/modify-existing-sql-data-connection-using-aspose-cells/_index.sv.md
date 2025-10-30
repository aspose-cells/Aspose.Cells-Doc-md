---
title: Ändra befintlig SQL datakälla med Aspose.Cells for JavaScript via C++
linktitle: Modifiera befintlig SQL Data Connection med hjälp av Aspose.Cells
type: docs
weight: 20
url: /sv/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Lär dig hur du ändrar egenskaper för befintliga SQL datakällor med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Aspose.Cells stöder att ändra befintlig SQL Data Connection. Artikeln förklarar hur man använder Aspose.Cells för att ändra olika egenskaper hos SQL Data Connection.  
Du kan lägga till eller se dataanslutningar inne i Microsoft Excel genom att följa menyn **Data > Connections**.  
På samma sätt ger Aspose.Cells möjlighet att komma åt och modifiera datakonnectioner med hjälp av Workbook.dataConnections-collectionen.
{{% /alert %}}

## Modifiera befintlig SQL Data Connection med hjälp av Aspose.Cells

Följande exempel visar användningen av Aspose.Cells for JavaScript via C++ för att ändra SQL Data Connection i arbetsboken. Du kan ladda ner den ursprungliga Excel-filen som används i denna kod och den genererade Excel-filen från följande länkar.

- [Käll-Excel-fil](5112357.xlsx)  
- [Utdata-Excel-fil](5112356.xlsx)  

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
