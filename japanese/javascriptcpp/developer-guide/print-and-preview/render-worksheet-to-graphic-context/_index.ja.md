---
title: JavaScriptをC++経由でワークシートをグラフィックコンテキストにレンダリングする
linktitle: グラフィックコンテキストにワークシートをレンダリングする
type: docs
weight: 300
url: /ja/javascript-cpp/render-worksheet-to-graphic-context/
description: Aspose.Cells for JavaScriptをC++で使用して、ワークシートを画像ファイル、スクリーン、プリンタにレンダリングする方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、ワークシートをグラフィックコンテキストにレンダリングする機能を備えています。グラフィックコンテキストは画像ファイル、画面、プリンタなど何でも構いません。以下のいずれかの方法を使用してワークシートをグラフィックコンテキストにレンダリングしてください。

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

以下のコードは、Aspose.Cellsを使用してワークシートをグラフィックコンテキストにレンダリングする方法を示しています。コードを実行すると、ワークシート全体が出力され、残りの空きスペースは青色で塗りつぶされ、画像は**OutputImage_out_.png**として保存されます。任意のExcelファイルを使用して試すことができます。コード内のコメントも参照してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Worksheet to Image</title>
    </head>
    <body>
        <h1>Render Worksheet to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, Utils } = AsposeCells;

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

            // Create empty image buffer options
            const bmpOptions = new ImageOrPrintOptions();
            bmpOptions.onePagePerSheet = true;

            // Render worksheet to image
            const sheetRender = new SheetRender(worksheet, bmpOptions);
            const imageData = sheetRender.toImage(0);

            // Create blob and provide download link for PNG
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputImage_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to download the PNG.</p>';
        });
    </script>
</html>
```
