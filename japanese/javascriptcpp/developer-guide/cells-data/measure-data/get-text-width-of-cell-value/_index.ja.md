---
title: セル値のテキスト幅を取得する
type: docs
weight: 50
url: /ja/javascript-cpp/get-text-width-of-cell-value/
description: C++ APIを通じてAspose.Cells for JavaScriptを使用してセルの値のテキスト幅を取得する方法を学びます。
keywords: C++を通じてJavaScriptでセルの値のテキスト幅を取得する方法、またはC++を通じてJavaScriptでセルの値のテキスト幅を取得する方法
---

## **セル値のテキスト幅を取得する**

時には、開発者はデータの配置のためにセルの値の幅を計算する必要があります。Aspose.Cells for JavaScriptをC++で使用すると、[**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-)メソッドを利用してセルの値のテキスト幅を取得できます。以下のサンプルコードは、[**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-)を使ってセルの値のテキスト幅にアクセスする方法を示しています。

以下のコードスニペットで使用されるソースファイルは参照用に添付されています。

[ソースファイル](96928090.xlsx)

## サンプルコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Text Width Example</title>
    </head>
    <body>
        <h1>Get Text Width Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and A1 cell
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Accessing default font style
            const font = workbook.defaultStyle.font;

            // Calculating text width using CellsHelper (converted getter name to property)
            const textWidth = AsposeCells.CellsHelper.textWidth(cell.stringValue, font, 1);

            resultDiv.innerHTML = `<p style="color: green;">Text width: ${textWidth}</p>`;
        });
    </script>
</html>
```
