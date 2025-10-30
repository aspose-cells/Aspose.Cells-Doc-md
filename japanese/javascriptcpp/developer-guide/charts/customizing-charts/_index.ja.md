---
title: JavaScriptを使用したC++によるチャートのカスタマイズ
linktitle: チャートのカスタマイズ
description: C++経由のAspose.Cells for JavaScriptでチャートをカスタマイズする方法を学びましょう。ガイドでは、レイアウトの変更、データ系列の追加とフォーマット、軸の調整、さまざまな書式設定オプションの適用方法を説明します。
keywords: C++経由のAspose.Cells for JavaScript、チャート作成、カスタマイズ、レイアウト、データ系列、軸、書式設定、外観、使いやすさ。
type: docs
weight: 40
url: /ja/javascript-cpp/customizing-charts/
---

## **カスタムチャートの作成**  

これまで、チャートについて議論してきた際は、標準の書式設定が施された標準的なチャートを見てきました。我々はデータソースを定義し、いくつかのプロパティを設定するだけで、チャートはデフォルトのフォーマット設定で作成されます。しかし、Aspose.Cells APIは、開発者が独自のフォーマット設定を持つカスタムチャートを作成できる機能もサポートしています。  

開発者は、Aspose.Cellsを使用して実行時にカスタムチャートを作成できます。  

チャートはデータ系列で構成されています。Aspose.Cellsにおける各データ系列は [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) オブジェクトで表され、[**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) オブジェクトは [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) オブジェクトのコレクションとして機能します。カスタムチャートを作成する際、開発者は異なるデータ系列（[**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) オブジェクトに収集された）に対して異なる種類のチャートを使用する自由があります。  

以下の例コードは、カスタムチャートの作成方法を示しています。この例では、最初のデータ系列には列チャートを使用し、2番目のデータ系列には折れ線グラフを使用しています。その結果、ワークシートには列チャートと折れ線グラフが組み合わされたチャートが追加されます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

現在、Aspose.Cellsはパイチャート、ラインチャート、カラムチャート、およびカラム積み上げチャートを組み合わせたカスタムチャートのみをサポートしていますが、今後のリリースでさらに多くのチャートがサポートされる予定です。  

{{% /alert %}}
