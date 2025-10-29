---
title: Redimensionner la forme de l étiquette de données du graphique pour qu elle s adapte au texte avec JavaScript via C++
linktitle: Redimensionner la forme de l étiquette de données du graphique pour s adapter au texte
description: Apprenez comment redimensionner la forme de l’étiquette de données dans un graphique pour qu’elle s’adapte au texte dans Aspose.Cells for JavaScript via C++. Notre guide vous montrera comment ajuster la taille et la forme du conteneur de l’étiquette pour s’assurer que le texte s’affiche correctement sans troncature ni chevauchement.
keywords: Aspose.Cells for JavaScript via C++, graphique, étiquettes de données, redimensionnement de la forme, adaptation du texte, troncature, chevauchement.
type: docs
weight: 220
url: /fr/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
L'application Excel propose l'option **Redimensionner la forme pour s'adapter au texte** pour les étiquettes de données du graphique afin d'augmenter la taille de la forme afin que le texte s'y insère.  
{{% /alert %}}  

## **Comment redimensionner la forme de l'étiquette de données du graphique pour s'adapter au texte dans Microsoft Excel**  

Cette option peut être accessible via l'interface Excel en sélectionnant n'importe quelle étiquette de données sur le graphique. Faites un clic droit et choisissez le menu **Format DataLabels**. Dans l'onglet **Taille & Propriétés**, développez **Alignement** pour révéler les propriétés associées, y compris l'option **Redimensionner la forme pour corriger le texte**.  

## **Comment redimensionner la forme de l’étiquette de données du graphique pour qu’elle s’adapte au texte en utilisant Aspose.Cells for JavaScript via C++**  

Pour imiter la fonction d'Excel de redimensionnement des formes d'étiquettes de données pour les adapter au texte, les APIs Aspose.Cells ont exposé la propriété Booléenne [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--). Le code ci-dessous montre un scénario d'utilisation simple de la propriété [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
