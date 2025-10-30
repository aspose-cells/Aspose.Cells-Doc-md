---
title: JavaScriptを使った動的ロールングチャートの作成方法（C++経由）
linktitle: 動的ローリングチャートの作成方法
description: C++を利用したAspose.Cells for JavaScriptを使用して動的ロールングチャートの作成方法を学びましょう。ガイドは、スムーズなデータ遷移とロール平均を実現し、連続的で更新された表示を行う方法を示します。
keywords: Aspose.Cells for JavaScriptを用いたC++による動的ロールングチャート、データ遷移、スムーズな平均、連続表示、更新された視覚化。
type: docs
weight: 74
url: /ja/javascript-cpp/create-dynamic-rolling-chart/
---

## **可能な使用シナリオ**
動的ローリングチャートとは、データポイントが常にシフトして更新されるグラフィカルな表現を指します。このタイプのチャートは継続的に自動更新され、新しいデータポイントが追加されると古いデータポイントは破棄されます。

動的ローリングチャートは、リアルタイムやストリーミングデータのトレンドやパターンを可視化するために一般的に使用されます。株式市場の分析、気象モニタリング、またはライブパフォーマンスの追跡など、時間的な側面や時間の経過に伴う変化が重要なシナリオで特に有用です。

これらのチャートは通常、アニメーションや自動スクロールのメカニズムを使用して、常に最新の情報が表示されるようにしています。ローリングウィンドウの長さは、過去の1時間、1日、または1週間など、特定の時間期間を表示するようにカスタマイズできます。

要約すると、動的なローリングチャートは、古いデータを破棄しながら最新のデータポイントを表示する連続的に更新されるグラフ表現であり、ユーザーがリアルタイムのトレンドやパターンを観察することができます。

## **Aspose Cellsを使用して動的なローリングチャートを作成する**
次の段落では、Aspose.Cellsを使用して動的なローリングチャートを作成する方法を示します。例のコードと、このコードで作成されたExcelファイルも表示します。

## **サンプルコード**
次のサンプルコードは[DynamicRollingChart.xlsx]を生成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Rolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A1").value = "Month";
            sheet.cells.get("A2").value = 1;
            sheet.cells.get("A3").value = 2;
            sheet.cells.get("A4").value = 3;
            sheet.cells.get("A5").value = 4;
            sheet.cells.get("A6").value = 5;
            sheet.cells.get("A7").value = 6;
            sheet.cells.get("A8").value = 7;

            sheet.cells.get("B1").value = "Sales";
            sheet.cells.get("B2").value = 50;
            sheet.cells.get("B3").value = 45;
            sheet.cells.get("B4").value = 55;
            sheet.cells.get("B5").value = 60;
            sheet.cells.get("B6").value = 55;
            sheet.cells.get("B7").value = 65;
            sheet.cells.get("B8").value = 70;

            // Set the dynamic range for the chart's data source.
            let index = sheets.names.add("Sheet1!ChtData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)";

            // Set the dynamic range for the chart's data labels.
            index = sheets.names.add("Sheet1!ChtLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 10, 3, 25, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicRollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **メモ**
生成されたファイルでは、列Aと列Bにデータを追加できます。これに対し、チャートは最新の5つのデータセットを動的にカウントします。これは、例のコードの「OFFSET」式を使用して行います。
