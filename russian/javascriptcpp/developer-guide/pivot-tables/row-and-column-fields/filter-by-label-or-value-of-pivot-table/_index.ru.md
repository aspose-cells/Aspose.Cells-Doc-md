---
title: Фильтрация сводных таблиц по метке или значению
linktitle: Фильтрация сводных таблиц по метке или значению
description: Aspose.Cells for JavaScript via C++ поддерживает расширенные возможности фильтрации сводных таблиц. В этой статье рассматриваются фильтрация данных сводной таблицы с помощью фильтров по меткам, датам и значениям, фильтра «10 лучших», а также скрытие и отображение элементов сводной таблицы.
keywords: Aspose.Cells, библиотека для JavaScript via C++, электронная таблица, сводная таблица, фильтрация, фильтр по метке, фильтр по значению, фильтр по дате, фильтр «10 лучших», элемент сводной таблицы, скрытие элемента сводной таблицы
type: docs
weight: 10
url: /ru/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предлагает пять практических стратегий фильтрации данных, отображаемых в сводной таблице. К текстовым полям строк или столбцов можно применять фильтры по меткам; фильтры по датам используются, когда поле содержит только ячейки с датой и временем или пустые ячейки; фильтры по значениям применяются к агрегированным числам; фильтр «10 лучших» обеспечивает ранжирование по полю значений. Отдельные элементы сводной таблицы можно также вручную скрывать и отображать с помощью свойства `isHidden`. Каждая стратегия доступна через специализированные API в классах `PivotField` и `PivotItem`.
{{% /alert %}}

## **Введение**
Сводные таблицы являются мощными аналитическими инструментами, однако исходные сводные данные зачастую содержат значительно больше информации, чем необходимо представить. Фильтрация — основной механизм сужения сводной таблицы до строк, столбцов или значений, важных для конкретного отчета. Aspose.Cells for JavaScript via C++ предоставляет программный доступ к возможностям фильтрации, соответствующим возможностям Microsoft Excel, что позволяет полностью автоматизировать создание отчетов.

В этой статье рассматриваются следующие стратегии фильтрации:

1. **Фильтр по метке** — фильтрует элементы полей строк или столбцов по их текстовым меткам.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, содержащие только значения даты и времени или пустые значения.
3. **Фильтр по значению** — фильтрует элементы по агрегированным значениям поля данных.
4. **Фильтр «10 лучших»** — отображает только N наибольших или N наименьших элементов, ранжированных по полю значений.
5. **Скрытие и отображение элементов сводной таблицы** — обеспечивает ручное управление видимостью каждого отдельного элемента в поле.

Каждый подход использует отдельный метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `pivotCache.refresh()` для сводной таблицы, чтобы кэшированные данные и вычисленные значения отражали новое состояние фильтра.

## **Фильтр по метке**
Фильтр по метке позволяет фильтровать элементы поля строки или столбца, сравнивая их текстовые подписи с заданным шаблоном. Это полезно, если требуется отображать только продукты, названия которых начинаются с определенной буквы, содержат конкретное слово или соответствуют другому критерию на основе подписи.

