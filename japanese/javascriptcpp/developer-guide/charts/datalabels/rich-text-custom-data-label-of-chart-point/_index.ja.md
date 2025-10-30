---
title: JavaScriptを使ったチャートポイントのリッチテキストカスタムデータラベル（C++経由）
description: Aspose.Cells for JavaScriptを使ったチャートポイントへのリッチテキストカスタムデータラベルの追加方法を学びます。このガイドでは、異なるフォント、色、配置オプションでラベルのフォーマットを行い、チャートの外観と読みやすさを向上させる方法を紹介します。
keywords: Aspose.Cells for JavaScriptを使ったチャート作成、リッチテキスト、カスタムデータラベル、フォント、色、配置、外観、読みやすさへの影響。
type: docs
weight: 10
url: /ja/javascript-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してチャートポイントのリッチテキストカスタムデータラベルを作成できます。Aspose.Cellsは[**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#characters-number-number-)メソッドを提供し、これによりテキストの色や太字などのフォントプロパティを設定できる[**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)オブジェクトを返します。

{{% /alert %}}

## チャートポイントのリッチテキストカスタムデータラベル

以下のコードは最初の系列の最初のチャートポイントにアクセスし、そのテキストを設定し、最初の10文字のフォントを赤色に設定し、太字にします。

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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = worksheet.charts.get(0);

            // Access the data label of first series first point
            const dlbls = chart.nSeries.get(0).points.get(0).dataLabels;

            // Set data label text
            dlbls.text = "Rich Text Label";

            // Set the font setting of the first 10 characters
            const fntSetting = dlbls.characters(0, 10);
            const font = fntSetting.font;
            font.color = AsposeCells.Color.Red;
            font.isBold = true;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
