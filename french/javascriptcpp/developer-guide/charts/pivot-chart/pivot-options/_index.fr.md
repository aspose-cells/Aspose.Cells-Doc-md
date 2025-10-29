---
title: Comment gérer PivotChart avec PivotOptions pour JavaScript via C++
linktitle: Options de pivot
type: docs
weight: 10
url: /fr/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Comment gérer PivotChart avec PivotOptions en JavaScript via C++.
keywords: PivotChart JavaScript via C++
---

## Qu'est-ce qu'un tableau croisé dynamique

Un tableau croisé dynamique dans Excel est une représentation graphique des données créée à partir d'un tableau croisé dynamique. Il permet aux utilisateurs de visualiser et d'analyser les données de manière dynamique en résumant et en affichant les informations sous forme de graphique. Les tableaux croisés dynamiques sont interactifs et peuvent être facilement modifiés pour montrer différentes perspectives des données, ce qui en fait un outil puissant pour l'analyse et la présentation de données dans Excel.

## Comment gérer un PivotChart avec PivotOptions

En utilisant Aspose.Cells for JavaScript via C++, vous pouvez utiliser [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/) pour gérer PivotChart.

Fichier et code d'exemple :
[Fichier d'exemple](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Avec le code d'exemple ci-dessus, vous pouvez vérifier le fichier résultant avec l'effet suivant, tel qu'illustré dans la figure :

**![Résultat](Output.png)**
