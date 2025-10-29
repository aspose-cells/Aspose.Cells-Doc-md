---
title: Vérifiez si les points de données se trouvent dans la deuxième tarte ou barre sur un graphique à parts ou barres avec JavaScript via C++  
linktitle: Trouver si les points de données sont dans le deuxième secteur ou barre d un diagramme de secteur ou barre de diagramme.  
description: Apprenez comment utiliser Aspose.Cells for JavaScript via C++ pour déterminer si les points de données se trouvent dans la deuxième tarte ou barre sur un graphique à parts ou barres. Ce guide montrera comment identifier et accéder à la tarte ou la barre secondaire sur un graphique composite, permettant une analyse et une manipulation efficaces des données.  
keywords: Aspose.Cells for JavaScript via C++, Graphique à parts avec tarte, Graphique à barres avec tarte, Tarte secondaire, Barre secondaire, Analyse des données, Manipulation des données.  
type: docs  
weight: 180  
url: /fr/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Scénarios d'utilisation possibles**  
Vous pouvez vérifier si les points de données d'une série se trouvent dans la deuxième tarte sur un graphique *Pie of Pie* ou dans la barre d'un graphique *Bar of Pie* en utilisant Aspose.Cells for JavaScript via C++. Veuillez utiliser la propriété [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) pour le déterminer.  

Veuillez télécharger le [fichier Excel d’exemple](5115193.xlsx) utilisé dans le code d’exemple suivant et voir sa sortie console. Si vous ouvrez le [fichier Excel d’exemple](5115193.xlsx), vous constaterez que tous les points de données inférieurs à 10 se trouvent dans la barre du graphique *Barre de secteurs*, comme le montre également la sortie de la console.  
## **Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles**  
Le code d’exemple suivant montre comment déterminer si les points de données se trouvent dans le second secteur ou la seconde barre sur un graphique *Secteur de secteurs* ou *Barre de secteurs*.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Bar of Pie Chart Data Points Example</h1>
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
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (e.g., PieBars.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart which is Bar of Pie chart and calculate it
            const chart = worksheet.charts.get(0);
            chart.calculate();

            // Access the chart series
            const series = chart.nSeries.get(0);

            // Iterate and collect output
            let outputLines = [];
            for (let i = 0; i < series.points.count; i++) {
                // Access chart point
                const chartPoint = series.points.get(i);

                // Skip null values
                if (chartPoint.yValue === null) continue;

                // Print the chart point value and see if it is inside bar or pie.
                // If the IsInSecondaryPlot is true, then the data point is inside bar 
                // otherwise it is inside the pie. 
                const valueLine = "Value: " + chartPoint.yValue;
                const inSecondaryLine = "IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot();
                console.log(valueLine);
                console.log(inSecondaryLine);
                console.log();

                outputLines.push(valueLine);
                outputLines.push(inSecondaryLine);
                outputLines.push("");
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p style="color: orange;">No data points found or all values are null.</p>';
            } else {
                resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
            }
        });
    </script>
</html>
```  
## **Sortie console**  
Veuillez consulter la sortie de la console suivante générée après l'exécution du code d'exemple ci-dessus avec le [fichier Excel d'exemple](5115193.xlsx). Si [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) est **faux**, le point de données se trouve à l'intérieur de la tarte ou, s'il est **vrai**, alors le point de données se trouve dans la barre.  

{{< highlight javascript >}}  
 Value: 15  
IsInSecondaryPlot: false  

Value: 9  
IsInSecondaryPlot: true  

Value: 2  
IsInSecondaryPlot: true  

Value: 40  
IsInSecondaryPlot: false  

Value: 5  
IsInSecondaryPlot: true  

Value: 4  
IsInSecondaryPlot: true  

Value: 25  
IsInSecondaryPlot: false  
{{< /highlight >}}
