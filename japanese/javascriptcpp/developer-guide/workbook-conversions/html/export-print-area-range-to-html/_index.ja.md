---
title: 印刷範囲をHTMLにエクスポート JavaScript経由のC++
linktitle: HTMLに印刷エリア範囲をエクスポートする
type: docs
weight: 60
url: /ja/javascript-cpp/export-print-area-range-to/
---

## **可能な使用シナリオ**

印刷範囲、つまり選択したセル範囲のみをHTMLにエクスポートする必要がある一般的な場面です。この機能はすでにPDFレンダリングには利用可能ですが、今度はHTMLでも行えます。まず、ワークシートのページ設定オブジェクトに印刷範囲を設定し、その後、[**HtmlSaveOptions.exportPrintAreaOnly()**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportPrintAreaOnly--)フラグを使用して選択範囲だけをエクスポートします。

## サンプルコード

次のサンプルコードはワークブックをロードし、プリントエリアをHTMLにエクスポートします。この機能のテスト用にサンプルファイルを以下のリンクからダウンロードできます。

[sampleInlineCharts.xlsx](79527946.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Print Area to HTML Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the print area.
            worksheet.pageSetup.printArea = "D2:M20";

            // Initialize HtmlSaveOptions
            const options = new AsposeCells.HtmlSaveOptions();

            // Set flag to export print area only
            options.exportPrintAreaOnly = true;

            // Save to HTML format (options specify HTML)
            const outputData = workbook.save(options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputInlineCharts.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
