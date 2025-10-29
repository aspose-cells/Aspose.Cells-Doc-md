---
title: Удаление дублирующихся строк в листе с помощью JavaScript через C++
linktitle: Удаление дублирующихся строк в листе
type: docs
weight: 370
url: /ru/javascript-cpp/remove-duplicate-rows-in-a-worksheet/
description: Научитесь удалять дублирующиеся строки в листе с помощью Aspose.Cells for JavaScript через C++ и выбирайте конкретные столбцы для проверки дублей.
---

Удаление дублирующихся строк — одна из полезных функций Microsoft Excel. Она позволяет пользователям удалять повторяющиеся строки в рабочем листе, и вы можете выбрать, какие столбцы проверять на дублирование информации.

Aspose.Cells for JavaScript через C++ предоставляет метод `Cells.removeDuplicates()` для этой задачи. Также можно установить `startRow`, `startColumn`, `endRow` и `endColumn`, чтобы задать диапазон столбцов для проверки дублей.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[removeduplicates.xlsx](removeduplicates.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Duplicates Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Create workbook from uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Remove Duplicate (converted getters to properties)
            book.worksheets.get(0).cells.removeDuplicates(0, 0, 5, 3);

            // Save result and provide download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'removeduplicates-result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            resultDiv.innerHTML = '<p style="color: green;">Duplicates removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
