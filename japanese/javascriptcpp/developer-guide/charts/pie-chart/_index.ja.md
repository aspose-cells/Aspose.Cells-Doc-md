---
title: JavaScriptをC++経由で使用してリーダーライン付きの円グラフを作成
description: C++経由のAspose.Cells for JavaScriptを使用してMicrosoft Excelでリーダーライン付きの円グラフを作成する方法を学びます。データポイントと凡例をつなぐリーダーラインを追加し、チャートの明確さを向上させる方法を示します。
keywords: C++経由のAspose.Cells for JavaScript、円グラフ、リーダーライン、Microsoft Excel、データビジュアリゼーション、チャートのカスタマイズ。
linktitle: 円グラフ
type: docs
weight: 45
url: /ja/javascript-cpp/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

この記事では、C++ APIのAspose.Cells for JavaScriptを使用してリーダーライン付きの円グラフをゼロから作成する方法を解説します。Excelでは、「リーダーラインを表示」オプションがデフォルトで設定されているため、Excelで円グラフを作成するとリーダーラインが表示されます。ただし、Aspose.Cells APIを使用して同様のグラフを作成する場合、明示的にプロパティ [**Series.hasLeaderLines**](https://reference.aspose.com/cells/javascript-cpp/series/#hasLeaderLines--) を設定する必要があります。

{{% /alert %}}

C++ API を使用して Aspose.Cells for JavaScript の使い方を示し、リーダーライン付きの円グラフを作成します。まず、新しい [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) を作成し、シリーズデータソースとして役立つデータを入力します。データが準備できたら、コレクションに [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart)（種類 [**ChartType.Pie**](https://reference.aspose.com/cells/javascript-cpp/charttype)）のチャートを追加し、そのさまざまな側面を設定して希望のチャートビューを得ます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Pie Chart Example</title>
    </head>
    <body>
        <h1>Create Pie Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LabelPositionType, DataLabelsSeparatorType } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add two columns of data
            worksheet.cells.get("A1").putValue("Retail");
            worksheet.cells.get("A2").putValue("Services");
            worksheet.cells.get("A3").putValue("Info & Communication");
            worksheet.cells.get("A4").putValue("Transport Equip");
            worksheet.cells.get("A5").putValue("Construction");
            worksheet.cells.get("A6").putValue("Other Products");
            worksheet.cells.get("A7").putValue("Wholesale");
            worksheet.cells.get("A8").putValue("Land Transport");
            worksheet.cells.get("A9").putValue("Air Transport");
            worksheet.cells.get("A10").putValue("Electric Appliances");
            worksheet.cells.get("A11").putValue("Securities");
            worksheet.cells.get("A12").putValue("Textiles & Apparel");
            worksheet.cells.get("A13").putValue("Machinery");
            worksheet.cells.get("A14").putValue("Metal Products");
            worksheet.cells.get("A15").putValue("Cash");
            worksheet.cells.get("A16").putValue("Banks");

            worksheet.cells.get("B1").putValue(10.4);
            worksheet.cells.get("B2").putValue(5.2);
            worksheet.cells.get("B3").putValue(6.4);
            worksheet.cells.get("B4").putValue(10.4);
            worksheet.cells.get("B5").putValue(7.9);
            worksheet.cells.get("B6").putValue(4.1);
            worksheet.cells.get("B7").putValue(3.5);
            worksheet.cells.get("B8").putValue(5.7);
            worksheet.cells.get("B9").putValue(3);
            worksheet.cells.get("B10").putValue(14.7);
            worksheet.cells.get("B11").putValue(3.6);
            worksheet.cells.get("B12").putValue(2.8);
            worksheet.cells.get("B13").putValue(7.8);
            worksheet.cells.get("B14").putValue(2.4);
            worksheet.cells.get("B15").putValue(1.8);
            worksheet.cells.get("B16").putValue(10.1);

            // Create a pie chart and add it to the collection of charts
            const id = worksheet.charts.add(ChartType.Pie, 3, 3, 23, 13);

            // Access newly created Chart instance
            const chart = worksheet.charts.get(id);

            // Set series data range
            chart.nSeries.add("B1:B16", true);

            // Set category data range
            chart.nSeries.categoryData = "A1:A16";

            // Turn off legend
            chart.showLegend = false;

            // Access data labels
            const dataLabels = chart.nSeries.get(0).dataLabels;

            // Turn on category names
            dataLabels.showCategoryName = true;

            // Turn on percentage format
            dataLabels.showPercentage = true;

            // Set position
            dataLabels.position = LabelPositionType.OutsideEnd;

            // Set separator
            dataLabels.separatorType = DataLabelsSeparatorType.Comma;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

これまでに円グラフを作成し、異なる側面を設定しました。これからは、チャートのリーダーラインをオンにします。リーダーラインを表示するには、データラベルを少し移動する必要があります。

次のコードは、リーダーラインをオンにし、チャートを更新し、それからデータラベルの位置を計算して適切に移動します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pie Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pie Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LabelPositionType, DataLabelsSeparatorType } = AsposeCells;

        const initPromise = AsposeCells.onReady({
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

            await initPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            const cells = worksheet.cells;

            // Add two columns of data
            cells.get("A1").value = "Retail";
            cells.get("A2").value = "Services";
            cells.get("A3").value = "Info & Communication";
            cells.get("A4").value = "Transport Equip";
            cells.get("A5").value = "Construction";
            cells.get("A6").value = "Other Products";
            cells.get("A7").value = "Wholesale";
            cells.get("A8").value = "Land Transport";
            cells.get("A9").value = "Air Transport";
            cells.get("A10").value = "Electric Appliances";
            cells.get("A11").value = "Securities";
            cells.get("A12").value = "Textiles & Apparel";
            cells.get("A13").value = "Machinery";
            cells.get("A14").value = "Metal Products";
            cells.get("A15").value = "Cash";
            cells.get("A16").value = "Banks";

            cells.get("B1").value = 10.4;
            cells.get("B2").value = 5.2;
            cells.get("B3").value = 6.4;
            cells.get("B4").value = 10.4;
            cells.get("B5").value = 7.9;
            cells.get("B6").value = 4.1;
            cells.get("B7").value = 3.5;
            cells.get("B8").value = 5.7;
            cells.get("B9").value = 3;
            cells.get("B10").value = 14.7;
            cells.get("B11").value = 3.6;
            cells.get("B12").value = 2.8;
            cells.get("B13").value = 7.8;
            cells.get("B14").value = 2.4;
            cells.get("B15").value = 1.8;
            cells.get("B16").value = 10.1;

            // Create a pie chart and add it to the collection of charts
            const id = worksheet.charts.add(ChartType.Pie, 3, 3, 23, 13);

            // Access newly created Chart instance
            const chart = worksheet.charts.get(id);

            // Set series data range
            chart.nSeries.add("B1:B16", true);

            // Set category data range
            chart.nSeries.categoryData = "A1:A16";

            // Turn off legend
            chart.showLegend = false;

            // Access data labels
            const dataLabels = chart.nSeries.get(0).dataLabels;

            // Turn on category names
            dataLabels.showCategoryName = true;

            // Turn on percentage format
            dataLabels.showPercentage = true;

            // Set position
            dataLabels.position = LabelPositionType.OutsideEnd;

            // Set separator
            dataLabels.separatorType = DataLabelsSeparatorType.Comma;

            // Turn on leader lines
            chart.nSeries.get(0).hasLeaderLines = true;

            // Calculate chart
            chart.calculate();

            // You need to move DataLabels a little leftward or rightward depending on their position to show leader lines
            const DELTA = 100;
            const series0 = chart.nSeries.get(0);
            for (let i = 0; i < series0.points.count; i++) {
                const pt = series0.points.get(i);
                let X = pt.dataLabels.x;
                // If it is greater than 2000, then move the X position a little right otherwise move the X position a little left
                if (X > 2000)
                    pt.dataLabels.x = X + DELTA;
                else
                    pt.dataLabels.x = X - DELTA;
            }

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

最後に、次のコードでチャートを画像形式で保存し、ワークブックをXLSX形式で保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pie Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none; margin-right: 10px;">Download Excel File</a>
        <a id="downloadImageLink" style="display: none;">Download Chart Image</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // If a file is provided, load it. Otherwise create a new workbook in XLSX format.
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook(AsposeCells.FileFormatType.Xlsx);
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add two columns of data
            worksheet.cells.get("A1").putValue("Retail");
            worksheet.cells.get("A2").putValue("Services");
            worksheet.cells.get("A3").putValue("Info & Communication");
            worksheet.cells.get("A4").putValue("Transport Equip");
            worksheet.cells.get("A5").putValue("Construction");
            worksheet.cells.get("A6").putValue("Other Products");
            worksheet.cells.get("A7").putValue("Wholesale");
            worksheet.cells.get("A8").putValue("Land Transport");
            worksheet.cells.get("A9").putValue("Air Transport");
            worksheet.cells.get("A10").putValue("Electric Appliances");
            worksheet.cells.get("A11").putValue("Securities");
            worksheet.cells.get("A12").putValue("Textiles & Apparel");
            worksheet.cells.get("A13").putValue("Machinery");
            worksheet.cells.get("A14").putValue("Metal Products");
            worksheet.cells.get("A15").putValue("Cash");
            worksheet.cells.get("A16").putValue("Banks");

            worksheet.cells.get("B1").putValue(10.4);
            worksheet.cells.get("B2").putValue(5.2);
            worksheet.cells.get("B3").putValue(6.4);
            worksheet.cells.get("B4").putValue(10.4);
            worksheet.cells.get("B5").putValue(7.9);
            worksheet.cells.get("B6").putValue(4.1);
            worksheet.cells.get("B7").putValue(3.5);
            worksheet.cells.get("B8").putValue(5.7);
            worksheet.cells.get("B9").putValue(3);
            worksheet.cells.get("B10").putValue(14.7);
            worksheet.cells.get("B11").putValue(3.6);
            worksheet.cells.get("B12").putValue(2.8);
            worksheet.cells.get("B13").putValue(7.8);
            worksheet.cells.get("B14").putValue(2.4);
            worksheet.cells.get("B15").putValue(1.8);
            worksheet.cells.get("B16").putValue(10.1);

            // Create a pie chart and add it to the collection of charts
            const id = worksheet.charts.add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

            // Access newly created Chart instance
            const chart = worksheet.charts.get(id);

            // Set series data range
            chart.nSeries.add("B1:B16", true);

            // Set category data range
            chart.nSeries.categoryData = "A1:A16";

            // Turn off legend
            chart.showLegend = false;

            // Access data labels
            const dataLabels = chart.nSeries.get(0).dataLabels;

            // Turn on category names
            dataLabels.showCategoryName = true;

            // Turn on percentage format
            dataLabels.showPercentage = true;

            // Set position
            dataLabels.position = AsposeCells.LabelPositionType.OutsideEnd;

            // Set separator
            dataLabels.separatorType = AsposeCells.DataLabelsSeparatorType.Comma;

            // In order to save the chart image, create an instance of ImageOrPrintOptions
            const anOption = new AsposeCells.ImageOrPrintOptions();

            // Set image format
            anOption.imageType = AsposeCells.ImageType.Png;

            // Set resolution
            anOption.horizontalResolution = 200;
            anOption.verticalResolution = 200;

            // Render chart to image (returns image byte array in browser)
            const imageData = chart.toImage(anOption);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            const downloadImageLink = document.getElementById('downloadImageLink');
            downloadImageLink.href = URL.createObjectURL(imageBlob);
            downloadImageLink.download = 'output_out.png';
            downloadImageLink.style.display = 'inline-block';
            downloadImageLink.textContent = 'Download Chart Image';

            // Save the workbook to see chart inside the Excel
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart created and files are ready. Click the download links to get the results.</p>';
        });
    </script>
</html>
```

|**作成された円グラフ**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高度なトピック**
- [円グラフでのカスタムスライスまたはセクターの色](/cells/ja/javascript-cpp/custom-slice-or-sector-colors-in-pie-chart/)
- [パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける](/cells/ja/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 関連記事

- [チャートの作成](/cells/ja/javascript-cpp/creating-charts/)
- [チャートのカスタマイズ](/cells/ja/javascript-cpp/customizing-charts/)
- [グラフのデータ整形](/cells/ja/javascript-cpp/data-formatting-in-charts/)
- [グラフの外観設定](/cells/ja/javascript-cpp/setting-chart-appearance/)
