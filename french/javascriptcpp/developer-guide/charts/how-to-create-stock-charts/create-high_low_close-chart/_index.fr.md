---
title: Créer un graphique boursier High Low Close (HLC) avec JavaScript via C++
linktitle: Créer un graphique de stocks High Low Close (HLC)
description: Apprenez à créer un graphique boursier high low close en utilisant Aspose.Cells for JavaScript via C++. Notre guide étape par étape vous montrera comment tracer des données de marché boursier, y compris les prix élevés, bas et de clôture, sur un graphique pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for JavaScript via C++, graphique stock High Low Close, données de marché boursier, analyse, visualisation.
type: docs
weight: 181
url: /fr/javascript-cpp/create-high-low-close-stock-chart/
---

## **Scénarios d'utilisation possibles**  
Le graphique de stock haut-bas-close (HLC) utilise quatre colonnes de données. La première colonne est une catégorie, généralement une date mais les noms d'actions peuvent aussi être utilisés. Les trois colonnes suivantes correspondent respectivement aux prix haut, bas et de clôture. La plage de prix pour chaque catégorie est indiquée par une ligne verticale allant du bas au haut, et le prix de clôture est représenté par une marque à droite de cette ligne.  

![todo:image_alt_text](sample.png)  
## **Améliorations de la visibilité dans le graphique**  
Parfois, pour rendre le graphique plus intuitif, nous pouvons modifier l'apparence du marqueur (clôture), ou le faire s'afficher sur l'axe secondaire.  

![todo:image_alt_text](sample2.png)  
## **Code d'exemple**  
Le code d'exemple suivant charge le [fichier Excel d'exemple](High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range (range and orientation)
            chart.chartDataRange = ["A1:D9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the marker with the built-in data for the 3rd series (index 2)
            const series2 = chart.nSeries.get(2);
            const marker = series2.marker;
            marker.markerStyle = AsposeCells.ChartMarkerType.Dash;
            marker.markerSize = 20;
            marker.area.formatting = AsposeCells.FormattingType.Custom;
            marker.area.foregroundColor = AsposeCells.Color.Maroon;

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
