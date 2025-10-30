---
title: ExcelをHTMLに変換  より良いレイアウトのためのPresentationPreferenceオプションをJavaScript経由のC++で使用します。
linktitle: ExcelをHTMLに変換する際、PresentationPreferenceオプションを使用してレイアウトを向上させる
type: docs
weight: 220
url: /ja/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、Microsoft ExcelファイルをHTMLまたはMHT形式に保存するときに見た目を改善するためのHtmlSaveOptions.presentationPreferenceプロパティを提供しています。デフォルトはfalseです。より魅力的なプレゼンテーションを得るために、このプロパティをtrueに設定することを推奨します。

{{% /alert %}} 

プレゼンテーションプリファレンスオンでExcelレポートからHTMLファイルをレンダリングする方法のサンプルコードを以下に示します。



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Excel to HTML with Presentation Preference</h1>
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

            // Instantiate the Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions object
            const options = new HtmlSaveOptions();
            // Set the Presentation preference option (converted from setPresentationPreference)
            options.presentationPreference = true;

            // Save the Excel file to HTML with specified option
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPresentationlayout1.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
