---
title: Загрузка и управление файлами Excel, OpenOffice, Json, Csv и Html
linktitle: Открытие файлов
type: docs
weight: 20
url: /ru/javascript-cpp/loading-saving-and-managing/
description: С Aspose.Cells легко создавать, открывать и управлять файлами Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, изображениями, Mht и XPS с помощью JavaScript через C++.
---

{{% alert color="primary" %}}

 С Aspose.Cells просто создавать, открывать и управлять файлами Excel, например извлекать данные или использовать дизайн-шаблон для ускорения процесса разработки.

{{% /alert %}}

## **Создание новой книги**
Следующий пример создает новую книгу с нуля.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Открытие и сохранение файла**
 С Aspose.Cells просто открывать, сохранять и управлять файлами Excel.

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Расширенные темы**
- [Различные способы открытия файлов](/cells/ru/javascript-cpp/different-ways-to-open-files/)
- [Фильтрация заданных имен при загрузке рабочей книги](/cells/ru/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [Фильтр объектов при загрузке книги или листа](/cells/ru/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Фильтрация типа данных при загрузке книги из файла шаблона](/cells/ru/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Получение предупреждений при загрузке файла Excel](/cells/ru/javascript-cpp/get-warnings-while-loading-excel-file/)
- [Загрузка исходного файла Excel без диаграмм](/cells/ru/javascript-cpp/load-source-excel-file-without-charts/)
- [Загрузка конкретных листов в книге](/cells/ru/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [Загружать книгу с указанным размером бумаги принтера](/cells/ru/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [Открытие файлов с различными форматами](/cells/ru/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [Открытие файлов с различными форматами](/cells/ru/javascript-cpp/opening-files-with-different-formats/)
- [Оптимизация использования памяти при работе с большими файлами с большими наборами данных](/cells/ru/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Чтение таблицы чисел, разработанной Apple Inc. с использованием Aspose.Cells](/cells/ru/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени](/cells/ru/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Использование API LightCells](/cells/ru/javascript-cpp/using-lightcells-api/)
- [Преобразовать CSV в JSON](/cells/ru/javascript-cpp/convert-csv-to-json/)
- [Преобразование Excel в JSON](/cells/ru/javascript-cpp/convert-excel-to-json/)
- [Преобразовать JSON в CSV](/cells/ru/javascript-cpp/convert-json-to-csv/)
- [Преобразовать JSON в Excel](/cells/ru/javascript-cpp/convert-json-to-excel/)
- [Преобразование Excel в Html](/cells/ru/javascript-cpp/convert-excel-to-html/)
