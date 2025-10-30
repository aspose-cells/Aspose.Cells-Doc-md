---
title: JavaScriptを使ったチャートの作成と管理（C++経由）
linktitle: チャート
description: Aspose.Cells for JavaScript via C++を使用してMicrosoft Excelでチャートを作成する方法を学びます。さまざまなチャートタイプとその外観や書式のカスタマイズ方法を示すガイドです。
keywords: Aspose.Cells for JavaScript via C++、チャート作成、Microsoft Excel、チャートタイプ、カスタマイズ、外観、書式設定。
type: docs
weight: 130
url: /ja/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

Aspose.Cellsでさまざまなチャートをスプレッドシートに追加できます。Aspose.Cellsは多くの柔軟なチャートオブジェクトを提供します。このトピックでは、Aspose.Cellsのチャートオブジェクトについて説明します。

{{% /alert %}}

## **チャートの作成**

### **単純なチャートの作成**
Aspose.Cellsで次の例コードを使用して簡単にチャートを作成できます：
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding sample values to cells
            worksheet.cells.get("A2").value = "Category1";
            worksheet.cells.get("A3").value = "Category2";
            worksheet.cells.get("A4").value = "Category3";

            worksheet.cells.get("B1").value = "Column1";
            worksheet.cells.get("B2").value = 4;
            worksheet.cells.get("B3").value = 20;
            worksheet.cells.get("B4").value = 50;

            worksheet.cells.get("C1").value = "Column2";
            worksheet.cells.get("C2").value = 50;
            worksheet.cells.get("C3").value = 100;
            worksheet.cells.get("C4").value = 150;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Setting chart data source as the range "A1:C4"
            chart.chartDataRange = { range: "A1:C4", isSeriesInRows: true };

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **チャート作成のための注意事項**

チャートを作成する前に、Aspose.Cellsを使ってチャートを作成する際に役立つ基本的な概念を理解しておくことが重要です。

#### **チャートオブジェクト**

以下にチャートオブジェクトを一覧します：

- シリーズ、チャート内の単一のデータシリーズ。
- 軸、チャートの軸。
- Chart, 単一のExcelグラフ。
- ChartArea, ワークシート内のグラフエリア。
- ChartDataTable, グラフデータテーブル。
- ChartFrame, グラフ内のフレームオブジェクト。
- ChartPoint, グラフ内のシリーズの単一のポイント。
- ChartPointCollection, 1つのシリーズ内のすべてのポイントを含むコレクション。
- Charts, Chartオブジェクトのコレクション。
- DataLabels, 指定されたシリーズのすべてのDataLabelオブジェクトのコレクション。
- FillFormat, シェイプの塗りつぶし形式。
- Floor, 3Dグラフの床。
- Legend, グラフの凡例。
- Line, グラフの線。
- SeriesCollection, Seriesオブジェクトのコレクション。
- TickLabels, グラフ軸の目盛りのラベル。
- Title, グラフまたは軸のタイトル。
- Trendline, グラフ内のトレンドライン。
- TrendlineCollection, 指定されたデータシリーズのすべてのTrendlineオブジェクトのコレクション。
- Walls, 3Dグラフの壁。

#### **Chartingオブジェクトの使用**

上記のように、すべてのチャートオブジェクトはそれぞれのクラスのインスタンスであり、特定のタスクを実行するための特定のプロパティとメソッドを提供します。チャートオブジェクトを使用して、チャートを作成します。

[**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--)コレクションを使用してワークシートに任意のタイプのチャートを追加します。[**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--)コレクション内の各アイテムは[**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)オブジェクトを表します。[**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)オブジェクトは、チャートの外観をカスタマイズするために必要なすべての他のチャートオブジェクトをカプセル化しています。次のセクションでは、基本的なチャートオブジェクトを使用してシンプルなチャートを作成する方法を示します。

### **Aspose.Cellsを使用したチャートの作成**



1. [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/)オブジェクトの[**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-)メソッドを使用して、ワークシートのセルにデータを追加します。
   これはグラフのデータソースとして使用されます。
2. [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)コレクションの[**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-)メソッドを呼び出してワークシートにチャートを追加し、その操作を[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/)オブジェクトにカプセル化します。
3. [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)列挙型を使用してチャートの種類を指定します。
   例えば、以下の例では[**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype)値をチャートタイプとして使用しています。
4. [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)コレクションから新しい[**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)オブジェクトにインデックスを渡してアクセスします。
5. [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)オブジェクトにカプセル化された任意のチャートオブジェクトを使用してチャートを管理します。
   以下の例では、[**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/)チャートオブジェクトを使用してチャートのデータソースを指定します。

チャートにソースデータを追加する際、データソースはセル範囲（例：「A1:C3」）や連続しないセルのシーケンス（例：「A1, A3, A5」）、値のシーケンス（例：「1,2,3」）のいずれかです。

