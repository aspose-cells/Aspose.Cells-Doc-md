---
title: C++を介したJavaScriptでCell.Calculateメソッドの計算時間を短縮
linktitle: Cell.Calculateメソッドの計算時間の短縮
description: この記事では、Aspose.Cellsライブラリを使用してJavaScriptを介したC++でのExcelのセル計算方法の計算時間を短縮する方法を紹介します。
keywords: Aspose.Cells、Excel、セル計算方法、最適化、パフォーマンス、計算時間の短縮、JavaScriptを介したC++
type: docs
weight: 100
url: /ja/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **可能な使用シナリオ**

通常、ユーザーには[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)メソッドを一度呼び出して、その後に個々のセルの計算結果を取得することを推奨します。しかし、時には、ユーザーはワークブック全体を計算したくない場合もあります。特定のセルだけを計算したい場合には、Aspose.Cellsが提供する[**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--)プロパティを**false**に設定することで、個々のセルの計算時間を大幅に短縮できます。再帰的プロパティを**true**に設定すると、すべての依存セルが各呼び出し時に再計算されますが、**false**に設定すると、依存セルは一度だけ計算され、その後の呼び出しでは再計算されません。

## **Cell.calculate()メソッドの計算時間を短縮**

以下のサンプルコードは[**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--)プロパティの使用例を示しています。このコードを[サンプルエクセルファイル](5113710.xlsx)とともに実行し、コンソール出力を確認してください。再帰的プロパティを**false**に設定すると、計算時間が大幅に短縮されることがわかります。このプロパティについての詳細なコメントも併せてお読みください。

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

## **コンソール出力**

上記のサンプルコードの実行結果は、[サンプルエクセルファイル](5113710.xlsx)を用いた場合のコンソール出力です。ご注意ください。出力は異なる場合がありますが、再帰的プロパティを**false**に設定した後の経過時間は、常に**true**に設定した場合より短くなります。

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}
