---
title: JavaScriptを使った出来高・始値・高値・安値・終値（VOHLC）株価チャートの作成（C++経由）
description: Aspose.Cells for JavaScriptを利用したC++による出来高・始値・高値・安値・終値株価チャートの作成方法を学びましょう。株式市場のデータ（出来高、始値、高値、安値、終値）をチャートにプロットします。
keywords: Aspose.Cells for JavaScriptを用いたC++による出来高・始値・高値・安値・終値株価チャート、株式市場データ、分析、視覚化。
type: docs
weight: 184
url: /ja/javascript-cpp/create-volume-open-high-low-close-stock-chart/
---

## **可能な使用シナリオ**
次に紹介する株価チャートはボリュームオープンハイロークローズチャートです。データの順番を守ることが重要です。必要に応じてデータテーブルを並べ替えてください。このチャートには、最初の（カテゴリ）列の直後にボリュームの列があり、主要軸にこのボリュームを示す棒グラフを配置し、価格は副軸に移動しています。

![todo:image_alt_text](data.png)
## **出来高-オープン-高値-安値-終値（VOHLC）株価チャート**

![todo:image_alt_text](sample.png)
## **サンプルコード**
[サンプルExcelファイル](Volume-Open-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Volume-Open-High-Low-Close Stock Chart Example</h1>
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

            // Create an instance of Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            // Create High-Low-Close-Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend can be showed
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Volume-Open-High-Low-Close Stock";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (preserve both arguments as an array)
            chart.chartDataRange = ["A1:F9", true];
            // Set category data 
            chart.nSeries.categoryData = "A2:A9";
            // Set Color for the first series (Volume) data 
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(79, 129, 189);
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;
            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
