---
title: スタイル.Customプロパティを設定する際にカスタム番号書式をチェックする
linktitle: スタイル.Customプロパティを設定する際にカスタム番号書式をチェックする
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのJavaScriptライブラリで、スタイル設定時にカスタム数字書式の確認をサポートしています。この記事では、Aspose.Cellsライブラリを使用してカスタム数字書式を確認し、スタイルが正しいことを保証する方法を示します。
keywords: Aspose.Cells、JavaScriptライブラリ、スプレッドシート、スタイリング、カスタム数字書式、検証、バリデーション
type: docs
weight: 170
url: /ja/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **可能な使用シナリオ**

無効なカスタム数字書式を[**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)プロパティに設定すると、Aspose.Cells for Javaスクリプト（C++経由）は例外をスローしません。ただし、Aspose.Cellsに割り当てたカスタム数字書式が正しいかどうかを確認させたい場合は、[**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-)プロパティを**true**に設定してください。

## **Style.customプロパティを設定する際のカスタム番号書式の確認**

以下のサンプルコードは、無効なカスタム番号書式を[**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)に割り当てる例です。既に[**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-)プロパティを**true**に設定しているため、例外（例：無効な番号書式）をスローします。コード内のコメントを参照して、詳細なヘルプを得てください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
