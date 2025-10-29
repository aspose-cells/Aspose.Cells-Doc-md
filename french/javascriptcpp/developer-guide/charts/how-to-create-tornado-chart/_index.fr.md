---
title: Comment créer un graphique en tornado avec JavaScript via C++
linktitle: Comment créer un graphique en entonnoir
type: docs
weight: 73
url: /fr/javascript-cpp/create-tornado-chart/
description: Apprenez comment créer un graphique en tornado avec Aspose.Cells for JavaScript via l API C++.
keywords: JavaScript créer un graphique en tornado, ajouter un graphique en tornado, insérer un graphique en tornado
---

## **Introduction**
Un diagramme en forme de tornade, également connu sous le nom de diagramme en forme de tornade ou graphique en forme de tornade, est un type de visualisation de données souvent utilisé pour l'analyse de sensibilité dans Excel. Il vous aide à comprendre l'impact des variables changeantes sur un résultat particulier.

## **Comment créer un diagramme en forme de tornade dans Excel**
Vous pouvez créer un diagramme en forme de tornade dans Excel en suivant ces étapes :
1. Sélectionnez les données et allez dans Insertion --> Graphiques --> Insérer un histogramme ou un graphique à barres --> Graphique à barres empilées. Cliquez dessus.
<br>
<img src="1.png" width=70% />
2. Modifiez l'axe des Y : Cliquez avec le bouton droit sur l'axe des y. Cliquez sur formater l'axe. Dans les étiquettes, cliquez sur le menu déroulant de la position des étiquettes et sélectionnez l'élément inférieur.
<br>
<img src="2.png" width=70% />
3. Sélectionnez une barre quelconque et allez dans le formatage. Définissez une largeur d'écart appropriée.
<br>
<img src="3.png" width=70% />
4. Supprimons le signe moins (-) du diagramme en forme de tornade. Sélectionnez l'axe des x. Allez dans le formatage. Dans les options d'axe, cliquez sur le nombre. Dans la catégorie, sélectionnez personnalisé. Dans le code de format, écrivez ###0,###0. Cliquez sur ajouter.
<br>
<img src="4.png" width=70% />
5. cliquez sur l'axe des y et allez dans les options d'axe. Dans les options d'axe, cochez Catégories dans l'ordre inverse.
<br>
<img src="5.png" width=70% />

## **Comment ajouter un graphique en tornado dans Aspose.Cells for JavaScript via C++**
Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](sample.xlsx) qui contient des données d'exemple. Ensuite, il crée le graphique à barres empilées basé sur les données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur au format [XLSX de sortie](out.xlsx). La capture d'écran suivante montre le diagramme en forme de tornade créé par Aspose.Cells dans le fichier Excel de sortie.
<br>
<img src="6.png" width=70% />

### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.category```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.categoryAxis.isPlotOrderReversed = true;

            chart.gapWidth = 10;

            const valueAxis = chart.valueAxis;
            valueAxis.tickLabels.numberFormat = "#,##0;#,##0";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
