---
title: Comment définir l axe de catégorie avec JavaScript via C++
linktitle: Comment définir l axe des catégories
description: Apprenez comment définir l axe de catégorie dans Aspose.Cells for JavaScript via C++. Notre guide vous aidera à comprendre comment définir la plage de l axe de catégorie, ajuster ses propriétés et formater ses étiquettes.
keywords: Aspose.Cells for JavaScript via C++, axe de catégorie, réglage, plage, propriétés, formatage.
type: docs
weight: 205
url: /fr/javascript-cpp/how-to-set-category-axis/
---

## **Scénarios d'utilisation possibles**
 Après avoir créé un graphique dans une feuille de calcul, vous pouvez définir l'axe de catégorie pour celui-ci. Dans cet article, nous vous montrerons comment définir l'axe de catégorie pour un graphique Excel en utilisant Aspose.Cells for JavaScript via C++ avec un exemple de code.

## **Les étapes dans le code d'exemple**

1. Créez un nouveau classeur.

2. Créez un nouveau graphique dans la première feuille de calcul.

3. Ajoutez quelques valeurs aux cellules de la première feuille de calcul.

4. Maintenant, vous pouvez définir l’axe des catégories ; il y a deux méthodes : en utilisant les données de cellules ou en utilisant directement des chaînes, comme indiqué dans le code d’exemple.

5. Définissez l'axe de valeur, puis enregistrez le classeur pour voir le résultat.

## **Code d'exemple**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
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
        const { Workbook, SaveFormat, ChartType, LegendPositionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CHART";

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 8, 0, 20, 10);
            const chart = worksheet.charts.get(chartIndex);

            // Add some values to cells
            worksheet.cells.get("A1").putValue("Sales");
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("A4").putValue(130);
            worksheet.cells.get("A5").putValue(160);
            worksheet.cells.get("A6").putValue(150);
            worksheet.cells.get("B1").putValue("Days");
            worksheet.cells.get("B2").putValue(1);
            worksheet.cells.get("B3").putValue(2);
            worksheet.cells.get("B4").putValue(3);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("B6").putValue(5);

            // Some values in string
            const Sales = "100,150,130,160,150";
            const Days = "1,2,3,4,5";

            // Set Category Axis Data with string
            chart.nSeries.categoryData = `{${Days}}`;
            // Or you can set Category Axis Data with data in cells
            // chart.nSeries.categoryData = "B2:B6";

            // Add Series to the chart
            chart.nSeries.add("Demand1", true);
            // Set value axis with string 
            chart.nSeries.get(0).values = `{${Sales}}`;
            chart.nSeries.add("Demand2", true);
            // Set value axis with data in cells
            chart.nSeries.get(1).values = "A2:A6";

            // Set some Category Axis properties
            chart.categoryAxis.tickLabels.rotationAngle = 45;
            chart.categoryAxis.tickLabels.font.size = 8;
            chart.legend.position = LegendPositionType.Bottom;

            // Save the workbook to view the result file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
