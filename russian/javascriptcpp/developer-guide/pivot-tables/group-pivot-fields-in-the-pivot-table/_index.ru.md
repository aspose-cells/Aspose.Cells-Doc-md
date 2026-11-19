---
title: Группировка полей сводной таблицы
linktitle: Группировать поля
type: docs
weight: 80
url: /ru/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Узнайте, как группировать поля строк и столбцов в сводной таблице по датам (например, месяцам и кварталам) и числовым диапазонам с помощью PivotField.group и PivotFieldGroupOptions в Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, сводная таблица, группировать поле сводной таблицы, PivotField.group, PivotFieldGroupOptions, группировка дат, группировка чисел, месяцы, кварталы, числовой диапазон, JavaScript via C++
---

## **Возможные сценарии использования**
- Группировка полей сводной таблицы полезна, когда поле строки или столбца содержит множество различных элементов, например, поле даты со сотнями дат или числовое поле с разбросанными значениями. Группировка сводит эти элементы в осмысленные разделы: даты — в месяцы, кварталы и годы, а числа — в диапазоны, такие как 0‑1, 2‑3, 4‑5. Это делает большую сводную таблицу компактнее и облегчает её анализ. Aspose.Cells предоставляет эту возможность через метод `PivotField.group()` (автоматическое группирование по типу данных) и `PivotField.group(PivotFieldGroupOptions)` (пользовательские параметры группирования).
- Группировка дат объединяет отдельные даты в более крупные периоды, такие как дни, месяцы, кварталы и годы, формируя иерархию времени (например, Годы, Кварталы, Месяцы). Тенденции во времени становятся видимыми сразу, а каждый уровень периода выступает отдельным полем в области строк или столбцов сводной таблицы.
- Группировка доступна только для полей, размещённых в области ROW или COLUMN сводной таблицы. Поле данных (значений) нельзя группировать напрямую. Чтобы сгруппировать такое поле, его необходимо сначала добавить в область строк или столбцов сводной таблицы.

## **Автоматическая группировка полей сводной таблицы**
Перегрузка без параметров `PivotField.group()` проверяет тип данных поля и группирует его автоматически. Поле, содержащее только даты (и пустые значения), группируется по месяцам. Поле, содержащее только числа (и пустые значения), группируется в числовые диапазоны с автоматическим интервалом.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Группировка полей сводной таблицы с пользовательскими параметрами**
Класс `PivotFieldGroupOptions` предоставляет возможности настройки группировки. Для дат задаются `startDate`, `endDate` и `groupTypes`. Для чисел задаются `startNumber`, `endNumber` и `interval`. Свойство `newPivotField` определяет, будет ли группировка создавать новые поля сводной таблицы рядом с оригиналом (см. раздел Примечание в конце статьи).

### **Группировка поля даты по месяцам и кварталам**
В следующем примере поле даты в строках образца сводной таблицы группируется по месяцам и кварталам в диапазоне от начальной до конечной даты. Код загружает [образец Excel‑файла](sampleGroupPivotFieldsInPivotTable.xlsx), выполняет группировку, вычисляет данные сводной таблицы и сохраняет полученный результат. На скриншоте показан эффект: поле даты теперь сгруппировано по кварталам и месяцам.  
Обратите внимание, что порядок значений в `options.groupTypes` игнорируется. Независимо от порядка перечисления типов групп, сгруппированные поля всегда отображаются от крупнейшего периода к наименьшему: годы, кварталы, месяцы, дни, часы, минуты, секунды. В данном примере месяцы указаны в `options.groupTypes` перед кварталами, однако кварталы отображаются как внешний уровень, а месяцы — как внутренний.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![Сводная таблица, сгруппированная по месяцам и кварталам](group-pivot-fields-in-the-pivot-table_1.png)

### **Группировка числового поля в диапазоны**
`FieldTwo` в образце сводной таблицы изначально является полем данных (значений). Поскольку группировать можно только поля строк или столбцов, код сначала вызывает `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")`, перемещая `FieldTwo` в область строк, обновляет сводную таблицу, а затем группирует числовое поле в диапазоны 0‑1, 2‑3 и 4‑5, используя `startNumber = 0`, `endNumber = 5` и `interval = 2`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Примечание**

{{% alert color="primary" %}}
- Перегрузки метода `PivotField.groupBy()` устарели и удалены из API. Вместо них используются `PivotField.group()` и `PivotField.group(PivotFieldGroupOptions)`.
- В Microsoft Excel группировка числового поля **заменяет** оригинальное поле сгруппированными диапазонами, тогда как группировка дат создаёт **новые** поля (по каждому уровню группировки, например Кварталы и Месяцы) рядом с исходным полем. Начиная с Aspose.Cells 26.10, методы `PivotField.group()` ведут себя так же, как в Excel. Свойство `PivotFieldGroupOptions.newPivotField` сохраняется для совместимости со старыми версиями: по умолчанию оно `false` для числовой группировки и `true` для даты‑времени; установите `false`, если хотите, чтобы группировка дат заменяла оригинальное поле вместо создания новых.
- Свойство `PivotFieldGroupOptions.interval` воздействует только на числовую группировку и на группировку дат по дням (например, группировка дат в 7‑дневные периоды); оно игнорируется при группировке дат по месяцам, кварталам или годам.
{{% /alert %}}

## **Связанные статьи**
- [Добавить поля строк и столбцов в сводную таблицу](/cells/ru/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Добавить поле страницы в сводную таблицу](/cells/ru/javascript-cpp/add-page-field-in-pivot-table/)
- [Применить стиль к сводной таблице](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)
- [Обновить сводную таблицу](/cells/ru/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}