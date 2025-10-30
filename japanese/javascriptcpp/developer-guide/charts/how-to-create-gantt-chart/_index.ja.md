---
title: C++経由でJavaScriptを使用したガントチャートの作り方
linktitle: ガントチャートの作成方法
type: docs
weight: 72
url: /ja/javascript-cpp/how-to-create-gantt-chart/
description: C++ APIを使用してAspose.Cells for JavaScriptでガントチャートを作成する方法を学びます。
keywords: JavaScriptでガントチャートを作成し、ガントチャートを追加し、ガントチャートを挿入する方法
---

## **ガントチャートとは何ですか**

ガントチャートは、プロジェクトスケジュールを示す棒グラフの一種です。各作業やアクティビティの開始・終了日を示し、その長さは期間に対応しています。タスク間の依存関係も示し、プロジェクトマネージャーが作業の順序を視覚化できるようにします。広くプロジェクト管理に利用され、計画・スケジューリング・進行状況の追跡に役立ちます。

## **Excelでガントチャートを作成する方法**

Excelでガントチャートを作成するには、次の手順に従います:
1. ガントチャート用のデータを追加します。 
<br>
<img src="00.png" width=50% />
1. データを選択し、「挿入」→「グラフ」→「積み上げ縦棒グラフ」→「積み上げ横棒グラフ」を選びます。例として、B1:B7を選択し、「積み上げ縦棒」グラフを挿入します。
<br>
<img src="1.png" width=50% />

1. チャートを選択し、「データの選択」 -> 「追加」をクリックし、「シリーズ名」と「シリーズ値」を設定します。
<br>
<img src="2.png" width=50% />

1. グラフを選択し、**横軸（カテゴリ）軸ラベルの編集**を行います。
<br>
<img src="3.png" width=50% />

1. Y軸の**軸の書式設定**で、**逆順にカテゴリ**を選択します。
1. 「ブルーシリーズ」を選択し、「塗りつぶし -> 塗りつぶしなし」を設定します。
1. X軸の「軸の書式設定」を行い、「最小値」と「最大値」を設定します（例：1/5/2019:43470、1/30/2019:43494）。
<br>
<img src="4.png" width=50% />

1. グラフに**データラベルを追加**すると、ガントチャートが完成します。
<br>
<img src="0.png" width=50% />


## **Aspose.Cellsでガントチャートを追加する方法**
以下のサンプルコードをご覧ください。サンプルExcelファイル（sample.xlsx）を読み込み、サンプルデータが含まれています。その後、初期データに基づいた積み上げ棒グラフを作成し、関連する設定を行います。最後に、Excelファイル（結果のxlsx）として保存します。以下のスクリーンショットは、Aspose.Cellsが作成したガントチャートです。
<br>
<img src="5.png" width=60% />

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
