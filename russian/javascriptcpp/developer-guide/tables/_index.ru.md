---
title: Создавайте и управляйте таблицами файлов Microsoft Excel с помощью JavaScript через C++
linktitle: Таблицы
type: docs
weight: 150
url: /ru/javascript-cpp/create-and-format-table/
description: Вставляйте, изменяйте размеры, редактируйте, удаляйте и форматируйте таблицы Excel с помощью Aspose.Cells for JavaScript через C++.
---

## **Создать таблицу**

Одним из преимуществ электронных таблиц является возможность создания различных типов списков, например, списков телефонов, списков задач, списков транзакций, активов или обязательств. Несколько пользователей могут вместе работать с созданием и поддержкой различных списков.

Aspose.Cells поддерживает создание и управление списками.

### **Преимущества объекта списка**

Существует несколько преимуществ при преобразовании списка данных в фактический объект списка

- Новые строки и столбцы автоматически включаются.
- Итоговая строка внизу списка легко добавляется для отображения SUM, AVERAGE, COUNT и т. д.
- Добавленные столбцы справа автоматически включаются в объект списка.
- Графики, основанные на строках и столбцах, будут автоматически расширены.
- Именованные диапазоны, присвоенные строкам и столбцам, будут автоматически расширены.
- Список защищен от случайного удаления строк и столбцов.

### **Создание объекта списка с использованием Microsoft Excel**

- Выбор диапазона данных для создания объекта List
- Это отображает диалоговое окно Создания списка.
- Реализация объекта List для данных и указание итоговой строки (выберите **Данные**, затем **Список**, затем **Итоговая строка**).

### **Использование API Aspose.Cells**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), позволяющую получить доступ к каждому листу в файле Excel.

Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет широкий набор свойств и методов для управления рабочим листом. Чтобы создать [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) в рабочем листе, используйте коллекцию [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) — это, по существу, объект класса [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/), который дополнительно предоставляет метод [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-) для добавления объекта List и указания диапазона ячеек для этого списка.

