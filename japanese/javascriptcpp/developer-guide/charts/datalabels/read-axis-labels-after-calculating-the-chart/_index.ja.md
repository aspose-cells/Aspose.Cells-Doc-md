---
title: JavaScriptを使用してC++経由でチャートの軸ラベルを計算後に読む方法
linktitle: チャートの計算後に軸ラベルを読む
description: Aspose.Cells for JavaScript via C++でチャートを計算した後の軸ラベルの読み取り方法を学びましょう。ガイドでは、軸ラベルのアクセスと取得方法、フォーマットや位置も紹介します。
keywords: Aspose.Cells for JavaScript、チャート、軸ラベル、計算、読み取り、アクセス、取得、フォーマット、位置、JavaScript via C++
type: docs
weight: 90
url: /ja/javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **可能な使用シナリオ**

チャートの値を計算した後、その軸ラベルを[**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--)メソッドを使用して読むことができます。この目的には、軸ラベルのリストを返す[**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--)プロパティを使用してください。

## **チャートを計算した後に軸ラベルを読み取る**

次のサンプルコードは、[サンプルExcelファイル](ReadAxisLabels.xlsx)を読み込み、最初のワークシートのチャートのカテゴリ軸ラベルを読み取ります。その後、軸ラベルの値をコンソールに出力します。参考のために、以下に示すサンプルコードのコンソール出力をご覧ください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **コンソール出力**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}
