---
title: JavaScript経由でC++を使用してワークシートの重複行を削除する
linktitle: ワークシート内の重複行を削除する
type: docs
weight: 370
url: /ja/javascript-cpp/remove-duplicate-rows-in-a-worksheet/
description: C++を使用してAspose.Cells for JavaScriptでワークシートの重複行を削除し、重複チェック用の特定の列を選択する方法を学びます。
---

重複行の削除は、Microsoft Excelの多くの便利な機能の一つです。これにより、ワークシート内の重複行を削除でき、重複情報を検出する列を選択できます。

Aspose.Cells for JavaScriptは、これを目的とした`Cells.removeDuplicates()`メソッドを提供します。`startRow`、`startColumn`、`endRow`、および`endColumn`を設定して、重複を確認する列の範囲を指定することもできます。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[removeduplicates.xlsx](removeduplicates.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Duplicates Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Remove Duplicate (converted getters to properties)
            book.worksheets.get(0).cells.removeDuplicates(0, 0, 5, 3);

            // Save result and provide download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'removeduplicates-result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            resultDiv.innerHTML = '<p style="color: green;">Duplicates removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
