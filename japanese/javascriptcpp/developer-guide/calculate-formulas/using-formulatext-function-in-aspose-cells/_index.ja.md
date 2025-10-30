---
title: C++経由のFormulaText関数を使用して
linktitle: Aspose.CellsでのFormulaText関数の使用
description: この記事では、Aspose.Cellsライブラリを使用してMicrosoft Excelの数式を処理するためのFormulaText関数の使い方を紹介します。セルの数式テキストを取得・設定し、編集後のExcelファイルを保存する方法をJavaScript経由のC++で学びます。
keywords: Aspose.Cells、Excel、FormulaText関数 JavaScript経由のC++
type: docs
weight: 60
url: /ja/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaTextはExcel 2013以降の関数です。以前のバージョン（Excel 2010や2007など）ではサポートされていません。その名前が示す通り、指定されたセル内に存在する数式のテキストを出力します。この関数の使用方法について、C++経由のAspose.Cells for JavaScriptを使った例を紹介します。

{{% /alert %}} 

次のサンプルコードは、C++経由のAspose.Cells for JavaScriptを使用したFormulaTextの利用例です。まずセルA1に数式を書き込み、その後セルA2でFormulaTextを使って数式のテキストを出力します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2, It will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```
## **コンソール出力**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
