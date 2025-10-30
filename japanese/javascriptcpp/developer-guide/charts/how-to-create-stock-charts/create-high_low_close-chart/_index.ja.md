---
title: JavaScriptを使った高値・安値・終値（HLC）株価チャートの作成（C++経由）
linktitle: HLC(高値 安値 終値)株価チャートの作成
description: Aspose.Cells for JavaScriptを利用したC++による高値・安値・終値株価チャートの作成方法を学びましょう。ステップバイステップのガイドでは、株式市場のデータ（高値、安値、終値）をチャートにプロットする方法を示します。
keywords: Aspose.Cells for JavaScriptを使ったC++による高値・安値・終値株価チャート、株式市場データ、分析、視覚化。
type: docs
weight: 181
url: /ja/javascript-cpp/create-high-low-close-stock-chart/
---

## **可能な使用シナリオ**  
ハイロークローズ（HLC）株価チャートは4つのデータ列を使用します。最初の列はカテゴリ（通常は日付、株名も使用可）、次の3列は高値、安値、終値です。各カテゴリーの価格範囲は、低値から高値までの垂直線で示され、終値はこの線の右側に伸びるティックマークで表示されます。  

![todo:image_alt_text](sample.png)  
## **チャートの可視性の改善**  
時には、チャートを直感的に見やすくするために、マーカー（終値）の外観を修正したり、2次軸に表示したりすることがあります。  

![todo:image_alt_text](sample2.png)  
## **サンプルコード**  
次のサンプルコードは[sample Excel file](High-Low-Close.xlsx)をロードし、[output Excel file](out.xlsx)を生成します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>High-Low-Close Stock Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);

            // Set the legend can be showed
            chart.showLegend = true;

            // Set the chart title name 
            chart.title.text = "High-Low-Close Stock";

            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set data range (range and orientation)
            chart.chartDataRange = ["A1:D9", true];

            // Set category data 
            chart.nSeries.categoryData = "A2:A9";

            // Set the marker with the built-in data for the 3rd series (index 2)
            const series2 = chart.nSeries.get(2);
            const marker = series2.marker;
            marker.markerStyle = AsposeCells.ChartMarkerType.Dash;
            marker.markerSize = 20;
            marker.area.formatting = AsposeCells.FormattingType.Custom;
            marker.area.foregroundColor = AsposeCells.Color.Maroon;

            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
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
