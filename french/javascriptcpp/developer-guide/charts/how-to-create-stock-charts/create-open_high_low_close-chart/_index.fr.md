---
title: Créer un graphique boursier Open High Low Close (OHLC) avec JavaScript via C++
description: Apprenez à créer un graphique boursier open high low close en utilisant Aspose.Cells for JavaScript via C++. Notre guide montrera comment tracer des données de marché boursier, y compris l ouverture, le haut, le bas et la clôture, pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for JavaScript via C++, graphique stock Open High Low Close, données de marché boursier, analyse, visualisation.
type: docs
weight: 182
url: /fr/javascript-cpp/create-open-high-low-close-stock-chart/
---

## **Scénarios d'utilisation possibles**
Le graphique Open-High-Low-Close (OHLC) utilise cinq colonnes de données, dans l'ordre : catégorie, ouverture, haut, bas et clôture. La plage de prix dans chaque catégorie est à nouveau indiquée par une ligne verticale, tandis que la plage entre l'ouverture et la clôture est donnée par une barre flottante plus large ; si le prix augmente dans la catégorie (la clôture est supérieure à l'ouverture), la barre est remplie d'une couleur, tandis que si le prix diminue, la barre est remplie d'une autre couleur. Ce type de graphique est souvent appelé un graphique en chandelier.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Améliorations de la visibilité dans le graphique**
Nous utilisons souvent des couleurs plutôt que du noir et blanc pour indiquer l'augmentation ou la diminution des prix. Dans le premier ensemble de chandeliers ci-dessous, le rouge montre une augmentation et le vert une diminution des prix.

![todo:image_alt_text](sample2.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](Open-High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open-High-Low-Close Stock Chart Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "Open-High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range
            chart.chartDataRange = ["A1:E9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the DownBars and UpBars with different color
            chart.nSeries.get(0).downBars.area.foregroundColor = AsposeCells.Color.Green;
            chart.nSeries.get(0).upBars.area.foregroundColor = AsposeCells.Color.Red;

            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
