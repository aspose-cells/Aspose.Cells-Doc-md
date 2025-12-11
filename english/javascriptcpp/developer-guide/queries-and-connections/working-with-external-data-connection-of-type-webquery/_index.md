---
title: Working with External Data Connection of type WebQuery with JavaScript via C++
linktitle: Working with External Data Connection of type WebQuery
type: docs
weight: 30
url: /javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: Learn how to work with external data connections of type WebQuery using Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

You can access external data connections of any type using the Workbook.DataConnections collection. One type of such a data connection is WebQuery. This article will show you how to work with a WebQuery data connection. You can create a WebQuery data connection in Microsoft Excel using the **Data** > **From Web** menu.

{{% /alert %}}

## Working with External Data Connection of type WebQuery

The following code shows how to work with an external data connection of type **WebQuery**. It uses the [sample Excel file](5112365.xlsx) which you can download from the provided link. You can also see the console output of this code shown below.

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

## Console Output



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}