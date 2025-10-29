---
title: Trouvez le type de valeurs X et Y des points dans la série de graphiques avec JavaScript via C++
linktitle: Trouver le type de valeurs X et Y des points dans la série de graphique
description: Apprenez à déterminer le type de valeurs X et Y dans les points de la série de graphiques en utilisant Aspose.Cells for JavaScript via C++. Ce guide explique les types de valeurs de données et comment y accéder et travailler avec elles dans vos graphiques.
keywords: Aspose.Cells for JavaScript via C++, graphique, valeurs X, valeurs Y, types de données, accès, travail avec, série de graphiques.
type: docs
weight: 150
url: /fr/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Scénarios d'utilisation possibles**  
Parfois, vous souhaitez connaître le type de valeurs X et Y des points d’un graphique dans une série. Aspose.Cells for JavaScript via C++ fournit les propriétés `ChartPoint.XValueType` et `ChartPoint.YValueType` qui peuvent être utilisées à cet effet. Veuillez noter que vous devrez appeler la méthode `Chart.calculate()` avant de pouvoir utiliser ces propriétés efficacement.  

## **Trouver le type de valeurs X et Y des points dans la série de graphiques**  
Le code exemple suivant charge le [fichier Excel d'exemple](64716905.xlsx) et accède au premier graphique dans la première feuille. Il appelle ensuite la méthode `Chart.calculate()` et détermine le type de valeurs X et Y du premier point du graphique, puis affiche ces informations dans la console. Voir la sortie de console ci-dessous pour référence.  

## **Code d'exemple**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **Sortie console**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
