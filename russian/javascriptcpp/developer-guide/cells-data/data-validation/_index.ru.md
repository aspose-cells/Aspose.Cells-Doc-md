---
title: Валидация данных
type: docs
weight: 90
url: /ru/javascript-cpp/data-validation/
description: Узнайте, как добавлять проверку данных через Aspose.Cells for JavaScript через C++ API.
keywords: Добавить проверку данных JavaScript через C++, получить значение проверки JavaScript через C++, добавить проверку целого числа JavaScript через C++, добавить списковую проверку JavaScript через C++, добавить проверку даты JavaScript через C++, добавить проверку времени JavaScript через C++, добавить проверку длины текста JavaScript через C++, добавить CellArea к существующей проверке JavaScript через C++, проверить, является ли проверка в ячейке выпадающим списком JavaScript через C++, добавить пользовательскую проверку JavaScript через C++
---

{{% alert color="primary" %}}
Microsoft Excel предоставляет хорошие функции для автоматической фильтрации или валидации данных листа. Aspose.Cells полностью поддерживает функции валидации данных и автофильтрации Microsoft Excel. Эта статья объясняет, как использовать эти функции в Microsoft Excel, и как прописывать их с помощью Aspose.Cells for JavaScript через C++.
{{% /alert %}}

## **Типы проверки данных и выполнение**

Проверка данных - это возможность устанавливать правила, касающиеся ввода данных на листе таблицы. Например, использовать проверку для обеспечения того, что столбец с подписью DATE содержит только даты, или что другой столбец содержит только числа. Вы даже можете обеспечить, что столбец с подписью DATE содержит только даты в определенном диапазоне. С помощью проверки данных вы можете контролировать то, что вводится в ячейки на листе таблицы.

Microsoft Excel поддерживает ряд различных типов проверки данных. Каждый тип используется для контроля типа данных, вводимого в ячейку или диапазон ячеек. Ниже приведены фрагменты кода, иллюстрирующие проверку, что:

- Числа являются целыми, то есть у них нет десятичной части.
- Десятичные числа соответствуют правильной структуре. Приведенный пример кода определяет, что диапазон ячеек должен иметь два десятичных знака.
- Значения ограничены списком значений. Проверка списка определяет отдельный список значений, которые можно применить к ячейке или диапазону ячеек.
- Даты находятся в определенном диапазоне.
- Время находится в определенном диапазоне.
- Текст имеет определенную длину.

### **Проверка данных в Microsoft Excel**

Для создания проверок с помощью Microsoft Excel:

1. В листе выберите ячейки, к которым вы хотите применить проверку.
1. Из меню **Данные** выберите **Проверку**. Диалоговое окно проверки будет отображено.
1. Нажмите вкладку **Настройки** и введите настройки.

### **Валидация данных в Aspose.Cells for JavaScript через C++**

