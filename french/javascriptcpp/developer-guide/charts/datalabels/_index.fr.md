---
title: Gérer DataLabels des graphiques Excel avec JavaScript via C++
description: Apprenez comment gérer efficacement les étiquettes de données dans les graphiques Excel avec Script Aspose.Cells for Java via C++. Ce guide complet couvre diverses tâches de gestion, y compris l ajout, la suppression et la modification des étiquettes pour améliorer la lisibilité et l utilisabilité du graphique.
keywords: Script Aspose.Cells for Java, graphiques Excel, étiquettes de données, gestion, lisibilité, convivialité, ajout, suppression, modification.
linktitle: Étiquettes de données
type: docs
weight: 50
url: /fr/javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

Les étiquettes de données sont une partie importante d'un graphique.  
Nous pouvons facilement connaître la valeur, le pourcentage, etc. de chaque série.  

{{% /alert %}}  

## **Options d'étiquettes de données**  
Script Aspose.Cells for Java via C++ permet également de gérer les étiquettes de données du graphique en temps réel, avec l'objet [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/), il est simple de déplacer, mettre à jour et formater les étiquettes de données du graphique.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Gérer les étiquettes de données du graphique**  
Gérez facilement les étiquettes de données du graphique avec Aspose.Cells [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/).  

L'extrait de code suivant montre comment gérer DataLabels :  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
            const workbook = new Workbook();

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
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Sujets avancés**  
- [Ajouter des étiquettes personnalisées aux points de données de la série du graphique](/cells/fr/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Désactiver le retour à la ligne pour les étiquettes de données du graphique](/cells/fr/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Redimensionner la forme de l'étiquette de données du graphique pour s'adapter au texte](/cells/fr/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Étiquette de données personnalisée Rich Text du point de graphique](/cells/fr/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Définir le type de forme des étiquettes de données du graphique](/cells/fr/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Affichage de la plage de cellules sous forme d'étiquettes de données](/cells/fr/javascript-cpp/showing-cell-range-as-the-data-labels/)
