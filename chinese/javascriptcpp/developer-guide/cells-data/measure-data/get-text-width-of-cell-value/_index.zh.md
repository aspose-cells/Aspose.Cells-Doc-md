---
title: 获取单元值的文本宽度
type: docs
weight: 50
url: /zh/javascript-cpp/get-text-width-of-cell-value/
description: 了解如何通过Aspose.Cells for JavaScript在C++ API中获取单元格值的文本宽度。
keywords: 通过C++获取单元格值的文本宽度JavaScript，获取单元格值的文本宽度JavaScript via C++
---

## **获取单元值的文本宽度**

有时，开发者可能需要计算单元格值的宽度，用于排版布局。Aspose.Cells for JavaScript通过C++提供[**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-)方法，允许开发者获取单元格值的文本宽度。以下示例代码演示如何使用[**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-)访问单元格值的文本宽度。

以下代码片段中使用的源文件，请参考附件。

[源文件](96928090.xlsx)

## 示例代码

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
