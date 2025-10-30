---
title: JavaScriptを使ってC++経由のExcelチャートのDataLabelsを管理する
description: Aspose.Cells for JavaScriptを利用したExcelチャートにおけるデータラベルの効果的な管理方法について学びます。ラベルの追加、削除、変更など、チャートの読みやすさと使いやすさを向上させるさまざまな管理タスクを網羅した総合ガイドです。
keywords: Aspose.Cells for JavaScript、Excelチャート、データラベル、管理、読みやすさ、使いやすさ、追加、削除、変更。
linktitle: データラベル
type: docs
weight: 50
url: /ja/javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

データラベルはチャートの重要な部分です。  
各シリーズの値、パーセンテージなどを簡単に把握できます。  

{{% /alert %}}  

## **データラベルオプション**  
C++経由のAspose.Cells for JavaScriptを使用して、チャートのデータラベルを実行時に管理でき、[DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/)オブジェクトを使ってチャートのデータラベルの移動、更新、フォーマットが簡単に行えます。  

|![todo:image_alt_text](chart_datalabels.png)|  

## **データラベルの管理**  
Aspose.Cellsの[DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/)を使ってチャートのデータラベルを管理するのは簡単です。  

 DataLabelsの管理方法例は次の通りです。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
            const workbook = new Workbook();

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
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **高度なトピック**  
- [チャートシリーズのデータポイントにカスタムラベルを追加する](/cells/ja/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [チャートのデータラベルのテキスト折り返しを無効にする](/cells/ja/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [テキストに合わせるようにチャートのデータラベルの形状をリサイズする](/cells/ja/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [チャートポイントのリッチテキストカスタムデータラベル](/cells/ja/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [チャートのデータラベルの形状タイプを設定する](/cells/ja/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [データラベルとしてセル範囲を表示する](/cells/ja/javascript-cpp/showing-cell-range-as-the-data-labels/)
