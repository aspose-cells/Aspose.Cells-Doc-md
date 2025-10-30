---
title: JavaScriptを使った動的スクロールチャートの作成方法（C++経由）
linktitle: 動的なスクロールチャートの作成方法
description: C++を利用したAspose.Cells for JavaScriptを用いた動的スクロールチャートの作成方法を学びましょう。ステップバイステップのガイドは、スムーズなデータ遷移と自動スクロールの実装方法を示し、連続的に更新される表示を行います。
keywords: Aspose.Cells for JavaScriptを用いたC++による動的スクロールチャート、データ遷移、スムーズなスクロール、連続表示、更新された視覚化。
type: docs
weight: 75
url: /ja/javascript-cpp/create-dynamic-scrolling-chart/
---

## **可能な使用シナリオ**
動的スクロールチャートは、時間の経過とともに変化するデータを表示するためのグラフ表現の一種です。リアルタイムのデータ表示を提供するよう設計されており、ユーザーが連続的な更新やトレンドを追跡できます。新しいデータが追加されると、チャートは自動的に更新され、最新の情報を表示します。

動的スクロールチャートは、ファイナンス、株式市場分析、気象追跡、ソーシャルメディア分析など、さまざまな産業で一般的に使用されます。リアルタイム情報に基づいた、データパターンの視覚化と分析をユーザーが行い、的確な意思決定を行うことができます。

これらのチャートは通常、インタラクティブであり、ユーザーがズームインまたはズームアウト、過去のデータをスクロール、時間間隔を調整することができます。通常、複数のデータシリーズをサポートし、異なるメトリクスおよび相関を包括的に表示します。

全体として、動的スクロールチャートは、時系列データのモニタリングと分析に貴重なツールであり、リアルタイムの意思決定を容易にし、データの可視化能力を向上させるものです。

## **Aspose.Cellsを使用してダイナミックスクロールチャートを作成する**
次の段落では、C++を利用したAspose.Cells for JavaScriptを使用して動的スクロールチャートを作成する方法を示します。例のコードと、このコードで作成されたExcelファイルも紹介します。

## **サンプルコード**
次のサンプルコードは[DynamicScrollingChart.xlsx]を生成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Scrolling Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, ChartType } = AsposeCells;

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
            sheet.cells.get("A1").value = "Day";
            sheet.cells.get("B1").value = "Sales";
            // In this example, we will add 30 days of data
            const allDays = 30;
            const showDays = 10;
            let currentDay = 1;

            for (let i = 0; i < allDays; i++) {
                const cellA = `A${i + 2}`;
                const cellB = `B${i + 2}`;
                sheet.cells.get(cellA).value = i + 1;
                sheet.cells.get(cellB).value = 50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3);
            }

            // This is the Dynamic Scrolling Control Data
            sheet.cells.get("G19").value = "Start Day";
            sheet.cells.get("G20").value = currentDay;
            sheet.cells.get("H19").value = "Show Days";
            sheet.cells.get("H20").value = showDays;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtScrollData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtScrollLabels");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)";

            // Add a ScrollBar for the Dynamic Scrolling Chart
            const bar = sheet.shapes.addScrollBar(2, 0, 3, 0, 200, 30);
            bar.min = 0;
            bar.max = allDays - showDays;
            bar.currentValue = currentDay;
            bar.linkedCell = "$G$20";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Line, 2, 4, 15, 10);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("Sales", true);
            chart.nSeries.get(0).values = "Sheet1!ChtScrollData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtScrollLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicScrollingChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **メモ**
生成されたファイルでは、スクロールバーを操作できます。このとき、チャートは最新の10つのデータセットを動的にカウントします。これは、例のコードの「OFFSET」式を使用して行います。
