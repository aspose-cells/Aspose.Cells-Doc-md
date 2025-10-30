---
title: Hitta om datapunkter finns i andra pie eller bar i en pie of pie eller bar of pie diagram med JavaScript via C++  
linktitle: Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj eller stapeldiagram  
description: Lär dig hur du använder Aspose.Cells for JavaScript via C++ för att hitta om datapunkter finns i den andra pie eller bar i ett pie av pie eller bar av pie diagram. Denna guide visar hur man identifierar och kommer åt den sekundära pie eller bar i en sammansatt diagram för att analysera och manipulera data effektivt.  
keywords: Aspose.Cells for JavaScript via C++, Pie of Pie Diagram, Bar of Pie Diagram, Sekundär Pie, Sekundär Bar, Dataanalys, Datahantering.  
type: docs  
weight: 180  
url: /sv/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Möjliga användningsscenario**  
Du kan avgöra om datapunkter i serien finns i den andra pie på *Pie of Pie* diagrammet eller i baren på *Bar of Pie* diagrammet med Aspose.Cells for JavaScript via C++. Använd egenskapen [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) för att bestämma detta.  

Hämta gärna [exempelfilen i Excel](5115193.xlsx) som används i följande exempel och se dess konsolutdata. Om du öppnar [exempelfilen i Excel](5115193.xlsx), kommer du att hitta alla datapunkter mindre än 10 som är inuti stapeln för *Bar of Pie*-diagrammet, som också visas av konsolutdata.  
## **Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram**  
 Följande exempel visar hur man avgör om datapunkter är i den andra cirkeln eller stapeln på ett *Pie of Pie* eller *Bar of Pie*-diagram.  

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
## **Konsoloutput**  
Vänligen se den följande konsolutmatningen som genererats efter körning av ovanstående exempel med filen [sample excel file](5115193.xlsx). Om [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) är **falsk**, är datapunkten inom pie, och om den är **sann**, är datapunkten inom baren.  

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
