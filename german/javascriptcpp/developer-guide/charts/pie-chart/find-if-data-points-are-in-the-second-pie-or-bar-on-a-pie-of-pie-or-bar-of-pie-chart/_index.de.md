---
title: Finden Sie heraus, ob Datenpunkte im zweiten Kreis oder Balken auf einem Pie of Pie oder Bar of Pie Diagramm mit JavaScript via C++ liegen  
linktitle: Feststellen, ob Datenauswahl in der zweiten Torte oder Balken in einem Tortendiagramm oder Balkendiagramm aufgeführt ist  
description: Lernen Sie, wie man mit Aspose.Cells for JavaScript via C++ erkennt, ob Datenpunkte im zweiten Kreis oder Balken eines Pie of Pie oder Bar of Pie Diagramms liegen. Dieser Leitfaden zeigt, wie man den sekundären Kreis oder Balken in einem zusammengesetzten Diagramm identifiziert und darauf zugreift, um die Daten effektiv zu analysieren und zu manipulieren.  
keywords: Aspose.Cells for JavaScript via C++, Pie of Pie Diagramm, Bar of Pie Diagramm, Sekundärer Kreis, Sekundärer Balken, Datenanalyse, Datenmanipulation.  
type: docs  
weight: 180  
url: /de/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Mögliche Verwendungsszenarien**  
Sie können feststellen, ob Datenpunkte einer Serie im zweiten Kreis eines *Pie of Pie*-Diagramms oder im Balken eines *Bar of Pie*-Diagramms mithilfe von Aspose.Cells for JavaScript via C++ liegen. Bitte verwenden Sie die Eigenschaft [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--), um dies zu bestimmen.  

Bitte laden Sie die [Beispieldatei Excel](5115193.xlsx) herunter, die im folgenden Beispielcode verwendet wird, und sehen Sie sich die Konsolenausgabe an. Wenn Sie die [Beispieldatei Excel](5115193.xlsx) öffnen, finden Sie alle Datenpunkte, die kleiner als 10 sind, innerhalb des Balkens des *Bar of Pie*-Diagramms, wie auch die Konsolenausgabe zeigt.  
## **Herausfinden, ob Datenpunkte in der zweiten Torte oder Balken in einem Tortendiagramm der Torten oder Balken sind**  
Das folgende Beispiel zeigt, wie man feststellt, ob Datenpunkte in der zweiten Scheibe oder im Balken eines *Pie of Pie*- oder *Bar of Pie*-Diagramms liegen.  

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
## **Konsolenausgabe**  
Bitte beachten Sie die folgende Konsolenausgabe, die nach Ausführung des obigen Beispielcodes mit der [Beispiel-Excel-Datei](5115193.xlsx) generiert wurde. Wenn [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) **false** ist, liegt der Datenpunkt im Kreis; ist er **true**, liegt der Datenpunkt im Balken.  

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
