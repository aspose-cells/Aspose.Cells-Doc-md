---
title: Форматирование строк и столбцов с помощью JavaScript через C++
linktitle: Строки и столбцы
type: docs
weight: 100
url: /ru/javascript-cpp/adjusting-row-height-and-column-width/
description: Aspose.Cells for JavaScript через C++ может менять высоту строк или ширину столбцов, а также применять форматирование к строкам или столбцам.
keywords: Настройте высоту строки и ширину столбца, отрегулируйте высоту строки и ширину столбца, измените высоту строки или ширину столбца, форматируйте строки и столбцы, как установить высоту строки и ширину столбца.
---

{{% alert color="primary" %}}
При работе с электронными таблицами и добавлении данных в строки или столбцы, возможно, потребуется изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что текущая высота или ширина должны измениться для отображения данных. Обычно пользователи регулируют высоту строк и ширину столбцов в WYSIWYG-редакторе с помощью Microsoft Excel. Но с Aspose.Cells разработчики могут выполнять эти операции во время выполнения.
{{% /alert %}}

## **Работа со строками**

### **Как настроить высоту строки**

Aspose.Cells for JavaScript через C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), позволяющий получить доступ к каждому листу в Excel-файле. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells), которая представляет все ячейки листа.

Коллекция [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них рассмотрены далее более подробно.

### **Как установить высоту строки**

Можно установить высоту отдельной строки, вызвав метод [**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Метод [**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы изменяете.
- **Высота строки**, высота строки, применяемая к строке.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Row Height Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.rows.get(1).height = 13;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Как установить высоту всех строк на листе**

Если разработчики хотят установить одинаковую высоту для всех строк на листе, они могут сделать это, используя свойство [**standardHeight()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardHeight--) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Standard Row Height</title>
    </head>
    <body>
        <h1>Set Standard Row Height Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the height of all rows in the worksheet to 15
            worksheet.cells.standardHeight = 15;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Standard row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Работа с колонками**

### **Как установить ширину столбца**

Установите ширину столбца, вызвав метод [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Метод [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-) принимает следующие параметры:

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.
- **Ширина колонки**, желаемая ширина колонки.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Column Width Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Set Column Width</button>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of the second column to 17.5
            worksheet.cells.columns.get(1).width = 17.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Как установить ширину столбца в пикселях**

Установите ширину столбца, вызвав метод [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Метод [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-) принимает следующие параметры:

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.
- **Ширина столбца**, желаемая ширина столбца в пикселях.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Column Width In Pixels</title>
    </head>
    <body>
        <h1>Set Column Width In Pixels</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the width of the column in pixels
            // Converted from: worksheet.getCells().setColumnWidthPixel(7, 200);
            // UNIVERSAL GETTER/SETTER CONVERSION applied:
            worksheet.cells.columnWidthPixel = [7, 200];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetColumnWidthInPixels_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Как установить ширину всех столбцов в листе Excel**

Чтобы установить одинаковую ширину столбцов для всех столбцов на листе, используйте свойство [**standardWidth()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardWidth--) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Standard Width Example</title>
    </head>
    <body>
        <h1>Set Standard Width Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of all columns in the worksheet to 20.5
            worksheet.cells.standardWidth = 20.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Standard width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Автоподгонка строк и столбцов](/cells/ru/javascript-cpp/autofit-rows-and-columns/)
- [Преобразование текста в столбцы с использованием Aspose.Cells](/cells/ru/javascript-cpp/convert-text-to-columns-using-aspose-cells/)
- [Копирование строк и столбцов](/cells/ru/javascript-cpp/copying-rows-and-columns/)
- [Удаление пустых строк и столбцов в листе Excel](/cells/ru/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/)
- [Группировка и разгруппировка строк и столбцов](/cells/ru/javascript-cpp/grouping-and-ungrouping-rows-and-columns/)
- [Скрытие и отображение строк и столбцов](/cells/ru/javascript-cpp/hiding-and-showing-rows-and-columns/)
- [Вставка или удаление строк в листе Excel](/cells/ru/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/)
- [Вставка и удаление строк и столбцов в файле Excel](/cells/ru/javascript-cpp/inserting-and-deleting-rows-and-columns/)
- [Удалить дублирующиеся строки в рабочем листе](/cells/ru/javascript-cpp/remove-duplicate-rows-in-a-worksheet/)
- [Обновление ссылок в других листах при удалении пустых столбцов и строк на листе](/cells/ru/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
