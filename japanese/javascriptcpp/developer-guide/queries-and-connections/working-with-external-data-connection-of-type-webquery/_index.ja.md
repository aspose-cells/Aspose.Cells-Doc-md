---
title: C++を使ったWebQueryタイプの外部データ接続の操作方法
linktitle: WebQueryタイプの外部データ接続の操作
type: docs
weight: 30
url: /ja/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: C++を使ったAspose.Cells for JavaScriptでWebQueryタイプの外部データ接続の操作方法を学びます。 
---

{{% alert color="primary" %}}

Workbook.DataConnectionsコレクションを使用して、任意の種類の外部データ接続にアクセスできます。そのようなデータ接続の1つはWebQueryです。この記事では、WebQueryデータ接続の操作方法を示します。Microsoft Excelで**Data** > **From Web** メニューを使用してWebQueryデータ接続を作成できます。

{{% /alert %}}

## WebQueryの外部データ接続を操作する

次のコードは、**WebQuery**タイプの外部データ接続を扱う方法を示しています。提供されたリンクからダウンロードできる[サンプルエクセルファイル](5112365.xlsx)を使用しています。コンソールには、このコードの出力も示されています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Web Query Connection Reader</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loading the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access data connections
            const connections = workbook.dataConnections;
            if (connections.count > 0) {
                const connection = connections.get(0);

                if (connection instanceof AsposeCells.WebQueryConnection) {
                    const webQuery = connection;
                    console.log("Web Query URL: " + webQuery.url);
                    resultDiv.innerHTML = '<p>Web Query URL: ' + webQuery.url + '</p>';
                } else {
                    resultDiv.innerHTML = '<p>No WebQueryConnection found in the first connection.</p>';
                }
            } else {
                resultDiv.innerHTML = '<p>No data connections found.</p>';
            }
        });
    </script>
</html>
```

## コンソール出力



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
