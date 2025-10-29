---
title: Comment créer un graphique TreeMap avec JavaScript via C++
linktitle: Comment créer un diagramme TreeMap
description: Apprenez à créer un graphique TreeMap en Aspose.Cells for JavaScript via C++. Notre guide vous aidera à comprendre les différentes propriétés et options de formatage disponibles pour les graphiques TreeMap, y compris les couleurs, étiquettes, et la représentation des données.
keywords: Aspose.Cells for JavaScript via C++, graphique TreeMap, création, propriétés, formatage, couleurs, étiquettes, représentation des données, graphique circulaire, hiérarchique.
type: docs
weight: 161
url: /fr/javascript-cpp/creating-treemap-chart/
---

## **Scénarios d'utilisation possibles**  
Un graphique à carte de chaleur fournit une vue hiérarchique de vos données et facilite la détection de schémas, tels que les articles les plus vendus d'un magasin. Les branches de l'arbre sont représentées par des rectangles et chaque sous-branche est présentée sous la forme d'un rectangle plus petit. Le graphique à carte de chaleur affiche les catégories par couleur et proximité et peut facilement montrer beaucoup de données qui seraient difficiles avec d'autres types de graphiques.  

![todo:image_alt_text](sample.png)  
## **Diagramme TreeMap**  
Après avoir exécuté le code ci-dessous, vous verrez le diagramme TreeMap comme indiqué ci-dessous.  

![todo:image_alt_text](result.png)  
## **Code d'exemple**  
Le code d'exemple suivant charge le [fichier Excel d'exemple](treemap.xlsx) et génère le [fichier Excel de sortie](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;

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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const pieIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "TreeMap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
