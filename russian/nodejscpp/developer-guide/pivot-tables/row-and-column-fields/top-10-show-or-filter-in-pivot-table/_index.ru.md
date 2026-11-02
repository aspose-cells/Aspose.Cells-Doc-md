---
title: Отображение или фильтрация топ-10 элементов в сводной таблице
linktitle: Отображение или фильтрация топ-10 элементов в сводной таблице
description: Узнайте, как отображать только элементы с самыми высокими или самыми низкими значениями в поле сводной таблицы с помощью Aspose.Cells for Node.js через C++. В этой статье рассматриваются метод Top10AutoShow для Excel 97-2003, чтение параметров с помощью Top10AutoShowSettings и фильтр «Топ-10» для Excel 2007-365 с помощью FilterTop10.
keywords: Aspose.Cells, Node.js через C++, сводная таблица, топ-10, автопоказ, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /ru/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводную таблицу, содержащую все элементы поля строки, иногда трудно читать, если в поле насчитываются десятки элементов. Отчёт «топ-10» оставляет только элементы с самыми высокими или самыми низкими значениями, что как раз требуется для отчётов с ранжированием: «5 товаров с наибольшей выручкой» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **Автопоказ Excel 97-2003** — метод `pivotField.top10AutoShow()`. Это классическая настройка «Показать верхние или нижние N элементов», которая хранится непосредственно в поле сводной таблицы. Она работает во всех версиях Excel, как старых, так и новых, поскольку является частью исходного формата сводной таблицы.
- **Фильтр топ-10 Excel 2007-365** — метод `pivotField.filterTop10()`. Это современный фильтр «Топ-10» по значениям, доступный в меню поля в разделе «Фильтры по значениям». Он хранится в виде объекта `PivotFilter`, связанного с полем, и поддерживает ранжирование по количеству элементов и в процентах.

## **Отображение топ-10 в Excel 97-2003 (top10AutoShow)**
Классический автопоказ настраивается одним вызовом `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)`:
- `isAutoShow` — включает или отключает параметр автопоказа в поле.
- `isTop` — значение `true` сохраняет элементы с самыми высокими значениями (Top), а `false` — с самыми низкими (Bottom).
- `count` — количество элементов, которые следует сохранить, например 10 для классического отчёта «топ-10».
- `rankBy` — индекс поля данных с отсчётом от нуля, по значениям которого ранжируются элементы. Передайте -1, чтобы ранжировать элементы по самому полю.
Ранжирование может выполняться по полю значений или по самому полю. Ниже приведены два варианта.

### **Ранжирование по полю значений**
Ранжирование элементов поля строки выполняется по данным обычного поля значений, например «Сумма продаж». В следующем примере создаётся сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображаются 2 вида спорта с наибольшим объёмом продаж. Значение `rankBy` равно 0, поскольку «Сумма продаж» — поле данных с индексом 0.

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Ранжирование по самому полю**
Поле также можно ранжировать по самому себе — передайте -1 в качестве `rankBy`. Для этого варианта дополнительное поле данных не требуется; достаточно разместить поле в области строк (или столбцов). В следующем примере показаны 3 вида спорта с наименьшими значениями поля, ранжированные по самому полю. При сохранении этой настройки атрибут `rankBy` не записывается в XML сводной таблицы, поскольку -1 является значением по умолчанию для данного формата, а `top10AutoShowSettings.getRankBy()` возвращает -1.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Чтение текущих параметров (Top10AutoShowSettings)**
Геттер `pivotField.getTop10AutoShowSettings()` возвращает объект `PivotFieldTop10AutoShowSettings`, предоставляющий доступ к параметрам автопоказа, которые в данный момент сохранены в поле. С его помощью можно проверить, как будут отображены элементы в существующей рабочей книге или только что настроенной сводной таблице, в том числе в рабочих книгах, загруженных из файла.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Четыре свойства соответствуют классическим атрибутам автопоказа, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому все версии Excel будут учитывать считанные значения.

## **Примечание**

{{% alert color="primary" %}}
- Прямые геттеры объекта `PivotField` — `isAutoShow`, `getIsAscendShow()`, `getAutoShowCount()` и `getAutoShowField()` — помечены как устаревшие. Вместо них используйте объект `Top10AutoShowSettings`: `pivotField.isAutoShow` заменяется на `top10AutoShowSettings.isAutoShow`, `pivotField.getIsAscendShow()` — на `top10AutoShowSettings.isTop`, `pivotField.getAutoShowCount()` — на `top10AutoShowSettings.getAutoShowCount()`, а `pivotField.getAutoShowField()` — на `top10AutoShowSettings.getRankBy()`. Сам метод `pivotField.top10AutoShow()` является поддерживаемым способом изменения параметров.
- `top10AutoShow()` работает с полями, расположенными в областях строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не отображаются в теле сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр топ-10 (filterTop10)**
Современные версии Excel позволяют применить фильтр «Топ-10» по значениям из меню поля (раздел «Фильтры по значениям», пункт «Топ-10...»). В Aspose.Cells этот фильтр реализован методом `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)`, который возвращает созданный объект `PivotFilter`:
- `valueFieldIndex` — индекс поля данных с отсчётом от нуля, агрегированные значения которого используются для ранжирования элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.Count` оставляет фиксированное количество элементов (вариант «Элементы» в диалоговом окне). `PivotFilterType.Percent` оставляет заданный процент элементов, поэтому `itemCount` сам является процентом: значение 30 оставляет 30 % лучших элементов. `PivotFilterType.SUM` ранжирует элементы по объёму накопленных значений.
- `isTop` — значение `true` для верхних элементов, `false` — для нижних.
- `itemCount` — число `N` в обозначении «топ `N`»; его единица измерения зависит от `type`.

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` и `filterTop10` — две отдельные возможности. Автопоказ записывает классический атрибут `autoShow` в поле сводной таблицы; этот параметр учитывают все версии Excel, начиная с Excel 97. `filterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. При открытии рабочей книги в более старой версии Excel сводная таблица с современным фильтром отображает все элементы. Для документов, которые должны поддерживать цикл сохранения и открытия с помощью устаревших инструментов, предпочтительнее использовать `top10AutoShow`; для современных рабочих книг — `filterTop10`, поскольку он сочетается с другими фильтрами по значениям.
{{% /alert %}}

## **Связанные статьи**
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Группировка полей в сводной таблице](/cells/ru/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/nodejs-cpp/refresh-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}