これらの一般的な手順を使用すると、任意のタイプのチャートを作成できます。異なるチャートオブジェクトを使用して、異なるチャートを作成します。

Aspose.Cellsでさまざまな種類のチャートを作成することが可能です。Aspose.Cellsでサポートされているすべての標準チャートは、[**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)という名前の列挙型で事前定義されています。

事前定義されたチャートの種類は:

|**チャートの種類**|**説明**|
| :- | :- |
|Column| クラスタ化された列チャートを表します。
|ColumnStacked| 積み上げ列チャートを表します。
|Column100PercentStacked| 100% 積み上げ列チャートを表します。
|Column3DClustered| 3D クラスタ化された列チャートを表します。
|Column3DStacked| 3D 積み上げ列チャートを表します。
|Column3D100PercentStacked| 3D 100% 積み上げ列チャートを表します。
|Column3D| 3D 列チャートを表します。
|Bar| クラスタ化された棒チャートを表します。
|BarStacked| 積み上げ棒チャートを表します。
|Bar100PercentStacked| 100% 積み上げ棒チャートを表します。
|Bar3DClustered| 3D クラスタ化された棒チャートを表します。
|Bar3DStacked| 3D 積み上げ棒チャートを表します。
|Bar3D100PercentStacked| 3D 100% 積み上げ棒チャートを表します。
|Line| 折れ線チャートを表します。
|LineStacked| 積み上げ折れ線チャートを表します。
|Line100PercentStacked| 100% 積み上げ折れ線チャートを表します。
|LineWithDataMarkers| データマーカー付きの折れ線チャートを表します。
|LineStackedWithDataMarkers| データマーカー付きの積み上げ折れ線チャートを表します。
|Line100PercentStackedWithDataMarkers| データマーカー付きの100% 積み上げ折れ線チャートを表します。
|Line3D| 3D 折れ線チャートを表します。
|Pie| 円グラフを表します。
|Pie3D| 3D 円グラフを表します。
|PiePie| パイ オブ パイ チャートを表します。
|PieExploded| 分解された円グラフを表します。
|Pie3DExploded| 3Dエクスプロード円グラフを表します|
|PieBar| パイチャートのバーを表します|
|Scatter| 散布図を表します|
|ScatterConnectedByCurvesWithDataMarker| データマーカー付きの曲線で接続された散布図を表します|
|ScatterConnectedByCurvesWithoutDataMarker| データマーカーなしの曲線で接続された散布図を表します|
|ScatterConnectedByLinesWithDataMarker| データマーカー付きの線で接続された散布図を表します|
|ScatterConnectedByLinesWithoutDataMarker| データマーカーなしの線で接続された散布図を表します|
|Area| エリアチャートを表します|
|AreaStacked| 積み上げエリアチャートを表します|
|Area100PercentStacked| 100% 積み上げエリアチャートを表します|
|Area3D| 3Dエリアチャートを表します|
|Area3DStacked| 3D積み上げエリアチャートを表します|
|Area3D100PercentStacked| 3D 100% 積み上げエリアチャートを表します|
|Doughnut| ドーナツチャートを表します|
|DoughnutExploded| 分裂したドーナツチャートを表します|
|Radar| レーダーチャートを表します|
|RadarWithDataMarkers| データマーカー付きのレーダーチャートを表します|
|RadarFilled| 塗りつぶしのレーダーチャートを表します|
|Surface3D| 3Dサーフェスチャートを表します|
|SurfaceWireframe3D| ワイヤーフレーム3Dサーフェスチャートを表します|
|SurfaceContour| 等高線チャートを表します|
|SurfaceContourWireframe| ワイヤーフレーム等高線チャートを表します|
|Bubble| バブルチャートを表します|
|Bubble3D| 3Dバブルチャートを表します|
|Cylinder| シリンダーチャートを表します|
|CylinderStacked| 積み上げシリンダーチャートを表します|
|Cylinder100PercentStacked| 100% 積み上げシリンダーチャートを表します|
|CylindericalBar| 円柱形バーチャートを表します|
|CylindericalBarStacked| 積み上げ円柱形バーチャートを表します|
|CylindericalBar100PercentStacked| 100% 積み上げ円柱形バーチャートを表します|
|CylindericalColumn3D| 3D円柱チャートを表します
|Cone| 円錐チャートを表します
|ConeStacked| 積み重ね円錐チャートを表します
|Cone100PercentStacked| 100% 積み重ね円錐チャートを表します
|ConicalBar| 円錐バーチャートを表します
|ConicalBarStacked 積み重ね円錐バーチャートを表します
|ConicalBar100PercentStacked| 100% 積み重ね円錐バーチャートを表します
|ConicalColumn3D| 3D円錐柱チャートを表します
|Pyramid| ピラミッドチャートを表します
|PyramidStacked| 積み重ねピラミッドチャートを表します
|Pyramid100PercentStacked| 100% 積み重ねピラミッドチャートを表します
|PyramidBar| ピラミッドバーチャートを表します
|PyramidBarStacked| 積み重ねピラミッドバーチャートを表します
|PyramidBar100PercentStacked| 100% 積み重ねピラミッドバーチャートを表します
|PyramidColumn3D| 3Dピラミッド柱チャートを表します

