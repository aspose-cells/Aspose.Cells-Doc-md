---
title: JavaScript経由でポイントを合計として設定する方法
linktitle: 合計としてポイントを設定する方法
description: C++経由でAspose.Cells for JavaScriptを使用しウォーターフォールチャートでポイントを合計に設定する方法を学びます。
keywords: ウォーターフォールチャート、ポイント、合計として設定、JavaScript経由のC++
type: docs
weight: 72
url: /ja/javascript-cpp/how-to-set-point-as-total/
---

## Excelチャートの「ポイントを合計に設定」とは

例えばWaterFallチャートなど、一部のExcelチャートでは、あるポイントデータが前のポイントの合計になっており、「ポイントを合計として設定」する必要があります。サンプルコードとイラストを下に示します。

## WaterFallチャートには"ポイントを合計に設定"が必要です 

![todo:image_alt_text](set-as-total1.png)

この画像はExcelのウォーターフォールチャートを示しています。「Total」で始まる四つのデータポイントがあり、これらは前のすべてのデータポイントをカウントするために使用されます。この図では設定が正確ではありません。「Total 2024」を選択すると、「合計として設定」オプションがExcelでチェックされていないことが確認できます。修正が必要なサンプルExcelファイル（SampleSheet.xlsx）を添付し、Aspose.Cells for JavaScriptを使用して正しく設定します。

## Aspose.Cells for JavaScriptをC++で使用して "ポイントを合計に設定" 

正しい設定を行うためのコードは以下の通りです：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

次の正しい[出力ファイル](output.xlsx)を取得できます。

図のように、4つの"合計"データポイントが正しく設定されているのが確認でき、前のチャートとの違いもわかります。

![todo:image_alt_text](set-as-total2.png)
