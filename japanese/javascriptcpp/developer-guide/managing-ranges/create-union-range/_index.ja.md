---
title: JavaScriptを通じて結合範囲を作成
linktitle: ユニオン範囲の作成
type: docs
weight: 360
url: /ja/javascript-cpp/create-union-range/
description: Aspose.Cells for JavaScriptを使ったユニオン範囲の作成方法を学びます。
keywords: JavaScriptを通じてユニオン範囲を作成し、Aspose.Cells JavaScriptを使ったユニオン範囲やワークシートコレクションによる作成例を示します。
---

## **ユニオン範囲の作成**
Aspose.Cellsは[WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-)メソッドを使用してユニオン範囲を作成する機能を提供します。このメソッドは二つのパラメータ、範囲のアドレスとワークシートのインデックスを受け取り、[UnionRange](https://reference.aspose.com/cells/javascript-cpp/unionrange)オブジェクトを返します。  

次のコードスニペットは、[WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-)メソッドを使用してユニオン範囲を作成する例を示しています。このコードで生成された出力ファイルは参照用に添付されています。  

- [出力ファイル](106364952.xlsx)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Union Range Example</title>
    </head>
    <body>
        <h1>Create Union Range Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create union range
            const unionRange = workbook.worksheets.createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

            // Put value "ABCD" in the range (converted setter to property)
            unionRange.value = "ABCD";

            // Save the output workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CreateUnionRange_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Union range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
