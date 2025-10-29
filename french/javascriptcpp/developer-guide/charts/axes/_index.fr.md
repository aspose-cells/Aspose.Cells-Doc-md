---
title: Gérer les axes des graphiques Excel avec JavaScript via C++
description: Découvrez comment configurer les axes des graphiques en Aspose.Cells for JavaScript via C++. Notre guide vous montrera comment ajuster les axes principaux et secondaires, définir leurs plages, et modifier leurs propriétés pour améliorer vos graphiques.
keywords: Aspose.Cells for JavaScript via C++, axes de graphique, configuration, axes principaux, axes secondaires, plage, propriétés.
linktitle: Axes
type: docs
weight: 50
url: /fr/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

Dans les graphiques Excel, il existe 3 types d'axes :  
1. Axe horizontal (Catégorie) : Axe X  
1. Axe Vertical (Valeur) : Axe des Y  
1. Axe de Profondeur (Série) : Axe des Z  

{{% /alert %}}  

## **Options d'Axe**  
Aspose.Cells for JavaScript via C++ permet également de gérer les axes du graphique en temps réel. Avec l'objet [Axis](https://reference.aspose.com/cells/javascript-cpp/axis/), vous pouvez modifier toutes les options de l'Axe comme dans Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Gérer les axes des X et Y**  
Dans un graphique Excel, les axes horizontal et vertical sont les deux axes les plus populaires à utiliser.  

Le fragment de code suivant montre comment définir les options des axes X et Y.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **Sujets avancés**  
- [Changer la direction des étiquettes des graduations](/cells/fr/javascript-cpp/change-tick-label-direction/)  
- [Déterminer quels axes existent dans le graphique](/cells/fr/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [Gérer les unités automatiques de l'axe du graphique comme dans Microsoft Excel](/cells/fr/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Lire les étiquettes des axes après le calcul du graphique](/cells/fr/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Comment définir l'axe des catégories dans un graphique Excel](/cells/fr/javascript-cpp/how-to-set-category-axis/)
