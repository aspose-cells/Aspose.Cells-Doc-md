---
title: HTMLからの大きな数値の指数表記を避ける
linktitle: HTMLからの大きな数値の指数表記を避ける
type: docs
weight: 10
url: /ja/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Aspose.Cells for JavaScriptを使用して、HTMLからインポートする際に大きな数字が指数表記に変換されるのを防ぐ方法を学びましょう。
--- 

{{% alert color="primary" %}}  

時々、あなたのHTMLには1234567890123456のような数字が含まれており、15桁を超えています。これらの数字をExcelファイルにインポートすると、1.23457E+15のような指数表記に変換されてしまいます。数字をそのままインポートし、指数表記に変換されないようにするには、[**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--)プロパティを使用し、読み込み時に**true**を設定してください。  

{{% /alert %}}  

以下のサンプルコードは、[**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--)プロパティの使用法を説明しています。APIは数字をそのままインポートし、指数表記に変換しません。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            // Sample Html containing large number with digits greater than 15
            const html = "<html><body><p>1234567890123456</p></body></html>";

            // Convert Html to byte array
            const byteArray = new TextEncoder().encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.keepPrecision = true;

            // Convert byte array into stream
            const stream = byteArray;

            // Create workbook from stream with Html load options
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAvoidExponentialNotationWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```
