---
title: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце
type: docs
weight: 600
url: /ru/javascript-cpp/get-max-index-in-row-and-column/
description: Узнайте, как получить максимальный индекс столбца в строке и максимальный индекс строки в столбце через скрипт Aspose.Cells for Java на C++ API.
keywords: Получить максимальный индекс столбца в строке через JavaScript с помощью C++, получить максимальный индекс строки в столбце через JavaScript с помощью C++, получить максимальный индекс данных в строке через JavaScript с помощью C++, получить максимальный индекс данных в столбце через JavaScript с помощью C++.
---

## **Возможные сценарии использования**
Когда вам нужно лишь манипулировать некоторыми данными в строках или столбцах, необходимо знать диапазон данных строк и столбцов. Скрипт Aspose.Cells for Java на C++ предлагает эту функцию. Чтобы получить максимальный индекс столбца в строке, используйте методы [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--) и [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--), затем используйте метод [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) для получения максимального индекса столбца и максимального индекса данных в столбце. Но для получения максимального индекса строки и максимального индекса данных строки в столбце необходимо создать диапазон по столбцу, обходить диапазон, чтобы найти последнюю ячейку, и, наконец, вызвать метод [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) на ячейке.

Скрипт Aspose.Cells for Java на C++ предоставляет следующие свойства и методы, чтобы помочь вам достичь целей.
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **Получение максимального индекса столбца в строке и максимального индекса строки в столбце**
Этот пример показывает, как:

1. Загрузите [образец файла](sample.xlsx).
1. Получите строку, которая нуждается в получении максимального индекса столбца и максимального индекса данных столбца.
1. Вызовите метод [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) на ячейке.
1. Создайте диапазон на основе столбца.
1. Получите итератор и пройдите по диапазону.
1. Вызовите метод [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) на ячейке.

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
