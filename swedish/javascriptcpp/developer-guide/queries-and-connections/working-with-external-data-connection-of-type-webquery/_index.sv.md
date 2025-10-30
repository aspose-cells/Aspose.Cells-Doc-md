---
title: Arbeta med extern dataanslutning av typ WebQuery med JavaScript via C++
linktitle: Arbeta med extern datanslutning av typ WebQuery
type: docs
weight: 30
url: /sv/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: Lär dig hur du arbetar med externa dataanslutningar av typ WebQuery med hjälp av Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Du kan komma åt extern datanslutning av vilken typ som helst genom att använda Workbook.DataConnections-samlingen. En typ av sådan datanslutning är WebQuery. Den här artikeln visar hur du arbetar med WebQuery-datanslutning. Du kan skapa WebQuery-datanslutning i Microsoft Excel med menyn **Data** > **Från webben**.

{{% /alert %}}

## Arbeta med extern datanslutning av typ WebQuery

Följande kod visar hur man arbetar med extern datanslutning av typ **WebQuery**. Den använder [exempel excelfilen](5112365.xlsx) som du kan ladda ner från den angivna länken. Du kan också se konsolens utdata av den här koden längre ner.

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

## Konsoloutput



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
