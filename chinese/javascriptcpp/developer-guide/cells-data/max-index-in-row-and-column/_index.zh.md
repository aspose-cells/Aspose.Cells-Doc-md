---
title: 获取行中最大列索引和列中最大行索引
type: docs
weight: 600
url: /zh/javascript-cpp/get-max-index-in-row-and-column/
description: 学习如何通过C++ API在行中获取最大列索引，在列中获取最大行索引。
keywords: 通过C++使用JavaScript获取行中的最大列索引，通过JavaScript获取列中的最大行索引，通过JavaScript获取行中的最大数据列索引，通过JavaScript获取列中的最大数据行索引。
---

## **可能的使用场景**
当只需要操作行或列中的部分数据时，需要知道行和列的数据范围。Aspose.Cells for JavaScript通过C++提供此功能。获取行中的最大列索引，可以使用[**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)和[**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)方法，然后用[**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)方法获取最大列索引和最大数据列索引。但为了获取列中的最大行索引和最大行数据索引，需要在列上创建范围，然后遍历范围找到最后一个单元格，最后在该单元格上调用[**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)方法。

Aspose.Cells for JavaScript通过C++提供以下属性和方法帮助你实现目标。
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **获取行中的最大列索引和列中的最大行索引**
此示例演示如何：

1. 加载[示例文件](sample.xlsx)。
1. 获取需要获取最大列索引和最大数据列索引的行。
1. 调用单元格的[**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)方法。
1. 根据列创建一个范围。
1. 获取迭代器并遍历范围。
1. 调用单元格的[**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)方法。

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
