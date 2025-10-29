---
title: Gérer la légende des graphiques Excel avec JavaScript via C++
description: Apprenez comment utiliser Aspose.Cells for JavaScript via C++ pour exploiter et personnaliser efficacement les légendes des graphiques dans Microsoft Excel. Notre guide complet explique la fonctionnalité de la légende, comment y accéder et la modifier, ainsi que comment améliorer la visualisation et la compréhension des données avec les légendes.
keywords: Aspose.Cells for JavaScript via C++, Légendes de graphiques, Microsoft Excel, Visualisation, Compréhension des données.
linktitle: Légende
type: docs
weight: 50
url: /fr/javascript-cpp/chart-legend/
---

## **Options de légende**
Aspose.Cells for JavaScript via C++ permet également de gérer la légende d'un graphique en temps réel. L'objet [Legend](https://reference.aspose.com/cells/javascript-cpp/legend/) peut être déplacé, mis à jour et formaté.

|![todo:image_alt_text](chart_legend.png)|

## **Définir la légende du graphique**
Il est simple de gérer la légende du graphique avec Aspose.Cells [Legend](https://reference.aspose.com/cells/javascript-cpp/legend/).

L'extrait de code suivant montre comment gérer la légende :


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Legend Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, LegendPositionType } = AsposeCells;

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
                // No file selected - a new workbook will be created
            }

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = Color.Blue;

            // Move the legend to left
            chart.legend.position = LegendPositionType.Left;

            // Set font color of the legend
            chart.legend.font.color = Color.Blue;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_legend.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart with legend created successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Définir le texte de l'entrée de la légende du graphique à aucun en utilisant Aspose.Cells](/cells/fr/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
