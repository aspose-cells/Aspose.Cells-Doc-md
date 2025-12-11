---
title: Read Axis Labels after Calculating the Chart with JavaScript via C++
linktitle: Read Axis Labels after Calculating the Chart
description: Learn how to read axis labels in Aspose.Cells for JavaScript via C++ after calculating the chart. Our guide will show you how to access and retrieve axis labels, including their formatting and positioning.
keywords: Aspose.Cells for JavaScript, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning, JavaScript via C++
type: docs
weight: 90
url: /javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Possible Usage Scenarios**

You can read axis labels of your chart after calculating its values using the [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--) method. Please use the [**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--) property for this purpose, which will return the list of axis labels.

## **Read Axis Labels after Calculating the Chart**

Please see the following sample code that loads the [sample Excel file](ReadAxisLabels.xlsx) and reads the category axis labels of the chart in the first worksheet. It then prints the values of the axis labels on the console. Please see the console output of the sample code given below for a reference.

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Console Output**

{{< highlight javascript >}}  
Category Axis Labels:  

---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}