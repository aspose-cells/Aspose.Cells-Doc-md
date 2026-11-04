---
title: Отображение или фильтрация топ-10 в сводной таблице
linktitle: Отображение или фильтрация топ-10 в сводной таблице
description: Узнайте, как с помощью Aspose.Cells for JavaScript via C++ отображать только элементы, занимающие верхние или нижние позиции в рейтинге поля сводной таблицы. В статье рассматриваются свойства AutoShow для Excel 97-2003 (isAutoShow, isAscendShow, autoShowCount и autoShowField), чтение их значений, а также фильтр «Топ-10» для Excel 2007-365 с помощью filterTop10.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, сводная таблица, топ-10, AutoShow, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /ru/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводную таблицу, в которой перечислены все элементы поля строки, может быть трудно читать, если поле содержит десятки элементов. Отчёт «Топ-10» оставляет только элементы с наивысшим или наименьшим рейтингом — именно то, что требуется для отчётов с ранжированием, например «5 продуктов с наибольшей выручкой» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма для этого, соответствующих двум поколениям Microsoft Excel.
- **AutoShow в Excel 97-2003** — четыре свойства `PivotField`: `isAutoShow`, `isAscendShow`, `autoShowCount` и `autoShowField`. Это классическая настройка «Отобразить N верхних/нижних элементов», которая хранится непосредственно в поле сводной таблицы. Она работает во всех версиях Excel, как старых, так и новых, поскольку входит в исходный формат сводной таблицы.
- **Фильтр «Топ-10» в Excel 2007-365** — метод `PivotField.filterTop10()`. Это современный фильтр значений «Топ-10», доступный в меню поля в разделе «Фильтры значений». Он хранится как объект `PivotFilter`, связанный с полем, и поддерживает ранжирование по количеству элементов и по процентам.

## **Отображение топ-10 в Excel 97-2003 (AutoShow)**
Классический механизм AutoShow настраивается с помощью четырёх свойств `PivotField`:
- `isAutoShow` — включает или отключает параметр AutoShow для поля.
- `isAscendShow` — значение `false` сохраняет элементы с наивысшим рейтингом (верхние), а `true` — с наименьшим (нижние).
- `autoShowCount` — число элементов, которые необходимо оставить, например 10 для классического отчёта «Топ-10».
- `autoShowField` — индекс (с нуля) **поля данных**, значения которого используются для ранжирования элементов. Передайте -1, чтобы ранжировать элементы по самому полю.
Ранжирование может выполняться по полю значений или по самому полю. Ниже приведены два варианта.

### **Ранжирование по полю значений**
Ранжирование элементов поля строки выполняется с помощью обычного поля значений, например «Сумма продаж». В следующем примере создаётся сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображаются 2 вида спорта с наибольшим объёмом продаж. Значение `rankBy` равно 0, поскольку «Сумма продаж» — поле данных с индексом 0.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Показать 2 верхних элемента, ранжированных по «Сумме продаж» (индекс поля данных 0)
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Ранжирование по самому полю**
Поле можно ранжировать по самому себе: передайте -1 в `autoShowField`. Для этого варианта дополнительное поле данных не требуется; достаточно разместить поле в области строки (или столбца). В следующем примере показаны 3 вида спорта, вошедшие в нижнюю тройку при ранжировании по самому полю. При сохранении этого параметра атрибут `rankBy` не записывается в XML сводной таблицы, поскольку -1 является значением по умолчанию для данного формата, а `autoShowField` считывает значение -1.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Показать 3 нижних элемента, ранжированных по самому полю (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Чтение текущих параметров AutoShow**
Свойства `PivotField` — `isAutoShow`, `isAscendShow`, `autoShowCount` и `autoShowField` — предоставляют доступ к текущим параметрам AutoShow, сохранённым в поле. Используйте их для проверки того, как будут отображаться элементы существующей рабочей книги или только что настроенной сводной таблицы. Эти свойства также можно использовать с рабочими книгами, загруженными из файла.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

Четыре свойства соответствуют классическим атрибутам AutoShow, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому считанные значения учитываются всеми версиями Excel.

## **Примечание**

{{% alert color="primary" %}}
- После изменения любого свойства AutoShow повторно вызовите `pivotTable.calculateData()` — настройки вступят в силу в отображаемой компоновке только после следующего пересчёта.
- Параметры AutoShow применимы к полям строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не размещаются в теле сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр «Топ-10» (filterTop10)**
Современные версии Excel предоставляют «Топ-10» как фильтр значений в меню поля (раздел «Фильтры значений», пункт «Топ-10...»). В Aspose.Cells этот фильтр реализован методом `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)`, который возвращает созданный объект `PivotFilter`:
- `valueFieldIndex` — индекс (с нуля) поля данных, агрегированные значения которого используются для ранжирования элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.Count` оставляет фиксированное число элементов (вариант «Элементы» в диалоговом окне). `PivotFilterType.Percent` оставляет заданный процент элементов, поэтому `itemCount` задаёт сам процент: значение 30 оставляет верхние 30 процентов. `PivotFilterType.Sum` ранжирует элементы по накопленной сумме значений.
- `isTop` — значение `true` соответствует верхним элементам (Top), а `false` — нижним (Bottom).
- `itemCount` — число N в выражении «Топ N»; его единица измерения зависит от `type`.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Свойства AutoShow и `filterTop10` — две отдельные возможности. AutoShow записывает классический атрибут `autoShow` в поле сводной таблицы и поддерживается всеми версиями Excel, начиная с Excel 97. `filterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. При открытии рабочей книги в более старой версии Excel сводная таблица, использующая современный фильтр, возвращается к отображению всех элементов. Для документов, которые необходимо открывать и сохранять устаревшими инструментами, предпочтительны свойства AutoShow; для современных рабочих книг предпочтителен `filterTop10`, поскольку он сочетается с другими фильтрами значений.
{{% /alert %}}

## **Связанные статьи**
- [Группирование полей сводной таблицы](/cells/ru/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}