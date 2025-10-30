---
title: JavaScript経由でチャートシリーズの値の書式コードを設定する方法 (C++)
description: C++を使用してAspose.Cells for Javaスクリプトでチャートシリーズの値の書式コードを設定する方法を学びます。このガイドでは、適切な書式コードを用いたデータのフォーマット方法を理解し、正確かつプロフェッショナルにデータを提示できるようになります。
keywords: Aspose.Cells for Javaスクリプト、C++、チャートシリーズ、値の書式コード、フォーマット、データ表示、正確性、プロフェッショナリズム。
linktitle: 数値形式
type: docs
weight: 100
url: /ja/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **可能な使用シナリオ**
[Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) プロパティを使用して、チャートシリーズの値の書式コードを設定できます。このプロパティは、ワークシート内の範囲に基づくシリーズだけでなく、値の配列を用いて作成されたシリーズにも有効です。

## **チャートシリーズの値の形式コードを設定する**
以下のサンプルコードは、以前にシリーズがなかった空のチャートにシリーズを追加し、値の配列を使用します。シリーズを追加したら、[Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) プロパティを使って `$#,##0` のコードで書式設定し、数字の 10000 を `$10,000` に変えます。スクリーンショットは、コードの効果を示しており、実行後の [サンプルExcelファイル](51740712.xlsx) と [出力Excelファイル](51740713.xlsx) を示しています。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