В соответствии с указанным диапазоном ячеек объект List создается с помощью Aspose.Cells. Используйте атрибуты (например, [**showTotals**](https://reference.aspose.com/cells/javascript-cpp/listobject/#showTotals--), [**listColumns**](https://reference.aspose.com/cells/javascript-cpp/listobject/#listColumns--) и т.д.) класса [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) для управления списком.

В приведенном ниже примере мы создали тот же [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/), используя API Aspose.Cells, как и в предыдущем разделе с Microsoft Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells ListObjects Example</title>
    </head>
    <body>
        <h1>ListObjects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TotalsCalculation } = AsposeCells;

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

            const listObjects = workbook.worksheets.get(0).listObjects;

            listObjects.add(1, 1, 7, 5, true);

            const firstList = listObjects.get(0);
            firstList.showTotals = true;

            firstList.listColumns.get(4).totalsCalculation = TotalsCalculation.Sum;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">List created and totals calculated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Форматирование таблицы**

Для управления и анализа группы связанных данных можно преобразить диапазон ячеек в объект списка (также известный как таблица Excel). Таблица представляет собой серию строк и столбцов, содержащих связанные данные, управляемые независимо от данных в других строках и столбцах. По умолчанию у каждого столбца в таблице включена фильтрация в строке заголовка, чтобы можно было быстро фильтровать или сортировать данные объекта списка. Можно добавить всю строку (специальная строка в списке, предоставляющая выбор агрегатных функций, полезных для работы с числовыми данными) к объекту списка, предоставляющую раскрывающийся список агрегатных функций для каждой ячейки всей строки. Aspose.Cells предоставляет возможности для создания и управления списками (или таблицами).

### **Форматирование объекта списка**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), позволяющую получить доступ к каждому листу в файле Excel.

Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет широкий набор свойств и методов для управления рабочими листами. Чтобы создать [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) в рабочем листе, используйте коллекцию [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Каждый [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) — это объект класса [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/), который предоставляет метод [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-) для добавления объекта List и указания диапазона ячеек. В соответствии с указанным диапазоном ячеек, в рабочем листе создается [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) с помощью Aspose.Cells. Используйте атрибуты (например, [**TableStyleType**](https://reference.aspose.com/cells/javascript-cpp/tablestyletype/)) класса [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) для форматирования таблицы по вашему требованию.

Пример ниже добавляет тестовые данные в рабочий лист, создает [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) и применяет к нему стандартные стили. Поддерживаются стили [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) от Microsoft Excel 2007/2010.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // This example does not require an input file; it creates a new workbook
            const workbook = new Workbook();

            // Obtaining the reference of the default(first) worksheet
            const sheet = workbook.worksheets.get(0);

            // Obtaining Worksheet's cells collection
            const cells = sheet.cells;

            // Setting the value to the cells (converted putValue -> value)
            cells.get(1, 1).value = "Employee";
            cells.get(1, 2).value = "Quarter";
            cells.get(1, 3).value = "Product";
            cells.get(1, 4).value = "Continent";
            cells.get(1, 5).value = "Country";
            cells.get(1, 6).value = "Sale";

            cells.get(2, 1).value = "David";
            cells.get(3, 1).value = "David";
            cells.get(4, 1).value = "David";
            cells.get(5, 1).value = "David";
            cells.get(6, 1).value = "James";
            cells.get(7, 1).value = "James";
            cells.get(8, 1).value = "James";
            cells.get(9, 1).value = "James";
            cells.get(10, 1).value = "James";
            cells.get(11, 1).value = "Miya";
            cells.get(12, 1).value = "Miya";
            cells.get(13, 1).value = "Miya";
            cells.get(14, 1).value = "Miya";
            cells.get(15, 1).value = "Miya";
            cells.get(2, 2).value = 1;
            cells.get(3, 2).value = 2;
            cells.get(4, 2).value = 3;
            cells.get(5, 2).value = 4;
            cells.get(6, 2).value = 1;
            cells.get(7, 2).value = 2;
            cells.get(8, 2).value = 3;
            cells.get(9, 2).value = 4;
            cells.get(10, 2).value = 4;
            cells.get(11, 2).value = 1;
            cells.get(12, 2).value = 1;
            cells.get(13, 2).value = 2;
            cells.get(14, 2).value = 2;
            cells.get(15, 2).value = 2;

            cells.get(2, 3).value = "Maxilaku";
            cells.get(3, 3).value = "Maxilaku";
            cells.get(4, 3).value = "Chai";
            cells.get(5, 3).value = "Maxilaku";
            cells.get(6, 3).value = "Chang";
            cells.get(7, 3).value = "Chang";
            cells.get(8, 3).value = "Chang";
            cells.get(9, 3).value = "Chang";
            cells.get(10, 3).value = "Chang";
            cells.get(11, 3).value = "Geitost";
            cells.get(12, 3).value = "Chai";
            cells.get(13, 3).value = "Geitost";
            cells.get(14, 3).value = "Geitost";
            cells.get(15, 3).value = "Geitost";

            cells.get(2, 4).value = "Asia";
            cells.get(3, 4).value = "Asia";
            cells.get(4, 4).value = "Asia";
            cells.get(5, 4).value = "Asia";
            cells.get(6, 4).value = "Europe";
            cells.get(7, 4).value = "Europe";
            cells.get(8, 4).value = "Europe";
            cells.get(9, 4).value = "Europe";
            cells.get(10, 4).value = "Europe";
            cells.get(11, 4).value = "America";
            cells.get(12, 4).value = "America";
            cells.get(13, 4).value = "America";
            cells.get(14, 4).value = "America";
            cells.get(15, 4).value = "America";

            cells.get(2, 5).value = "China";
            cells.get(3, 5).value = "India";
            cells.get(4, 5).value = "Korea";
            cells.get(5, 5).value = "India";
            cells.get(6, 5).value = "France";
            cells.get(7, 5).value = "France";
            cells.get(8, 5).value = "Germany";
            cells.get(9, 5).value = "Italy";
            cells.get(10, 5).value = "France";
            cells.get(11, 5).value = "U.S.";
            cells.get(12, 5).value = "U.S.";
            cells.get(13, 5).value = "Brazil";
            cells.get(14, 5).value = "U.S.";
            cells.get(15, 5).value = "U.S.";

            cells.get(2, 6).value = 2000;
            cells.get(3, 6).value = 500;
            cells.get(4, 6).value = 1200;
            cells.get(5, 6).value = 1500;
            cells.get(6, 6).value = 500;
            cells.get(7, 6).value = 1500;
            cells.get(8, 6).value = 800;
            cells.get(9, 6).value = 900;
            cells.get(10, 6).value = 500;
            cells.get(11, 6).value = 1600;
            cells.get(12, 6).value = 600;
            cells.get(13, 6).value = 2000;
            cells.get(14, 6).value = 500;
            cells.get(15, 6).value = 900;

            // Adding a new List Object to the worksheet
            const index = sheet.listObjects.add("A1", "F15", true);

            const listObject = sheet.listObjects.get(index);

            // Adding Default Style to the table (converted setter -> property)
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium10;

            // Show Total
            listObject.showTotals = true;

            // Set the Quarter field's calculation type (converted getter/setter -> property)
            listObject.listColumns.get(1).totalsCalculation = AsposeCells.TotalsCalculation.Count;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and table added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Преобразовать таблицу в ODS](/cells/ru/javascript-cpp/convert-table-to-ods/)
- [Поиск таблиц запросов и объектов списка, связанных с внешними подключениями к данным](/cells/ru/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Чтение и запись таблицы с источником данных из запроса к таблице](/cells/ru/javascript-cpp/read-and-write-table-with-query-table-data-source/)
- [Установите комментарий таблицы или объекта списка внутри листа.](/cells/ru/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Таблицы и диапазоны](/cells/ru/javascript-cpp/tables-and-ranges/)
