---
title: Работа с внешним подключением данных типа WebQuery с помощью JavaScript через C++
linktitle: Работа с внешним подключением данных типа WebQuery
type: docs
weight: 30
url: /ru/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: Узнайте, как работать с внешними подключениями данных типа WebQuery с использованием Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Вы можете получить доступ к внешнему подключению данных любого типа, используя коллекцию Workbook.DataConnections. Одним из таких подключений данных является WebQuery. В этой статье будет показано, как работать с подключением данных WebQuery. Вы можете создать подключение данных WebQuery в Microsoft Excel, используя меню **Данные** > **Из Интернета**.

{{% /alert %}}

## Работа с внешним подключением данных типа WebQuery

В следующем коде показано, как работать с внешним подключением данных типа **WebQuery**. Он использует [образец электронного файла](5112365.xlsx), который вы можете скачать по предоставленной ссылке. Вы также можете увидеть вывод консоли этого кода ниже.

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

## Вывод в консоль



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
