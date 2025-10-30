---
title: Verkürzen Sie die Berechnungszeit der Cell.Calculate Methode mit JavaScript via C++
linktitle: Verringerung der Berechnungszeit der Cell.Calculate Methode
description: Dieser Artikel führt ein, wie man die Aspose.Cells Bibliothek nutzt, um die Berechnungszeit für Zellberechnungsmethoden in Excel mit JavaScript via C++ zu verringern.
keywords: Aspose.Cells, Excel, Zellberechnungsmethoden, Optimierung, Leistung, Verringerung der Berechnungszeit, JavaScript via C++
type: docs
weight: 100
url: /de/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Mögliche Verwendungsszenarien**

 Normalerweise empfehlen wir Benutzern, die [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)-Methode einmal aufzurufen und dann die berechneten Werte der einzelnen Zellen abzurufen. Manchmal möchten Benutzer jedoch nicht die gesamte Arbeitsmappe berechnen. Sie möchten nur eine einzelne Zelle berechnen. Aspose.Cells bietet die Eigenschaft [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--), die Sie auf **false** setzen können, um die Berechnungszeit einzelner Zellen erheblich zu verkürzen. Wenn die rekursive Eigenschaft auf **true** gesetzt ist, werden alle Abhängigen der Zellen bei jedem Aufruf neu berechnet. Bei Einstellung auf **false** werden abhängige Zellen nur einmal berechnet und bei nachfolgenden Aufrufen nicht erneut.

## **Verringern Sie die Berechnungszeit der Methode Cell.calculate()**

 Der folgende Beispielcode veranschaulicht die Verwendung der Eigenschaft [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--). Bitte führen Sie diesen Code mit der angegebenen [Beispieldatei Excel](5113710.xlsx) aus und prüfen Sie die Konsolenausgabe. Sie werden feststellen, dass das Setzen der rekursiven Eigenschaft auf **false** die Berechnungszeit deutlich verringert hat. Lesen Sie auch die Kommentare für ein besseres Verständnis dieser Eigenschaft.

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

## **Konsolenausgabe**

 Dies ist die Konsolenausgabe des oben genannten Beispielcodes, der mit der angegebenen [Beispieldatei Excel](5113710.xlsx) auf unserem Rechner ausgeführt wurde. Bitte beachten Sie, dass Ihre Ausgabe abweichen kann, aber die verstrichene Zeit nach Einstellung der rekursiven Eigenschaft auf **false** immer kürzer sein wird als bei **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}
