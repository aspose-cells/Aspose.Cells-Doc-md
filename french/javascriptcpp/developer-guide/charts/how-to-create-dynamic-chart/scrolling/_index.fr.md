---
title: Comment créer un graphique déroulant dynamique avec JavaScript via C++
linktitle: Comment créer un graphique dynamique déroulant
description: Apprenez à créer un graphique déroulant dynamique en utilisant Aspose.Cells for JavaScript via C++. Notre guide étape par étape montrera comment implémenter des transitions de données fluides et un défilement automatique dans votre graphique pour un affichage continu et mis à jour.
keywords: Aspose.Cells for JavaScript via C++, graphique déroulant dynamique, transitions de données, défilement fluide, affichage continu, visualisation en mise à jour.
type: docs
weight: 75
url: /fr/javascript-cpp/create-dynamic-scrolling-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique déroulant est un type de représentation graphique utilisé pour afficher des données qui changent avec le temps. Il est conçu pour fournir une vue en temps réel des données, permettant aux utilisateurs de suivre les mises à jour et les tendances continues. Le graphique se met à jour en continu lorsque de nouvelles données sont ajoutées, et il défile automatiquement pour afficher les informations les plus récentes.

Les graphiques dynamiques déroulants sont couramment utilisés dans diverses industries, telles que la finance, l'analyse du marché boursier, le suivi météorologique et l'analyse des médias sociaux. Ils permettent aux utilisateurs de visualiser et d'analyser les motifs de données et de prendre des décisions éclairées en fonction des informations en temps réel.

Ces graphiques sont généralement interactifs, permettant à l'utilisateur de zoomer, de faire défiler les données historiques et d'ajuster les intervalles de temps. Ils prennent souvent en charge plusieurs séries de données, offrant une vue complète des différentes mesures et de leurs corrélations.

 Globalement, les graphiques dynamiques déroulants sont des outils précieux pour surveiller et analyser les données en séries chronologiques, faciliter la prise de décisions en temps réel et améliorer les capacités de visualisation des données.

## **Utilisez Aspose.Cells pour créer un graphique défilant dynamique**
Dans les paragraphes suivants, nous vous montrerons comment créer un graphique déroulant dynamique en utilisant Aspose.Cells for JavaScript via C++. Nous afficherons le code pour l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [Fichier de graphique dynamique déroulant](DynamicScrollingChart.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Scrolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, ChartType } = AsposeCells;

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
            sheet.cells.get("A1").value = "Day";
            sheet.cells.get("B1").value = "Sales";
            // In this example, we will add 30 days of data
            const allDays = 30;
            const showDays = 10;
            let currentDay = 1;

            for (let i = 0; i < allDays; i++) {
                const cellA = `A${i + 2}`;
                const cellB = `B${i + 2}`;
                sheet.cells.get(cellA).value = i + 1;
                sheet.cells.get(cellB).value = 50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3);
            }

            // This is the Dynamic Scrolling Control Data
            sheet.cells.get("G19").value = "Start Day";
            sheet.cells.get("G20").value = currentDay;
            sheet.cells.get("H19").value = "Show Days";
            sheet.cells.get("H20").value = showDays;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtScrollData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtScrollLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Add a ScrollBar for the Dynamic Scrolling Chart
            const bar = sheet.shapes.addScrollBar(2, 0, 3, 0, 200, 30);
            bar.min = 0;
            bar.max = allDays - showDays;
            bar.currentValue = currentDay;
            bar.linkedCell = "$G$20";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 2, 4, 15, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtScrollData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtScrollLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicScrollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Remarques**
Dans le fichier généré, vous pouvez agir sur la barre de défilement, tandis que le graphique compte dynamiquement les 10 derniers ensembles de données. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple:
