---
title: ExcelファイルをHTMLに保存する際にコメントをエクスポートします JavaScript経由のC++
linktitle: Excel ファイルを HTML に保存する際にコメントをエクスポート
type: docs
weight: 40
url: /ja/javascript-cpp/export-comments-while-saving-excel-file-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際、コメントはエクスポートされません。ただし、Aspose.Cells for JavaScript via C++は、[**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/javascript-cpp/export-comments-while-saving-excel-file-to/)プロパティを使用してこの機能を提供します。これを **true** に設定すると、HTMLにもExcelファイル内のコメントが表示されます。

## **ExcelファイルをHTMLに保存する際にコメントをエクスポート**

次のサンプルコードでは[**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/javascript-cpp/export-comments-while-saving-excel-file-to/)プロパティの使用方法を説明しています。コードによるHTMLへの影響を示すスクリーンショットが**true**として設定されている場合に表示されます。参照用に、[サンプルExcelファイル](50528260.xlsx)と[生成されたHTML](5052826.txt)をダウンロードしてください。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Comments to HTML</title>
    </head>
    <body>
        <h1>Export Comments to HTML Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HTML save options and set IsExportComments to true
            const opts = new HtmlSaveOptions();
            opts.isExportComments = true;

            // Save the workbook to HTML format with the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportCommentsHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
