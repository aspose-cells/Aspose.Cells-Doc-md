---
title: 行内の最大列インデックスと列内の最大行インデックスの取得
type: docs
weight: 600
url: /ja/javascript-cpp/get-max-index-in-row-and-column/
description: C++を通じてAspose.Cells for JavaScriptを使い、行の最大列インデックスと列の最大行インデックスを取得する方法を学びます。
keywords: C++を使用したJavaScriptでの行の最大列インデックス取得、C++を使用したJavaScriptでの列の最大行インデックス取得、C++を使用したJavaScriptでの行の最大データ列インデックス取得、C++を使用したJavaScriptでの列の最大データ行インデックス取得。
---

## **可能な使用シナリオ**
行や列の一部のデータだけを操作する必要がある場合、行列のデータ範囲を知る必要があります。C++を通じてAspose.Cells for JavaScriptはこの機能を提供します。特定の行の最大列インデックスを取得するには、[**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)と[**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)メソッドを使用し、その後、[**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)メソッドを使って最大列インデックスと最大データ列インデックスを取得します。ただし、列の最大行インデックスと最大行データインデックスを取得するには、列範囲を作成し、その範囲を走査して最後のセルを見つけ、最終的にそのセルに対して[**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)メソッドを呼び出します。

C++を通じてAspose.Cells for JavaScriptは、あなたの目的達成を助ける以下のプロパティとメソッドを提供します。
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **行の最大列インデックスと列の最大行インデックスを取得**
この例では、次のことができます:

1. [サンプルファイル](sample.xlsx)をロードする。
1. 最大列インデックスと最大データ列インデックスを取得する行を取得します。
1. セルの[**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)メソッドを呼び出します。
1. 列に基づいて範囲を作成します。
1. イテレータを取得して範囲をトラバースします。
1. セルの[**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)メソッドを呼び出します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result pre { background: #f4f4f4; padding: 10px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
        </style>
    </head>
    <body>
        <h1>Get Max Row/Column Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Accessing cells collection
            const cells = sheet.cells;

            // Check row at index 1
            const row = cells.checkRow(1);
            const outputLines = [];

            if (row != null) {
                // get Maximum column index of Row which contains data or style.
                outputLines.push("Max column index in row: " + row.lastCell.column);

                // get Maximum column index of Row which contains data.
                outputLines.push("Max data column index in row: " + row.lastDataCell.column);
            } else {
                outputLines.push("Row 1 is empty (checkRow returned null).");
            }

            // create the range of column B (index 1)
            const columnRange = cells.createRange(1, 1, true);

            var max_row_index  = cells.maxRow + 1;
            var maxRow = 0;
            var maxDataRow = 0;

            for (let row_index = 0; row_index < max_row_index; row_index++) {
                var curr_cell = cells.get(row_index, 1);

                if (curr_cell) {
                    if (curr_cell.stringValue) {
                        maxDataRow = curr_cell.row;
                    }

                    if (curr_cell.stringValue || curr_cell.hasCustomStyle) {
                        maxRow = curr_cell.row;
                    }
                }
            }

            // Maximum row index of Column which contains data or style.
            outputLines.push("Max row index in Column: " + maxRow);

            // Maximum row index of Column which contains data.
            outputLines.push("Max data row index in Column: " + maxDataRow);

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```