Проверка данных - мощная функция для проверки введенной информации в таблицы. С помощью проверки данных разработчики могут предоставлять пользователям список выбора, ограничивать ввод данных определенного типа или размера и т. д.
В Aspose.Cells for JavaScript через C++, у каждого класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) есть коллекция [**validations**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#validations--), которая представляет собой коллекцию объектов [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation). Для настройки валидации задайте некоторые свойства класса [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) следующим образом:

- Тип – представляет тип проверки, который можно задать, используя один из предопределённых значений перечисления [**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype).
- Оператор – представляет оператор, используемый при проверке, который можно задать с помощью одного из предопределённых значений перечисления [**OperatorType**](https://reference.aspose.com/cells/javascript-cpp/operatortype).
- Формула1 – представляет значение или выражение, связанное с первой частью валидации данных.
- Формула2 – представляет значение или выражение, связанное со второй частью валидации данных.

Когда свойства объекта [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) настроены, разработчики могут использовать структуру [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) для хранения информации о диапазоне ячеек, которые будут проверены с помощью созданной проверки.

#### **Типы проверки данных**

Перечисление [**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype) содержит следующие члены:

|**Название элемента**|**Описание**|
| :- | :- |
|AnyValue|Обозначает значение любого типа.|
|WholeNumber|Обозначает тип проверки для целых чисел.|
|Decimal|Обозначает тип проверки для десятичных чисел.|
|List|Обозначает тип проверки для выпадающего списка.|
|Date|Обозначает тип проверки для дат.|
|Time|Обозначает тип проверки для времени.|
|TextLength|Обозначает тип проверки для длины текста.|
|Custom|Обозначает настраиваемый тип проверки.|

##### **Проверка данных на целые числа**

С помощью этого типа валидации пользователи могут вводить только целые числа в пределах заданного диапазона в проверяемых ячейках. Последующие примеры показывают, как реализовать тип валидации WholeNumber. Этот пример создает такую же проверку данных с помощью Aspose.Cells for JavaScript через C++, как и в Microsoft Excel выше.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');

            if (fileInput.files.length > 0) {
                // If a file is provided, we will open it; otherwise create a new workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                // Instantiate workbook from uploaded file
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook
                var workbook = new Workbook();
            }

            // Create a worksheet and get the first worksheet.
            const ExcelWorkSheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Creating a Validation object
            const idx = validations.add(ca);
            const validation = validations.get(idx);

            // Setting the validation type to whole number
            validation.type = AsposeCells.ValidationType.WholeNumber;

            // Setting the operator for validation to Between
            validation.operator = AsposeCells.OperatorType.Between;

            // Setting the minimum value for the validation
            validation.formula1 = "10";

            // Setting the maximum value for the validation
            validation.formula2 = "1000";

            // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
            const area = new AsposeCells.CellArea();
            area.startRow = 0;
            area.endRow = 1;
            area.startColumn = 0;
            area.endColumn = 1;

            // Adding the cell area to Validation
            validation.addArea(area);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Validation added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Проверка данных на список**

Этот тип проверки позволяет пользователю вводить значения из выпадающего списка. Он предоставляет список: серию строк, содержащих данные. В примере во втором рабочем листе добавляется список источников. Пользователи могут выбирать значения только из списка. Область проверки - это диапазон ячеек A1:A5 на первом рабочем листе.

Важно отметить, что необходимо установить свойство [**Validation.inCellDropDown(boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown-boolean-) в значение **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // This example creates a new workbook in the browser (file input is optional here).
            const workbook = new Workbook();

            // Get the first worksheet.
            const worksheet1 = workbook.worksheets.get(0);

            // Add a new worksheet and access it.
            const i = workbook.worksheets.add();
            const worksheet2 = workbook.worksheets.get(i);

            // Create a range in the second worksheet.
            const range = worksheet2.cells.createRange("E1", "E4");

            // Name the range.
            range.name = "MyRange";

            // Fill different cells with data in the range.
            range.get(0, 0).value = "Blue";
            range.get(1, 0).value = "Red";
            range.get(2, 0).value = "Green";
            range.get(3, 0).value = "Yellow";

            // Get the validations collection.
            const validations = worksheet1.validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Create a new validation to the validations list.
            const validation = validations.get(validations.add(ca));

            // Set the validation type.
            validation.type = ValidationType.List;

            // Set the operator.
            validation.operator = OperatorType.None;

            // Set the in cell drop down.
            validation.inCellDropDown = true;

            // Set the formula1.
            validation.formula1 = "=MyRange";

            // Enable it to show error.
            validation.showError = true;

            // Set the alert type severity level.
            validation.alertStyle = ValidationAlertType.Stop;

            // Set the error title.
            validation.errorTitle = "Error";

            // Set the error message.
            validation.errorMessage = "Please select a color from the list";

            // Specify the validation area.
            const area = new CellArea();
            area.startRow = 0;
            area.endRow = 4;
            area.startColumn = 0;
            area.endColumn = 0;

            // Add the validation area.
            validation.addArea(area);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation list created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


##### **Проверка данных на дату**

С этим типом проверки пользователи вводят значения дат в указанном диапазоне или отвечающие определенным критериям в проверяемые ячейки. В примере пользователь ограничен вводом дат с 1970 по 1999 год. Здесь область проверки – ячейка B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Date Validation Example</h1>
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
            // This example creates a new workbook in the browser (no file input required)
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into the A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter Date b/w 1/1/1970 and 12/31/1999";

            // Set row height and column width for the cells by accessing row/column objects
            const row0 = cells.rows.get(0);
            row0.height = 31;
            const col0 = cells.columns.get(0);
            col0.width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = AsposeCells.ValidationType.Date;

            // Set the operator for the data validation
            validation.operator = AsposeCells.OperatorType.Between;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "1/1/1970";

            // The value or expression associated with the second part of the data validation.
            validation.formula2 = "12/31/1999";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = AsposeCells.ValidationAlertType.Stop;

            // Set the title of the data-validation error dialog box
            validation.errorTitle = "Date Error";

            // Set the data validation error message.
            validation.errorMessage = "Enter a Valid Date";

            // Set and enable the data validation input message.
            validation.inputMessage = "Date Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and validation added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

##### **Проверка данных на время**

С этим типом проверки пользователи могут вводить время в указанном диапазоне, или соответствующее некоторым критериям, в проверяемые ячейки. В примере пользователь ограничен вводом времени с 09:00 по 11:30 утра. Здесь область проверки – ячейка B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Time Validation Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into A1 cell.
            const a1 = cells.get("A1");
            a1.value = "Please enter Time b/w 09:00 and 11:30 'o Clock";

            // Set the row height and column width for the cells using row/column objects.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation and obtain it.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type and other properties.
            validation.type = AsposeCells.ValidationType.Time;
            validation.operator = AsposeCells.OperatorType.Between;
            validation.formula1 = "09:00";
            validation.formula2 = "11:30";
            validation.showError = true;
            validation.alertStyle = AsposeCells.ValidationAlertType.Information;
            validation.errorTitle = "Time Error";
            validation.errorMessage = "Enter a Valid Time";
            validation.inputMessage = "Time Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Проверка данных на длину текста**

С помощью этого типа проверки пользователи могут вводить текстовые значения заданной длины в проверяемые ячейки. В примере пользователь ограничен вводом строковых значений не более 5 символов. Область проверки - это ячейка B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Text Length Validation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // Create a new workbook.
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Put a string value into A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter a string not more than 5 chars";

            // Set row height and column width for the cell.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = ValidationType.TextLength;

            // Set the operator for the data validation.
            validation.operator = OperatorType.LessOrEqual;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "5";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = ValidationAlertType.Warning;

            // Set the title of the data-validation error dialog box.
            validation.errorTitle = "Text Length Error";

            // Set the data validation error message.
            validation.errorMessage = " Enter a Valid String";

            // Set and enable the data validation input message.
            validation.inputMessage = "TextLength Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Правила проверки данных**

При реализации проверок данных можно проверить их, присваивая ячейкам разные значения. [**cell.validationValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) можно использовать для получения результата проверки. Следующий пример демонстрирует эту возможность с разными значениями. Тестовый файл можно скачать по следующей ссылке для проверки:

[sampleDataValidationRules.xlsx](77496339.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Data Validation Check Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            const messages = [];

            // Enter 3 inside this cell
            // Since it is not between 10 and 20, it should fail the validation
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const isValid3 = cell.validationValue;
            messages.push(`Is 3 a Valid Value for this Cell: ${isValid3}`);

            // Enter 15 inside this cell
            // Since it is between 10 and 20, it should succeed the validation
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const isValid15 = cell.validationValue;
            messages.push(`Is 15 a Valid Value for this Cell: ${isValid15}`);

            // Enter 30 inside this cell
            // Since it is not between 10 and 20, it should fail the validation again
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const isValid30 = cell.validationValue;
            messages.push(`Is 30 a Valid Value for this Cell: ${isValid30}`);

            // Display results
            resultDiv.innerHTML = messages.map(m => `<p>${m}</p>`).join('');

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```


## **Проверить, если проверка в ячейке выпадающая**

Как мы увидели, существует много видов проверок, которые можно реализовать внутри ячейки. Если вы хотите проверить, является ли проверка списком выбора или нет, для этого можно использовать метод [**validation.inCellDropDown**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown--). Следующий пример показывает, как применяется эта функция. Тестовый файл для проверки можно скачать по следующей ссылке:

[sampleValidation.xlsx](79527947.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Data Validation Drop-downs</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the worksheet named "Sheet1"
            const sheet = workbook.worksheets.get("Sheet1");
            const cells = sheet.cells;

            const appendMessage = (msg, color = 'black') => {
                const p = document.createElement('p');
                p.style.color = color;
                p.textContent = msg;
                resultDiv.appendChild(p);
            };

            const checkDropDown = (cell, cellRef) => {
                const validation = cell.validation;
                if (validation.inCellDropDown) {
                    appendMessage(`${cellRef} is a dropdown`, 'green');
                } else {
                    appendMessage(`${cellRef} is NOT a dropdown`, 'orange');
                }
            };

            checkDropDown(cells.get("A2"), "A2");
            checkDropDown(cells.get("B2"), "B2");
            checkDropDown(cells.get("C2"), "C2");
        });
    </script>
</html>
```


## **Добавить CellArea к существующей Validation**

Могут быть ситуации, когда вы захотите добавить [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) к существующему [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation). При добавлении [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) с помощью [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-) Aspose.Cells проверяет все существующие области, чтобы убедиться, что новая область уже не существует. Если файл содержит много проверок, это может повлиять на производительность. Чтобы этого избежать, API предоставляет метод [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-). Параметр *checkIntersection* указывает, нужно ли проверять пересечение области с существующими зонами проверки. Установка его в **false** отключит проверку других областей. Параметр *checkEdge* указывает, нужно ли проверять применяемые области. Если новая область становится верхним левым углом, внутренние настройки пересоздаются. Если вы уверены, что новая зона не является верхним левым углом, вы можете задать этот параметр как **false**.

Следующий фрагмент кода демонстрирует использование метода [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-) для добавления новой [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) к существующим [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Validations</title>
    </head>
    <body>
        <h1>Validations Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validation = worksheet.validations.get(0);

            // Create your cell area.
            const cellArea = AsposeCells.CellArea.createCellArea("D5", "E7");

            // Adding the cell area to Validation
            validation.addArea(cellArea, false, false);

            // Save the output workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ValidationsSample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation area added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Исходный и выходной файлы Excel прикреплены для справки.

[Исходный файл](96928093.xlsx)

[Выходной файл](96928220.xlsx)

## **Продвинутые темы**
- [Получить проверку ячейки в файлах ODS](/cells/ru/javascript-cpp/get-cell-validation-in-ods-files/)
- [Получить примененную проверку данных к ячейке](/cells/ru/javascript-cpp/get-validation-applied-on-a-cell/)
- [Проверьте, что значение ячейки удовлетворяет правилам проверки данных](/cells/ru/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/)
