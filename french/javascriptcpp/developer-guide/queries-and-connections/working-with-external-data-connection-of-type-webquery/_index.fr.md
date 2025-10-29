---
title: Travailler avec une connexion de données externe de type WebQuery avec JavaScript via C++
linktitle: Travailler avec une connexion de données externe de type WebQuery
type: docs
weight: 30
url: /fr/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: Apprenez comment travailler avec des connexions de données externes de type WebQuery en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Vous pouvez accéder à n'importe quel type de connexion de données externe en utilisant la collection Workbook.DataConnections. Un type de cette connexion de données est WebQuery. Cet article vous montrera comment travailler avec la connexion de données WebQuery. Vous pouvez créer une connexion de données WebQuery dans Microsoft Excel en utilisant le menu **Données** > **À partir du Web**.

{{% /alert %}}

## Travail avec une connexion de données externe de type WebQuery

Le code suivant montre comment travailler avec une connexion de données externe de type **WebQuery.** Il utilise le [fichier Excel d'exemple](5112365.xlsx) que vous pouvez télécharger à partir du lien fourni. Vous pouvez également voir la sortie de la console de ce code ci-dessous.

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

## Sortie de la console



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
