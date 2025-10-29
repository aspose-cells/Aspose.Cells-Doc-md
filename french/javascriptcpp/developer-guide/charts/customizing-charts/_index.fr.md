---
title: Personnalisation des graphiques avec JavaScript via C++
linktitle: Personnalisation des graphiques
description: Apprenez à personnaliser les graphiques dans Aspose.Cells for JavaScript via C++. Notre guide vous montrera comment modifier la disposition du graphique, ajouter et formater les séries de données, ajuster les axes et appliquer diverses options de mise en forme pour améliorer l apparence et l utilisabilité de vos graphiques.
keywords: Aspose.Cells for JavaScript via C++, création de graphiques, personnalisation, dispositions, séries de données, axes, mise en forme, apparence, utilisabilité.
type: docs
weight: 40
url: /fr/javascript-cpp/customizing-charts/
---

## **Création de graphiques personnalisés**  

Jusqu'à présent, lorsque nous avons parlé de graphiques, nous avons considéré les graphiques standards avec leurs paramètres de mise en forme par défaut. Nous définissons simplement la source de données, réglons quelques propriétés, et le graphique est créé avec ses paramètres par défaut. Mais les API Aspose.Cells supportent également la création de graphiques personnalisés qui permettent aux développeurs de créer des graphiques avec leurs propres paramètres de mise en forme.  

Les développeurs peuvent créer des graphiques personnalisés à l'exécution à l'aide d'Aspose.Cells.  

Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells est représentée par un objet [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) alors que l'objet [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) sert de collection d'objets [**Series**](https://reference.aspose.com/cells/javascript-cpp/series). Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans l'objet [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)).  

Le code d'exemple ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un graphique en colonnes pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique en colonnes, combiné à un graphique linéaire, à la feuille de calcul.  

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

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

Actuellement, Aspose.Cells ne supporte que les graphiques personnalisés combinant pie, line, column, et column stack, mais d'autres graphiques seront supportés dans les futures versions.  

{{% /alert %}}
