---
title: JavaScript経由のC++を使用して、ワークシート内のテーブルまたはリストオブジェクトのコメントを設定
linktitle: ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください
type: docs
weight: 40
url: /ja/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Aspose.Cells for JavaScriptを使用して、ワークシート内のテーブルまたはリストオブジェクトのコメントを設定する方法を学びます。 
---

{{% alert color="primary" %}}

Worksheet内のテーブルまたはリストオブジェクトのコメントは、[**ListObject.comment**](https://reference.aspose.com/cells/javascript-cpp/listobject/#comment--)プロパティを使用して設定できます。コメントはxl/tables/tableName.xmlファイル内に表示されます。

{{% /alert %}}

## **ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください**

以下のサンプルコードは、[ソースエクセルファイル](5115514.xlsx)を読み込み、ワークシート内の最初のテーブルまたはリストオブジェクトのコメントを設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Comment of Table/ListObject</title>
    </head>
    <body>
        <h1>Set Comment of Table/ListObject</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first list object or table.
            const lstObj = worksheet.listObjects.get(0);

            // Set the comment of the list object
            lstObj.comment = "This is Aspose.Cells comment.";

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetCommentOfTableOrListObject_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
