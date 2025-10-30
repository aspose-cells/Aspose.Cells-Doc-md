---
title: C++経由でJavaScriptを使用したトルネードチャートの作り方
linktitle: 竜巻チャートの作成方法
type: docs
weight: 73
url: /ja/javascript-cpp/create-tornado-chart/
description: C++ APIを使ったAspose.Cells for JavaScriptでのトルネードチャート作成方法を学びます。
keywords: JavaScriptでトルネードチャートを作成し、追加し、挿入する方法
---

## **紹介**
竜巻チャート、または竜巻ダイアグラムまたは竜巻グラフとしても知られるものは、Excelで感度分析によく使用されるデータの視覚化タイプです。これは、特定の結果や成果に対する変数変更の影響を理解するのに役立ちます。

## **Excelで竜巻チャートを作成する方法**
Excelで竜巻チャートを作成する方法は次の通りです：
1. データを選択し、挿入 --> グラフ --> 挿入列または棒グラフ --> 積み上げ棒グラフに移動し、そこをクリックします。
<br>
<img src="1.png" width=70% />
2. Y軸を変更：Y軸を右クリックします。軸の書式設定をクリックします。ラベルで、ラベル位置ドロップダウンをクリックして、Low項目を選択します。
<br>
<img src="2.png" width=70% />
3. 任意の棒を選択し、書式設定に移動します。適切なギャップ幅を設定します。
<br>
<img src="3.png" width=70% />
4. 竜巻チャートからマイナス記号（-）を削除しましょう。X軸を選択します。書式設定に移動し、軸オプションで数字をクリックします。カテゴリでカスタムを選択し、フォーマットコードに###0,###0を記入します。追加をクリックします。
<br>
<img src="4.png" width=70% />
5. Y軸をクリックし、軸オプションに移動します。軸オプションで逆順でカテゴリをチェックします。
<br>
<img src="5.png" width=70% />

## **C++経由でAspose.Cells for JavaScriptにトルネードチャートを追加する方法**
次のサンプルコードをご覧ください。[サンプルExcelファイル](sample.xlsx)を読み込み、いくつかのサンプルデータが含まれているとします。次に、初期データに基づいて積み上げ棒グラフを作成し、関連するプロパティを設定します。最後に、ワークブックを[出力XLSX形式](out.xlsx)に保存します。次のスクリーンショットは、出力ExcelファイルでAspose.Cellsによって作成された竜巻チャートを示しています。
<br>
<img src="6.png" width=70% />

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.category```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.categoryAxis.isPlotOrderReversed = true;

            chart.gapWidth = 10;

            const valueAxis = chart.valueAxis;
            valueAxis.tickLabels.numberFormat = "#,##0;#,##0";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
