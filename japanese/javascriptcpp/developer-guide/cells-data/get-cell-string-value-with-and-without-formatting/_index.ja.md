---
title: 書式設定ありおよびなしでセル文字列の値を取得
type: docs
weight: 240
url: /ja/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: C++ APIによるAspose.Cells for JavaScriptを使用したセルの文字列値の取得方法（フォーマットあり・なし）について学習してください。
keywords: JavaScript経由のC++でセルの文字列値を取得（フォーマットあり・なし）、JavaScript経由のC++でセルの文字列値を取得（フォーマットあり・なし）、C++経由のJavaScriptでセルの文字列値を取得（フォーマットあり・なし）
---

{{% alert color="primary" %}}

Aspose.Cellsは、セルの文字列値をフォーマットの有無にかかわらず取得できる[**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--)というプロパティを提供します。例えば、値が0.012345のセルをありのまま表示すると小数点以下2桁だけにフォーマットした場合、Excelには0.01と表示されます。[**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--)プロパティを使えば、0.01としても0.012345としても文字列値を取得できます。パラメータには以下の値を持つ[**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/)列挙体が渡されます。

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

以下のサンプルコードは、[**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--)プロパティの使用例を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Cell } = AsposeCells;

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
            // Creating a new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Put value inside the cell
            cell.putValue(0.012345);

            // Format the cell that it should display 0.01 instead of 0.012345
            const style = cell.style;
            style.number = 2;
            cell.style = style;

            // Get string value as Cell Style
            let value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML = `<p>Formatted string value: ${value}</p>`;

            // Get string value without any formatting
            value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML += `<p>Unformatted string value: ${value}</p>`;

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
