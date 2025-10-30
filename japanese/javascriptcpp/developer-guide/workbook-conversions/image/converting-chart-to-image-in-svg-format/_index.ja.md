---
title: C++経由のJavaScriptでチャートをSVG形式の画像に変換する方法を学びます。
linktitle: SVG形式でチャートを画像に変換
type: docs
weight: 240
url: /ja/javascript-cpp/converting-chart-to-image-in-svg-format/
description: チャートをviewBox属性付きのSVG形式にエクスポートする方法を学びます。
---

{{% alert color="primary" %}}

スケーラブル・ベクター・グラフィックス（SVG）は、二次元グラフィックス用のXMLベースのベクター画像形式であり、対話性やアニメーションもサポートしています。SVG仕様は、1999年以来世界広範囲のウェブ consortium（W3C） によって開発されたオープンスタンダードです。

SVG画像とその動作はXMLテキストファイルで定義されています。これにより、検索、索引付け、スクリプト作成、圧縮が可能です。SVG画像はXMLファイルとして任意のテキストエディタで作成および編集できますが、一般的には図形作成ソフトウェアで作成されます。

Aspose.Cellsは、チャートをBMP、JPEG、PNG、GIF、SVGなどさまざまなフォーマットの画像として保存できます。この記事では、チャートをSVG形式に保存する方法を説明します。

{{% /alert %}}

次のサンプルコードは、Aspose.Cellsを使用してチャートをSVG形式の画像に変換する方法について説明しています。このコードは、ソースとなるMicrosoft Excelファイルを読み込み、次に最初のワークシートで見つかった最初のチャートをSVG形式で保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Chart to SVG</title>
    </head>
    <body>
        <h1>Export First Chart to SVG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType } = AsposeCells;

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

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Set image or print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Svg;

            // Export the chart to SVG format (returns image bytes)
            const imageData = chart.toImage(opts);

            // Create downloadable SVG blob
            const blob = new Blob([imageData], { type: 'image/svg+xml' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to SVG. Click the download link to download the SVG file.</p>';
        });
    </script>
</html>
```
