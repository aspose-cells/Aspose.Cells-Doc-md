---
title: Обновление сводных таблиц и их кэшей в Aspose.Cells for JavaScript via C++
linktitle: Обновление сводных таблиц и их кэшей в Aspose.Cells for JavaScript via C++
description: Узнайте, как обновлять сводные таблицы в Aspose.Cells for JavaScript via C++ с помощью API обновления сводных таблиц v26.7+. В этой статье рассматриваются workbook.refreshAll, worksheet.refreshPivotTables, pivotCache.refresh, pivotTable.calculateData и pivotCache.getPivotTables с практическими примерами кода.
keywords: Aspose.Cells, JavaScript via C++, сводная таблица, обновление, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /ru/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет многоуровневый API обновления, который позволяет перезагружать данные сводных таблиц на четырех уровнях — от всей рабочей книги до отдельной сводной таблицы. Начиная с **Aspose.Cells for JavaScript via C++ v26.7**, метод `pivotTable.refreshData()` помечен как устаревший и должен быть заменён более эффективными API, учитывающими кэш, которые описаны в этой статье.
{{% /alert %}}

## Введение
Обновление сводной таблицы редко сводится к одной операции. Aspose.Cells поддерживает многоуровневую цепочку данных, связывающую исходные данные с отображаемыми значениями на рабочем листе. Понимание этой цепочки — ключ к выбору подходящего API обновления в любой ситуации.
Цепочка данных состоит из четырех уровней:
1. **Источник данных** — исходные диапазоны рабочих листов, запрос к базе данных или диапазон консолидации, в котором хранятся необработанные значения.
2. **`PivotCache`** — снимок исходных данных в памяти. Каждая сводная таблица строится поверх `PivotCache`; здесь собираются и агрегируются все данные.
3. **`PivotTable`** — объект представления, определяющий поля строк, столбцов, значений и фильтров. `PivotTable` читает данные *только* из своего `PivotCache`, а не напрямую из источника данных.
4. **`Cells`** — ячейки рабочего листа, возвращаемые `getCells()`, в которых `PivotTable` отображает вычисленные значения и стили.

{{% alert color="primary" %}}
`pivotCache.getSourceType()` (перечисление `PivotTableSourceType`) указывает, откуда получены данные кэша. Начиная с v26.7, `pivotCache.refresh()` поддерживает только типы источников **`SHEET`** и **`CONSOLIDATION`** — то есть данные, находящиеся в диапазонах рабочих листов. Внешние источники (базы данных, внешние подключения и т. д.) пока нельзя обновить с помощью API для работы с кэшем.
Из-за этой цепочки в Aspose.Cells существуют два основных пути обновления:
- **`pivotTable.calculateData()`** — пересчитывает отображение одной `PivotTable` по уже кэшированным данным, без обратного обращения к источнику данных.
Во всех сценариях этой статьи ячейки рабочего листа используются в качестве источника данных, поэтому тип источника — `SHEET`, а операции обновления выполняются согласно описанию.
{{% /alert %}}

## Быстрый старт
Если требуется обновить все сводные таблицы в рабочей книге, самый краткий вариант — один вызов:

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
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

Далее в статье объясняется, когда следует выбрать API с более узкой областью действия.

## Необходимые импорты
Все примеры на JavaScript в этой статье начинаются со следующего импорта модуля, поскольку типы сводных таблиц доступны через namespace `Aspose.Cells.Pivot`:
- `const Aspose = require('aspose.cells');`

## Обновление всех сводных таблиц в рабочей книге
Если необходимо, чтобы каждый кэш сводных таблиц и каждая сводная таблица в рабочей книге отражали актуальные исходные данные, используйте наиболее простой и универсальный API — `workbook.refreshAll()`. Один вызов обрабатывает всю рабочую книгу: обновляет каждый `PivotCache` из соответствующего источника, а затем пересчитывает каждую зависимую `PivotTable`. Это рекомендуемый подход к полному обновлению документа, когда производительность не критична.
В следующем примере создается рабочая книга с исходным диапазоном Fruit/Year/Amount, добавляется одна сводная таблица, изменяются некоторые исходные значения, после чего `refreshAll()` одним вызовом приводит все данные в актуальное состояние.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Создать новую книгу
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Записать строку заголовков в ячейки A1:C1
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Записать строки данных в ячейки A2:C9 (8 строк данных о фруктах за 2020 и 2021 годы)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // Добавить сводную таблицу: исходный диапазон "A1:C9", целевая ячейка "E3"
            const pivotTableIndex = worksheet.pivotTables.add(
                "=A1:C9",
                "E3",
                "PivotTable1"
            );
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Назначить поля сводной таблицы: Fruit в строки, Year в столбцы, Amount в данные
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Изменить несколько значений Amount в исходных данных для имитации изменений
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // Обновить все сводные таблицы / кэши сводных таблиц в книге
            workbook.refreshAll();
            // Сохранить книгу
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Обновление всех сводных таблиц на одном рабочем листе
Иногда требуется обновить только сводные таблицы, расположенные на одном конкретном рабочем листе, например, когда известно, что сводные таблицы на других рабочих листах не имеют отношения к обновлению и их не следует затрагивать. В таком случае Aspose.Cells предоставляет `worksheet.refreshPivotTables()`, область действия которого ограничена одним экземпляром `Worksheet`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTableIndex = worksheet.pivotTables.add("=A1:C9", "E3", "PivotTable1");
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## Обновление одной сводной таблицы
Если требуется детальный контроль над одной сводной таблицей, API на основе кэша предлагает два варианта. Выбор зависит от того, что именно изменилось: исходные данные или только параметры отображения и макета сводной таблицы.

