---
title: Comment créer un graphique à rouleau dynamique avec JavaScript via C++
linktitle: Comment créer un graphique dynamique roulant
description: Apprenez comment créer un graphique à rouleau dynamique en utilisant Aspose.Cells for JavaScript via C++. Notre guide vous montrera comment implémenter des transitions de données fluides et des moyennes mobiles dans votre graphique pour un affichage continu et mis à jour.
keywords: Aspose.Cells for JavaScript via C++, graphique à rouleau dynamique, transitions de données, moyennes fluides, affichage continu, visualisation en mise à jour.
type: docs
weight: 74
url: /fr/javascript-cpp/create-dynamic-rolling-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique roulant se réfère à une représentation graphique qui affiche des points de données constamment en mouvement et se met à jour au fil du temps. Il s'agit d'un type de graphique qui se met continuellement à jour, présentant une fenêtre roulante des points de données les plus récents tout en éliminant les anciens points de données au fur et à mesure que de nouveaux arrivent.

Les graphiques dynamiques roulants sont couramment utilisés pour visualiser les tendances et les motifs dans les données en temps réel ou en continu. Ils sont particulièrement utiles dans des scénarios où les aspects temporels et les changements au fil du temps sont critiques, comme l'analyse du marché boursier, la surveillance météorologique ou le suivi des performances en direct.

Ces graphiques utilisent généralement des mécanismes d'animation ou de défilement automatique pour garantir que les informations les plus récentes sont toujours présentées. La longueur de la fenêtre roulante peut être personnalisée pour afficher une période de temps spécifique, comme la dernière heure, le jour ou la semaine.

En résumé, un graphique dynamique roulant est une représentation graphique continuellement mise à jour qui affiche les derniers points de données tout en éliminant les anciens, permettant aux utilisateurs d'observer les tendances et les motifs en temps réel.

## **Utilisez Aspose Cells pour créer un graphique dynamique roulant**
Dans les prochains paragraphes, nous vous montrerons comment créer un graphique dynamique roulant en utilisant Aspose.Cells. Nous vous montrerons le code de l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [fichier Dynamic Rolling Chart](DynamicRollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Remarques**
Dans le fichier généré, vous pouvez continuer à ajouter des données dans les colonnes A et B, tandis que le graphique comptera dynamiquement les 5 ensembles de données les plus récents. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple :
