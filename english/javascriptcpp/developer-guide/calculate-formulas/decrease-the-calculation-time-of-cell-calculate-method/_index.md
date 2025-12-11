---
title: Decrease the Calculation Time of Cell.calculate method with JavaScript via C++
linktitle: Decrease the Calculation Time of Cell.calculate method
description: This article introduces how to use the Aspose.Cells library to reduce calculation time for cell calculation methods in Excel using JavaScript via C++.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time, JavaScript via C++
type: docs
weight: 100
url: /javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Possible Usage Scenarios**

Normally, we recommend that users call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate the entire workbook; they just want to calculate a single cell. Aspose.Cells provides [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--) property, which you can set to **false** to decrease the calculation time of individual cells significantly. When the recursive property is set to **true**, all the dependents of cells are recalculated on each call. However, when the recursive property is **false**, dependent cells are calculated only once and are not recalculated on subsequent calls.

## **Decrease the Calculation Time of Cell.calculate() method**

The following sample code illustrates the usage of [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--) property. Please execute this code with the given [sample Excel file](5113710.xlsx) and check its console output. You will find that setting the recursive property to **false** has significantly decreased the calculation time. Please also read the comments for a better understanding of this property.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Calculate Formulas Example</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Test calculation time after setting recursive to true
            workbook.calculateFormula(); // initiate calculation

            // Test calculation time after setting recursive to false (specify ignoreError as false)
            workbook.calculateFormula(false);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.calculated.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Calculated Excel File';

            resultEl.innerHTML = '<p style="color: green;">Calculation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Calculation Time Recursive Test</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Calculation Test (Recursive true/false)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions } = AsposeCells;
        
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            const runs = [true, false];
            let outputHtml = '';
            for (let r = 0; r < runs.length; r++) {
                const rec = runs[r];

                // Set the calculation option, set recursive true or false as per parameter
                const opts = new CalculationOptions();
                opts.recursive = rec;

                // Start stopwatch
                const start = performance.now();

                // Calculate cell A1 one million times
                for (let i = 0; i < 1000000; i++) {
                    ws.cells.get("A1").calculate(opts);
                }

                // Stop the stopwatch
                const end = performance.now();

                // Calculate elapsed time in seconds
                const estimatedTime = (end - start) / 1000;

                // Record the elapsed time
                const message = `Recursive ${rec}: ${estimatedTime} seconds`;
                console.log(message);
                outputHtml += `<p>${message}</p>`;
            }

            resultDiv.innerHTML = `<div style="color: green;">${outputHtml}</div>`;
        });
    </script>
</html>
```

## **Console Output**

This is the console output of the above sample code when executed with the given [sample Excel file](5113710.xlsx) on our machine. Please note, your output may differ, but the elapsed time after setting the recursive property to **false** will always be less than after setting it to **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}