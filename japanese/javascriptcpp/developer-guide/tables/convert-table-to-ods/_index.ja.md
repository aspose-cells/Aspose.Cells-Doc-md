---
title: C++経由のJavaScriptを使用してテーブルをODSに変換
linktitle: テーブルをODSに変換
type: docs
weight: 70
url: /ja/javascript-cpp/convert-table-to-ods/
description: Aspose.Cells for JavaScriptを使用して、テーブル付きのExcelファイルをODS形式に変換する方法を学びます。
---

Aspose.Cellsは、テーブルを含むExcelファイルをODSファイルに変換することをサポートしています。ファイルをODS形式で保存すると、機能するテーブルを持つODSファイルが生成されます。

## サンプルコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Table to ODS Example</title>
    </head>
    <body>
        <h1>Convert Table to ODS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Opening the Excel file from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the file to ODS format and providing download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertTableToOds_out.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the ODS file.</p>';
        });
    </script>
</html>
```

サンプルコードによって生成された出力ODSファイルが添付されています。

[**Output ODS File**](ConvertTableToOds_out.ods)
