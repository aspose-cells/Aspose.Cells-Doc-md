---
title: Изменить существующее SQL соединение данных с помощью Aspose.Cells for JavaScript через C++
linktitle: Изменение существующего SQL соединения с данными с использованием Aspose.Cells
type: docs
weight: 20
url: /ru/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Узнайте, как изменить свойства существующего SQL соединения данных с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает изменение существующего SQL-соединения с данными. В статье будет объяснено, как использовать Aspose.Cells для модификации различных свойств SQL-соединения с данными.  
Вы можете добавить или просмотреть соединения с данными внутри Microsoft Excel, следуя команде меню **Данные > Соединения**.  
Аналогично, Aspose.Cells предоставляет средства для доступа и изменения подключений данных с помощью коллекции Workbook.dataConnections.
{{% /alert %}}

## Изменение существующего SQL-соединения с данными с использованием Aspose.Cells

Следующий пример иллюстрирует использование Aspose.Cells for JavaScript через C++ для изменения SQL Data Connection книги. Вы можете скачать исходный Excel-файл, использованный в этом коде, и выходной Excel-файл, созданный этим кодом, по следующим ссылкам.

- [Исходный файл Excel](5112357.xlsx)  
- [Выходной файл Excel](5112356.xlsx)  

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
