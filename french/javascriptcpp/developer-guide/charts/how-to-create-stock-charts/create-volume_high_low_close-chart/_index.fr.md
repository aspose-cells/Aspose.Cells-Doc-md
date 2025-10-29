---
title: Créer un graphique boursier Volume High Low Close (VHLC) avec JavaScript via C++
linktitle: Créer un graphique boursier Volume High Low Close (VHLC)
description: Apprenez à créer un graphique boursier volume high low close en utilisant Aspose.Cells for JavaScript via C++. Notre guide montrera comment tracer des données de marché boursier, y compris le volume, le haut, le bas, et la clôture, pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for JavaScript via C++, graphique stock Volume High Low Close, données de marché boursier, analyse, visualisation.
type: docs
weight: 183
url: /fr/javascript-cpp/create-volume-high-low-close-stock-chart/
---

## **Scénarios d'utilisation possibles**
Le troisième graphique que nous examinerons est le graphique Volume High Low Close. Encore une fois, il est important de répéter que vous devez disposer des données dans le bon ordre. Si vous avez besoin de réarranger votre tableau de données, faites-le avant de configurer votre graphique.
Ce graphique inclut une colonne pour le volume immédiatement après la première colonne (catégorie), et les graphiques incluent un graphique en colonnes sur l'axe principal affichant ce volume, tandis que les prix sont déplacés vers l'axe secondaire.

![todo:image_alt_text](data.png)
## **Graphique boursier Volume-Haut-Bas-Fermeture (VHLC)**

![todo:image_alt_text](sample.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](Volume-High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Volume-High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend can be showed
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Volume-High-Low-Close Stock";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (converted from setChartDataRange(range, isVertical))
            chart.chartDataRange = ["A1:E9", true];
            // Set category data 
            chart.nSeries.categoryData = "A2:A9";
            // Set Color for the first series(Volume) data 
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(79, 129, 189);
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
