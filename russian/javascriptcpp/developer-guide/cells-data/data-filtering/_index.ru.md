---
title: Фильтрация данных
type: docs
weight: 85
url: /ru/javascript-cpp/data-filtering/
description: Узнайте, как добавлять фильтр данных с помощью Aspose.Cells for JavaScript через API C++.
keywords: Добавить фильтр по цвету JavaScript через C++, добавить фильтры по дате JavaScript через C++, добавить числовые фильтры JavaScript через C++, добавить динамический фильтр JavaScript через C++, добавить текстовые фильтры JavaScript через C++, добавить пользовательский фильтр с Contains JavaScript через C++, добавить пользовательский фильтр с NotContains JavaScript через C++, добавить пользовательский фильтр с BeginsWith JavaScript через C++, добавить пользовательский фильтр с EndsWith JavaScript через C++
---

{{% alert color="primary" %}}
Microsoft Excel предоставляет хорошие функции для автоматической фильтрации данных листа. Aspose.Cells полностью поддерживает функции автофильтрации Microsoft Excel. Эта статья объясняет, как использовать эти функции в Microsoft Excel и как прописывать их с помощью Aspose.Cells for JavaScript через C++.
{{% /alert %}}

## **Автофильтрация данных**

Автофильтрация - самый быстрый способ выбрать только те элементы с листа, которые вы хотите отображать в списке. Функция автофильтрации позволяет фильтровать элементы в списке в соответствии с набором критериев. Отфильтруйте на основе текста, чисел или дат.

### **Автофильтр в Microsoft Excel**

Чтобы активировать функцию автофильтра в Microsoft Excel:

1. Щелкните строку заголовка на листе.
1. В меню **Данные** выберите **Фильтр**, а затем **Автофильтр**.

При применении автофильтра к листу появляются переключатели фильтра (черные стрелки) справа от заголовков столбцов.

1. Щелкните стрелку фильтра, чтобы увидеть список вариантов фильтра.

Некоторые из вариантов автофильтра:

|**Опции**|**Описание**|
| :- | :- |
|All|Показать все элементы в списке один раз.|
|Custom|Настроить критерии фильтрации, такие как содержит/не содержит.|
|Filter by Color|Фильтрация на основе заполненного цвета.|
|Date Filters|Фильтрация строк на основе различных критериев по дате.|
|Number Filters|Несколько видов фильтров для чисел, таких как сравнение, средние значения и Топ-10 и т.д.|
|Text Filters|Различные фильтры, такие как начинается с, заканчивается на, содержит и т. д.|
|Blanks/Non Blanks|Эти фильтры могут быть применены с помощью пустого текстового фильтра.|

Пользователи вручную фильтруют данные своего листа в Microsoft Excel, используя эти опции.

### **Автофильтр с Aspose.Cells for JavaScript через C++**

Aspose.Cells предоставляет класс, Workbook, который представляет файл Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому рабочему листу в файле Excel.

Лист представлен классом Worksheet. Класс Worksheet предоставляет широкий спектр свойств и методов для управления листами. Для создания автофильтра используйте свойство AutoFilter класса Worksheet. Свойство AutoFilter является объектом класса AutoFilter, который предоставляет свойство Range для указания диапазона ячеек, образующих строку заголовка. Автофильтр применяется к диапазону ячеек, который является строкой заголовка.

Для каждого листа вы можете указать только один диапазон фильтра. Это ограничено Microsoft Excel. Для настраиваемой фильтрации данных используйте метод AutoFilter.Custom.

В приведённом ниже примере мы создали такой же автофильтр с помощью Aspose.Cells for JavaScript через C++, как и в Microsoft Excel в предыдущем разделе.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range of the heading row
            worksheet.autoFilter.range = "A1:B1";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">AutoFilter created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Различные типы фильтров**

Aspose.Cells предоставляет несколько вариантов применения различных типов фильтров, таких как Фильтр по цвету, Фильтр по дате, Фильтр по числам, Фильтр по тексту, Фильтры для заполненных ячеек и незаполненных ячеек.

##### **Цвет заливки**

Aspose.Cells предоставляет функцию AddFillColorFilter для фильтрации данных на основе цвета заливки ячеек. В приведенном ниже примере используется файл-шаблон, содержащий различные цвета заливки в первом столбце листа, для тестирования функции фильтрации по цвету. Образцы файлов можно скачать по следующим ссылкам.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Coloured Cells Example</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiating a CellsColor object for foreground color
            const clrForeground = workbook.createCellsColor();
            clrForeground.color = AsposeCells.Color.fromArgb(255, 0, 0); // Red color

            // Instantiating a CellsColor object for background color
            const clrBackground = workbook.createCellsColor();
            clrBackground.color = AsposeCells.Color.fromArgb(255, 255, 255); // White color

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call AddFillColorFilter function to apply the filter
            worksheet.autoFilter.addFillColorFilter(0, AsposeCells.BackgroundType.Solid, clrForeground, clrBackground);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredColouredCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Дата**

