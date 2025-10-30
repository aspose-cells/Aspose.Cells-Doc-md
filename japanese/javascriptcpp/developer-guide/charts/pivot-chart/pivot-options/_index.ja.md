---
title: JavaScriptをC++経由で使用したPivotOptionsを使用したPivotChartの管理方法
linktitle: Pivot Options
type: docs
weight: 10
url: /ja/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: JavaScriptをC++経由で使用したPivotChartの管理方法。
keywords: C++を使用したPivotChart JavaScript
---

## PivotChartとは

ExcelのPivotChartは、PivotTableから作成されたデータの視覚的な表現です。これにより、ユーザーは情報を要約してチャート形式で表示し、データをダイナミックに視覚化して分析することができます。PivotChartは対話型であり、データの異なる視点を簡単に表示するように修正できるため、Excelでのデータ分析とプレゼンテーションにおける強力なツールとなっています。

## PivotOptionsを使用してPivotChartを管理する方法

 Aspose.Cells for JavaScriptをC++経由で使用することで、[**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/)を利用してPivotChartを管理できます。

サンプルファイルとコード:
[サンプルファイル](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

上記の例のコードを使用すると、次の効果が表示された結果ファイルを確認できます。

**![Output](Output.png)**
