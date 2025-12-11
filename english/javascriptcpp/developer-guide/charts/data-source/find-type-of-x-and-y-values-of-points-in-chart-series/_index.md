---
title: Find Type of X and Y Values of Points in Chart Series with JavaScript via C++
linktitle: Find Type of X and Y Values of Points in Chart Series
description: Learn how to determine the type of X and Y values in chart series points using Aspose.Cells for JavaScript via C++. This guide explains the types of data values and how to access and work with them in your charts.
keywords: Aspose.Cells for JavaScript via C++, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possible Usage Scenarios**  
Sometimes, you want to know the type of X and Y values of chart points in a series. Aspose.Cells for JavaScript via C++ provides `ChartPoint.XValueType` and `ChartPoint.YValueType` properties that can be used for this purpose. Please note that you will have to call the `Chart.calculate()` method before you can use these properties effectively.  

## **Find Type of X and Y Values of Points in Chart Series**  
The following sample code loads the [sample Excel file](64716905.xlsx) and accesses the first chart inside the first worksheet. It then calls the `Chart.calculate()` method and finds the type of X and Y values of the first chart point and prints them in the console. Please see the console output shown below for a reference.  

## **Sample Code**  
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

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access the first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of the chart point.
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

## **Console Output**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}