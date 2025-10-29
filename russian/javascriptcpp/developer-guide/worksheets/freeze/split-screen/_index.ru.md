---
title: Разделение экрана листа Excel с помощью JavaScript через C++
linktitle: Разделенный экран
type: docs
weight: 190
url: /ru/javascript-cpp/how-to-split-screen-of-excel-worksheet
description: В этой статье вы узнаете, как программно отображать определённые строки и/или столбцы в отдельных панелях, разделяя лист на две или четыре части с помощью JavaScript через дополнение C++.
keywords: Заморозить верхние строки, Заморозить верхнюю строку.
---

## **Введение**

В этой статье мы узнаем, как отображать определенные строки и/или столбцы в отдельных панелях с помощью разделения листа на две или четыре части. При работе с большими наборами данных нам нужно видеть несколько областей одного листа одновременно, чтобы сравнить разные подмножества данных. Функция разделения экрана поможет вам в этом.

## **Как разделить экран в Excel**
Чтобы разделить таблицу на две или четыре части, выполните следующее:

1. Выберите строку/столбец/ячейку до которой вы хотите разместить разбиение.
2. На вкладке Вид в группе Окна нажмите кнопку Разделить.

**![Разделить экран](Split-Screen.png)**

## **Разделить лист вертикально по столбцам**

Для разделения двух областей электронной таблицы вертикально выберите столбец справа от столбца, где вы хотите появление разделения, и нажмите кнопку Разделить в Excel.

Легко разделить лист на вертикальные панели по столбцам программно с помощью Aspose.Cells for JavaScript через C++, для этого нужно выбрать одну ячейку в верхней строке как активную и затем разделить с помощью метода [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets C1 cell in the top row as the active cell.
            sheet.activeCell = "C1";

            // Split worksheet vertically on columns
            sheet.split();

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Разделить лист горизонтально по строкам**
Чтобы разделить ваше окно Excel горизонтально, выберите строку ниже строки, где вы хотите, чтобы произошло разделение в Excel.

Легко разделить лист горизонтально по строкам программно с помощью Aspose.Cells for JavaScript через C++, достаточно выбрать одну ячейку в левом столбце как активную, а затем разделить с помощью метода [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--).

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
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Sets A6 cell in the left column as the active cell.
            sheet.activeCell = "A6";

            // Split worksheet horizontally on rows
            sheet.split();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Разделение листа на четыре части**
Чтобы просматривать одновременно четыре различных раздела одного листа, разделите экран как вертикально, так и горизонтально в Excel.

Легко разделить лист вертикально по столбцам программно с помощью Aspose.Cells for JavaScript через C++, нужно выбрать одну ячейку, не находящуюся в первой строке и столбце как активную, и затем разделить с помощью метода [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Active Cell and Split Worksheet Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets E6 cell as the active cell.
            sheet.activeCell = "E6";

            // Split worksheet into four parts
            sheet.split();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Как удалить разделение**
Чтобы удалить разделение листа, просто повторно нажмите кнопку Разделить.

Aspose.Cells for JavaScript через C++ предоставляет метод [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--) для удаления настроек разделения.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Worksheet Example</title>
    </head>
    <body>
        <h1>Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Remove split and then split worksheet into four parts
            sheet.removeSplit();
            sheet.split();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet split operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
