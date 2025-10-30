---
title: JavaScriptをC++経由でページ設定の縮尺係数を計算
linktitle: ページ設定スケーリングファクターを計算します
type: docs
weight: 300
url: /ja/javascript-cpp/calculate-page-setup-scaling-factor/
description: この記事では、C++経由でJavaScript APIを使用してExcelワークシートのページ設定の縮尺係数を、自動的に幅nページ、高さmページにフィットさせるオプションを使ってプログラム的に計算するサンプルコードを提供します。
keywords: Excelの幅nページ高さmページにフィットさせるJavaScriptをC++で利用し、ページ設定の縮尺係数を計算
---

{{% alert color="primary" %}}

**Fit to n page(s) wide by m tall**オプションを利用したページ設定の拡大縮小率は、Microsoft Excelが計算します。同じ値は[**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--)プロパティを使用して取得できます。このプロパティはパーセンテージに変換可能な倍精度浮動小数点値を返します。例：0.5なら拡大縮小率は50%。

{{% /alert %}}

次のサンプルコードは、[**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--) プロパティを使用してページ設定のスケーリングファクターを計算する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Scale</title>
    </head>
    <body>
        <h1>Page Scale Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetRender, ImageOrPrintOptions, PaperSizeType, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some data in these cells
            worksheet.cells.get("A4").putValue("Test");
            worksheet.cells.get("S4").putValue("Test");

            // Set paper size
            worksheet.pageSetup.paperSize = PaperSizeType.PaperA4;

            // Set fit to pages wide as 1
            worksheet.pageSetup.fitToPagesWide = 1;

            // Calculate page scale via sheet render
            const sr = new SheetRender(worksheet, new ImageOrPrintOptions());

            // Convert page scale double value to percentage
            const strPageScale = (sr.pageScale * 100).toFixed(0) + "%";

            // Write the page scale value
            document.getElementById('result').innerHTML = `<p>Page Scale: ${strPageScale}</p>`;
            console.log(strPageScale);
        });
    </script>
</html>
```
