---
title: Транспонирование диапазона
linktitle: Транспонирование диапазона
description: Эта статья объясняет, как транспонировать или вращать данные из строк в столбцы и наоборот в файлах Excel с использованием Aspose.Cells for JavaScript via C++ с тремя различными подходами.
keywords: Aspose.Cells, JavaScript via C++, электронная таблица, транспонирование диапазона, вращение данных, функция транспонирования, формула динамического массива, массивная формула, Excel TRANSPOSE, строки в столбцы
type: docs
weight: 80
url: /ru/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ поддерживает транспонирование (поворот) данных, позволяя превратить строки в столбцы и столбцы в строки тремя различными способами. Первый подход использует метод `range.transpose()` «на месте» и работает во всех версиях Excel, второй — `cell.setDynamicArrayFormula()` для записи современной формулы динамического массива `=TRANSPOSE(...)`, которая автоматически «разливается» в Excel 365 или Excel 2021. Третий подход использует `cell.setArrayFormula()` для записи классической формулы Ctrl+Shift+Enter (CSE), совместимой со старыми версиями Excel. В этой статье рассматриваются каждый из подходов с пошаговыми инструкциями и полными примерами кода.
{{% /alert %}}

## **Введение**
Транспонирование диапазона означает вращение его таким образом, чтобы прежняя строка стала столбцом, а прежний столбец — строкой, фактически отражая данные относительно главной диагонали. В Microsoft Excel функция листа `TRANSPOSE` выполняет эту операцию, подробное описание доступно по ссылке https://support.microsoft.com/en-us/excel/functions/transpose-function. Эта концепция может быть применена программно к диапазону ячеек, что полезно во многих бизнес‑ и отчётных сценариях.  
- Перераспределение квартальных или годовых отчётов о продажах, когда кварталы обычно располагаются по строкам, а регионы — по столбцам, или наоборот.  
- Смена ориентации осей в панелях мониторинга или диаграммах, чтобы временной ряд отображался по строкам вместо по столбцам.  
- Преобразование данных, импортированных из внешних систем, чтобы они соответствовали требуемому макету для последующего анализа или шаблонов отчётов.  
Для наглядности все примеры используют небольшую таблицу продаж по регионам и кварталам. В образце рабочей книги эта таблица занимает диапазон **A1:D5**, при этом **A1** оставлена пустой как левый верхний угол, **B1:D1** содержат заголовки регионов, а **A2:A5** — заголовки кварталов.  
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
Статья затем представляет три разных способа транспонирования этих данных с помощью Aspose.Cells for JavaScript via C++, каждый из которых подходит для определённой версии Excel и конкретного сценария.

## **Подход 1 — Транспонирование диапазона на месте (Range.transpose)**
Используйте этот подход, когда необходимо транспонировать данные без применения функции листа `TRANSPOSE`. Он работает **во всех версиях Excel** и не зависит от динамических массивов, что делает его самым надёжным решением кросс‑версий. Подойдёт, если вам нужен только окончательный транспонированный результат и нет необходимости сохранять формулу `TRANSPOSE` в книге.

### **Используемый API**
`Range.transpose()` — метод экземпляра класса `Aspose.Cells.Range`. Вызов меняет диапазон «на месте», переставляя его строки и столбцы, то есть строка становится столбцом и наоборот. Метод изменяет ячейки напрямую без записи формулы.

### **Шаги**
1. Откройте исходную рабочую книгу, задав `LoadOptions` с форматом `.xlsx`, вызвав `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.  
2. Получите первый **рабочий лист** книги с помощью `workbook.getWorksheets().get(0)`.  
3. Получите коллекцию ячеек рабочего листа через `worksheet.getCells()`.  
4. Создайте исходный диапазон, охватывающий **A1:D5**, вызвав `cells.createRange("A1:D5")`.  
5. Вызовите `source.transpose()`, чтобы вращать диапазон «на месте», меняя строки и столбцы местами.  
6. Сохраните книгу с помощью `workbook.save(outputFile)`.  
После транспонирования в этом **якорном диапазоне** находятся повернутые данные. Первая строка читается как (пусто, **Europe**, **Asia**, **North America**), а первый столбец — как (пусто, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Каждый исходный столбец продаж превращается в строку в транспонированном диапазоне.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **Подход 2 — Транспонирование с помощью формулы динамического массива (Excel 365 / 2021)**
Применяйте этот подход, когда нужно сохранить формулу `=TRANSPOSE(A1:D5)` в виде живой формулы в результирующей книге, чтобы результат обновлялся автоматически при изменении исходных данных, и целевой файл будет открыт в **Excel 365 / Excel 2021 или новее**, где поддерживаются динамические массивы и оператор «разлив».

### **Используемый API**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` — метод класса `Aspose.Cells.Cell`, задающий формулу ячейки как **формулу динамического массива**. Excel вычисляет формулу один раз и автоматически «разливает» результат в соседние ячейки. Третий параметр, установленный в `true`, инструктирует Aspose.Cells также вычислить значения при записи.

