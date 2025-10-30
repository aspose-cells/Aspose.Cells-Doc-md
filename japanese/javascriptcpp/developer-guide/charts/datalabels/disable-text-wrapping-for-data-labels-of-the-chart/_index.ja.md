---
title: JavaScriptを使用してC++経由でチャートのデータラベルのテキスト折り返しを無効にする方法
description: Aspose.Cells for JavaScript via C++を使用してチャートのデータラベルのテキスト折り返しを無効にする方法を学びましょう。長いラベルが重ならないように防ぎ、より読みやすく明確なチャート表示を実現します。
keywords: Aspose.Cells for JavaScript via C++、チャート作成、データラベル、テキスト折り返し、重なる、可読性、表示。
type: docs
weight: 70
url: /ja/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013では、ユーザーはチャートのデータラベル内のテキストを折り返すか折り返さないかを選択できます。デフォルトでは、チャートのデータラベル内のテキストは折り返し状態になっています。

Aspose.Cellsは、[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#isTextWrapped--)プロパティを提供しており、これをtrueまたはfalseに設定することで、データラベルのテキスト折り返しを有効または無効にできます。

{{% /alert %}}

次のコードサンプルは、チャートのデータラベルのテキスト折り返しを無効にする方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Data Label Text Wrapping</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by loading uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Disable the Text Wrapping of Data Labels in all Series
            chart.nSeries.get(0).dataLabels.isTextWrapped = false;
            chart.nSeries.get(1).dataLabels.isTextWrapped = false;
            chart.nSeries.get(2).dataLabels.isTextWrapped = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
