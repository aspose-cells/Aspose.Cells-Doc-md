---
title: Minska beräkningstiden för Cell.Calculate metoden med JavaScript via C++
linktitle: Minska beräkningstiden för Cell.Calculate metoden
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att minska beräkningstiden för cellberäkningar i Excel med JavaScript via C++.
keywords: Aspose.Cells, Excel, Cellberäkningsmetoder, optimering, prestanda, minskning av beräkningstid, JavaScript via C++
type: docs
weight: 100
url: /sv/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Möjliga användningsscenario**

 Normalt rekommenderar vi användare att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) metoden en gång och sedan få de beräknade värdena för de enskilda cellerna. Men ibland vill inte användaren beräkna hela arbetsboken. De vill bara beräkna en enskild cell. Aspose.Cells tillhandahåller [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--)-egenskapen, som du kan ställa in till **false** för att avsevärt minska beräkningstiden för individuella celler. När den rekursiva egenskapen är inställd på **true**, så omberäknas alla beroende celler vid varje anrop. Men när den är **false**, beräknas beroende celler endast en gång och omberäknas inte vid efterföljande anrop.

## **Minska beräkningstiden för Cell.calculate() metod**

 Följande exempel kod illustrerar användningen av [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--)-egenskapen. Kör denna kod med den givna [exempel excel-filen](5113710.xlsx) och kontrollera dess konsolutmatning. Du kommer att märka att inställningen av den rekursiva egenskapen till **false** har minskat beräkningstiden avsevärt. Läs även kommentarerna för en bättre förståelse av denna egenskap.

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

            // Test calculation time after setting recursive true
            workbook.calculateFormula(); // initiate calculation

            // Test calculation time after setting recursive false (specify ignoreError as false)
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

                // Stop the watch
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

## **Konsoloutput**

 Detta är konsolutmatningen för ovanstående exempel kod när den körs med vår [exempel excel-fil](5113710.xlsx). Observera att utgången kan skilja sig, men den förflutna tiden efter att den rekursiva egenskapen har ställts in på **false** kommer alltid att vara mindre än när den är **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}
