---
title: Comment définir un point comme total avec JavaScript via C++
linktitle: Comment définir un point comme total
description: Apprenez à définir des points comme total dans les graphiques waterfall en utilisant Aspose.Cells for JavaScript via C++.
keywords: Graphique WaterFall, Point, Définir comme total, JavaScript via C++
type: docs
weight: 72
url: /fr/javascript-cpp/how-to-set-point-as-total/
---

## Qu'est-ce que "Définir le point comme total" dans un graphique Excel

Dans certains graphiques Excel, par exemple un graphique en cascade, certaines données de points sont la somme des points précédents, et vous pouvez avoir besoin de "définir le point comme total". Nous montrerons le code d'exemple et l'illustration ci-dessous.

## Un graphique en cascade nécessite de "Définir le point comme total" 

![todo:image_alt_text](set-as-total1.png)

Cette image montre un graphique waterfall dans Excel. Nous pouvons voir qu'il y a quatre points de données commençant par "Total", et qu'ils sont utilisés pour compter tous les points de données précédents. Sur cette image, les paramètres ne sont pas tout à fait corrects. Lorsque nous sélectionnons un point "Total 2024", nous pouvons voir que l'option "Définir comme total" n'est pas cochée dans Excel. Ci-dessous, le fichier Excel [exemple](SampleSheet.xlsx) qui doit être modifié, et nous utiliserons Aspose.Cells for JavaScript via C++ pour le configurer correctement.

## Utiliser Aspose.Cells for JavaScript via C++ pour "Définir le point comme total" 

Nous utilisons le code suivant pour configurer le fichier correctement :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Vous pouvez obtenir le [fichier de sortie correct](output.xlsx) suivant

Comme le montre la figure ci-dessous, les quatre points de données "Total" sont correctement configurés, et vous pouvez voir la différence avec le graphique précédent.

![todo:image_alt_text](set-as-total2.png)