Можно реализовать различные типы фильтров дат, например фильтрацию всех строк с датами в январе 2018 года. Следующий пример демонстрирует этот фильтр с помощью функции AddDateFilter. Примерные файлы приведены ниже.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Date Filter</title>
    </head>
    <body>
        <h1>Date Filter Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call AddDateFilter function to apply the filter
            worksheet.autoFilter.addDateFilter(0, AsposeCells.DateTimeGroupingType.Month, 2018, 1, 0, 0, 0, 0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredDate.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Динамическая дата**

Иногда требуются динамические фильтры на основе даты, например, все ячейки с датами в январе независимо от года. В этом случае используется функция DynamicFilter, как показано в приведенном ниже образце кода. Примеры файлов даны ниже.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Dynamic Date Example</h1>
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

            // Call DynamicFilter function to apply the filter
            worksheet.autoFilter.dynamic_Filter(0, AsposeCells.DynamicFilterType.January);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredDynamicDate.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Число**

Пользовательские фильтры могут быть применены с использованием Aspose.Cells, например, выбор ячеек с числами в заданном диапазоне. В следующем примере демонстрируется использование функции Custom() для фильтрации чисел. Приведены примеры файлов.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Filter Numbers</title>
    </head>
    <body>
        <h1>Filter Numbers Example</h1>
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

            // Call Custom function to apply the filter
            worksheet.autoFilter.custom(0, AsposeCells.FilterOperatorType.GreaterOrEqual, 5, true, AsposeCells.FilterOperatorType.LessOrEqual, 10);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Текст**

Если столбец содержит текст, и необходимо выбрать ячейки с определённым текстом, можно использовать функцию Filter(). В следующем примере файл-шаблон содержит список стран, и необходимо выбрать строки с названием конкретной страны. Следующий код демонстрирует фильтрацию текста. Примерные файлы приведены ниже.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter AutoFilter Example</h1>
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

            // Call Filter function to apply the filter
            const autoFilter = worksheet.autoFilter;
            autoFilter.filter(0, "Angola");

            // Call refresh function to update the worksheet
            autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredText.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Пустые**

Если столбец содержит текст так, что некоторые ячейки пусты, и требуется выбрать только те строки, где присутствуют пустые ячейки, используйте функцию MatchBlanks(), как показано ниже. Примеры файлов даны ниже.

1. [Пустой.xlsx](72417324.xlsx)
1. [ОтфильтрованныйПустой.xlsx](72417325.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Blank Rows Example</title>
    </head>
    <body>
        <h1>Filter Blank Rows Example</h1>
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

            // Call MatchBlanks function to apply the filter
            worksheet.autoFilter.matchBlanks(0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlank.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filtering completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Не пустые**

Когда нужно отфильтровать ячейки с любым текстом, используйте функцию фильтрации MatchNonBlanks, как показано ниже. Примеры файлов даны ниже.

1. [Пустой.xlsx](72417324.xlsx)
1. [ОтфильтрованныеНеПустой.xlsx](72417326.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Filter Non-Blank Example</h1>
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

            // Read the selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlank.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Пользовательский фильтр с содержит**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, содержащих определенную подстроку. Эта функция доступна в Aspose.Cells и демонстрируется ниже путем фильтрации имен в примере файла. Приведены примеры файлов.

1. [ИсходныйОбразецНазванийСтран.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows containing string "Ba"
            worksheet.autoFilter.custom(0, FilterOperatorType.Contains, "Ba");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Пользовательский фильтр с не содержит**

Excel предоставляет пользовательские фильтры, такие как фильтр строк, не содержащих определённую строку. Эта функция доступна в Aspose.Cells и продемонстрирована ниже на примере фильтрации имён в указанных ниже файлах.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows not containing string "Be"
            worksheet.autoFilter.custom(0, FilterOperatorType.NotContains, "Be");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Пользовательский фильтр с начинается с**

Excel предоставляет пользовательские фильтры, такие как фильтр строк с началом на определённую строку. Эта функция доступна в Aspose.Cells и показана ниже на примере фильтрации имён в приведённых файлах.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Countries Starting With "Ba"</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows starting with string "Ba"
            worksheet.autoFilter.custom(0, FilterOperatorType.BeginsWith, "Ba");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Пользовательский фильтр с EndsWith**

Excel предоставляет пользовательские фильтры, такие как фильтрация строк, которые заканчиваются определенной строкой. Эта функция доступна в Aspose.Cells и демонстрируется ниже по фильтру имен в предоставленном образце файла.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply AutoFilter Example</h1>
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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            const autoFilter = worksheet.autoFilter;
            autoFilter.range = "A1:A18";

            // Initialize filter for rows end with string "ia"
            autoFilter.custom(0, AsposeCells.FilterOperatorType.BeginsWith, "ia");

            // Refresh the filter to show/hide filtered rows
            autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Продвинутые темы**
- [Применение расширенного фильтра Microsoft Excel для отображения записей, удовлетворяющих сложным критериям](/cells/ru/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Получить все скрытые индексы строк после обновления автофильтра](/cells/ru/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
