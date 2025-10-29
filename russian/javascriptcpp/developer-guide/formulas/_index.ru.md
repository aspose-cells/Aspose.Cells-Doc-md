---
title: Управлять формулами Excel с помощью JavaScript через C++
linktitle: Формулы
type: docs
weight: 122
url: /ru/javascript-cpp/using-formulas-or-functions-to-process-data/
description: Узнайте, как управлять формулами Excel через Aspose.Cells for JavaScript через C++. Aspose.Cells может просто получать, устанавливать и вычислять формулы Excel.
keywords: Как вычислять формулы в JavaScript через C++, Формулы и функции с помощью JavaScript через C++, Управление встроенными функциями JavaScript через C++, Как использовать дополнительные функции с помощью JavaScript через C++, Как использовать массивные формулы via JavaScript через C++, Как использовать формулу R1C1 в JavaScript через C++.
---

## **Введение**

Одной из привлекательных особенностей Microsoft Excel является его способность обрабатывать данные с помощью формул и функций. В Excel встроен набор функций и формул, который помогает пользователям быстро выполнять сложные вычисления. Aspose.Cells также предоставляет огромный набор встроенных функций и формул, облегчающих расчет значений для разработчиков. Aspose.Cells поддерживает дополнения функций, а также формулы массива и R1C1.

## **Как использовать формулы и функции**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Каждый элемент в коллекции Cells представляет объект класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Можно применять формулы к ячейкам, используя свойства и методы, предлагаемые классом [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), подробно обсуждаемым ниже.

- Использование встроенных функций.
- Использование функций дополнений.
- Работа с массивными формулами.
- Создание формулы R1C1.

## **Как использовать встроенные функции**

Встроенные функции или формулы предоставляются в виде готовых функций для сокращения усилий и времени разработчиков. См. [список встроенных функций](/cells/ru/javascript-cpp/supported-formula-functions/), поддерживаемых Aspose.Cells. Функции расположены в алфавитном порядке. В будущем будет поддерживаться больше функций.

Aspose.Cells поддерживает большинство формул или функций, предлагаемых Microsoft Excel. Разработчики могут использовать эти формулы через API или [дизайнерскую таблицу](/cells/ru/javascript-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells поддерживает широкий набор математических, строковых, логических, даты/времени, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) для добавления формулы в ячейку. **Сложные формулы**, например

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, также поддерживаются в Aspose.Cells. Применяя формулу к ячейке, всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

В приведенном ниже примере к первой ячейке каталога [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) применяется сложная формула. Формула использует встроенную **Функцию IF**, предоставленную Aspose.Cells.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **Как использовать функции дополнений**

Может быть добавлены пользовательские формулы, которые мы хотим включить как дополнение Excel. При установке функции cell.formula встроенные функции работают нормально, однако необходимо установить пользовательские функции или формулы с помощью функций дополнения.

Aspose.Cells предоставляет функции для регистрации функций дополнений с помощью [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). После этого, когда мы устанавливаем cell.formula = любаяФункцияИзДополнения, выходной файл Excel содержит рассчитанное значение из функции дополнения.

Для регистрации функции добавления в приведенном ниже образце кода следует загрузить файл XLAM. Аналогично, файл вывода "test_udf.xlsx" можно загрузить для проверки вывода.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Как использовать массивную формулу**

Массивные формулы – это формулы, которые принимают массивы в качестве аргументов для функций, составляющих формулу. Когда массивная формула отображается, она окружена фигурными скобками ({}).

Некоторые функции Microsoft Excel возвращают массивы значений. Для вычисления нескольких результатов с помощью массивной формулы введите массив в диапазон ячеек с тем же количеством строк и столбцов, что и аргументы массива.

Возможно применить массивную формулу к ячейке, вызвав метод класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-). Метод [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) принимает следующие параметры:

- **Массивная Формула**, массивная формула.
- **Количество строк**, количество строк для заполнения результата массивной формулы.
- **Количество столбцов**, количество столбцов для заполнения результата массивной формулы.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **Как использовать формулу R1C1**

Добавить формулу со ссылкой стиля **R1C1** в ячейку с помощью свойства [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--) класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Предшественники и зависимые](/cells/ru/javascript-cpp/precedents-and-dependents/)
- [Установка внешних ссылок в формулах](/cells/ru/javascript-cpp/set-external-links-in-formulas/)
- [Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки](/cells/ru/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Установка формулы для именованного диапазона](/cells/ru/javascript-cpp/setting-formula-for-named-range/)
- [Установка формул - уведомление для пользователей не на английском языке](/cells/ru/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [Установка общей формулы](/cells/ru/javascript-cpp/setting-shared-formula/)
- [Укажите максимальное количество строк общей формулы](/cells/ru/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [Поддерживаемые функции Excel](/cells/ru/javascript-cpp/supported-formula-functions/)
