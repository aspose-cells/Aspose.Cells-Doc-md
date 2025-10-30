---
title: C++経由でJavaScriptを使用してExcelグラフの凡例を管理
description: Microsoft Excelでチャートの凡例を効果的に利用・カスタマイズするために、C++経由のAspose.Cells for JavaScriptを活用する方法を学びます。当ガイドでは凡例の機能、アクセス方法、編集方法、視覚化とデータ理解の向上について詳しく説明します。
keywords: C++経由でAspose.Cells for JavaScript、チャートの凡例、Microsoft Excel、ビジュアリゼーション、データ理解。
linktitle: 凡例
type: docs
weight: 50
url: /ja/javascript-cpp/chart-legend/
---

## **凡例オプション**
C++経由のAspose.Cells for JavaScriptを使用すると、ランタイム中にチャートの凡例を管理できます。 [凡例](https://reference.aspose.com/cells/javascript-cpp/legend/) オブジェクトは移動、更新、書式設定が可能です。

|![todo:image_alt_text](chart_legend.png)|

## **チャートの凡例の設定**
Aspose.Cellsの[凡例](https://reference.aspose.com/cells/javascript-cpp/legend/)を使えば、チャートの凡例を簡単に管理できます。

凡例管理のためのコードスニペットは次のとおりです：


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Legend Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, LegendPositionType } = AsposeCells;

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
                // No file selected - a new workbook will be created
            }

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = Color.Blue;

            // Move the legend to left
            chart.legend.position = LegendPositionType.Left;

            // Set font color of the legend
            chart.legend.font.color = Color.Blue;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_legend.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart with legend created successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [Aspose.Cellsを使用して、チャートの凡例エントリの塗りをなしに設定する方法を説明します。](/cells/ja/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
