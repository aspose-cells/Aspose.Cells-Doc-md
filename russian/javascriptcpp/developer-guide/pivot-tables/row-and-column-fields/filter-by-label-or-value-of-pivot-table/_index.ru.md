---
title: Фильтрация сводных таблиц по метке или значению
linktitle: Фильтрация сводных таблиц по метке или значению
description: Aspose.Cells for JavaScript via C++ поддерживает расширенные возможности фильтрации сводных таблиц. В этой статье объясняется, как фильтровать данные сводной таблицы с помощью фильтров по меткам, фильтров по датам, фильтров по значениям, фильтров топ-10, а также скрывать или отображать элементы сводной таблицы.
keywords: Aspose.Cells, библиотека JavaScript via C++, электронная таблица, сводная таблица, фильтр, фильтр по метке, фильтр по значению, фильтр по дате, фильтр топ-10, элемент сводной таблицы, скрытие элемента сводной таблицы
type: docs
weight: 10
url: /ru/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет пять практических стратегий фильтрации данных, отображаемых в сводной таблице. К текстовым полям в областях строк или столбцов можно применять фильтры по меткам; фильтры по датам — только если поле содержит исключительно ячейки с датой и временем или пустые значения; фильтры по значениям предназначены для агрегированных числовых значений; фильтры топ-10 позволяют ранжировать элементы по полю значений. Отдельные элементы сводной таблицы также можно вручную скрывать и отображать с помощью свойства `isHidden`. Каждая стратегия доступна через отдельные API в классах `PivotField` и `PivotItem`.
{{% /alert %}}

## **Введение**
Сводные таблицы — мощный аналитический инструмент, однако необработанные итоги часто содержат значительно больше информации, чем необходимо для конкретного отчета. Фильтрация — основной механизм, позволяющий сузить сводную таблицу до нужных строк, столбцов или значений. Aspose.Cells for JavaScript via C++ предоставляет те же возможности фильтрации, что и Microsoft Excel, и позволяет полностью автоматизировать создание отчетов с помощью программного интерфейса.
В этой статье рассматриваются следующие стратегии фильтрации:
1. **Фильтр по метке** — фильтрует элементы поля строки или поля столбца по их текстовым меткам.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, содержащие только значения даты и времени или пустые значения.
3. **Фильтр по значению** — фильтрует элементы по агрегированным значениям поля данных.
4. **Фильтр топ-10** — отображает только N элементов с наибольшими или наименьшими значениями в соответствии с ранжированием по полю значений.
5. **Скрытие и отображение элементов сводной таблицы** — позволяет вручную управлять видимостью каждого отдельного элемента поля.
Каждый подход использует отдельный метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `pivotCache.refresh()` для сводной таблицы, чтобы кэшированные данные и вычисленные значения отражали новое состояние фильтра.

