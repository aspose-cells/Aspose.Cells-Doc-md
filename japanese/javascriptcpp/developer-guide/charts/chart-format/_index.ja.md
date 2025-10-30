---
title: JavaScriptを使用したC++によるチャートの外観設定
description: C++経由のAspose.Cells for JavaScriptを使用して、チャートの外観を設定する方法を学びましょう。ガイドでは、チャートレイアウト、色、フォント、効果を変更して、望ましいビジュアルスタイルを実現し、ワークシートを改善する方法を示します。
keywords: C++経由のAspose.Cells for JavaScriptによるチャート、チャートの外観、レイアウト、色、フォント、効果、ワークシート。
linktitle: チャートの形式
type: docs
weight: 20
url: /ja/javascript-cpp/setting-chart-appearance/
---

## **グラフの外観設定**
チャートの作成方法では、Aspose.Cellsが提供するチャートの種類やオブジェクトについて簡単に紹介し、それらの作成方法について説明しました。この記事では、プロパティを設定してチャートの外観をカスタマイズする方法について説明します。

- チャートエリアの設定。
- チャートラインの設定。
- テーマの適用。
- チャートと軸のタイトルの設定。
- グリッド線の操作。

### **チャートエリアの設定**
チャートには異なる種類のエリアがあり、Aspose.Cellsは各エリアの外観を変更する柔軟性を提供します。開発者は、前景色、背景色、塗りつぶし形式などの異なる書式設定をエリアに適用して、その外観を変更できます。

以下の例では、チャートの異なる種類のエリアに異なる書式設定を適用しました。

- プロットエリア
- チャートエリア
- SeriesCollectionエリア
- SeriesCollection内の単一のポイントのエリア

