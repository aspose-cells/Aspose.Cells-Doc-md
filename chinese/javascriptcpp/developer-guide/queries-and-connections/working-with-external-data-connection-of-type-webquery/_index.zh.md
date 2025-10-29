---
title: 使用JavaScript通过C++处理WebQuery类型的外部数据连接。
linktitle: 使用  WebQuery  类型的外部数据连接
type: docs
weight: 30
url: /zh/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: 学习如何使用Aspose.Cells for JavaScript通过C++处理WebQuery类型的外部数据连接。 
---

{{% alert color="primary" %}}

您可以使用 Workbook.DataConnections 集合访问任何类型的外部数据连接。其中一种数据连接类型是 WebQuery。本文将向您展示如何处理 WebQuery 数据连接。您可以使用 Microsoft Excel 中的 **数据** > **来自网络** 菜单创建 WebQuery 数据连接。

{{% /alert %}}

## 使用 **WebQuery** 类型的外部数据连接

以下代码显示了如何处理类型为 **WebQuery** 的外部数据连接。它使用了您可以从提供的链接下载的 [示例 Excel 文件](5112365.xlsx)。您还可以在下文看到此代码的控制台输出。

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

## 控制台输出



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
