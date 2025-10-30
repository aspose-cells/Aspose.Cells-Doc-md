---
title: セルに適用された検証を取得
type: docs
weight: 200
url: /ja/javascript-cpp/get-validation-applied-on-a-cell/
description: この記事では、C++経由のJavaScriptを使用してセルに検証を適用する方法を紹介します。
keywords: Excelにセル検証を適用する C++経由のJavaScript、Excelのセルに検証を適用するC++経由のJavaScript、C++経由のJavaScriptでExcelに検証を適用、C++経由のJavaScriptでExcelのセル検証を行う、JavaScriptでC++を使ったExcelのセル検証、C++経由のJavaScriptでExcelのセルに検証を適用、C++経由のJavaScriptでExcelのセルに検証を行う
---

{{% alert color="primary" %}}

C++経由のAspose.Cells for JavaScriptを使用してセルに適用された検証を取得できます。Aspose.Cellsはこれ用途のために[**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--)メソッドを提供します。セルに検証が適用されていない場合はnullを返します。

同様に、[**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-)メソッドを使用して、行と列のインデックスを指定してセルに適用された検証を取得できます。

{{% /alert %}}

## セルに適用された検証を取得するJavaScriptコード

以下のコード例は、検証をセルに取得する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Validation Properties Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook from the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Cell C1 has the Decimal Validation applied on it.
            const cell = worksheet.cells.get("C1");

            // Access the validation applied on this cell
            const validation = cell.validation;

            // Read various properties of the validation
            let output = '';
            output += '<p>Reading Properties of Validation</p>';
            output += '<hr />';
            output += `<p>Type: ${validation.type}</p>`;
            output += `<p>Operator: ${validation.operator}</p>`;
            output += `<p>Formula1: ${validation.formula1}</p>`;
            output += `<p>Formula2: ${validation.formula2}</p>`;
            output += `<p>Ignore blank: ${validation.ignoreBlank}</p>`;

            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```


## 関連記事

- [データの検証](/cells/ja/javascript-cpp/data-validation/)
