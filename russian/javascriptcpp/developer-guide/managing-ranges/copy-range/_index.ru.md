---
title: Копирование диапазонов Excel с помощью JavaScript через C++
linktitle: Копирование диапазонов
type: docs
weight: 105
url: /ru/javascript-cpp/copy-ranges-of-Excel/
---

## **Введение**

В Excel вы можете выбрать диапазон, скопировать его, а затем вставить его с определенными параметрами на ту же рабочую книгу, другие листы или другие файлы.

## **Копирование диапазонов с помощью Aspose.Cells for JavaScript через C++**

Aspose.Cells for JavaScript через C++ предоставляет несколько методов перегрузки [Range.copy(Range, PasteOptions)](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-pasteoptions-) для копирования диапазона. И [Range.copyStyle(Range)](https://reference.aspose.com/cells/javascript-cpp/range/#copyStyle-range-) копирует только стиль диапазона; [Range.copyData(Range)](https://reference.aspose.com/cells/javascript-cpp/range/#copyData-range-) копирует только значения диапазона.

## **Копировать диапазон**

Создайте два диапазона: исходный диапазон и целевой, затем скопируйте исходный диапазон в целевой с помощью метода `Range.copy`.

См. следующий код:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get all the worksheets in the book.
            let worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            let worksheet = workbook.worksheets.get(0);

            // Create a range of cells.
            let sourceRange = worksheet.cells.createRange("A1", "A2");

            // Input some data with some formattings into A few cells in the range.
            sourceRange.get(0, 0).value = "Test";
            sourceRange.get(1, 0).value = 123;

            // Create target range of cells.
            let targetRange = worksheet.cells.createRange("B1", "B2");

            // Copy source range to target range in the same worksheet 
            targetRange.copy(sourceRange);

            // Create target range of cells.
            workbook.worksheets.add();
            worksheet = workbook.worksheets.get(1);

            targetRange = worksheet.cells.createRange("A1", "A2");
            // Copy source range to target range in another worksheet 
            targetRange.copy(sourceRange);

            // Copy to another workbook
            const anotherWorkbook = new Workbook();

            worksheet = workbook.worksheets.get(0);

            targetRange = worksheet.cells.createRange("A1", "A2");
            // Copy source range to target range in another workbook 
            targetRange.copy(sourceRange);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```

## **Вставка диапазона с параметрами**

Aspose.Cells for JavaСкрипт через C++ поддерживает вставку диапазона с определёнными типами.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Paste Range Example</title>
    </head>
    <body>
        <h1>Paste Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteOptions, PasteType } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = workbook.worksheets.get(0);

            // Create a range of cells.
            const sourceRange = worksheet.cells.createRange("A1", "A2");

            // Input some data with some formattings into a few cells in the range.
            sourceRange.get(0, 0).value = "Test";
            sourceRange.get(1, 0).value = 123;

            // Create target range of cells.
            const targetRange = worksheet.cells.createRange("B1", "B2");

            // Init paste options.
            const options = new PasteOptions();
            // Set paste type.
            options.pasteType = PasteType.ValuesAndFormats;
            options.skipBlanks = true;

            // Copy source range to target range
            targetRange.copy(sourceRange, options);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Range copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Только копирование данных из диапазона**

Также вы можете скопировать данные с помощью метода `Range.copyData`, как показано в следующем примере:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Range Example</h1>
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

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = worksheets.get(0);

            // Create a range of cells.
            const sourceRange = worksheet.cells.createRange("A1", "A2");

            // Input some data with some formattings into a few cells in the range.
            sourceRange.get(0, 0).value = "Test";
            sourceRange.get(1, 0).value = 123;

            // Create target range of cells.
            const targetRange = worksheet.cells.createRange("B1", "B2");

            // Copy the data of source range to target range
            targetRange.copyData(sourceRange);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Range copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Копировать высоты строк исходного диапазона в целевой диапазон](/cells/ru/javascript-cpp/copy-row-heights-of-source-range-to-destination-range/)
