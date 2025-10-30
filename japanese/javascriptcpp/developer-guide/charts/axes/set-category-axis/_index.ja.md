---
title: JavaScriptを使用してC++でカテゴリ軸を設定する方法
linktitle: カテゴリ軸の設定方法
description: C++のAspose.Cells for JavaScriptでカテゴリ軸の設定方法を学びましょう。軸範囲の定義やプロパティの調整、ラベルのフォーマット方法について解説します。
keywords: C++を用いたAspose.Cells for JavaScriptでのカテゴリ軸設定、範囲、プロパティ、フォーマット
type: docs
weight: 205
url: /ja/javascript-cpp/how-to-set-category-axis/
---

## **可能な使用シナリオ**
ワークシートにチャートを作成した後、そのチャートにカテゴリ軸を設定できます。この記事では、C++のAspose.Cells for JavaScriptを使用してExcelチャートのカテゴリ軸を設定するサンプルコードを紹介します。

## **サンプルコードの手順**

1. 新しいブックを作成します。

2. 最初のワークシートで新しいチャートを作成します。

3. 最初のワークシートのセルにいくつかの値を追加します。

4. これでカテゴリ軸を設定できます。セルデータを使用する方法と文字列を直接使用する二つの方法がサンプルコードで示されています。

5. 値軸を設定し、結果を確認するためにワークブックを保存します。

## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
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
        const { Workbook, SaveFormat, ChartType, LegendPositionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CHART";

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 8, 0, 20, 10);
            const chart = worksheet.charts.get(chartIndex);

            // Add some values to cells
            worksheet.cells.get("A1").putValue("Sales");
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("A4").putValue(130);
            worksheet.cells.get("A5").putValue(160);
            worksheet.cells.get("A6").putValue(150);
            worksheet.cells.get("B1").putValue("Days");
            worksheet.cells.get("B2").putValue(1);
            worksheet.cells.get("B3").putValue(2);
            worksheet.cells.get("B4").putValue(3);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("B6").putValue(5);

            // Some values in string
            const Sales = "100,150,130,160,150";
            const Days = "1,2,3,4,5";

            // Set Category Axis Data with string
            chart.nSeries.categoryData = `{${Days}}`;
            // Or you can set Category Axis Data with data in cells
            // chart.nSeries.categoryData = "B2:B6";

            // Add Series to the chart
            chart.nSeries.add("Demand1", true);
            // Set value axis with string 
            chart.nSeries.get(0).values = `{${Sales}}`;
            chart.nSeries.add("Demand2", true);
            // Set value axis with data in cells
            chart.nSeries.get(1).values = "A2:A6";

            // Set some Category Axis properties
            chart.categoryAxis.tickLabels.rotationAngle = 45;
            chart.categoryAxis.tickLabels.font.size = 8;
            chart.legend.position = LegendPositionType.Bottom;

            // Save the workbook to view the result file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
