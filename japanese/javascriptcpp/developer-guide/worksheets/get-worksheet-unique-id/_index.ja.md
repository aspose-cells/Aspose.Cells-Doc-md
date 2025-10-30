---
title: JavaScriptを使ったC++でワークシートの一意のIDを取得
linktitle: ワークシートの一意のIDを取得
type: docs
weight: 190
url: /ja/javascript-cpp/get-worksheet-unique-id/
description: この記事では、JavaScriptライブラリとC++ APIを使ってExcelのワークシートの一意のIDをプログラム的に取得する方法を紹介します。
keywords: JavaScriptをC++で使用したExcelワークシートの一意のID取得、C++でJavaScriptを使用したワークシートの一意のID
---

## **ワークシートの一意のIDを取得**

Aspose.Cells for JavaScriptをC++で使用して、[**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--)プロパティを利用してワークシートの一意のIDを取得できます。以下のコードスニペットは、[**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--)プロパティを用いてワークシートの一意のIDを表示する例です。なお、このサンプルには[サンプルエクセルファイル](105480213.xlsx)を使用しています。

### ソースコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Worksheet Unique Id Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Unique Id
            const uniqueId = worksheet.uniqueId;
            console.log("Unique Id: " + uniqueId);

            document.getElementById('result').innerHTML = '<p style="color: green;">Unique Id: ' + uniqueId + '</p>';
        });
    </script>
</html>
```
