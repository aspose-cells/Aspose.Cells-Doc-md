---
title: Изменение макета поля страницы в сводной таблице
linktitle: Изменение макета поля страницы в сводной таблице
description: Узнайте, как управлять макетом области полей страницы в сводной таблице с помощью Aspose.Cells for Node.js via Java, включая настройку порядка отображения, количества полей перед переносом и порядка полей страницы в верхней части сводной таблицы.
keywords: Aspose.Cells, Node.js via Java библиотека, электронная таблица, сводная таблица, поле страницы, порядок полей страницы, количество полей перед переносом, перемещение поля страницы
type: docs
weight: 191
url: /ru/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Эта статья является продолжением темы **Добавление поля страницы в сводную таблицу**. В ней показано, как управлять макетом области полей страницы — полосой элементов управления фильтрами в верхней части сводной таблицы — включая порядок отображения, количество полей перед переносом и изменение порядка полей.
{{% /alert %}}
## **Введение**
Сводная таблица в Microsoft Excel предоставляет выделенную **область полей страницы**, которая расположена над телом таблицы со строками, столбцами и данными. Эта область отображается в виде полосы раскрывающихся элементов управления фильтрами (по одному для каждого поля страницы), на которые конечные пользователи нажимают, чтобы разрезать сводную таблицу по таким критериям, как год или регион. Aspose.Cells моделирует эту область через коллекцию `PivotTable.PageFields` и предоставляет три свойства, которые управляют визуальным расположением этой полосы:
- `PivotTable.PageFieldOrder` (значение `Aspose.Cells.PrintOrderType`) определяет, будут ли дополнительные поля страницы размещены *рядом* с существующими или *под* ними.
- `PivotTable.PageFieldWrapCount` задаёт, сколько полей страницы размещается в каждой строке или столбце перед переносом.
- `PivotTable.PageFields.Move(currIndex, destIndex)` изменяет порядок полей страницы без изменения режима упорядочивания.
В этой статье рассматриваются три примера кода, которые демонстрируют каждую из этих операций на общем наборе данных, чтобы вы могли сравнить полученные макеты бок о бок.
## **Исходные данные**
Во всех трёх примерах ниже эти восемь строк данных о продажах загружаются на рабочий лист с именем `PivotData`. Данные содержат два кандидата в поля страницы (`Year`, `Region`), один кандидат в строковое поле (`Fruit`) и один показатель (`Amount`), что делает полосу полей страницы удобной для изучения.
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
Все восемь строк заполняются в каждом примере кода в одинаковом порядке, поэтому исходные данные никогда не различаются между сценариями — различаются только свойства макета полей страницы.
## **Пример 1: Сначала по горизонтали, затем вниз**
В первом сценарии мы настраиваем два поля страницы (`Year`, `Region`) так, чтобы они отображались **бок о бок в одной строке** в верхней части сводной таблицы. Мы назначаем `Fruit` на ось строк, размещаем `Year` первым и `Region` вторым на оси страниц (порядок вызовов `addFieldToArea` определяет начальный индекс), добавляем `Amount` (Sum) в качестве поля данных, а затем устанавливаем `PageFieldOrder` в `PrintOrderType.OVER_THEN_DOWN` со значением `PageFieldWrapCount = 2`. С параметром `OVER_THEN_DOWN` и количеством полей перед переносом равным 2 два поля страницы располагаются горизонтально бок о бок в одной строке в верхней части сводной таблицы, поэтому полоса занимает одну строку шириной в два столбца.
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });

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

// Строка 1: Яблоко, 2022, Север, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Строка 2: Яблоко, 2023, Север, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Строка 3: Банан, 2022, Юг, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Строка 4: Банан, 2023, Юг, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Строка 5: Вишня, 2022, Восток, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Строка 6: Вишня, 2023, Восток, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Строка 7: Виноград, 2022, Запад, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Строка 8: Виноград, 2023, Запад, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Добавить лист PivotTableReport
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// Создать сводную таблицу из PivotData!A1:D9, размещённую на A1 листа PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// Добавить поля
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Фрукт
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Год
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Регион
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Сумма
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// Настроить компоновку области полей страницы: сначала размещать поля страницы по горизонтали, переносить после каждых 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// Обновить и вычислить
pivotTable.calculateData();

// Сохранить
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **Пример 2: Сначала сверху вниз, затем вправо**
В этом примере мы размещаем `Fruit` на оси строк, `Year` и `Region` на оси страниц (с `Year` первым), и `Amount` (Sum) в качестве поля данных — точно так же, как в примере 1. Затем мы устанавливаем `PageFieldOrder` в `PrintOrderType.DOWN_THEN_OVER` и `PageFieldWrapCount` в `2`. С параметром `DOWN_THEN_OVER` и количеством полей перед переносом равным 2 два поля страницы располагаются вертикально друг под другом — `Year` сверху, `Region` непосредственно под ним — формируя один столбец в верхней части сводной таблицы. Таким образом, полоса занимает две строки шириной в один столбец, в отличие от примера 1.
```javascript
var workbook = new AsposeCells.Workbook();
var pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
var pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
var pivotReport = workbook.getWorksheets().get(pivotReportIdx);

var headers = ["Fruit", "Year", "Region", "Amount"];
for (var c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

var data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];

for (var r = 0; r < data.length; r++)
{
    for (var c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

var idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **Пример 3: Перемещение поля страницы**
В третьем сценарии мы сохраняем этот набор данных и распределение полей, задаём нейтральный макет (`OVER_THEN_DOWN` с количеством полей перед переносом `2`), а затем демонстрируем операцию `PageFields.Move`. Вызов `Move(0, 1)` перемещает поле страницы с индексом 0 (`Year`) на позицию 1, а поле страницы, которое было на позиции 1 (`Region`), сдвигается на позицию 0. После этого вызова `Region` является первым полем страницы, а `Year` — вторым. Режим переноса и упорядочивания не изменяются, поэтому полоса по-прежнему отображается горизонтально бок о бок — изменён только порядок двух раскрывающихся списков.
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

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **Связанные статьи**
- [Добавление поля страницы в сводную таблицу](/cells/ru/nodejs-java/add-page-field-in-pivot-table/) — родительская страница, которая знакомит с тем, как поля страницы добавляются в сводную таблицу.
- [Поля строк и столбцов в сводной таблице](/cells/ru/nodejs-java/row-and-column-fields/) — описывает распределение полей по осям строк и столбцов, дополняя работу с осью страниц, показанную здесь.
- [Управление полями значений в сводной таблице](/cells/ru/nodejs-java/manage-value-fields/) — описывает, как настроить область данных (значений), включая агрегацию `Sum`, используемую в этой статье.
- [Обновление сводной таблицы](/cells/ru/nodejs-java/refresh-pivot-table/) — объясняет `refreshData` и `calculateData`, которые требуются после изменения порядка полей страницы.
- [Применение стиля к сводной таблице](/cells/ru/nodejs-java/apply-style-to-pivot-table/) — показывает, как отформатировать отображаемую сводную таблицу после размещения полосы полей страницы.
{{< app/cells/assistant language="nodejs-java" >}}