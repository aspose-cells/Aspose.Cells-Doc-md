---
title: Просмотры листа Excel с помощью JavaScript через C++
linktitle: Представления листа
type: docs
weight: 40
url: /ru/javascript-cpp/worksheet-views/
description: Эта статья опишет, как использовать JavaScript и API JavaScript для взаимодействия с предварительным просмотром разрывов страниц в книге Excel и листах, работу с разбитыми панелями, зафиксированными панелями и масштабом.
---

## **Предпросмотр разрывов страниц**

Все листы могут быть просмотрены в двух режимах:

- Обычный вид.
- Предварительный просмотр разрыва страницы.

Нормальный режим просмотра — это стандартный вид листа. Предварительный просмотр разрывов страниц — это режим редактирования, который отображает лист так, как он будет напечатан. Предварительный просмотр показывает, какие данные пойдут на каждую страницу, чтобы вы могли настроить область печати и разрывы страниц. Используя Aspose.Cells for JavaScript в C++, разработчики могут включать режим нормального просмотра или предварительного просмотра разрывов страниц.

### **Управление режимами просмотра**

Aspose.Cells предоставляет класс, который представляет файл Microsoft Excel. Класс содержит коллекцию, которая позволяет получить доступ к каждой таблице в файле Excel.

Таблица представлена классом. Класс предоставляет широкий спектр свойств и методов для управления таблицами. Чтобы включить обычный или режим предварительного просмотра разрыва страницы, используйте свойство класса. Это логическое свойство, которое может хранить только значение **true** или **false**.

#### **Включение нормального режима**

Установите таблицу в обычный вид, установив свойство класса в **false**.

#### **Включение предварительного просмотра разрывов страниц**

Установите любую таблицу в режим предварительного просмотра разрыва страницы, установив свойство класса в **true**. Таким образом, таблица переключится из обычного вида в режим предварительного просмотра разрыва страницы.

Приведен полный пример ниже, демонстрирующий, как использовать свойство для включения режима просмотра предварительного просмотра разрыва страницы для первой таблицы файла Excel.

Файл book1.xls открывается созданием экземпляра класса. Просмотр переключается на предварительный просмотр разрыва страницы для первой таблицы, установив свойство в **true**. Измененный файл сохраняется как output.xls.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Break Preview</title>
    </head>
    <body>
        <h1>Page Break Preview Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Displaying the worksheet in page break preview
            worksheet.isPageBreakPreview = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Коэффициент масштабирования**

### **Использование Microsoft Excel**

Microsoft Excel предоставляет возможность установить коэффициент масштабирования листа. Эта функция помогает пользователям просматривать содержимое листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.

### **Aspose.Cells и коэффициент увеличения**

Aspose.Cells позволяет разработчикам установить коэффициент увеличения таблицы.
Aspose.Cells предоставляет класс, который представляет файл Microsoft Excel. Класс содержит коллекцию, которая позволяет получить доступ к каждой таблице в файле Excel.

Таблица представлена классом. Класс предоставляет широкий спектр свойств и методов для управления таблицами. Чтобы установить коэффициент увеличения таблицы, используйте свойство класса. Коэффициент увеличения устанавливается путем назначения числового (целочисленного) значения свойству.

Ниже приведен полный пример, демонстрирующий, как использовать свойство [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) для установки коэффициента масштабирования первого листа файла Excel.

Файл book1.xls открывается путем создания экземпляра класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). Коэффициент масштабирования первого листа устанавливается на 75, и измененный файл сохраняется как output.xls.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Worksheet Zoom Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the zoom factor of the worksheet to 75
            worksheet.zoom = 75;

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Zoom set to 75 successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Закрепить области**

### **Использование Microsoft Excel**

Закрепление области экрана - это функция, предоставляемая Microsoft Excel. Закрепление области экрана позволяет выбрать данные, которые останутся видимыми при прокрутке на листе.

### **Aspose.Cells и заморозка панелей**

Aspose.Cells позволяет разработчикам применять замороженные панели к листам во время выполнения.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет широкий диапазон свойств и методов для управления листами. Чтобы настроить закрепление панелей, вызовите метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) класса Worksheet. Метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) принимает следующие параметры:

- **Строка**, индекс строки, с которой начнется закрепление.
- **Столбец**, индекс столбца, с которого начнется закрепление.
- **Закрепленные строки**, количество видимых строк в верхней панели.
- **Закрепленные столбцы** — количество видимых столбцов в левой панели.

Файл book1.xls открывается путем вызова конструктора класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) при его создании, и в первом листе замораживается несколько строк и столбцов. Измененный файл сохраняется как output.xls.

Ниже приведен полный пример, показывающий, как использовать метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) для замораживания строк и столбцов (начиная с C4, представленного 4-й строкой и 3-й колонкой, где строки и столбцы начинаются с индекса 0) первого листа файла Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Applying freeze panes settings: topRows = 3, leftColumns = 2, top = 3, left = 2
            worksheet.freezePanes(3, 2, 3, 2);

            // Saving the modified Excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Разделение областей экрана**

Если вам нужно разделить экран для получения двух разных представлений на одном листе, используйте разделение областей экрана. Microsoft Excel предлагает очень удобную функцию, которая позволяет просматривать более одной копии вашего листа и прокручивать каждую область листа независимо: разделение областей экрана.

Разделы работают одновременно. Если вы внесете изменение в один, изменение одновременно появится в другом. Aspose.Cells предоставляет функцию разделения панелей для пользователей.

### **Применение и удаление разделенных панелей**

#### **Разделение панелей**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) , который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) предоставляет широкий спектр свойств и методов для управления файлом Excel. Чтобы реализовать разделенные виды, используйте метод [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) класса [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--). Чтобы удалить разделение панелей, используйте метод [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--).

В примере мы используем простой шаблонный файл, который загружается, затем устанавливается функция разделенных панелей для ячейки на первом листе. Обновленный файл сохраняется.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Window Example</title>
    </head>
    <body>
        <h1>Split Worksheet Window Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new workbook and open the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Set the active cell (converted from setActiveCell -> activeCell)
            sheet.activeCell = "A20";

            // Split the worksheet window
            sheet.split();

            // Save the excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet window split and active cell set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

После выполнения вышеуказанного кода сгенерированный файл будет иметь разделенный вид.

#### **Удаление панелей**

Удаление разделенных панелей с использованием метода [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Remove Split Example</h1>
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

            // Instantiate a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Set the active cell
            worksheet.activeCell = "A20";

            // Split the worksheet window - remove any existing split
            worksheet.removeSplit();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Скрытие отображения нулевых значений в таблице](/cells/ru/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Установить цвет вкладки листа](/cells/ru/javascript-cpp/set-worksheet-tab-color/)
- [Показывать и скрывать линии сетки и заголовки строк и столбцов](/cells/ru/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Показывать и скрывать строки, столбцы и полосы прокрутки](/cells/ru/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Показать и скрыть листы и вкладки](/cells/ru/javascript-cpp/show-and-hide-worksheets-and-tabs/)
- [Показывать формулы вместо значений в листе](/cells/ru/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Использовать параметры проверки ошибок](/cells/ru/javascript-cpp/use-error-checking-options/)
