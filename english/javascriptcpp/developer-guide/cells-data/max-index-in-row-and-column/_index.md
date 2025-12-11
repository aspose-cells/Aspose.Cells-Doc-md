---
title: Get Max Column Index in Row and Max Row Index in Column
type: docs
weight: 600
url: /javascript-cpp/get-max-index-in-row-and-column/
description: Learn how to get the max column index in a row and the max row index in a column through the Aspose.Cells for JavaScript via C++ API.
keywords: Get Max Column Index in Row JavaScript via C++, Get Max Row Index in Column JavaScript via C++, Get Max Data Column Index in Row JavaScript via C++, Get Max Data Row Index in Column JavaScript via C++.
---

## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of rows and columns. Aspose.Cells for JavaScript via C++ offers this feature. To obtain the maximum column index on a row, you can obtain the [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--) and [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--) methods, and then use the [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) method to obtain the maximum column index and maximum data column index. But in order to obtain the maximum row index and maximum data row index on a column, you need to create a range on the column, then traverse the range to find the last cell, and finally call the [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) method on the cell.

Aspose.Cells for JavaScript via C++ provides the following properties and methods to help you achieve your goals.
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **Get Max Column Index in Row and Max Row Index in Column**
This example shows how to:

1. Load the [sample file](sample.xlsx).  
2. Get the row for which you need to obtain the maximum column index and maximum data column index.  
3. Call the [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) method on the cell.  
4. Create a range based on the column.  
5. Get an iterator and traverse the range.  
6. Call the [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) method on the cell.

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

            // Check the row at index 1
            const row = cells.checkRow(1);
            const outputLines = [];

            if (row != null) {
                // get maximum column index of row which contains data or style.
                outputLines.push("Max column index in row: " + row.lastCell.column);

                // get maximum column index of row which contains data.
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

            // Maximum row index of the column that contains data or style.
            outputLines.push("Max row index in Column: " + maxRow);

            // Maximum row index of the column that contains data.
            outputLines.push("Max data row index in Column: " + maxDataRow);

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```