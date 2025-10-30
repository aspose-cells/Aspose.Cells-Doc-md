---
title: Individuare se i punti dati sono nella seconda fetta o barra di un grafico a torta di torte o a barre di torta con JavaScript via C++  
linktitle: Trova se i punti dati sono nel secondo grafico a torta o a barre su un grafico a torta di torta o a barre. Trova come usare Aspose.Cells for .NET per trovare se i punti dati sono nel secondo grafico a torta o barre su un grafico a torta di torta o a barre. La nostra guida dimostrerà come identificare e accedere al secondo grafico a torta o a barre su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.  
description: Impara come usare Aspose.Cells for JavaScript via C++ per verificare se i punti dati sono nella seconda fetta o barra di un grafico a torta di torte o a barre di torta. Questa guida dimostrerà come identificare e accedere alla seconda fetta o barra di un grafico composito, consentendo di analizzare e manipolare efficacemente i dati.  
keywords: Aspose.Cells for JavaScript via C++, Grafico a Torta di Torta, Grafico a Barre di Torta, Seconda Fetta, Seconda Barre, Analisi dei Dati, Manipolazione dei Dati.  
type: docs  
weight: 180  
url: /it/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Possibili Scenari di Utilizzo**  
Puoi verificare se i punti dati di una serie si trovano nella seconda fetta di un grafico *Pie of Pie* o nella barra di un grafico *Bar of Pie* usando Aspose.Cells for JavaScript via C++. Si prega di usare la proprietà [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) per determinarlo.  

Scarica il [file Excel di esempio](5115193.xlsx) usato nel codice di esempio seguente e verifica l'output sulla console. Se apri il [file Excel di esempio](5115193.xlsx), troverai che tutti i punti dati inferiori a 10 sono all’interno della barra di *Bar of Pie* come mostrato anche dall’output della console.  
## **Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta**  
Il codice di esempio seguente mostra come trovare se i punti dati sono nel secondo settore o barra di un grafico *Pie of Pie* o *Bar of Pie*.  

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
## **Output della console**  
Consulta la seguente uscita della console generata dopo l'esecuzione del codice di esempio con il [file excel di esempio](5115193.xlsx). Se [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) è **falso**, il punto dati si trova all’interno della torta o, se è **vero**, il punto dati si trova all’interno della barra.  

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
