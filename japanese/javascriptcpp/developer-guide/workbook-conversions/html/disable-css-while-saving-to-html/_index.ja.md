---
title: CSSを無効にしてJavaScript経由のC++でHTMLに保存します。
linktitle: HTMLに保存する際にCSSを無効にする
type: docs
weight: 320
url: /ja/javascript-cpp/disable-css-while-saving-to-html/
description: ExcelファイルをHTMLに保存する際にCSSを無効にする方法をAspose.Cells for JavaScriptを使用して学びます（C++）。 
---

## **可能な使用シナリオ**

ExcelファイルをシングルページHTMLに保存するとき、通常CSS要素はHTMLファイル内に埋め込まれやすく、HEADセクションに位置します。このファイルをコンテンツ/本文としてメールに添付すると、多くのメールクライアントによってCSS要素が除去され、不適切な表示となる場合があります。Aspose.Cellsのバージョン24.12では、CSSをオプションで無効にできる機能が導入されており、スタイルをHTML要素内に直接適用できるようになっています。メールの本文としてHTMLを設定したい場合は、[**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--)プロパティを使用し、**true**に設定してください。

## **HTML保存時にCSSを無効にする**

次のサンプルコードは、[**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) プロパティの使用例を示しています。 

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
