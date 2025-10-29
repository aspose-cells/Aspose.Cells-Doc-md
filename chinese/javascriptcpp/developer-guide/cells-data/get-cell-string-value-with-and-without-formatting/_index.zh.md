---
title: 获取带格式和不带格式的单元格字符串值
type: docs
weight: 240
url: /zh/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: 学习如何通过 Aspose.Cells for JavaScript 通过 C++ API 获取带格式和不带格式的单元格字符串值。
keywords: 使用 C++ 通过 JavaScript 获取带格式和不带格式的单元格字符串值，检索不带格式的单元格字符串值，使用 C++ 和 JavaScript。
---

{{% alert color="primary" %}}

Aspose.Cells 提供了 [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) 属性，可用于获取带格式或不带格式的单元格字符串值。假设一个单元格的值为 0.012345，并已设置为只显示两位小数，则在 Excel 中会显示为 0.01。您可以通过 [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) 属性以 0.01 或 0.012345 形式检索字符串值。它接受 [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) 枚举，其值如下：

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

以下示例代码说明了 [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) 属性的用法。

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
