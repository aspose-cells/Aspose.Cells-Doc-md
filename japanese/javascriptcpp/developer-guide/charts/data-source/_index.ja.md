---
title: JavaScriptを使用したC++によるチャートのデータソース設定
description: C++経由のAspose.Cells for JavaScriptがサポートするさまざまなデータソースについて学びましょう。ガイドでは、利用可能なデータソースの種類と、それらに接続してデータを取得し、ワークシートを埋める方法を説明します。
keywords: C++経由のAspose.Cells for JavaScriptを使用したチャート作成、チャート化、データフォーマット、ラベル、色、フォント、外観、使いやすさ。
linktitle: データソース
type: docs
weight: 10
url: /ja/javascript-cpp/data-formatting-in-charts/
---

以前のトピックで、多くの例を示してチャートのデータソースの設定方法を説明しました。このトピックでは、チャートに設定できるデータの種類について詳細を提供します。

## **チャートデータの設定**

Aspose.Cellsを使用してチャートを作成する際に扱うデータには、次の2種類があります：

- チャートデータ。
- カテゴリデータ。

### **チャートデータ**

チャートのデータは、チャートを構築するために使用するデータソースのデータです。セルの範囲（チャートデータを含む）を [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) オブジェクトの [**add(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/#add-string-boolean-) メソッドを呼び出して追加できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Worksheet and Chart Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 170;
            worksheet.cells.get("A4").value = 300;
            worksheet.cells.get("B1").value = 160;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 40;

            // Adding sample values to cells as category data
            worksheet.cells.get("C1").value = "Q1";
            worksheet.cells.get("C2").value = "Q2";
            worksheet.cells.get("C3").value = "Y1";
            worksheet.cells.get("C4").value = "Y2";

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

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

### **カテゴリデータ**

カテゴリデータは、チャートデータのラベル付けに使用され、[**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) の [**categoryData**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/#categoryData--) プロパティを使用して追加できます。以下に例を示し、チャートとカテゴリデータの使用例を示します。上記の例コードを実行すると、列チャートがワークシートに追加されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Create Workbook with Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const arrayBuffer = await fileInput.files[0].arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(10);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(170);
            worksheet.cells.get("A4").putValue(200);
            worksheet.cells.get("B1").putValue(120);
            worksheet.cells.get("B2").putValue(320);
            worksheet.cells.get("B3").putValue(50);
            worksheet.cells.get("B4").putValue(40);

            // Adding sample values to cells as category data
            worksheet.cells.get("C1").putValue("Q1");
            worksheet.cells.get("C2").putValue("Q2");
            worksheet.cells.get("C3").putValue("Y1");
            worksheet.cells.get("C4").putValue("Y2");

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the data source for the category data of SeriesCollection
            chart.nSeries.categoryData = "C1:C4";

            // Saving the Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**  
- [行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する](/cells/ja/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [動的なチャートを作成する](/cells/ja/javascript-cpp/create-dynamic-charts/)  
- [Chart.chartDataRangeメソッドを使ったチャート設定の簡単な方法](/cells/ja/javascript-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [チャートシリーズのX値とY値のタイプを検索する](/cells/ja/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
