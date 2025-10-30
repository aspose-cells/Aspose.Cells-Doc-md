---
title: JavaScriptを使用してC++で列の幅をemやパーセントのようなスケーラブルな単位に設定します。
linktitle: 列幅をemやパーセントのようなスケーラブルユニットに設定します
type: docs
weight: 130
url: /ja/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aspose.Cells for JavaScriptを使用してC++で生成されたHTMLテーブルのプレゼンテーションを改善するために、列の幅をemやパーセントに設定する方法を学習します。
---

スプレッドシートからHTMLファイルを生成するのは非常に一般的です。列のサイズは「pt」で定義され、多くの場合で機能します。ただし、この固定サイズが不要な場合もあります。たとえば、コンテナパネルの幅が600pxの場合、そのHTMLページが表示される場所では、生成されたテーブルの幅が大きいと横スクロールバーが出る場合があります。この固定サイズをemやパーセントのようなスケーラブルユニットに変更して、より良いプレゼンテーションを実現する必要があります。以下のサンプルコードでは、[**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--)を**true**に設定することでスケーラブルな幅の作成が可能です。

サンプルのソースファイルと出力ファイルは以下のリンクからダウンロードできます：

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
