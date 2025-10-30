---
title: JavaScriptを使用してExcelをHTMLに変換し、ツールチップで完全なテキストを表示  
linktitle: ツールチップ付きでExcelをHTMLに変換する  
type: docs  
weight: 200  
url: /ja/javascript-cpp/convert-excel-to-html-with-tooltip/  
description: Aspose.Cells for JavaScriptを使用して、ExcelファイルをHTML形式に変換し、完全なテキスト表示のためにツールチップを追加する方法を学びましょう。  
---

## **ツールチップ付きでExcelをHTMLに変換する**

生成されたHTMLでテキストが切り取られる場合があり、ホバーイベント時に完全なテキストをツールチップとして表示したい場合があります。Aspose.Cells for JavaScriptでは、[**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--)プロパティを提供してこれをサポートしています。[**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--)プロパティを**true**に設定すると、完全なテキストがツールチップとしてHTMLに追加されます。

次の画像は、生成されたHTMLファイル内のツールチップを示しています。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

次のコードサンプルは、[源となるExcelファイル](98107416.xlsx)を読み込み、ツールチップ付きの[出力HTMLファイル](98107417.zip)を生成します。

サンプルコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Tooltip to HTML Example</title>
    </head>
    <body>
        <h1>Add Tooltip to HTML Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and enable tooltip text
            const options = new HtmlSaveOptions();
            options.addTooltipText = true;

            // Save workbook as HTML with the specified options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddTooltipToHtmlSample_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