Aspose.Cells предоставляет фильтрацию по меткам с помощью метода `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. Аргумент `filterType` определяет режим сравнения (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и т. д.). Аргументы `label1` и `label2` задают текст для сравнения — передайте `""` для `label2`, если достаточно одного условия сравнения, например «начинается с» или «содержит».

В следующем примере загружается рабочая книга с существующей сводной таблицей и применяется фильтр по метке, при котором остаются видимыми только элементы, подписи которых начинаются с заданного префикса. Затем сводная таблица обновляется, а результат сохраняется.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **Фильтр по дате**
Фильтры по дате позволяют сузить сводную таблицу с помощью критериев, связанных с датами, например по сегодняшнему дню, прошлой неделе, текущему месяцу, следующему кварталу или определенному диапазону дат. Это специализированные фильтры, применимые только к полям, содержащим сведения о дате и времени.

{{% alert color="primary" %}}
Фильтр по дате работает только тогда, когда область строк или столбцов содержит исключительно ячейки с датой и временем либо пустые ячейки. Если исходное поле содержит другие типы данных, например числа или текст, фильтр по дате не даст ожидаемого результата. Перед применением фильтра убедитесь, что поле отформатировано как дата, а все значения представлены допустимыми экземплярами `DateTime` или пустыми ячейками.

Aspose.Cells предоставляет фильтрацию по датам с помощью метода `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. Перечисление `PivotFilterType` содержит специальные значения для фильтрации по датам, например `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра передается одно или два значения `DateTime` (для `Between` передаются начальная и конечная даты).

В следующем примере загружается рабочая книга со сводной таблицей, в области строк которой находится поле даты. Затем применяется фильтр по дате, ограничивающий видимые элементы определенным диапазоном дат, сводная таблица обновляется, а рабочая книга сохраняется.
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
        const { Workbook } = AsposeCells;
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
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **Фильтр по значению**
Фильтры по значениям применяются к агрегированным значениям, которые сводная таблица вычисляет в области данных. Вместо сопоставления текстовых меток они сравнивают числовые итоги с пороговым значением. Типичные сценарии использования — отображение только продуктов, сумма продаж которых превышает заданное значение, или только регионов, количество транзакций которых находится в определенном диапазоне.

Aspose.Cells предоставляет фильтрацию по значениям с помощью метода `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Параметр `valueFieldIndex` указывает, какое поле данных используется для вычисления значений (используйте `pivotTable.getDataFields().indexOf(dataField)` или переберите коллекцию, чтобы найти позицию). Параметр `filterType` принимает значения, например `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Два аргумента `double` задают одно или два пороговых значения.

В следующем примере загружается рабочая книга со сводной таблицей и применяется фильтр по значению, оставляющий только элементы, суммарные продажи которых превышают числовой порог. Затем сводная таблица обновляется, а рабочая книга сохраняется.

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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.pivotCache.refresh();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Фильтр «10 лучших»**
Фильтр «10 лучших» — специализированная разновидность фильтра по значениям, которая оставляет только N наибольших или N наименьших элементов по выбранному полю значений. Его часто используют для отчетов с ранжированием, например «10 продуктов с наибольшей выручкой» или «5 регионов с наименьшим количеством продаж».

{{% alert color="primary" %}}
Фильтр «10 лучших» действует только тогда, когда в области данных сводной таблицы есть одно или несколько полей значений. Без хотя бы одного поля значения не существует агрегированной метрики, по которой можно ранжировать элементы, поэтому применить фильтр нельзя.

Aspose.Cells предоставляет фильтрацию «10 лучших» с помощью метода `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Параметр `valueFieldIndex` — индекс поля данных, агрегированные значения которого используются для ранжирования элементов; `filterType` определяет, как интерпретируется `itemCount` (`Count` оставляет фиксированное число элементов, `Percent` — процент элементов, поэтому `itemCount` задает сам процент); `isTop` указывает, следует ли оставить элементы с наибольшими (true) или наименьшими (false) значениями, а `itemCount` задает, сколько элементов или какой процент следует оставить.

В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значения, и применяется фильтр «10 лучших», чтобы оставить только 10 элементов с наибольшей суммой продаж. Затем сводная таблица обновляется, а рабочая книга сохраняется.
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
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
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
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **Фильтрация путем скрытия или отображения элементов сводной таблицы**
Помимо структурированных API для фильтрации, Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Для этого переберите коллекцию `pivotField.getPivotItems()` объекта `PivotField` и переключайте свойство `isHidden`, чтобы выборочно скрывать определенные элементы без применения фильтра на основе формулы. Установка `pivotItem.isHidden = true` скрывает элемент в сводной таблице, а установка `pivotItem.isHidden = false` отменяет скрытие и снова делает элемент видимым.

Этот подход полезен, если правило фильтрации является нестандартным или зависящим от конкретных элементов, например если необходимо скрыть небольшое число категорий с заданными именами, которые не должны отображаться в определенном отчете. В примере ниже загружается рабочая книга со сводной таблицей, скрывается конкретный элемент по имени, а затем демонстрируется его отображение. После этого сводная таблица обновляется, а рабочая книга сохраняется.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Сводка**
Aspose.Cells for JavaScript via C++ предоставляет полный набор возможностей фильтрации сводных таблиц, аналогичный доступным в Microsoft Excel. Фильтры по меткам, датам и значениям охватывают наиболее распространенные аналитические сценарии, а фильтр «10 лучших» предназначен для отчетов с ранжированием. Если правило фильтрации нестандартное, свойство `pivotItem.isHidden` предлагает гибкий резервный механизм на уровне отдельных элементов. Сочетание этих стратегий — например, применение фильтра по метке с последующим скрытием определенных элементов — позволяет создавать точно настроенные отчеты сводных таблиц исключительно с помощью кода.

{{< app/cells/assistant language="javascript-cpp" >}}