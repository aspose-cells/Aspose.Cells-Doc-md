---
title: JavaScriptを使用したC++によるTreeMapチャートの作成方法
linktitle: ツリーマップチャートの作成方法
description: C++を経由したAspose.Cells for JavaScriptでのTreemapチャートの作成方法を学習しましょう。色、ラベル、データ表現などのTreemapチャートのさまざまなプロパティや書式設定オプションについて理解を深めます。
keywords: C++を使用したAspose.Cells for JavaScriptによるTreemapチャートの作成、プロパティ設定、書式設定、色、ラベル、データ表現、円形・階層型チャート
type: docs
weight: 161
url: /ja/javascript-cpp/creating-treemap-chart/
---

## **可能な使用シナリオ**  
ツリーマップチャートは、データを階層ビューで表し、店舗の売れ筋商品などのパターンを簡単に把握できます。ツリーのブランチは長方形で表され、各サブブランチは小さな長方形として表示されます。ツリーマップチャートは、色と近接性でカテゴリを表示し、他のチャートタイプでは難しい大量のデータを簡単に表示できます。  

![todo:image_alt_text](sample.png)  
## **ツリーマップチャート**  
以下のコードを実行すると、下記のツリーマップチャートが表示されます。  

![todo:image_alt_text](result.png)  
## **サンプルコード**  
下記のサンプルコードは、[サンプルExcelファイル](treemap.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;

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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const pieIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "TreeMap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
