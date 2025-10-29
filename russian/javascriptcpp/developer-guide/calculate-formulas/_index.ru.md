---
title: Вычисление формул с помощью JavaScript через C++
linktitle: Расчет формул
description: В этой статье рассказывается о том, как использовать библиотеку Aspose.Cells для вычисления формул в Microsoft Excel с помощью JavaScript через C++. Загружая существующий файл Excel или создавая новый, мы можем использовать предоставленные Aspose.Cells методы для вычисления формулы и получения результата. В конце мы сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, формулы, вычисления, прямое вычисление формул, многократное вычисление формул, добавление формул JavaScript через C++
type: docs
weight: 125
url: /ru/javascript-cpp/calculate-formulas/
---

## **Добавление формул и вычисление результатов**

У Aspose.Cells встроен движок вычисления формул. Он может не только пересчитывать импортированные из шаблонов Excel формулы, но и поддерживает вычисление результатов добавленных формул в режиме выполнения.

Поддержка Aspose.Cells большинства формул или функций, входящих в Microsoft Excel (см. [список поддерживаемых функций движком вычислений](/cells/ru/javascript-cpp/supported-formula-functions/)). Эти функции можно использовать через API или через дизайн таблиц. Aspose.Cells поддерживает большой набор математических, строковых, логических, дата/время, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) или методы [**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-) класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) для добавления формулы в ячейку. При применении формулы всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

Чтобы вычислить результаты формул, пользователь может вызвать метод [**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который обрабатывает все встроенные формулы в файле Excel. Или пользователь может вызвать метод [**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet), который обрабатывает все формулы внутри листа. Или пользователь может также вызвать метод [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-) класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), который обрабатывает формулу одной ячейки:

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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **Важно знать о формулах**

{{% alert color="primary" %}}

Свойство **Formula** и методы **formula(...)** класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) отличаются от методов **calculate** классов [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) и [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Свойство **Formula** и методы **formula(...)** просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Для получения результата формул вызовите методы **calculate**.

{{% /alert %}}

## **Прямое вычисление формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Кроме того, в Aspose.Cells можно вычислять результаты формул непосредственно, импортированных из файла дизайнера.

Иногда нужно вычислить результаты формул напрямую, не добавляя их в лист. Значения ячеек, используемых в формуле, уже существуют в листе, и все, что нужно — это найти результат этих значений на основе формулы Microsoft Excel без добавления самой формулы в лист.

Можно использовать API движка вычислений формул Aspose.Cells для [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) для получения результатов таких формул без добавления их в лист:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

Приведенный выше код производит следующий вывод:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Как рассчитать формулы повторно**

Если в рабочей книге много формул и необходимо повторно вычислять их при изменении только части, может быть полезно включить цепочку вычислений формул: [**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка вычислений отключена. Создание цепочки занимает дополнительное время, поэтому первый расчет формул ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)) может потреблять больше ресурсов процессора и памяти по сравнению с вычислением без цепочки. Если повторный расчет формул не требуется, лучше оставить поведение по умолчанию (без цепочки).

{{% /alert %}}

## **Продвинутые темы**
- [Добавление ячеек в окно наблюдения формул Microsoft Excel](/cells/ru/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Вычисление функции IFNA с помощью Aspose.Cells](/cells/ru/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [Расчет массивной формулы таблиц данных](/cells/ru/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [Расчет функций MINIFS и MAXIFS Excel 2016](/cells/ru/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшение времени вычисления метода Cell.calculate](/cells/ru/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Обнаружение циклических ссылок](/cells/ru/javascript-cpp/detecting-circular-reference/)
- [Прямой расчет пользовательской функции без записи ее на лист](/cells/ru/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Реализация пользовательского расчетного механизма для расширения расчетного механизма по умолчанию Aspose.Cells](/cells/ru/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Прерывание или отмена расчета формул книги](/cells/ru/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Возвращение диапазона значений с использованием абстрактного расчетного механизма](/cells/ru/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Установка режима расчета формул книги](/cells/ru/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [Использование функции FormulaText в Aspose.Cells](/cells/ru/javascript-cpp/using-formulatext-function-in-aspose-cells/)
