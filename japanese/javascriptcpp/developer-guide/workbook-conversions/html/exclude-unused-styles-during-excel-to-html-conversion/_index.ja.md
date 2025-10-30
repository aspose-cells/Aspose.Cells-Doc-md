---
title: 未使用のスタイルを除外してExcelをHTMLに変換します（JavaScript経由のC++）。
linktitle: Excel を HTML に変換する際に未使用のスタイルを除外
type: docs
weight: 30
url: /ja/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: 8.6.0版のAspose.Cells for JavaScriptを使用して、ExcelをHTMLに変換する際に未使用のスタイルを除外する方法を学びます（C++）。
---

## **可能な使用シナリオ**  

Microsoft Excelファイルには、多くの未使用スタイルが含まれることがあります。これらをHTMLにエクスポートすると、ファイルサイズが増加します。ExcelからHTMLへの変換時に未使用のスタイルを除外するには、[**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--)プロパティを使用します。**true**に設定すると、未使用のスタイルはすべて除外されます。以下のスクリーンショットは出力HTML内の未使用スタイルの例です。  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **ExcelからHTMLへの変換時に未使用のスタイルを除外**  

以下のサンプルコードでは、ワークブックを作成し、未使用の名前付きスタイルも作成しています。[**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--)が**true**に設定されているため、未使用の名前付きスタイルは[出力HTML](61767778.zip)にエクスポートされません。ただし、**false**に設定すると、未使用のスタイルがHTML内に保持され、上記スクリーンショットのようにHTMLマークアップ上で確認できます。  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Exclude Unused Styles</title>
    </head>
    <body>
        <h1>Exclude Unused Styles from Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            if (fileInput.files.length > 0 && fileInput.files[0].size === 0) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a valid Excel file.</p>';
                return;
            }

            // Instantiate workbook from selected file or create a new one
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Create an unused named style
            const style = wb.createStyle();
            style.name = "UnusedStyle_XXXXXXXXXXXXXX";

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some value in cell C7
            const cell = ws.cells.get("C7");
            cell.value = "This is sample text.";

            // Specify html save options, we want to exclude unused styles
            const opts = new HtmlSaveOptions();
            // Comment this line to include unused styles
            opts.excludeUnusedStyles = true;

            // Save the workbook in html format
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExcludeUnusedStylesInExcelToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML generated successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
