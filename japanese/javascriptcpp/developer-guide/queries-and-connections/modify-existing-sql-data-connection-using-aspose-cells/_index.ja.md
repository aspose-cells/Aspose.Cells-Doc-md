---
title: 既存のSQLデータ接続をAspose.Cells for JavaScriptを使用してC++で修正する
linktitle: 既存のSQLデータ接続をAspose.Cellsを使用して変更する
type: docs
weight: 20
url: /ja/javascript-cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Aspose.Cells for JavaScriptを使用して既存のSQLデータ接続のプロパティを変更する方法を学びます。
---

{{% alert color="primary" %}}
Aspose.Cellsは既存のSQLデータ接続を変更する機能をサポートしています。この記事では、Aspose.Cellsを使用してSQLデータ接続のさまざまなプロパティを変更する方法について説明します。  
Microsoft Excel内のデータ接続を追加または参照するには、**データ > 接続** メニューコマンドに従ってください。  
同様に、Aspose.CellsはWorkbook.dataConnectionsコレクションを使用してデータ接続にアクセスし、変更する手段を提供します。
{{% /alert %}}

## Aspose.Cellsを使用して既存のSQLデータ接続を変更する

以下のサンプルは、C++を使用したAspose.Cells for JavaScriptの使用例を示しています。これにより、ワークブックのSQLデータ接続を変更できます。このコードで使用された元のExcelファイルと、コードによって生成された出力Excelファイルは、以下のリンクからダウンロードできます。

- [元のExcelファイル](5112357.xlsx)  
- [出力Excelファイル](5112356.xlsx)  

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
