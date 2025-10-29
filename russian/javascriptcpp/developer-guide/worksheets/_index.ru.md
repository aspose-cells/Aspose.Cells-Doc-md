---
title: Управление рабочими листами файлов Microsoft Excel с помощью JavaScript через C++
linktitle: Рабочие листы
type: docs
weight: 90
url: /ru/javascript-cpp/manage-worksheets/
description: Добавляйте, удаляйте и активируйте рабочие листы, используя Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}
Разработчики могут легко создавать и управлять листами в файлах Microsoft Excel программно, используя гибкий API Aspose.Cells. В этой теме описываются подходы к добавлению и удалению листов в файлах Microsoft Excel.
{{% /alert %}}

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), позволяющую получить доступ к каждому листу в файле Excel.

Лист представляет класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет широкий спектр свойств и методов для управления листами.

## **Добавление рабочих листов в новый файл Excel**

Для создания нового файла Excel программно:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).  
2. Вызовите метод [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#add-sheettype-) класса [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection). В файл Excel автоматически добавляется пустой рабочий лист. Его можно ссылаться, передав индекс нового листа в коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--).  
3. Получите ссылку на рабочий лист.  
4. Выполняйте работу с рабочими листами.  
5. Сохраните новый файл Excel с новыми рабочими листами, вызвав метод [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Worksheet Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Get current worksheet count (converted from getWorksheets().getCount())
            const i = workbook.worksheets.count;

            // Add a new worksheet (converted from getWorksheets().add())
            workbook.worksheets.add();

            // Obtain the newly added worksheet by index (converted from getWorksheets().get(i))
            const worksheet = workbook.worksheets.get(i);

            // Set the name of the newly added worksheet (converted from setName)
            worksheet.name = "My Worksheet";

            // Save the workbook to XLS format and prepare download
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Добавление листов в дизайнерскую электронную таблицу**

Процесс добавления листов в дизайн-таблицу совпадает с добавлением нового листа, за исключением того, что файл Excel уже существует и должен быть открыт перед добавлением листов. Дизайн-таблицу можно открыть с помощью класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Worksheet</title>
    </head>
    <body>
        <h1>Add Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Setting the name of the newly added worksheet
            worksheet.name = "My Worksheet";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Доступ к листам с использованием имени листа**

Получите доступ к любому листу, указав его имя или индекс.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example: Read Cell Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing a worksheet using its sheet name
            const worksheet = workbook.worksheets.get("Sheet1");
            const cell = worksheet.cells.get("A1");

            console.log(cell.value);
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.value}</p>`;
        });
    </script>
</html>
```

## **Удаление листов с использованием имени листа**

Чтобы удалить листы из файла, вызовите метод [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) класса [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection). Передайте имя листа в метод [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-), чтобы удалить конкретный лист.

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

            // Removing a worksheet using its sheet name
            workbook.worksheets.removeAt("Sheet1");

            // Save workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Удаление рабочих листов с использованием индекса листа.**

Удаление листов по имени хорошо работает, когда известно имя листа. Если имя листа неизвестно, используйте перегруженную версию метода [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-), которая принимает индекс листа вместо его имени.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Remove First Worksheet</h1>
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

            // Removing a worksheet using its sheet index
            workbook.worksheets.removeAt(0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Активация листов и установка активной ячейки на листе**

Иногда необходимо, чтобы определенный лист был активен и отображался при открытии файла Microsoft Excel. Аналогично, можно активировать конкретную ячейку и настроить прокрутки для отображения активной ячейки. Aspose.Cells способен выполнять все эти задачи.

Активный лист - это лист, над которым вы работаете: имя активного листа на вкладке жирным шрифтом по умолчанию.

Активная ячейка - это выбранная ячейка, в которую вводятся данные при начале набора текста. Одновременно может быть активна только одна ячейка. Активная ячейка выделяется толстой границей.

### **Активация листов и установка активной ячейки**

Aspose.Cells предоставляет конкретные вызовы API для активации листа и ячейки. Например, свойство [**WorksheetCollection.activeSheetIndex**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#activeSheetIndex--) полезно для установки активного листа в книге. Аналогично, свойство [**Worksheet.activeCell**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#activeCell--) используется для установки и получения активной ячейки в листе.

Чтобы убедиться, что горизонтальные или вертикальные полосы прокрутки находятся в нужной позиции по индексам строк и столбцов для отображения определенных данных, используйте свойства [**Worksheet.firstVisibleRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleRow--) и [**Worksheet.firstVisibleColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleColumn--).

В следующем примере показано, как активировать лист и сделать активной ячейку. В сгенерированном выводе полосы прокрутки будут прокручены, чтобы сделать 2-ю строку и 2-й столбец первой видимой строкой и столбцом.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Add a worksheet if collection is empty
            const worksheets = workbook.worksheets;
            if (worksheets.count === 0) {
                worksheets.add();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = worksheets.get(0);

            // Get the cells in the worksheet.
            const cells = worksheet1.cells;

            // Input data into B2 cell.
            const cell = cells.get(1, 1);
            cell.value = "Hello World!";

            // Set the first sheet as an active sheet.
            worksheets.activeSheetIndex = 0;

            // Set B2 cell as an active cell in the worksheet.
            worksheet1.activeCell = "B2";

            // Set the B column as the first visible column in the worksheet.
            worksheet1.firstVisibleColumn = 1;

            // Set the 2nd row as the first visible row in the worksheet.
            worksheet1.firstVisibleRow = 1;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Копирование и перемещение листов](/cells/ru/javascript-cpp/copying-and-moving-worksheets/)  
- [Посчитать количество ячеек в листе](/cells/ru/javascript-cpp/count-number-of-cells-in-the-worksheet/)  
- [Обнаружение пустых листов](/cells/ru/javascript-cpp/detecting-empty-worksheets/)  
- [Определить, является ли рабочий лист диалоговым листом](/cells/ru/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Получить уникальный идентификатор листа](/cells/ru/javascript-cpp/get-worksheet-unique-id/)  
- [Создание, изменение или удаление сценариев из листов](/cells/ru/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Управление разрывами страницы](/cells/ru/javascript-cpp/managing-page-breaks/)  
- [Возможности настройки страницы](/cells/ru/javascript-cpp/page-setup-features/)  
- [Использование свойства Sheet.SheetId из OpenXml с помощью Aspose.Cells](/cells/ru/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Просмотр листов](/cells/ru/javascript-cpp/worksheet-views/)