## **Фильтр по метке**
Фильтр по метке позволяет отбирать элементы поля строки или поля столбца путем сравнения их текстовых подписей с заданным шаблоном. Это полезно, если требуется отображать только продукты, названия которых начинаются с определенной буквы, содержат конкретное слово или соответствуют другому критерию, основанному на подписях.
Aspose.Cells предоставляет фильтрацию по метке через метод `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. Аргумент `filterType` задает режим сравнения (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и т. д.). Аргументы `label1` и `label2` задают текст для сравнения — передайте `""` для `label2`, если для сравнения достаточно одного значения (например, «начинается с» или «содержит»).
В следующем примере загружается рабочая книга с существующей сводной таблицей, применяется фильтр по метке, чтобы оставить видимыми только элементы, подписи которых начинаются с указанного префикса, затем обновляется сводная таблица и сохраняется результат.

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
                    // Загрузить существующую книгу, содержащую сводную таблицу
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Получить лист по индексу (первый лист)
                    const worksheet = workbook.worksheets.get(0);
                    // Получить сводную таблицу по индексу
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Получить первое поле строки PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Применить фильтр меток — отображать только элементы строк, метки которых начинаются с указанного префикса
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Обновить и пересчитать данные сводной таблицы, чтобы применить фильтр
                    pivotTable.refreshData();
                    // Сохранить книгу обратно на диск
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
Фильтры по дате позволяют сузить сводную таблицу по критериям, связанным с датами, например «сегодня», «прошлая неделя», «текущий месяц», «следующий квартал» или конкретный диапазон дат. Это специализированные фильтры, которые работают только с полями, содержащими сведения о дате и времени.

{{% alert color="primary" %}}
Фильтр по дате работает только тогда, когда область строк или столбцов содержит исключительно ячейки с датой и временем либо пустые значения. Если исходное поле содержит другие типы данных, например числа или текст, фильтр по дате не даст ожидаемого результата. Перед применением фильтра убедитесь, что для поля установлен формат даты и что все его значения являются допустимыми экземплярами `DateTime` или пустыми ячейками.
Aspose.Cells предоставляет фильтрацию по дате через метод `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. Перечисление `PivotFilterType` содержит отдельные значения, связанные с датами, например `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра передается одно или два значения `DateTime`; для `Between` передаются начальная и конечная даты.
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
                // Загрузить существующую книгу, содержащую сводную таблицу
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Получить доступ к листу, содержащему сводную таблицу (по индексу)
                const worksheet = workbook.worksheets.get(0);
                // Получить доступ к сводной таблице по индексу
                const pivotTable = worksheet.pivotTables.get(0);
                // Получить поле даты PivotField из области строк
                // (Фильтр по дате работает только тогда, когда область строк/столбцов содержит только ячейки с датой и временем или пустые ячейки)
                const dateField = pivotTable.rowFields.get(0);
                // Определить критерий даты для фильтра «Между»
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Применить фильтр по дате к полю сводной таблицы
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Обновить и пересчитать сводную таблицу, чтобы фильтр вступил в силу
                pivotTable.refreshData();
                // Сохранить книгу
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
Фильтры по значениям работают с агрегированными значениями, которые сводная таблица вычисляет в области данных. Вместо сопоставления с текстовыми метками они сравнивают числовые итоги с пороговым значением. Типичные сценарии применения — отображение только продуктов, сумма продаж которых превышает заданное значение, или только регионов, количество транзакций которых попадает в определенный диапазон.
Aspose.Cells предоставляет фильтрацию по значениям через метод `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Параметр `valueFieldIndex` указывает, какое поле данных следует использовать для вычислений (используйте `pivotTable.getDataFields().indexOf(dataField)` или переберите коллекцию, чтобы найти нужную позицию). Параметр `filterType` использует такие значения, как `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Пороговые значения задаются двумя аргументами типа `double`.
В следующем примере загружается рабочая книга со сводной таблицей, применяется фильтр по значению, сохраняющий только элементы, у которых агрегированное значение продаж превышает числовой порог, сводная таблица обновляется, а рабочая книга сохраняется.

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
                // Находим индекс поля данных вручную, поскольку в PivotFieldCollection нет метода IndexOf
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
                pivotTable.refreshData();
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

## **Фильтр топ-10**
Фильтр топ-10 — специализированная разновидность фильтра по значениям, которая оставляет только N элементов с наибольшими или наименьшими значениями по выбранному полю значений. Его часто используют для ранжированных отчетов, например «топ-10 продуктов по выручке» или «5 регионов с наименьшим количеством продаж».

{{% alert color="primary" %}}
Фильтр топ-10 действует только тогда, когда в области данных сводной таблицы есть одно или несколько полей значений. Без хотя бы одного поля значений агрегированная метрика, по которой можно ранжировать элементы, отсутствует, поэтому применить фильтр невозможно.
Aspose.Cells предоставляет фильтрацию топ-10 через метод `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Параметр `valueFieldIndex` — индекс поля данных, агрегированные значения которого используются для ранжирования элементов; `filterType` задает единицу измерения `itemCount` (`Count` оставляет фиксированное число элементов, а `Percent` — процент элементов, поэтому `itemCount` задает сам процент); `isTop` указывает, следует ли оставить элементы с наибольшими (true) или наименьшими (false) значениями; `itemCount` определяет количество элементов или процент элементов, которые следует оставить.
В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значений, применяется фильтр топ-10, оставляющий только 10 элементов с наибольшей суммой продаж, сводная таблица обновляется, а рабочая книга сохраняется.
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
                // Загрузить существующую книгу, содержащую сводную таблицу
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Получить доступ к листу, содержащему сводную таблицу (индекс 0)
                const worksheet = workbook.worksheets.get(0);
                // Получить доступ к сводной таблице по индексу
                const pivotTable = worksheet.pivotTables.get(0);
                // Убедиться, что в области данных есть хотя бы одно поле значений PivotField
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Получить целевое поле строки PivotField (поле, к которому применяется Top 10)
                const rowField = pivotTable.rowFields.get(0);
                // Первое (и единственное) поле данных находится по индексу 0; Top 10 ранжирует по нему.
                const valueFieldIndex = 0;
                // Применить фильтр Top 10 к полю строки:
                //   - valueFieldIndex = 0 — поле данных, используемое для ранжирования элементов
                //   - filterType  = PivotFilterType.Count (сохранять фиксированное количество элементов;
                //     PivotFilterType.Percent интерпретировал бы 10 как «верхние 10 процентов»)
                //   - isTop       = true (верхние N; false означало бы нижние N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Обновить данные сводной таблицы и пересчитать ее, чтобы применить фильтр
                pivotTable.refreshData();
                // Сохранить книгу
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
В дополнение к структурированным API фильтрации Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Перебирая коллекцию `pivotField.getPivotItems()` объекта `PivotField` и изменяя свойство `isHidden`, можно избирательно скрывать заданные элементы без применения формульного фильтра. Установка `pivotItem.isHidden = true` скрывает элемент в сводной таблице; установка `pivotItem.isHidden = false` отображает его и делает снова видимым.
Этот подход полезен, когда правило фильтрации нестандартное или относится к отдельным элементам, например при необходимости скрыть небольшое количество указанных категорий, которые не должны отображаться в конкретном отчете. В приведенном ниже примере загружается сводная таблица, скрывается определенный элемент по имени, демонстрируется способ его отображения, сводная таблица обновляется, а рабочая книга сохраняется.

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
                // Загрузить существующую книгу, содержащую сводную таблицу
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Получить доступ к первому листу, содержащему сводную таблицу
                const sheet = workbook.worksheets.get(0);
                // Получить доступ к сводной таблице по индексу (первая сводная таблица на листе)
                const pivotTable = sheet.pivotTables.get(0);
                // Получить целевое поле PivotField (первое поле строковых меток, в котором мы будем скрывать и отображать элементы)
                const pivotField = pivotTable.rowFields.get(0);
                // Перебрать коллекцию PivotItems выбранного поля PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Скрыть элементы сводной таблицы, соответствующие указанному имени или критерию
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Продемонстрировать отображение: повторно показать ранее скрытый элемент сводной таблицы
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Обновить и пересчитать сводную таблицу, чтобы изменения вступили в силу
                pivotTable.refreshData();
                // Сохранить книгу — скрытые элементы остаются в исходных данных
                // но исключаются из отображаемого результата сводной таблицы
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
Aspose.Cells for JavaScript via C++ предоставляет полный набор возможностей фильтрации сводных таблиц, соответствующий возможностям Microsoft Excel. Фильтры по меткам, датам и значениям охватывают наиболее распространенные сценарии анализа, а фильтр топ-10 предназначен для ранжированных отчетов. Если правило фильтрации нестандартное, свойство `pivotItem.isHidden` предоставляет гибкий резервный вариант на уровне отдельных элементов. Сочетание этих стратегий — например, применение фильтра по метке с последующим скрытием определенных элементов — позволяет создавать отчеты сводных таблиц с точно заданными критериями исключительно с помощью кода.

{{< app/cells/assistant language="javascript-cpp" >}}