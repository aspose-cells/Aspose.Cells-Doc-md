---
title: Comment créer un diagramme de Gantt avec JavaScript via C++
linktitle: Comment créer un graphique de Gantt
type: docs
weight: 72
url: /fr/javascript-cpp/how-to-create-gantt-chart/
description: Apprenez comment créer un diagramme de Gantt avec Aspose.Cells for JavaScript via l API C++.
keywords: JavaScript créer un diagramme de Gantt, ajouter un diagramme de Gantt, insérer un diagramme de Gantt
---

## **Qu’est-ce qu’un graphique de Gantt**

Un graphique de Gantt est un type de diagramme à barres qui illustre un calendrier de projet. Il montre les dates de début et de fin des différents éléments d’un projet. Chaque tâche ou activité est représentée par une barre, dont la longueur correspond à sa durée. Les graphiques de Gantt indiquent également les dépendances entre les tâches, permettant aux gestionnaires de visualiser la séquence dans laquelle les tâches doivent être accomplies. Ils sont largement utilisés en gestion de projet pour planifier, programmer et suivre efficacement les projets.

## **Comment créer un graphique de Gantt dans Excel**

Vous pouvez créer un graphique de Gantt dans Excel en suivant ces étapes :
1. Ajoutez des données pour le graphique de Gantt. 
<br>
<img src="00.png" width=50% />
1. Sélectionnez les données et allez dans Insertion --> Graphiques --> Insérer un graphique à colonnes ou à barres --> Graphique à barres empilées. Dans notre exemple, c’est B1:B7, puis insérez le **Graphique à barres empilées**.
<br>
<img src="1.png" width=50% />

1. Sélectionnez le graphique, **Sélectionner les données** -> **Ajouter**, configurez le **Nom de la série** et **Valeurs de la série** comme suit.
<br>
<img src="2.png" width=50% />

1. Sélectionnez le graphique, modifiez les **Labels de l’axe horizontal (catégorie)**.
<br>
<img src="3.png" width=50% />

1. **Mettre en forme l’axe** Y, sélectionnez **Catégories en ordre inverse**.
1. Sélectionnez la **série bleue** et définissez la **Remplissage -> Sans remplissage**.
1. **Mettre en forme l’axe** X, définissez le **Minimum** et **Maximum** (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Ajouter des étiquettes de données** pour le graphique, vous obtiendrez ainsi un graphique de Gantt.
<br>
<img src="0.png" width=50% />


## **Comment ajouter un graphique de Gantt dans Aspose.Cells**
Veuillez voir le code exemple ci-dessous. Il charge le [fichier Excel exemple](sample.xlsx) contenant des données exemples. Il crée ensuite le graphique à barres empilées basé sur ces données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur au format [XLSX de sortie](result.xlsx). La capture d’écran suivante montre le graphique de Gantt créé par Aspose.Cells dans le fichier Excel de sortie.
<br>
<img src="5.png" width=60% />

### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
