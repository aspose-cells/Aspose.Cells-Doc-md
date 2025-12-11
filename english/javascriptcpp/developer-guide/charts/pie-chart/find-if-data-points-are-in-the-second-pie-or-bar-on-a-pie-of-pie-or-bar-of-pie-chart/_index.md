---  
title: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart with JavaScript via C++  
linktitle: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart  
description: Learn how to use Aspose.Cells for JavaScript via C++ to find if data points are in the second pie or bar on a pie of pie or bar of pie chart. This guide will demonstrate how to identify and access the secondary pie or bar on a composite chart, allowing you to analyze and manipulate the data effectively.  
keywords: Aspose.Cells for JavaScript via C++, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.  
type: docs  
weight: 180  
url: /javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Possible Usage Scenarios**  
You can find if data points of a series are in the second pie on *Pie of Pie* chart or in the bar of *Bar of Pie* chart using Aspose.Cells for JavaScript via C++. Please use the [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) property to determine it.  

Please download the [sample Excel file](5115193.xlsx) used in the following sample code and see its console output. If you open the [sample Excel file](5115193.xlsx), you will find that all data points less than 10 are inside the bar of *Bar of Pie* chart, as also shown in the console output.  

## **Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart**  
The following sample code shows how to find if data points are in the second pie or bar on a *Pie of Pie* or *Bar of Pie* chart.  

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

            // Access first chart which is a Bar of Pie chart and calculate it
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

                // Print the chart point value and see if it is inside the bar or the pie.
                // If IsInSecondaryPlot is true, then the data point is inside the bar;
                // otherwise, it is inside the pie.
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

## **Console Output**  
Please see the following console output generated after the execution of the above sample code with the [sample Excel file](5115193.xlsx). If [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) is **false**, the data point is inside the pie; if it is **true**, the data point is inside the bar.  

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