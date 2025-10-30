---
title: HTMLをインポートする際に改行後の余分な空白を削除します（JavaScript経由のC++）。
linktitle: HTMLのインポート時に改行後の余分なスペースを削除する
type: docs
weight: 20
url: /ja/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aspose.Cells for JavaScriptを使用してHTMLをインポートする際に改行後の余分な空白を削除する方法を学びます（C++）。
---

{{% alert color="primary" %}}

[**HtmlLoadOptions.deleteRedundantSpaces**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#deleteRedundantSpaces--) プロパティを使用し、それを **true** に設定して、改行タグの後に来るすべての余分なスペースを削除してください。デフォルトではこのプロパティは **false** であり、余分なスペースは出力されるExcelファイルに保持されます。

{{% /alert %}}

## HTMLLoadOptions.deleteRedundantSpacesプロパティをfalseとtrueに設定した場合の効果

このプロパティを**false**と**true**に設定した効果を以下のスクリーンショットで示します。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTMLをインポートする際に改行後の余分なスペースを削除する効果

### プログラミングサンプル

以下のサンプルコードは、[**HtmlLoadOptions.deleteRedundantSpaces**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#deleteRedundantSpaces--)プロパティの使用例を示しています。出力結果を上記スクリーンショットのように得るには、**true**または**false**に設定してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Delete Redundant Spaces While Importing From HTML</title>
    </head>
    <body>
        <h1>Delete Redundant Spaces While Importing From HTML</h1>
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
            // Sample Html containing redundant spaces after <br> tag
            const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

            // Convert Html to byte array
            const encoder = new TextEncoder();
            const byteArray = encoder.encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.deleteRedundantSpaces = true;

            // Create workbook from stream with Html load options
            const stream = byteArray;
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Saving the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
