---
title: JavaScriptを使用してC++経由でシリーズを非表示にする方法
linktitle: シリーズを非表示にする方法
description: C++経由でAspose.Cells for JavaScriptを使用してExcelグラフのシリーズを非表示にする方法を学びます。 
keywords: Excelグラフ、シリーズ、非表示、IsFiltered JavaScriptをC++経由で使用
type: docs
weight: 74
url: /ja/javascript-cpp/how-to-set-series-invisible/
---

## Excelチャートでシリーズを非表示にする方法

Excelチャートでは、チャートを右クリックして「データの選択」をクリックし、表示・非表示の設定をチェック・解除できます。以下の[サンプルファイル](SeriesFiltered.xlsx)をダウンロードし、図のように操作してこの機能を実現できます。次に、Aspose.Cellsライブラリを使った方法をご説明します。

![todo:image_alt_text](series-invisible.png)

## Aspose.Cellsでシリーズを非表示に設定する方法 

Aspose.Cellsを使ってシリーズを非表示に設定するコードは以下の通りです：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

以下の[入力ファイル](SeriesFiltered.xlsx)と[出力ファイル](output.xlsx)を取得できます。

図のように、最初に表示されていた2つのシリーズが、出力ファイルで非表示になっています。
![todo:image_alt_text](output.png)
