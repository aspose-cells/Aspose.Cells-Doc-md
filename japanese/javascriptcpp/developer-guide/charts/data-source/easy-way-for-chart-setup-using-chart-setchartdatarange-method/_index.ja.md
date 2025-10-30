---
title: JavaScript経由のC++でのチャートデータ範囲設定を簡単に行う方法
linktitle: JavaScript経由のC++でのチャート設定を簡単に行う方法
description: Chart.chartDataRangeメソッドを使用してAspose.Cells for JavaScript via C++で簡単にチャートを設定する方法を学びましょう。ガイドでは、チャートのデータ範囲を指定する方法を示し、最小限の労力でプロフェッショナルで正確なチャートを作成できます。
keywords: Aspose.Cells for JavaScript via C++、チャート作成、chartDataRangeメソッド、データ範囲、プロフェッショナル、正確な、チャート。
type: docs
weight: 190
url: /ja/javascript-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/
---

{{% alert color="primary" %}}

Aspose.Cellsは今、チャートを簡単にセットアップするための[**Chart.chartDataRange(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/chart/#chartDataRange-string-boolean-)メソッドを提供しています。このメソッドを使用することで、シリーズおよびカテゴリ軸データを別々に追加する必要がなくなります。

{{% /alert %}}

以下のサンプルコードは、[**Chart.chartDataRange(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/chart/#chartDataRange-string-boolean-)メソッドを使用してチャートを簡単に設定する方法を説明しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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
            // Creating a new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add data for chart
            // Category Axis Values
            worksheet.cells.get("A2").value = "C1";
            worksheet.cells.get("A3").value = "C2";
            worksheet.cells.get("A4").value = "C3";

            // First vertical series
            worksheet.cells.get("B1").value = "T1";
            worksheet.cells.get("B2").value = 6;
            worksheet.cells.get("B3").value = 3;
            worksheet.cells.get("B4").value = 2;

            // Second vertical series
            worksheet.cells.get("C1").value = "T2";
            worksheet.cells.get("C2").value = 7;
            worksheet.cells.get("C3").value = 2;
            worksheet.cells.get("C4").value = 5;

            // Third vertical series
            worksheet.cells.get("D1").value = "T3";
            worksheet.cells.get("D2").value = 8;
            worksheet.cells.get("D3").value = 4;
            worksheet.cells.get("D4").value = 2;

            // Create Column chart with easy way
            const idx = worksheet.charts.add(ChartType.Column, 6, 5, 20, 13);
            const ch = worksheet.charts.get(idx);
            ch.chartDataRange = { range: "A1:D4", isVertical: true };

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
