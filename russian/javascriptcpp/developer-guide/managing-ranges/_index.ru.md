---
title: Управление диапазонами с помощью JavaScript через C++
linktitle: Диапазоны
type: docs
weight: 105
url: /ru/javascript-cpp/managing-ranges/
description: Изучите, как управлять диапазонами в Excel с помощью Aspose.Cells for JavaScript через C++. Создавайте диапазоны, задавайте значения, стили и выполняйте различные операции.
---

## **Введение**

В Excel можно выделять несколько ячеек с помощью рамки мыши; выбранный набор ячеек называется "Диапазон".

Например, вы можете щёлкнуть левой кнопкой мыши в ячейке "A1" Excel и затем перетащить к ячейке "C4". Выбранную прямоугольную область также можно легко создать как объект, используя Aspose.Cells for JavaScript через C++.

Вот как создать диапазон, вставить значение, установить стиль и выполнить другие операции с объектом "Диапазон".

## **Управление диапазонами с помощью Aspose.Cells for JavaScript через C++**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

### **Создать диапазон**

 Когда вы хотите создать прямоугольную область, расширяющуюся на A1:C4, вы можете использовать следующий код:

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells (converted from getWorksheets().get(0).getCells() to properties)
            const cells = workbook.worksheets.get(0).cells;

            // Create Range A1:C4
            const range = cells.createRange("A1:C4");

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Range A1:C4 created successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Поместить значение в ячейки диапазона**

Предположим, что у вас есть диапазон ячеек, который расширяется от A1 до C4. Матрица состоит из 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].

 В следующем примере показано, как ввести некоторые значения в ячейки диапазона.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Range Value Example</title>
    </head>
    <body>
        <h1>Range Value Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            const range = cells.createRange("A1:C4");

            range.get(0, 0).value = "A1";
            range.get(0, 1).value = "B1";
            range.get(0, 2).value = "C1";
            range.get(3, 0).value = "A4";
            range.get(3, 1).value = "B4";
            range.get(3, 2).value = "C4";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeValueTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **Установить стиль ячеек диапазона**

Следующий пример показывает, как установить стиль ячеек диапазона.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Range Style Example</h1>
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
            const resultDiv = document.getElementById('result');

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Gets Cells
            const cells = workbook.worksheets.get(0).cells;
            // Creates Range
            const range = cells.createRange("A1:C4");
            // Puts value
            range.get(0, 0).value = "A1";
            range.get(3, 2).value = "C4";
            // Sets Style
            let style00 = workbook.createStyle();
            style00.pattern = AsposeCells.BackgroundType.Solid;
            style00.foregroundColor = new AsposeCells.Color(255, 0, 0); // Red
            range.get(0, 0).style = style00;
            let style32 = workbook.createStyle();
            style32.pattern = AsposeCells.BackgroundType.HorizontalStripe;
            style32.foregroundColor = new AsposeCells.Color(0, 255, 0); // Green
            range.get(3, 2).style = style32;
            // Saves the Workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeStyleTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **Получить текущий регион диапазона**

CurrentRegion - это свойство, которое возвращает объект Range, представляющий текущий регион. 

Текущий регион - это диапазон, ограниченный любой комбинацией пустых строк и столбцов. Только для чтения.

В Excel текущий регион можно получить следующим образом:
1. Выберите область (диапазон1) с помощью мыши.
2. Нажмите "Главная - Редактирование - Поиск и выделение - Перейти специальное - Текущий регион", или используйте "Ctrl+Shift+*", вы увидите, как Excel автоматически поможет вам выбрать область (диапазон2). Теперь вы это сделали, диапазон2 является Текущим регионом диапазона1.

Пожалуйста, скачайте следующий тестовый файл, откройте его в Excel, с помощью мыши выделите область "A1:D7", затем нажмите "Ctrl+Shift+*", вы увидите выделенной область "A1:C3".

[current_region.xlsx](current_region.xlsx)

Теперь запустите следующий пример, чтобы увидеть, как он работает в Aspose.Cells:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Current Region Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Cells
            const cells = worksheet.cells;

            // Create Range
            const src = cells.createRange("A1:D7");

            // Get CurrentRegion (converted from getCurrentRegion())
            const A1C3 = src.currentRegion;

            // Save the workbook (no modifications were required by original code)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.current_region.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Current region obtained successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```


## **Продвинутые темы**
- [Автозаполнение диапазона в файле Excel](/cells/ru/javascript-cpp/autofill-ranges/)
- [Копирование диапазонов в Excel](/cells/ru/javascript-cpp/copy-ranges-of-Excel/)
- [Копировать только данные диапазона](/cells/ru/javascript-cpp/copy-range-data-only/)
- [Копировать данные диапазона со стилем](/cells/ru/javascript-cpp/copy-range-data-with-style/)
- [Копировать только стиль диапазона](/cells/ru/javascript-cpp/copy-range-style-only/)
- [Создать объединенный диапазон](/cells/ru/javascript-cpp/create-union-range/)
- [Вырезать и вставить диапазон](/cells/ru/javascript-cpp/cut-and-paste-cells/)
- [Удалить диапазоны](/cells/ru/javascript-cpp/delete-ranges-from-Excel/)
- [Получить адрес ячейки смещения количества исходной колонки и строки всего диапазона](/cells/ru/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Вставить диапазоны](/cells/ru/javascript-cpp/insert-ranges-to-Excel/)
- [Объединить или разделить диапазон ячеек](/cells/ru/javascript-cpp/merge-or-unmerge-range-of-cells/)
- [Перемещение диапазона ячеек на листе](/cells/ru/javascript-cpp/move-range-of-cells-in-a-worksheet/)
- [Создать именованные диапазоны с учетом книги и листа](/cells/ru/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Поиск и замена данных в диапазоне](/cells/ru/javascript-cpp/search-and-replace-data-in-a-range/)
