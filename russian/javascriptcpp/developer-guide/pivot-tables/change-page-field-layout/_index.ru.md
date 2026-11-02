---
title: Изменение макета полей страницы в сводной таблице
linktitle: Изменение макета полей страницы в сводной таблице
description: Узнайте, как управлять макетом области полей страницы в сводной таблице с помощью Aspose.Cells for JavaScript via C++, включая настройку порядка отображения, количества полей до переноса и порядка полей страницы в верхней части сводной таблицы.
keywords: Aspose.Cells for JavaScript via C++, электронная таблица, сводная таблица, поле страницы, порядок полей страницы, количество полей страницы до переноса, перемещение поля страницы
type: docs
weight: 191
url: /ru/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Эта статья продолжает тему **Добавление поля страницы в сводной таблице**. В ней показано, как управлять макетом области полей страницы (полосы элементов управления фильтрами в верхней части сводной таблицы), включая порядок отображения, количество полей до переноса и изменение порядка полей.
{{% /alert %}}

## **Введение**
Сводная таблица в Microsoft Excel предоставляет отдельную **область полей страницы**, расположенную над телом таблицы, содержащим строки, столбцы и данные. Эта область отображается в виде полосы раскрывающихся элементов управления фильтрами (по одному для каждого поля страницы). С их помощью конечные пользователи фильтруют данные в сводной таблице, например по году или региону. Aspose.Cells представляет эту область с помощью коллекции `pivotTable.pageFields` и предоставляет три средства управления визуальным макетом полосы:
- `pivotTable.pageFieldOrder` (значение `Aspose.Cells.PrintOrderType`) определяет, размещаются ли дополнительные поля страницы *рядом* с существующими или *под* ними.
- `pivotTable.pageFieldWrapCount` задает количество полей страницы, размещаемых в строке или столбце до переноса.
- `pivotTable.pageFields.move(currIndex, destIndex)` изменяет порядок полей страницы, не меняя режим размещения.
В статье приведены три примера кода, каждый из которых демонстрирует одну из этих операций на одном и том же наборе данных, чтобы можно было сравнить полученные макеты.

## **Исходные данные**
| Фрукт   | Год  | Регион | Количество |
|---------|------|--------|------------|
| Яблоко  | 2022 | Север  | 150        |
| Яблоко  | 2023 | Север  | 180        |
| Банан   | 2022 | Юг     | 120        |
| Банан   | 2023 | Юг     | 140        |
| Вишня   | 2022 | Восток | 200        |
| Вишня   | 2023 | Восток | 220        |
| Виноград | 2022 | Запад  | 90         |
| Виноград | 2023 | Запад  | 110        |
Во всех трех примерах кода заполнены все восемь строк в одинаковом порядке, поэтому исходные данные не изменяются от сценария к сценарию — различаются только свойства макета полей страницы.

## **Пример 1: сначала по горизонтали, затем по вертикали**
В первом сценарии настраиваем два поля страницы (`Year`, `Region`) так, чтобы они отображались **рядом в одной строке** в верхней части сводной таблицы. Поле `Fruit` назначаем оси строк, первым на оси страницы размещаем `Year`, вторым — `Region` (порядок вызовов `addFieldToArea` задает начальные позиции полей), добавляем `Amount` (`Sum`) как поле данных, а затем устанавливаем для `pivotTable.pageFieldOrder` значение `PrintOrderType.OverThenDown`, а для количества полей до переноса — `pivotTable.pageFieldWrapCount = 2`. При режиме `OverThenDown` и количестве полей до переноса, равном 2, два поля страницы располагаются горизонтально рядом в одной строке в верхней части сводной таблицы, поэтому полоса занимает одну строку шириной в два поля.

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
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // Заголовки (строка 0)
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // Строка 1: Яблоко, 2022, Север, 150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // Строка 2: Яблоко, 2023, Север, 180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // Строка 3: Банан, 2022, Юг, 120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // Строка 4: Банан, 2023, Юг, 140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // Строка 5: Вишня, 2022, Восток, 200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // Строка 6: Вишня, 2023, Восток, 220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // Строка 7: Виноград, 2022, Запад, 90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // Строка 8: Виноград, 2023, Запад, 110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // Добавить лист PivotTableReport
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // Создать сводную таблицу из PivotData!A1:D9, размещенную в A1 на листе PivotTableReport
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Добавить поля
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Фрукт
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Год
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Регион
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Сумма
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // Настроить макет области полей страницы: сначала разместить поля страницы по горизонтали, переносить после каждых 2
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // Обновить и вычислить
            pivotTable.calculateData();
            // Сохранить
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Пример 2: сначала по вертикали, затем по горизонтали**
В этом примере размещаем `Fruit` на оси строк, `Year` и `Region` на оси страницы (причем `Year` первым), а `Amount` (`Sum`) — как поле данных — точно как в примере 1. Затем задаем для `pivotTable.pageFieldOrder` значение `PrintOrderType.DownThenOver`, а для `pivotTable.pageFieldWrapCount` — `2`. При режиме `DownThenOver` и количестве полей до переноса, равном 2, два поля страницы располагаются вертикально друг над другом: `Year` сверху, а `Region` непосредственно под ним, образуя один столбец в верхней части сводной таблицы. Поэтому полоса занимает две строки шириной в одно поле, в отличие от примера 1.

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
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Пример 3: перемещение поля страницы**
В третьем сценарии оставляем тот же набор данных и распределение полей, задаем нейтральный макет (`OverThenDown` с количеством полей до переноса `2`), а затем демонстрируем операцию `pivotTable.pageFields.move`. Вызов `move(0, 1)` перемещает поле страницы с индексом 0 (`Year`) на позицию 1, а поле страницы, находившееся на позиции 1 (`Region`), сдвигается на позицию 0. После этого вызова `Region` становится первым полем страницы, а `Year` — вторым. Количество полей до переноса и режим размещения не изменяются, поэтому поля в полосе по-прежнему расположены горизонтально, рядом друг с другом; изменен только порядок двух раскрывающихся списков.

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
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Связанные статьи**
- [Добавление поля страницы в сводной таблице](/cells/ru/javascript-cpp/add-page-field-in-pivot-table/) — родительская страница, на которой представлены способы добавления полей страницы в сводную таблицу.
- [Управление полями значений в сводной таблице](/cells/ru/javascript-cpp/manage-value-fields/) — описывает настройку области данных (значений), включая агрегацию `Sum`, используемую в этой статье.
- [Применение стиля к сводной таблице](/cells/ru/javascript-cpp/apply-style-to-pivot-table/) — показывает, как форматировать отображаемую сводную таблицу после формирования макета полосы полей страницы.

{{< app/cells/assistant language="javascript-cpp" >}}