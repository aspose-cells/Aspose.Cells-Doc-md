---
title: Управление данными файлов Excel
linktitle: Данные ячеек
type: docs
weight: 110
url: /ru/javascript-cpp/view-and-edit-excel-data/
description: В этой статье описывается, как просматривать и редактировать данные Excel файлов с помощью библиотеки Aspose.Cells для JavaScript через C++.
keywords: Aspose.Cells JavaScript через C++, управление данными Excel файла, добавление данных в Excel, получение данных из Excel, как повысить эффективность добавления данных, управление данными ячеек, обновление данных ячеек, получение данных ячеек, вставка данных в ячейки
---

{{% alert color="primary" %}}

В [Доступе к ячейкам листа](/cells/ru/javascript-cpp/accessing-cells-of-a-worksheet/) мы рассмотрели основные подходы для доступа к ячейкам листа. В этой статье используется один из этих подходов для добавления различных типов данных в ячейки.

{{% /alert %}}

## **Как добавить данные в ячейки**

Aspose.Cells for JavaScript через C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Каждый элемент коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) представляет объект класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells позволяет разработчикам добавлять данные в ячейки листов, вызывая метод класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-). Предоставляются перегруженные версии метода [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-), которые позволяют добавлять различные виды данных в ячейки. Используя эти перегруженные версии метода [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-), можно добавлять в ячейку значения типа Boolean, строка, двойное, целое или дата/время.

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **Как улучшить эффективность**

Если вы используете метод [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) для вставки большого объема данных в лист, рекомендуется добавлять значения сначала по строкам, затем по столбцам. Такой подход значительно повышает эффективность ваших приложений.

## **Как извлечь данные из ячеек**

Aspose.Cells for JavaScript via C++ предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получать доступ к листам в файле. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Каждый элемент в коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) представляет объект класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Класс [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) содержит несколько свойств, позволяющих получать значения из ячеек в зависимости от их типа данных. Эти свойства включают:

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): возвращает строковое значение ячейки.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): возвращает двойное значение ячейки.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): возвращает логическое значение ячейки.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): возвращает значение даты/времени ячейки.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): возвращает значение с плавающей точкой ячейки.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): возвращает целочисленное значение ячейки.

При незаполненном поле ячейки с [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) или [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) вызывают исключение.

Тип данных, содержащийся в ячейке, также можно проверить, используя метод [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). На самом деле, метод [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) основан на перечислении [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype), предопределённые значения которого приведены ниже:

|**Типы Значений Ячеек**|**Описание**|
| :- | :- |
|IsBool|Указывает, что значение ячейки является логическим.|
|IsDateTime|Указывает, что значение ячейки является дата/время.|
|IsNull|Представляет пустую ячейку.|
|IsNumeric|Указывает, что значение ячейки является числовым.|
|IsString|Указывает, что значение ячейки является строкой.|
|IsUnknown|Указывает, что значение ячейки неизвестно.|

Вы также можете использовать вышеупомянутые предопределённые типы значений ячеек для сравнения с типом данных, присутствующих в каждой ячейке.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Работая с листами, пользователи могут добавлять в ячейки различные типы данных. Эти типы могут включать логические значения, целые числа, числа с плавающей точкой, текст или значения даты/времени. С Aspose.Cells вы можете получать соответствующие значения из ячеек в зависимости от их типа данных.

{{% /alert %}}

## **Продвинутые темы**
- [Доступ к ячейкам листа](/cells/ru/javascript-cpp/accessing-cells-of-a-worksheet/)
- [Преобразование текстовых числовых данных в число](/cells/ru/javascript-cpp/convert-text-numeric-data-to-number/)
- [Создание итогов](/cells/ru/javascript-cpp/creating-subtotals/)
- [Фильтрация данных](/cells/ru/javascript-cpp/data-filtering/)
- [Сортировка данных](/cells/ru/javascript-cpp/sort-data-of-excel/)
- [Валидация данных](/cells/ru/javascript-cpp/data-validation/)
- [Поиск или поиск данных](/cells/ru/javascript-cpp/find-or-search-data/)
- [Получение строкового значения ячейки с или без форматирования](/cells/ru/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [Добавление HTML-форматированного текста в ячейку](/cells/ru/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [Вставка гиперссылок в Excel или OpenOffice](/cells/ru/javascript-cpp/insert-hyperlinks-to-excel/)
- [Как и где использовать перечислители](/cells/ru/javascript-cpp/how-and-where-to-use-enumerators/)
- [Измерение ширины и высоты значения ячейки в пикселях](/cells/ru/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Чтение значений ячеек в нескольких потоках одновременно](/cells/ru/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Преобразование между именем ячейки и индексом строки/столбца](/cells/ru/javascript-cpp/names-and-indices/)
- [Сначала заполняется строка, а затем столбец.](/cells/ru/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [Сохранить префикс одинарной кавычки значения ячейки или диапазона](/cells/ru/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Доступ и обновление частей Rich Text ячейки](/cells/ru/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
