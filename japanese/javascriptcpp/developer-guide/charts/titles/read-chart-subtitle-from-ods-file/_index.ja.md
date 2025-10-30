---
title: ODSファイルからチャートのサブタイトルをJavaScriptをC++経由で読み取る方法
linktitle: ODSファイルからチャートサブタイトルを読む
description: C++を使ったAspose.Cells for JavaScriptを使用して、OpenDocumentスプレッドシート（ODS）ファイルからチャートのサブタイトルを読み取る方法を学びます。ガイドでは、チャートのサブタイトルを抽出し、アクセスして、さらなる分析や表示を行う方法を示します。
keywords: Aspose.Cells for JavaScript、C++でのチャートサブタイトルの読み取り、OpenDocumentスプレッドシート、ODSファイル、チャート抽出、データ分析。
type: docs
weight: 160
url: /ja/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **ODSファイルからチャートサブタイトルを読む**

Aspose.Cellsは、[**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) プロパティを使用してODSファイルのチャートサブタイトルを読み取る機能を提供します。以下のサンプルコードは、[サンプルODSファイル](89620481.ods)を読み込み、[**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) プロパティを使用してチャートサブタイトルを取得し、コンソールウィンドウに出力します。以下のコードのコンソール出力例もご参照ください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **コンソール出力**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