以下のコードスニペットは、チャートエリアを設定する方法を示しています。

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
            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 60;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = new AsposeCells.Color(0, 0, 255);

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = new AsposeCells.Color(255, 255, 0);

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(255, 0, 0);

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = new AsposeCells.Color(0, 255, 255);

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **チャートラインの設定**
開発者は、[SeriesCollection](https://reference.aspose.com/cells/javascript-cpp/seriescollection/)のラインやデータマーカーにさまざまなスタイルを適用できます。以下のコードスニペットは、Aspose.Cells APIを使用してチャートの線を設定する方法を示しています。

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
            // Instantiating a Workbook object
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

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Applying a dotted line style on the lines of a SeriesCollection
            chart.nSeries.get(0).border.style = AsposeCells.LineType.Dot;

            // Applying a triangular marker style on the data markers of a SeriesCollection
            chart.nSeries.get(0).marker.markerStyle = AsposeCells.ChartMarkerType.Triangle;

            // Setting the weight of all lines in a SeriesCollection to medium
            chart.nSeries.get(1).border.weight = AsposeCells.WeightType.MediumLine;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Microsoft Excel 2007/2010のテーマをチャートに適用**
開発者は、以下の例のように、[SeriesCollection](https://reference.aspose.com/cells/javascript-cpp/seriescollection/)や他のチャートオブジェクトにMicrosoft Excelのテーマや色を適用できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Chart Series Fill Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FillType, ThemeColor, ThemeColorType } = AsposeCells;

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

            // Loads the workbook containing the chart
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the first chart in the sheet
            const chart = worksheet.charts.get(0);

            // Specify the FillFormat's type to Solid Fill of the first series
            const series = chart.nSeries.get(0);
            series.area.fillFormat.fillType = FillType.Solid;

            // Get the CellsColor of SolidFill
            const cc = series.area.fillFormat.solidFill.cellsColor;

            // Create a theme in Accent style
            cc.themeColor = new ThemeColor(ThemeColorType.Accent6, 0.6);

            // Apply the theme to the series
            series.area.fillFormat.solidFill.cellsColor = cc;

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart series fill updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **チャートや軸のタイトルの設定**
Microsoft Excelを使用して、チャートとその軸のタイトルをWYSIWYG環境で設定できます。Aspose.Cellsも、開発者が実行時にチャートとその軸のタイトルを設定できるようにします。すべてのチャートと軸には[Title](https://reference.aspose.com/cells/javascript-cpp/title/)プロパティがあり、これを使用してタイトルを設定できます。例を以下に示します。

次のコードスニペットは、チャートと軸にタイトルを設定する方法を示しています。

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
        const { Workbook, SaveFormat, ChartType, GradientStyleType, Color } = AsposeCells;

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
            // Creating a new Workbook object
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
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [Color.Lime, 1, GradientStyleType.Horizontal, 1];

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = Color.Blue;

            // Setting the title of category axis of the chart
            chart.categoryAxis.title.text = "Category";

            // Setting the title of value axis of the chart
            chart.valueAxis.title.text = "Value";

            // Saving the Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **主な目盛りの操作**
主な目盛りの外観をカスタマイズできます。目盛りを非表示にしたり表示したり、その色やその他の設定を定義できます。以下では、目盛りを非表示にする方法と色を変更する方法を説明します。

#### **メジャーグリッドラインの非表示**
開発者は、[Line](https://reference.aspose.com/cells/javascript-cpp/line/)オブジェクトの[isVisible()](https://reference.aspose.com/cells/javascript-cpp/line/#isVisible--)プロパティを**true**または**false**に設定して、主グリッドラインの表示・非表示を制御できます。

以下のコードスニペットは、メジャーグリッド線を非表示にする方法を示します。メジャーグリッド線を非表示にすると、その後追加される列グラフにはグリッド線が表示されません。

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

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Hiding the major gridlines of Category Axis
            chart.categoryAxis.majorGridLines.isVisible = false;

            // Hiding the major gridlines of Value Axis
            chart.valueAxis.majorGridLines.isVisible = false;

            // Saving the Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **メジャーグリッドラインの設定変更**
開発者は、メジャーグリッド線の可視性だけでなく、色などの他のプロパティも制御できます。

以下のコードスニペットは、メジャーグリッド線の色を変更する方法を示します。色を設定した後、グリッド線が変更された列グラフがワークシートに追加されます。

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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Creating a new Workbook object
                const workbook = new Workbook();

                // Adding a new worksheet to the Workbook object
                const sheetIndex = workbook.worksheets.add();

                // Obtaining the reference of the newly added worksheet by passing its sheet index
                const worksheet = workbook.worksheets.get(sheetIndex);

                // Adding sample values to cells
                worksheet.cells.get("A1").value = 50;
                worksheet.cells.get("A2").value = 100;
                worksheet.cells.get("A3").value = 150;
                worksheet.cells.get("B1").value = 60;
                worksheet.cells.get("B2").value = 32;
                worksheet.cells.get("B3").value = 50;

                // Adding a chart to the worksheet
                const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

                // Accessing the instance of the newly added chart
                const chart = worksheet.charts.get(chartIndex);

                // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
                chart.nSeries.add("A1:B3", true);

                // Setting the foreground color of the plot area
                chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

                // Setting the foreground color of the chart area
                chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

                // Setting the foreground color of the 1st SeriesCollection area
                chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

                // Setting the foreground color of the area of the 1st SeriesCollection point
                chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

                // Filling the area of the 2nd SeriesCollection with a gradient
                chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

                // Setting the color of Category Axis' major gridlines to silver
                chart.categoryAxis.majorGridLines.color = AsposeCells.Color.Silver;

                // Setting the color of Value Axis' major gridlines to red
                chart.valueAxis.majorGridLines.color = AsposeCells.Color.Red;

                // Saving the Excel file and creating download link
                const outputData = workbook.save(SaveFormat.Excel97To2003);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'book1.out.xls';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
            });
        });
    </script>
</html>
```

## **高度なトピック**
- [チャートシリーズの値の形式コードを設定する](/cells/ja/javascript-cpp/set-the-values-format-code-of-chart-series/)
- [グラフの背景に画像を設定する](/cells/ja/javascript-cpp/set-picture-as-background-fill-in-the-chart/)
