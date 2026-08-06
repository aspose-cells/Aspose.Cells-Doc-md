---
title: Изменение макета поля страницы в сводной таблице
linktitle: Изменение макета поля страницы в сводной таблице
description: Узнайте, как управлять макетом области полей страницы в сводной таблице с помощью Aspose.Cells for Node.js via C++, включая настройку порядка отображения, количества полей перед переносом и порядка полей страницы в верхней части сводной таблицы.
keywords: Aspose.Cells, Node.js via C++, библиотека, электронная таблица, сводная таблица, поле страницы, порядок полей страницы, количество полей перед переносом, перемещение поля страницы
type: docs
weight: 191
url: /ru/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Эта статья является продолжением темы **«Добавление поля страницы в сводную таблицу»**. В ней показано, как управлять макетом области полей страницы — полосы элементов управления фильтрами в верхней части сводной таблицы — включая порядок отображения, количество полей перед переносом и изменение порядка полей.
{{% /alert %}}
## **Введение**
Сводная таблица в Microsoft Excel содержит выделенную **область полей страницы**, которая расположена над телом таблицы (строками, столбцами и данными). Эта область отображается как полоса раскрывающихся элементов управления фильтрами (по одному для каждого поля страницы), на которые пользователи нажимают, чтобы отфильтровать сводную таблицу по таким критериям, как год или регион. Aspose.Cells for Node.js via C++ моделирует эту область через коллекцию `pivotTable.pageFields` и предоставляет три свойства, управляющих визуальным расположением полосы:
- `pivotTable.pageFieldOrder` (значение `Aspose.Cells.PrintOrderType`) определяет, размещаются ли дополнительные поля страницы *рядом* с существующими или *под* ними.
- `pivotTable.pageFieldWrapCount` задаёт, сколько полей страницы размещается в каждой строке или столбце до переноса.
- `pivotTable.pageFields.move(currIndex, destIndex)` изменяет порядок полей страницы без изменения режима упорядочивания.
В этой статье последовательно рассматриваются три примера кода, демонстрирующие каждую из этих операций на общем наборе данных, чтобы вы могли сравнить полученные макеты между собой.
## **Исходные данные**
Во всех трёх примерах ниже эти восемь строк данных о продажах загружаются на рабочий лист с именем `PivotData`. Данные содержат два кандидата для поля страницы (`Year`, `Region`), одного кандидата для поля строки (`Fruit`) и одну меру (`Amount`), что делает полосу полей страницы удобной для анализа.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Во всех примерах кода заполнены все восемь строк в одинаковом порядке, поэтому исходные данные никогда не различаются между сценариями — различаются только свойства макета полей страницы.
## **Пример 1: Over Then Down**
В первом сценарии мы настраиваем два поля страницы (`Year`, `Region`) так, чтобы они отображались **рядом в одной строке** в верхней части сводной таблицы. Мы назначаем `Fruit` оси строк, размещаем `Year` первым и `Region` вторым на оси страницы (порядок вызовов `addFieldToArea` определяет начальный индекс), добавляем `Amount` (Sum) в качестве поля данных, а затем устанавливаем `pageFieldOrder` в значение `PrintOrderType.OverThenDown` с `pageFieldWrapCount = 2`. С `OverThenDown` и количеством полей перед переносом 2 два поля страницы располагаются горизонтально рядом в одной строке в верхней части сводной таблицы, поэтому полоса занимает одну строку шириной в два.
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// Заголовки (строка 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Строка 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Строка 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Строка 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Строка 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Строка 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Строка 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Строка 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Строка 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Добавляем лист PivotTableReport
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// Создаём сводную таблицу из PivotData!A1:D9, размещённую в A1 на листе PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// Добавляем поля
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Фрукт
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Год
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Регион
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Сумма
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// Настраиваем компоновку области полей страницы: сначала поля страницы по горизонтали, перенос после каждых 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// Обновляем и вычисляем
pivotTable.calculateData();

// Сохраняем
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **Пример 2: Down Then Over**
В этом примере мы размещаем `Fruit` на оси строк, `Year` и `Region` на оси страницы (с `Year` первым), а `Amount` (Sum) в качестве поля данных — точно так же, как в примере 1. Затем устанавливаем `pageFieldOrder` в значение `PrintOrderType.DownThenOver` и `pageFieldWrapCount` в `2`. С `DownThenOver` и количеством полей перед переносом 2 два поля страницы располагаются вертикально друг под другом — `Year` сверху, `Region` непосредственно под ним — формируя один столбец в верхней части сводной таблицы. Таким образом, полоса занимает две строки шириной один, в отличие от примера 1.
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);

const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
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
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **Пример 3: Перемещение поля страницы**
В третьем сценарии мы сохраняем этот набор данных и распределение полей, задаём нейтральный макет (`OverThenDown` с количеством полей перед переносом `2`), а затем демонстрируем операцию `pageFields.move`. Вызов `move(0, 1)` перемещает поле страницы с индексом 0 (`Year`) в позицию 1, а поле страницы, которое было в позиции 1 (`Region`), смещается в позицию 0. После этого вызова `Region` является первым полем страницы, а `Year` — вторым. Режим переноса и упорядочивания остаются без изменений, поэтому полоса по-прежнему отображается горизонтально рядом — изменился только порядок двух раскрывающихся списков.
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();

const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);

const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **Связанные статьи**
- [Добавление поля страницы в сводную таблицу](/cells/ru/nodejs-cpp/add-page-field-in-pivot-table/) — родительская страница, описывающая процесс добавления полей страницы в сводную таблицу.
- [Поля строк и столбцов в сводной таблице](/cells/ru/nodejs-cpp/row-and-column-fields/) — описывает распределение полей по осям строк и столбцов, дополняя работу с осью страницы, показанную в этой статье.
- [Управление полями значений в сводной таблице](/cells/ru/nodejs-cpp/manage-value-fields/) — описывает настройку области данных (значений), включая агрегацию `Sum`, используемую в этой статье.
- [Обновление сводной таблицы](/cells/ru/nodejs-cpp/refresh-pivot-table/) — объясняет методы `refreshData` и `calculateData`, которые необходимо вызывать после изменения порядка полей страницы.
- [Применение стиля к сводной таблице](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/) — показывает, как отформатировать отображаемую сводную таблицу после размещения полосы полей страницы.
{{< app/cells/assistant language="nodejs-cpp" >}}