{{% alert color="primary" %}}

セルの範囲をデータソースとして割り当てると、左上から右下までの範囲を設定できます。例えば、"A1:C3"は有効ですが、"C3:A1"は無効です。

{{% /alert %}}

#### **ピラミッドチャート**

例のコードを実行すると、ワークシートにピラミッドチャートが追加されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Chart and Download</h1>
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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **折れ線グラフ**

上記の例では、[**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)を*Line*に変更するだけでラインチャートが作成されます。完全なソースは以下に示します。コードを実行すると、ワークシートにラインチャートが追加されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Chart</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **バブルチャート**

バブルチャートを作成するには、[**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)を[**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype)に設定し、BubbleSizes、Values、XValuesなどいくつかの追加プロパティを適切に設定する必要があります。次のコードを実行すると、ワークシートにバブルチャートが追加されます。

#### **データマーカー付きラインチャート**

データマーカー付きラインチャートを作成するには、[**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)を*ChartType.LineWithDataMarkers*に設定し、背景エリア、Series Markers、Values、XValuesなどいくつかの追加プロパティを適切に設定する必要があります。以下のコードを実行すると、データマーカー付きのラインチャートがワークシートに追加されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Line With Data Marker Chart</title>
    </head>
    <body>
        <h1>Line With Data Marker Chart Example</h1>
        <p>You may optionally select an existing Excel file to modify, or leave empty to create a new workbook.</p>
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
            if (fileInput.files.length === 0) {
                // Proceed with a new workbook if no file selected
            }

            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set columns title 
            worksheet.cells.get(0, 0).putValue("X");
            worksheet.cells.get(0, 1).putValue("Y");

            // Random data shall be used for generating the chart
            // Create random data and save in the cells
            for (let i = 1; i < 21; i++) {
                worksheet.cells.get(i, 0).putValue(i);
                worksheet.cells.get(i, 1).putValue(0.8);
            }

            for (let i = 21; i < 41; i++) {
                worksheet.cells.get(i, 0).putValue(i - 20);
                worksheet.cells.get(i, 1).putValue(0.9);
            }

            // Add a chart to the worksheet
            const idx = worksheet.charts.add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

            // Access the newly created chart
            const chart = worksheet.charts.get(idx);

            // Set chart style
            chart.style = 3;

            // Set autoscaling value to true
            chart.autoScaling = true;

            // Set foreground color white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set Properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set Properties of categoryaxis title
            chart.categoryAxis.title.text = "Units";

            //Set Properties of nseries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set IsColorVaried to true for varied points color
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers
            const series2 = chart.nSeries.get(s2_idx);
            series2.area.formatting = AsposeCells.FormattingType.Custom;
            series2.marker.area.foregroundColor = AsposeCells.Color.Yellow;
            series2.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series2.xValues = "A2:A21";
            series2.values = "B2:B21";

            // Set properties of background area and series markers for series3
            const series3 = chart.nSeries.get(s3_idx);
            series3.area.formatting = AsposeCells.FormattingType.Custom;
            series3.marker.area.foregroundColor = AsposeCells.Color.Green;
            series3.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series3.xValues = "A22:A41";
            series3.values = "B22:B41";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'LineWithDataMarkerChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [Excel 2016のチャートの読み込みと操作](/cells/ja/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [Excelチャートの軸の管理](/cells/ja/javascript-cpp/chart-axes/)
- [グラフの外観設定](/cells/ja/javascript-cpp/setting-chart-appearance/)
- [チャートタイプ](/cells/ja/javascript-cpp/chart-types/)
- [チャートのカスタマイズ](/cells/ja/javascript-cpp/customizing-charts/)
- [チャートのデータソースを設定する](/cells/ja/javascript-cpp/data-formatting-in-charts/)
- [Excelチャートのデータラベルの管理](/cells/ja/javascript-cpp/insert-datalabels-to-chart/)
- [チャートのワークシートを取得する](/cells/ja/javascript-cpp/get-worksheet-of-the-chart/)
- [Excelチャートの凡例の管理](/cells/ja/javascript-cpp/chart-legend/)
- [チャートの位置、サイズ、デザインの操作](/cells/ja/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [リーダーライン付き円グラフの作成](/cells/ja/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [グラフ内の図形](/cells/ja/javascript-cpp/controls-in-charts/)
- [Excelグラフのタイトルの管理](/cells/ja/javascript-cpp/chart-and-axis-titles/)
- [グラフのレンダリング](/cells/ja/javascript-cpp/chart-rendering/)
- [グラフトレンドラインの方程式テキストを取得](/cells/ja/javascript-cpp/get-equation-text-of-chart-trendline/)
