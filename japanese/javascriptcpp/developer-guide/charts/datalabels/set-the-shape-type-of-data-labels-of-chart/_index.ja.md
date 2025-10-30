---
title: JavaScriptを使ったチャートのデータラベルのシェイプタイプ設定（C++経由）
linktitle: チャートのデータラベルのシェイプタイプを設定する
description: Aspose.Cells for JavaScriptを使ってチャートのデータラベルのシェイプタイプを設定する方法を学びます。このガイドでは、利用可能なさまざまなシェイプタイプを説明し、プレゼンテーションと使いやすさを向上させるために適切なシェイプを選択する方法を示します。
keywords: Aspose.Cells for JavaScriptを使ったチャートのデータラベルのセル範囲表示（C++経由）
type: docs
weight: 110
url: /ja/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **可能な使用シナリオ**
`DataLabels.shapeType`プロパティを使用してチャートのデータラベルのシェイプタイプを変更できます。これは`DataLabelShapeType`列挙型の値を取り、データラベルのシェイプタイプを適宜変更します。その値の一部は

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **チャートのデータラベルの形状タイプを設定する**
以下のサンプルコードは、チャートのデータラベルのシェイプタイプを`DataLabelShapeType.WedgeEllipseCallout`に変更します。コードで使用されたサンプルExcelファイル（60489778.xlsx）と、それによって生成された出力Excelファイル（60489779.xlsx）をご覧ください。スクリーンショットは、このコードの効果を示すサンプルExcelファイルの様子です。

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
