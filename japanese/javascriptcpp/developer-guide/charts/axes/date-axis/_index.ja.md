---
title: JavaScriptを使用したC++による日付軸の管理方法
description: C++を使用したAspose.Cells for JavaScriptの日付軸管理方法を学習しましょう。さまざまな日付フォーマット、タイムスケール、ティックラベルの頻度について理解を深めます。
keywords: C++を使用したAspose.Cells for JavaScriptの日付軸管理、フォーマット、タイムスケール、ティックラベルの頻度調整
type: docs
weight: 200
url: /ja/javascript-cpp/date-axis/
---

## **可能な使用シナリオ**
 グラフ作成時に日付を使用したワークシートデータから、横軸（カテゴリ軸）に日付がプロットされる場合、Aspose.Cells for JavaScriptは自動的にカテゴリ軸を日時（タイムスケール）軸に変更します。
日付軸は、特定の間隔や基本単位（日数、月、年など）で、ワークシートの日付を年代順に表示します。ワークシート上の日付が順次に並んでいない場合や基本単位が同じでない場合でも、表示されます。
 デフォルトでは、Aspose.Cellsはワークシートのデータ内の任意の2つの日付間の最小差に基づいて日付軸の基本単位を決定します。例として、株価データの最小差が7日間の場合、Excelは基本単位を日として設定しますが、長期のパフォーマンス表示のために月や年に変更できます。

## **Microsoft Excelのように日付軸を処理する**
新しいExcelファイルを作成し、最初のワークシートにチャートの値を配置するサンプルコードをご覧ください。 
その後、チャートを追加し、[**Axis**](https://reference.aspose.com/cells/javascript-cpp/axis/)の種類を設定します。 
[**Axis.categoryType**](https://reference.aspose.com/cells/javascript-cpp/axis/#categoryType--)のタイプを設定し、その後基本単位を日に設定します。

![todo:image_alt_text](excel.png)

## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Date Axis Chart Example</title>
    </head>
    <body>
        <h1>Date Axis Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, CategoryType, TimeUnit, ChartTextDirectionType, FillType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Shortcut to cells collection
            const cells = worksheet.cells;

            // Add the sample values to cells
            cells.get("A1").value = "Date";

            // 14 means datetime format
            const style = cells.style;
            style.number = 14;

            // Put values to cells for creating chart
            const cellA2 = cells.get("A2");
            cellA2.style = style;
            cellA2.value = new Date(Date.UTC(2022, 5, 26));

            const cellA3 = cells.get("A3");
            cellA3.style = style;
            cellA3.value = new Date(Date.UTC(2022, 4, 22));

            const cellA4 = cells.get("A4");
            cellA4.style = style;
            cellA4.value = new Date(Date.UTC(2022, 7, 3));

            cells.get("B1").value = "Price";
            cells.get("B2").value = 40;
            cells.get("B3").value = 50;
            cells.get("B4").value = 60;

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 9, 6, 21, 13);
            // Access the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            // Converted setter to property assignment (range and boolean passed as array)
            chart.chartDataRange = ["A1:B4", true];

            // Set the Axis type to Date time
            chart.categoryAxis.categoryType = CategoryType.TimeScale;
            // Set the base unit for CategoryAxis to days
            chart.categoryAxis.baseUnitScale = TimeUnit.Days;
            // Set the direction for the axis text to be vertical
            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Vertical;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;
            // Set max value of Y axis.
            chart.valueAxis.maxValue = 70;
            // Set major unit.
            chart.valueAxis.majorUnit = 10;

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DateAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
