---
title: Чтение и запись внешнего подключения XLS и XLSB файлов с помощью JavaScript через C++
linktitle: Чтение и запись внешнего соединения файлов XLS и XLSB
type: docs
weight: 80
url: /ru/javascript-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: Узнайте, как читать и записывать внешние подключения XLS и XLSB файлов с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

Aspose.Cells уже поддерживает чтение и запись внешних подключений XLSX файлов, а теперь также поддерживает эти функции для XLSB и XLS файлов. Однако код для всех типов форматов одинаков.  

## **Чтение и запись внешнего соединения файлов XLS/XLSB**  

Следующий пример кода загружает пример XLSB файла (также можно загрузить XLS) и читает его первое внешнее подключение, которое фактически является подключением к базе данных Microsoft Access. Затем он изменяет свойство [**DBConnection.name**](https://reference.aspose.com/cells/javascript-cpp/dbconnection/#name--) и сохраняет его как выходной файл XLS/XLSB. Скриншот показывает эффект работы кода на [примере XLSB файла](51740722.xlsb) и [выходном XLSB файле](51740723.xlsb) после его выполнения. Также смотрите вывод в консоль примера кода, приведённый ниже для справки.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Образец кода**  

Следующий код будет работать как для файлов XLSB, так и для файлов XLS, загружая и сохраняя файлы с соответствующим расширением.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read and Modify External DB Connection (XLSB)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the source Excel Xlsb file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Read the first external connection which is actually a DB-Connection
            const dbCon = workbook.dataConnections.get(0);

            // Print the Name, Command and Connection Info of the DB-Connection
            const outputLines = [];
            outputLines.push("Connection Name: " + dbCon.name);
            outputLines.push("Command: " + dbCon.command);
            outputLines.push("Connection Info: " + dbCon.connectionString);

            // Modify the Connection Name
            dbCon.name = "NewCust";

            // Save the Excel Xlsb file
            const outputData = workbook.save(SaveFormat.Xlsb);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExternalConnection_XLSB.xlsb';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<pre style="color: green;">' + outputLines.join('\n') + '\n\nModified connection name to: NewCust</pre>';
        });
    </script>
</html>
```  

## **Вывод в консоль**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}
