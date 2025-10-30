---
title: Lavorare con la Connessione Dati Esterna di tipo WebQuery con JavaScript tramite C++
linktitle: Lavorare con la connessione dati esterna di tipo WebQuery
type: docs
weight: 30
url: /it/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: Impara come lavorare con connessioni dati esterne di tipo WebQuery usando Aspose.Cells for JavaScript tramite C++. 
---

{{% alert color="primary" %}}

Puoi accedere alle connessioni dati esterne di qualsiasi tipo utilizzando la raccolta Workbook.DataConnections. Un tipo di connessione dati del genere è WebQuery. Questo articolo ti mostrerà come lavorare con la connessione dati WebQuery. Puoi creare una connessione dati WebQuery in Microsoft Excel utilizzando il menu **Dati** > **Da Web**.

{{% /alert %}}

## Lavorare con la connessione dati esterna di tipo WebQuery

Il seguente codice mostra come lavorare con la connessione dati esterna di tipo **WebQuery**. Utilizza il [file di Excel di esempio](5112365.xlsx), che puoi scaricare dal link fornito. Puoi anche vedere l'output della console di questo codice di seguito.

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

## Output della console



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
