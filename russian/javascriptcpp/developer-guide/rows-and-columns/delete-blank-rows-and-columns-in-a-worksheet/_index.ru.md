---
title: Удаление пустых строк и столбцов в листе с помощью JavaScript через C++
linktitle: Удаление пустых строк и столбцов в листе
type: docs
weight: 300
url: /ru/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Узнайте, как удалять все пустые строки и столбцы в листе, используя Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Возможно удалить все пустые строки и столбцы из листа. Это полезно, например, при генерации PDF-файла из файла Microsoft Excel и желании преобразовать только строки и столбцы, содержащие данные или связанные объекты.

Используйте следующие методы Aspose.Cells для удаления пустых строк и столбцов:

1. Для удаления пустых строк используйте метод [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankRows--). Обратите внимание, для удаляемых пустых строк требуется, чтобы [**Row.isBlank()**](https://reference.aspose.com/cells/javascript-cpp/row/#isBlank--) был равен true, а также не должно быть видимых комментариев для любой ячейки в этих строках, и не должно быть сводной таблицы, диапазон которой пересекается с ними.
2. Для удаления пустых столбцов используйте метод [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankColumns--).

{{% /alert %}}

## JavaScript код для удаления пустых строк

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Delete Blank Rows Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;

            // Get first worksheet
            const sheet = sheets.get(0);

            // Delete blank rows from the worksheet
            sheet.cells.deleteBlankRows();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Blank rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## JavaScript код для удаления пустых столбцов

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Blank Columns Example</title>
    </head>
    <body>
        <h1>Delete Blank Columns Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = workbook.worksheets;

            // Get first Worksheet from WorksheetCollection
            const sheet = sheets.get(0);

            // Delete the Blank Columns from the worksheet
            sheet.cells.deleteBlankColumns();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Blank columns deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
