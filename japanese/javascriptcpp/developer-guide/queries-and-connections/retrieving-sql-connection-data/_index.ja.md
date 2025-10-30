---
title: C++を用いたJavaScriptによるSQL接続データの取得
linktitle: SQL接続データの取得
type: docs
weight: 10
url: /ja/javascript-cpp/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、SQL接続データを取得できます。これには、SQLサーバへの接続に必要なすべてのデータが含まれます。たとえば、**サーバーURL**、**ユーザー名**、**テーブル名**、**完全なSQLクエリ**、**クエリの種類**、**テーブルの場所**、およびそれに関連付けられた**名前付き範囲の名前**などです。

{{% /alert %}}

Microsoft Excelでは、データベースに接続するには:

1. **データ**メニューをクリックし、**その他のソース**、その後 **SQL Server** を選択します。  
1. 次に、**データ**、その後 **Connections** を選択します。  
1. Connectionsウィザードを使用してデータベースに接続し、データベースクエリを作成します。

Aspose.Cells for JavaScriptは、Workbook.dataConnectionsプロパティを提供し、外部接続を取得します。これは、ワークブック内のExternalConnectionオブジェクトの配列を返します。

ExternalConnectionオブジェクトにSQL接続データが含まれている場合は、DBConnectionにキャストでき、そのプロパティを使ってデータベースコマンド、コマンドタイプ、接続の説明、接続情報、認証情報などを取得できます。

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
