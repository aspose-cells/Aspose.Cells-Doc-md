---
title: JavaScriptを介してC++でチャートのトレンドラインの方程式テキストを取得する
description: Microsoft Excelで作成されたチャートのトレンドラインの方程式テキストを取得する方法を学びます。ガイドでは、トレンドラインの方程式にアクセスし、抽出する方法を示します。
keywords: Aspose.Cells for JavaスクリプトをC++経由で使用したチャートのトレンドライン、方程式テキスト、Microsoft Excel、データ分析、表示。
linktitle: トレンドライン
type: docs
weight: 110
url: /ja/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

 Aspose.Cells for JavaスクリプトをC++で使用してチャートのトレンドラインの方程式テキストを取得できます。Aspose.Cellsは[**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--)プロパティを提供し、グラフのトレンドラインの方程式テキストを返します。このプロパティを使用するには、まず[**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--)メソッドを呼び出す必要があります。

{{% /alert %}}

以下のスクリーンショットは、トレンドライン付きのチャートと、その式テキストが赤色で表示されたものです。この式テキストは、以下のサンプルコードの [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) プロパティを使用して取得します。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## チャートのトレンドラインの方程式テキストを取得するJavaScriptコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

## サンプルコードによって生成された出力

これは上記のサンプルコードのコンソール出力です。

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
