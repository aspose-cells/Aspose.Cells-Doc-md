---
title: Comment créer un graphique en cascade avec JavaScript via C++
linktitle: Comment créer un diagramme en cascade
type: docs
weight: 160
url: /fr/javascript-cpp/creating-waterfall-chart/
description: Créez des graphiques en cascade dans Excel avec JavaScript et Aspose.Cells for JavaScript via C++.
keywords: créez un graphique en cascade dans Excel avec JavaScript via C++, création de graphique en cascade dans Excel avec JavaScript via C++, comment créer un graphique en cascade dans Excel avec JavaScript via C++
---

{{% alert color="primary" %}}

Un graphique en cascades est un type particulier de graphique utilisé généralement pour démontrer comment la position de départ augmente ou diminue. Microsoft Excel propose de nombreux types de graphiques prédéfinis, y compris colonnes, lignes, pie, barres, radar, etc., mais le graphique en cascades dépasse les graphiques de base et peut être créé en utilisant les types de graphiques existants avec peu ou beaucoup de personnalisation.

{{% /alert %}} 

Les API Aspose.Cells permettent de créer un graphique en cascades avec l'aide du graphique linéaire. L'API permet également de personnaliser l'apparence du graphique pour lui donner la forme d'une cascade en réglant les propriétés [**Series.upBars**](https://reference.aspose.com/cells/javascript-cpp/series/#upBars--) et [**Series.downBars**](https://reference.aspose.com/cells/javascript-cpp/series/#downBars--).

Le morceau de code ci-dessous démontre l'utilisation de Aspose.Cells for JavaScript via C++ pour créer un graphique en cascade à partir de zéro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Waterfall Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, FormattingType } = AsposeCells;

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

            // Load workbook from selected file if provided, otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Retrieve the first Worksheet in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Retrieve the Cells of the first Worksheet
            const cells = worksheet.cells;

            // Input some data which chart will use as source
            cells.get("A1").value = "Previous Year";
            cells.get("A2").value = "January";
            cells.get("A3").value = "March";
            cells.get("A4").value = "August";
            cells.get("A5").value = "October";
            cells.get("A6").value = "Current Year";

            cells.get("B1").value = 8.5;
            cells.get("B2").value = 1.5;
            cells.get("B3").value = 7.5;
            cells.get("B4").value = 7.5;
            cells.get("B5").value = 8.5;
            cells.get("B6").value = 3.5;

            cells.get("C1").value = 1.5;
            cells.get("C2").value = 4.5;
            cells.get("C3").value = 3.5;
            cells.get("C4").value = 9.5;
            cells.get("C5").value = 7.5;
            cells.get("C6").value = 9.5;

            // Add a Chart of type Waterfall in same worksheet as of data
            const idx = worksheet.charts.add(ChartType.Waterfall, 4, 4, 25, 13);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(idx);

            // Add Series
            chart.nSeries.add("$B$1:$C$6", true);

            // Add Category Data
            chart.nSeries.categoryData = "$A$1:$A$6";

            // Series has Up Down Bars
            chart.nSeries.get(0).hasUpDownBars = true;

            // Set the colors of Up and Down Bars
            chart.nSeries.get(0).upBars.area.foregroundColor = Color.Green;
            chart.nSeries.get(0).downBars.area.foregroundColor = Color.Red;

            // Make both Series Lines invisible
            chart.nSeries.get(0).border.isVisible = false;
            chart.nSeries.get(1).border.isVisible = false;

            // Set the Plot Area Formatting Automatic
            chart.plotArea.area.formatting = FormattingType.Automatic;

            // Delete the Legend
            chart.legend.legendEntries.get(0).isDeleted = true;
            chart.legend.legendEntries.get(1).isDeleted = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Articles Connexes

- [Création de graphiques](/cells/fr/javascript-cpp/creating-charts/)
- [Personnalisation des graphiques](/cells/fr/javascript-cpp/customizing-charts/)
