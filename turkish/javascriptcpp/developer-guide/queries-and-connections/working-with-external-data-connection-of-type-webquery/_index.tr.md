---
title: JavaScript ile C++ kullanarak WebQuery türünde Dış Veri Bağlantısı ile Çalışmak
linktitle: WebQuery Türünden Dış Veri Bağlantısı ile Çalışmak
type: docs
weight: 30
url: /tr/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: JavaScript ile C++ kullanarak WebQuery türünde dış veri bağlantılarıyla nasıl çalışılacağını öğrenin. 
---

{{% alert color="primary" %}}

Çalışma Kitabı.DataConnections koleksiyonunu kullanarak herhangi bir türdeki harici veri bağlantısına erişebilirsiniz. Bu türden bir veri bağlantısı WebQuery'dir. Bu makale, WebQuery veri bağlantısıyla nasıl çalışılacağını gösterecektir. Microsoft Excel'de **Veri** > **Web'den** menüsünü kullanarak WebQuery veri bağlantısı oluşturabilirsiniz.

{{% /alert %}}

## WebQuery türündeki Harici Veri Bağlantısı ile Çalışma

Aşağıdaki kod, **WebQuery** türündeki harici veri bağlantısıyla nasıl çalışılacağını göstermektedir. İndirebileceğiniz [örnek excel dosyası](5112365.xlsx) kullanılmaktadır. Ayrıca bu kodun konsol çıktısını aşağıda görebilirsiniz.

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

## Konsol Çıkışı



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
