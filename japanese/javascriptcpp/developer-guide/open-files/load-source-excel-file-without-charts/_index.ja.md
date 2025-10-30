---
title: チャートなしのExcelファイルをJavaScriptとC++を使用して読み込む
linktitle: グラフを含まないソースエクセルファイルを読み込む
type: docs
weight: 420
url: /ja/javascript-cpp/load-source-excel-file-without-charts/
description: Aspose.Cells for JavaScriptを使用してチャートなしのExcelファイルを読み込む方法を学びます。 
---

{{% alert color="primary" %}}

Aspose.Cellsでは、チャートのないExcelファイルを読み込むことが可能です。これには[**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--)プロパティを使用してください。

{{% /alert %}}

## **グラフを含まないスプレッドシートを読み込む**

以下のサンプルコードは、チャートなしのExcelファイルを読み込み、それを出力PDF形式で保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook Without Charts to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Specify the load options and filter the data
            const options = new LoadOptions();
            // Include everything except charts
            options.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Load the workbook with specified load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ResultWithoutChart.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download ResultWithoutChart.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to PDF without charts. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