### **Шаги**
1. Загрузите исходную рабочую книгу, используя `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.  
2. Получите первый **рабочий лист** и доступ к его коллекции ячеек.  
3. Разместите формулу динамического массива в ячейке **A6**, сразу под исходным диапазоном, вызвав `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.  
4. Параметр `new FormulaParseOptions()` использует настройки по умолчанию, а третий аргумент `true` указывает Aspose.Cells рассматривать формулу как динамический массив и вычислять её, чтобы разлитые значения были записаны в книгу.  
5. Сохраните книгу с помощью `workbook.save(outputFile)`.  
Ячейка **A6** содержит формулу `=TRANSPOSE(A1:D5)`, и Excel автоматически «разливает» результат в диапазон **A6:E9** — блок 4 строки × 5 столбцов, соответствующий транспонированным данным.

{{% alert color="primary" %}}
Этот подход работает **только в Excel 365 / 2021 или новее**. Более старые версии Excel не будут корректно разливать формулы динамического массива.
{{% /alert %}}

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
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Подход 3 — Транспонирование с помощью классической массивной формулы (CSE)**
Применяйте этот подход, когда необходимо сохранить формулу `TRANSPOSE` в книге, но целевой файл может открываться в **старых версиях Excel (до 2021, включая 2019, 2016, 2013 и др.)**, где разлив динамических массивов не поддерживается. Классическая формула Ctrl+Shift+Enter (CSE) — это совместимый со всеми версиями вариант.

### **Используемый API**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` — метод класса `Aspose.Cells.Cell`, назначающий **классическую массивную (CSE) формулу** якорной ячейке и объявляющий размеры результирующего массива. Aspose.Cells записывает маркер многоклеточной формулы, поэтому Excel вычисляет её как единое массивное выражение, заполняющее указанный диапазон.

### **Шаги**
1. Загрузите исходную рабочую книгу, как описано в предыдущих подходах.  
2. Получите первый **рабочий лист** и доступ к его коллекции ячеек.  
3. Вызовите `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Второй аргумент `4` — количество строк целевого массива, третий аргумент `5` — количество столбцов.  
4. Сохраните книгу с помощью `workbook.save(outputFile)`.  
Ячейка **A6** служит **якорной ячейкой** массивной формулы, а вычисленный массив охватывает 4 строки × 5 столбцов, начиная с A6, соответствуя транспонированным размерам исходного диапазона A1:D5. Excel записывает единый маркер формулы по всему диапазону, поэтому старые версии корректно её обрабатывают.

{{% alert color="primary" %}}
Массивные формулы CSE — классический способ Excel оценить выражение `TRANSPOSE`, и этот подход совместим со всеми версиями Excel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // Загрузить исходную книгу с параметрами загрузки xlsx
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // Получить доступ к первому рабочему листу и его коллекции ячеек
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Установить классическую формулу массива CSE в ячейку A6.
                // Формула =TRANSPOSE(A1:D5) вращает исходный диапазон 5 строк на 4 столбца
                // в массив 4 строки на 5 столбцов. Второй аргумент (4) — количество строк,
                // а третий аргумент (5) — количество столбцов получаемого массива.
                // Aspose.Cells записывает маркер формулы массива CSE, чтобы Excel вычислял её как
                // одну многоклеточную формулу массива, совместимую со старыми версиями Excel
                // (2019, 2016, 2013 и др.), которые не поддерживают динамический массивный вывод.
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // Сохранить книгу, чтобы маркер формулы массива был сохранён
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Сравнение — Когда использовать каждый подход**
| Подход | API / Метод | Версия Excel | Сохранена исходная формула? | Выходной диапазон |
|--------|--------------|--------------|----------------------------|-------------------|
| Подход 1 — Транспонирование на месте | `range.transpose()` | Все версии Excel | Нет (только значения) | Исходный якорный диапазон, 5×4 |
| Подход 2 — Формула динамического массива | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | Да (разливается динамически) | Разлито от якоря |
| Подход 3 — Классическая массивная формула (CSE) | `cell.setArrayFormula()` | Все версии Excel | Да (многоклеточная формула) | Явный размер, 4×5 |
Используйте **Подход 1**, когда требуется быстрая кросс‑версионная трансформация и нужны лишь транспонированные значения в файле. Примените **Подход 2**, если гарантировано использование современного Excel и требуется, чтобы формула оставалась живой и обновлялась при изменении исходных данных. Выбирайте **Подход 3**, когда нужна максимальная совместимость и сохранение формулы во всех версиях Excel, включая старые, не поддерживающие динамические массивы.

{{< app/cells/assistant language="javascript-cpp" >}}