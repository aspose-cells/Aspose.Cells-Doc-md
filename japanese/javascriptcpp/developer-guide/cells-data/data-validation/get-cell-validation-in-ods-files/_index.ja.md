---
title: ODSファイルでのセル検証の取得
type: docs
weight: 180
url: /ja/javascript-cpp/get-cell-validation-in-ods-files/
description: ODSファイル内のセルバリデーションを取得する方法について、C++ APIを使用したAspose.Cells for JavaScriptで学びます。
keywords: C++経由のセル検証JavaScriptを取得、C++経由のセル検証JavaScriptを取得
---

## **ODS ファイルでのセル検証を取得**  

C++経由のAspose.Cells for JavaScriptを使用すると、ODSファイルのセルに適用された検証を取得できます。これには、APIが[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/)クラスの[**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--)プロパティを提供します。  

以下のコードサンプルは、[ソースODS](101089354.ods)ファイルを読み込み、セルA9の検証を取得することで[**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--)プロパティの使用例を示しています。  

### **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```
