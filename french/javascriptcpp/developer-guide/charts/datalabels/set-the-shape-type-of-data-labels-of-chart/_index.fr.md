---
title: Définir le type de forme des étiquettes de données du graphique avec JavaScript via C++
linktitle: Définir le type de forme des étiquettes de données du graphique
description: Apprenez comment définir le type de forme des étiquettes de données dans les graphiques en utilisant Aspose.Cells for JavaScript via C++. Ce guide expliquera les différents types de formes disponibles et vous montrera comment choisir la forme appropriée pour vos étiquettes de données afin d’améliorer la présentation et l’utilité.
keywords: Aspose.Cells for JavaScript via C++, création de graphiques, étiquettes de données, types de formes, présentation, utilité.
type: docs
weight: 110
url: /fr/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Scénarios d'utilisation possibles**
Vous pouvez changer le type de forme des étiquettes de données du graphique en utilisant la propriété `DataLabels.shapeType`. Elle accepte la valeur de l'énumération `DataLabelShapeType` et modifie le type de forme des étiquettes de données en conséquence. Certains de ses valeurs sont

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Définir le type de forme des étiquettes de données du graphique**
Le code d'exemple suivant change le type de forme des étiquettes de données du graphique en `DataLabelShapeType.WedgeEllipseCallout`. Consultez le fichier Excel d'exemple ([fichier.xlsx](60489778.xlsx)) utilisé dans ce code et le fichier Excel de sortie ([fichier.xlsx](60489779.xlsx)) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Code d'exemple**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
