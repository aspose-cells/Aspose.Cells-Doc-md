---
title: Arbeiten mit externer Datenverbindung vom Typ WebQuery mit JavaScript über C++
linktitle: Arbeiten mit externer Datenverbindungstyp WebQuery
type: docs
weight: 30
url: /de/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: Erfahren Sie, wie Sie mit externen Datenverbindungen vom Typ WebQuery mit Aspose.Cells for JavaScript über C++ arbeiten. 
---

{{% alert color="primary" %}}

Sie können auf eine externe Datenverbindung beliebigen Typs über die Workbook.DataConnections-Sammlung zugreifen. Eine solche Datenverbindung ist z.B. WebQuery. In diesem Artikel wird gezeigt, wie Sie mit einer WebQuery-Datenverbindung arbeiten können. Sie können eine WebQuery-Datenverbindung in Microsoft Excel über das **Daten** > **Aus dem Web**-Menü erstellen.

{{% /alert %}}

## Arbeiten mit externer Datenverbindung des Typs WebQuery

Der folgende Code zeigt, wie Sie mit externen Datenverbindungen des Typs **WebQuery** arbeiten. Er verwendet die [Beispieldatei](5112365.xlsx), die Sie von dem bereitgestellten Link herunterladen können. Sie können auch die Konsolenausgabe dieses Codes weiter unten sehen.

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

## Konsolenausgabe



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
