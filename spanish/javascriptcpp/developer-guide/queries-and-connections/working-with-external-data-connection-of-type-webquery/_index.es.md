---
title: Trabajando con conexión de datos externos de tipo WebQuery con JavaScript a través de C++
linktitle: Trabajar con conexión de datos externos de tipo WebQuery
type: docs
weight: 30
url: /es/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: Aprende cómo trabajar con conexiones de datos externas de tipo WebQuery usando Aspose.Cells for JavaScript a través de C++. 
---

{{% alert color="primary" %}}

Puede acceder a conexiones de datos externas de cualquier tipo utilizando la colección Workbook.DataConnections. Un tipo de dicha conexión de datos es WebQuery. Este artículo le mostrará cómo trabajar con una conexión de datos de tipo WebQuery. Puede crear una conexión de datos de tipo WebQuery en Microsoft Excel utilizando el menú **Datos** > **Desde la Web**.

{{% /alert %}}

## Trabajando con Conexiones de Datos Externas de tipo WebQuery

El siguiente código muestra cómo trabajar con una conexión de datos externa de tipo **WebQuery**. Utiliza el [archivo de Excel de ejemplo](5112365.xlsx) que puede descargar desde el enlace proporcionado. También puede ver la salida de la consola de este código más abajo.

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

## Salida de la consola



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
