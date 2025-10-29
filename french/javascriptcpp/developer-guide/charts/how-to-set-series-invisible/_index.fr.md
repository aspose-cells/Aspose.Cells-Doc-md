---
title: Comment rendre une série invisible avec JavaScript via C++
linktitle: Comment définir une série comme invisible
description: Apprenez comment rendre une série invisible dans un graphique Excel en utilisant Aspose.Cells for JavaScript via C++. 
keywords: Graphique Excel, Série, Invisible, IsFiltered JavaScript via C++.
type: docs
weight: 74
url: /fr/javascript-cpp/how-to-set-series-invisible/
---

## Comment définir une série comme invisible dans un graphique Excel

Dans un graphique Excel, vous pouvez faire un clic droit sur un graphique, cliquer sur "Sélectionner des données", et dans la fenêtre contextuelle, vous pouvez définir si une série est visible en cochant ou décochant l’option. Vous pouvez télécharger le [fichier d’exemple]([SeriesFiltered.xlsx](https://example.com/SeriesFiltered.xlsx)) et l’opérer dans Excel comme indiqué dans la figure pour réaliser cette fonction. Ensuite, nous vous expliquerons comment faire cela en utilisant la bibliothèque Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Comment définir une série comme invisible en utilisant Aspose.Cells 

Nous utilisons le code suivant pour définir une série comme invisible en utilisant Aspose.Cells :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Vous pouvez obtenir le [Fichier d'entrée](SeriesFiltered.xlsx) et le [Fichier de sortie](output.xlsx).

Comme indiqué dans la figure ci-dessous, les deux premières séries qui étaient initialement visibles, sont devenues invisibles dans le fichier de sortie.
![todo:image_alt_text](output.png)