### Изменились исходные данные — используйте `pivotCache.refresh()`
Если изменились исходные данные, следует использовать `pivotTable.getPivotCache().refresh()`. Этот вызов повторно считывает исходные данные в кэш, а затем пересчитывает каждую `PivotTable`, зависящую от этого кэша.

### Изменилось только представление или макет — используйте `pivotTable.calculateData()`
Если исходные данные не изменились, а были изменены только параметры отображения или макета сводной таблицы (например, поле перемещено в другую область или переключен параметр обновления при открытии), нет необходимости возвращаться к источнику данных. Кэш уже содержит нужные данные; пересчитать требуется только отображаемую `PivotTable`. В этом случае следует использовать `pivotTable.calculateData()`.
В следующем примере изменяется свойство, не связанное с источником, а затем вызывается `calculateData()` для повторного отображения таблицы из существующего кэша.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Записать строку заголовков Fruit / Year / Amount
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // Записать 8 строк данных (строки 2-9, соответствующие исходному диапазону A1:C9)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // Добавить сводную таблицу, размещённую в целевой ячейке E3, с источником данных A1:C9
                const pivotTableIndex = worksheet.pivotTables.add(
                    "=A1:C9",
                    "E3",
                    "PivotTable1"
                );
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                // Назначить поля: Fruit в строки, Year в столбцы, Amount в данные
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // Изменить свойство представления/макета — это изменение только для отображения,
                // поэтому для него НЕ требуется повторное чтение исходных данных через PivotCache.Refresh().
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData() повторно отрисовывает отображение ЭТОЙ сводной таблицы (данные + стиль) из
                // данных, уже хранящихся в PivotCache. Поскольку исходные данные не изменились,
                // переход к источнику не выполняется — пересчитываются только кэшированные значения
                // в ячейках листа.
                pivotTable.calculateData();
                // Сохранить книгу на диск
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Рабочая книга часто содержит множество сводных таблиц, использующих один общий кэш. Чтобы получить их перечень, например перед массовым обновлением или для диагностики влияния общего кэша, используйте `pivotCache.getPivotTables()`. Этот метод возвращает коллекцию всех `PivotTable`, зависящих от указанного кэша.

## Миграция с устаревшего `pivotTable.refreshData()`
До Aspose.Cells for JavaScript via C++ v26.7 стандартным способом обновления сводной таблицы был вызов `pivotTable.refreshData()` для каждой сводной таблицы отдельно. Начиная с v26.7, этот метод помечен как **устаревший** и должен быть заменён API, учитывающими кэш, которые описаны выше.
При использовании подхода с `refreshData()` для каждой таблицы в реальных рабочих книгах возникают две проблемы:
- Метод `refreshData()` повторно извлекает данные из источника *при каждом* вызове, даже если источник не изменился.
Рекомендуемые замены:
В следующем примере демонстрируется новый эффективный подход для рабочих книг с несколькими сводными таблицами, использующими один кэш.

## Какой API обновления следует использовать?
В таблице ниже перечислены доступные API обновления и условия их выбора.
| Цель | Рекомендуемый API | Примечания |
|------|-----------------|-------|
| Обновить все данные в рабочей книге | `workbook.refreshAll()` | Один вызов; охватывает все кэши и таблицы. |
| Обновить только сводные таблицы на одном рабочем листе | `worksheet.refreshPivotTables()` | Ограничен одним рабочим листом. |
| Исходные данные изменились для одного кэша | `pivotTable.getPivotCache().refresh()` | Обновляет ВСЕ сводные таблицы, использующие этот общий кэш. |
| Изменились только параметры отображения или макета | `pivotTable.calculateData()` | Исключает ненужное обращение к источнику. |
| Перечислить все сводные таблицы в общем кэше | `pivotCache.getPivotTables()` | Используйте для перечисления перед массовым обновлением. |
На практике предпочитайте API, основанные на кэше, устаревшему подходу с вызовом `refreshData()` для каждой таблицы. Такие API учитывают общие кэши, исключают избыточные обращения к источнику и позволяют выбрать наименьшую область действия, достаточную для выполнения обновления.

## Типичные ошибки
- **Забыли обновить данные перед сохранением.** Сводная таблица записывает свои отображаемые значения на рабочий лист только после обновления цепочки данных. Если вы изменили исходные ячейки, вызовите `pivotCache.refresh()` (или `workbook.refreshAll()`) перед `workbook.save()`, иначе сохранённый файл по-прежнему будет содержать старые агрегированные значения.
- **Вызываете устаревший `refreshData()` для каждой таблицы.** В v26.7 метод `pivotTable.refreshData()` помечен как устаревший и при каждом вызове повторно извлекает данные из источника. При нескольких сводных таблицах, использующих один кэш, это приводит к N избыточным обращениям к источнику. Замените его одним вызовом `pivotCache.refresh()`, после чего вызовите `pivotTable.calculateData()` для каждой таблицы.
- **Выполняете обновление, когда изменился только макет.** Если изменено только представление сводной таблицы (порядок столбцов, `getConsolidationFunction()` и т. д.), а исходные данные не затронуты, вызов `pivotCache.refresh()` не требуется и приводит к ненужным затратам времени. Вызовите `pivotTable.calculateData()`, чтобы повторно отобразить данные из существующего кэша.
- **Внешний источник не поддерживается методом `pivotCache.refresh()`.** Если данные сводной таблицы поступают из внешнего подключения (база данных, OLAP-куб и т. д.), `pivotCache.refresh()` не может обновить его в v26.7 — в настоящее время метод поддерживает только типы источников `SHEET` и `CONSOLIDATION`. Для внешних источников заново откройте рабочую книгу или пересоздайте кэш из источника.

{{< app/cells/assistant language="javascript-cpp" >}}