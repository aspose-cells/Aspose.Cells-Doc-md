---
title: Modificar la conexión de datos SQL existente usando Aspose.Cells for JavaScript a través de C++
linktitle: Modificar una Conexión de Datos SQL existente utilizando Aspose.Cells
type: docs
weight: 20
url: /es/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Aprenda cómo modificar las propiedades de la conexión de datos SQL existentes usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}}
Aspose.Cells permite modificar una Conexión de Datos SQL existente. El artículo explicará cómo usar Aspose.Cells para modificar diferentes propiedades de una Conexión de Datos SQL.  
Puedes añadir o ver Conexiones de Datos dentro de Microsoft Excel siguiendo el comando de menú **Datos > Conexiones**.  
De manera similar, Aspose.Cells proporciona los medios para acceder y modificar las conexiones de datos utilizando la colección Workbook.dataConnections.
{{% /alert %}}

## Modificar una conexión de datos SQL existente usando Aspose.Cells

 El siguiente ejemplo ilustra el uso de Aspose.Cells for JavaScript a través de C++ para modificar la conexión de datos SQL del libro de trabajo. Puedes descargar el archivo Excel fuente utilizado en este código y el archivo Excel de salida generado por el código desde los siguientes enlaces.

- [Archivo de Excel Fuente](5112357.xlsx)  
- [Archivo de Excel de Salida](5112356.xlsx)  

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
