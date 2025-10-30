---
title: フレームスクリプトとドキュメントプロパティのエクスポートをJavaScript経由のC++で無効にします。
linktitle: フレームスクリプトとドキュメントプロパティのエクスポートを無効にする
type: docs
weight: 310
url: /ja/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/
description: ExcelワークブックをHTMLに変換する際にフレームスクリプトとドキュメントプロパティのエクスポートを無効にする方法をAspose.Cells for JavaScriptを使用して学びます（C++）。
--- 

{{% alert color="primary" %}}

Aspose.CellsはワークブックをHTMLに変換する際にフレームスクリプトとドキュメントプロパティをエクスポートします。Aspose.Cells for JavaScriptのバージョン8.6.0では、これらのエクスポートを任意で無効にするオプションが導入されています。`HtmlSaveOptions.exportFrameScriptsAndProperties` プロパティを使用して無効にしてください。

{{% /alert %}}

## **フレームスクリプトとドキュメントプロパティのエクスポートを無効にする**

以下のサンプルコードを使用すると、フレームスクリプトとドキュメントプロパティのエクスポートを無効にできます。ワークブックをHTMLに変換すると、出力ファイルにフレームスクリプトとドキュメントプロパティは含まれません。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Disable exporting frame scripts and document properties
            const options = new HtmlSaveOptions();
            options.exportFrameScriptsAndProperties = false;

            // Save workbook as HTML
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
