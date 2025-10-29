---
title: Получить примененную валидацию для ячейки
type: docs
weight: 200
url: /ru/javascript-cpp/get-validation-applied-on-a-cell/
description: Эта статья показывает, как применять проверку к ячейке с помощью JavaScript через C++.
keywords: применять проверку ячейки в Excel с помощью JavaScript через C++, применять проверку к ячейке в Excel с помощью JavaScript через C++, применять проверку в Excel с помощью JavaScript через C++, проверка ячейки в Excel с помощью JavaScript через C++, JavaScript через C++ применяет проверку ячейки в Excel, JavaScript через C++ применяет проверку к ячейке в Excel, проверка ячейки в Excel с помощью JavaScript через C++
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells for JavaScript через C++, чтобы получить проверку, примененную к ячейке. Aspose.Cells предоставляет метод [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) для этой цели. Если на ячейке не применяется проверка, он возвращает null.

Точно так же можно использовать метод [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-), чтобы получить примененную валидацию для ячейки, указав её индексы строки и столбца.

{{% /alert %}}

## JavaScript-код для получения проверки, примененной к ячейке

Следующий пример показывает, как получить проверку, примененную к ячейке.

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


## Связанные статьи

- [Валидация данных](/cells/ru/javascript-cpp/data-validation/)
