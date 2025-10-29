---
title: Obtenir le texte de l’équation de la ligne de tendance du graphique avec JavaScript via C++
description: Apprenez comment utiliser Aspose.Cells for JavaScript via C++ pour récupérer le texte de l’équation d’une ligne de tendance dans un graphique créé dans Microsoft Excel. Notre guide montrera comment accéder et extraire l’équation d’une ligne de tendance pour une analyse ou un affichage ultérieur.
keywords: Aspose.Cells for JavaScript via C++, Ligne de tendance du graphique, Texte de l’équation, Microsoft Excel, Analyse de données, Affichage.
linktitle: Trendlines
type: docs
weight: 110
url: /fr/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Vous pouvez récupérer le texte de l’équation de la ligne de tendance du graphique en utilisant Aspose.Cells for JavaScript via C++. Aspose.Cells fournit la propriété [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) qui retourne le texte de l’équation de la ligne de tendance du graphique. Pour utiliser cette propriété, vous devrez d’abord appeler la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--).

{{% /alert %}}

La capture d'écran suivante montre le graphique avec une ligne de tendance et son texte d'équation en rouge. Nous allons récupérer ce texte en utilisant la propriété [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) dans l'exemple de code ci-dessous.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Code JavaScript pour obtenir le texte de l’équation de la ligne de tendance du graphique

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

## Sortie générée par le code d'exemple

Il s'agit de la sortie de la console du code d'exemple ci-dessus.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
