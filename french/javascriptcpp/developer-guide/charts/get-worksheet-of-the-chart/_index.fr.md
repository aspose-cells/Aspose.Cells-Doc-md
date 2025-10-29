---
title: Obtenez la feuille de calcul du graphique avec JavaScript via C++
linktitle: Obtenir la feuille de calcul du graphique
description: Apprenez comment récupérer la feuille associée à un graphique Excel en utilisant Script Aspose.Cells for Java via C++. Accédez et manipulez efficacement les données sous jacentes du graphique.
keywords: Script Aspose.Cells for Java, graphiques Excel, feuilles de calcul, manipulation des données, données sous jacentes, opérations, JavaScript via C++
type: docs
weight: 1000
url: /fr/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Parfois, vous voulez accéder à une feuille de calcul à partir d'une référence à un graphique. Aspose.Cells fournit la propriété [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) qui renvoie la référence de la feuille de calcul contenant le graphique.

{{% /alert %}}

L'exemple suivant montre comment utiliser la propriété [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--). Le code affiche d’abord le nom de la feuille, puis accède au premier graphique de la feuille. Ensuite, il affiche à nouveau le nom de la feuille en utilisant la propriété [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Print worksheet name
            const sheetName = worksheet.name;
            let outputHtml = `<p>Sheet Name: ${sheetName}</p>`;

            // Access the first chart inside this worksheet
            const charts = worksheet.charts;
            if (charts.count > 0) {
                const chart = charts.get(0);

                // Access the chart's sheet and display its name again
                const chartSheetName = chart.worksheet.name;
                outputHtml += `<p>Chart's Sheet Name: ${chartSheetName}</p>`;
            } else {
                outputHtml += `<p>No charts available in the worksheet.</p>`;
            }

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```

Voici la sortie console que le code d'exemple produit. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul à chaque fois.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
