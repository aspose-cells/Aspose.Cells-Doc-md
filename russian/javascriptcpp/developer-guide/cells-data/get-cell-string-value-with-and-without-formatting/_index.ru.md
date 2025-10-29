---
title: Получить строковое значение ячейки с или без форматирования
type: docs
weight: 240
url: /ru/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: Узнайте, как получить строковое значение ячейки с форматированием и без него через Aspose.Cells for JavaScript через C++ API.
keywords: Получить строковое значение ячейки с форматированием и без него через C++, Получить строковое значение ячейки с форматированием и без него через JavaScript через C++, Получить строковое значение ячейки с форматированием и без него через C++
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет свойство [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--), которое можно использовать для получения строкового значения ячейки с или без форматирования. Предположим, у вас есть ячейка со значением 0.012345 и вы отформатировали ее так, чтобы отображать только две десятичные. Тогда в Excel она будет отображаться как 0.01. Вы можете получать строковые значения как 0.01, так и 0.012345, используя свойство [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--). Оно принимает в качестве параметра перечисление [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) со следующими значениями.

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Следующий пример кода иллюстрирует использование свойства [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--).

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
