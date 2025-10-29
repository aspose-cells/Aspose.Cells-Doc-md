---
title: Ajouter des étiquettes personnalisées aux points de données dans la série du graphique avec JavaScript via C++
linktitle: Ajouter des étiquettes personnalisées aux points de données de la série du graphique
description: Apprenez comment ajouter des étiquettes personnalisées aux points de données dans la série d’un graphique en utilisant Aspose.Cells for JavaScript via C++. Ce guide vous montrera comment modifier l’apparence, la position et la mise en forme des étiquettes, tout en les liant à votre source de données pour une représentation précise.
keywords: Aspose.Cells for JavaScript via C++, graphique, étiquettes personnalisées, points de données, série, apparence, position, mise en forme, source de données, représentation.
type: docs
weight: 100
url: /fr/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/
---

{{% alert color="primary" %}}

Vous pouvez ajouter des étiquettes personnalisées aux points de données de la série du graphique à l'aide de la propriété [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--). Cet article expliquera comment utiliser cette propriété pour ajouter des étiquettes personnalisées aux points de données de la série du graphique.

{{% /alert %}}

Le code suivant crée un **Grafique en dispersion reliés par des lignes avec des marqueurs de données** et ajoute **des étiquettes personnalisées** aux **points de données** dans la **série** du **graphique**. Chaque étiquette personnalisée affiche le **nom de la série** et le **nom du point**. Vous pouvez utiliser tout autre texte à la place.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Put data
            sheet.cells.get(0, 0).value = 1;
            sheet.cells.get(0, 1).value = 2;
            sheet.cells.get(0, 2).value = 3;

            sheet.cells.get(1, 0).value = 4;
            sheet.cells.get(1, 1).value = 5;
            sheet.cells.get(1, 2).value = 6;

            sheet.cells.get(2, 0).value = 7;
            sheet.cells.get(2, 1).value = 8;
            sheet.cells.get(2, 2).value = 9;

            // Generate the chart
            const chartIndex = sheet.charts.add(ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
            const chart = sheet.charts.get(chartIndex);

            chart.title.text = "Test";
            chart.categoryAxis.title.text = "X-Axis";
            chart.valueAxis.title.text = "Y-Axis";

            chart.nSeries.categoryData = "A1:C1";

            // Insert series 1
            chart.nSeries.add("A2:C2", false);

            let series = chart.nSeries.get(0);

            let pointCount = series.points.count;
            for (let i = 0; i < pointCount; i++) {
                const pointIndex = series.points.get(i);
                pointIndex.dataLabels.text = "Series 1" + "\n" + "Point " + i;
            }

            // Insert series 2
            chart.nSeries.add("A3:C3", false);

            series = chart.nSeries.get(1);

            pointCount = series.points.count;
            for (let i = 0; i < pointCount; i++) {
                const pointIndex = series.points.get(i);
                pointIndex.dataLabels.text = "Series 2" + "\n" + "Point " + i;
            }

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
