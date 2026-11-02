---
title: Отображение или фильтрация топ-10 в сводной таблице
linktitle: Отображение или фильтрация топ-10 в сводной таблице
description: Узнайте, как отображать только элементы, занимающие верхние или нижние позиции в рейтинге поля сводной таблицы, в Aspose.Cells for Node.js via Java. В этой статье рассматриваются метод Top10AutoShow для Excel 97-2003, чтение параметров с помощью Top10AutoShowSettings и фильтр «Топ-10» для Excel 2007-365 с помощью FilterTop10.
keywords: Aspose.Cells, Node.js via Java, сводная таблица, топ-10, AutoShow, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /ru/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица, в которой перечислены все элементы поля строки, может быть трудна для чтения, если это поле содержит десятки элементов. Отчет «Топ-10» оставляет только элементы, занимающие верхние или нижние позиции в рейтинге. Такой формат необходим для рейтинговых отчетов, например «5 лидирующих товаров по выручке» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма для этого, которые соответствуют двум поколениям Microsoft Excel.
- **Excel 97-2003 AutoShow** — метод `PivotField.top10AutoShow()`. Это классическая настройка «Показать верхние/нижние N элементов», которая сохраняется непосредственно в поле сводной таблицы. Она работает во всех версиях Excel, поскольку является частью исходного формата сводной таблицы.
- **Фильтр «Топ-10» для Excel 2007-365** — метод `PivotField.filterTop10()`. Это современный фильтр значений «Топ-10», доступный в меню поля в разделе «Фильтры значений». Он сохраняется как объект `PivotFilter`, связанный с полем, и позволяет выполнять ранжирование на основе количества элементов или процента.

## **Отображение топ-10 элементов в Excel 97-2003 (Top10AutoShow)**
Классический механизм AutoShow настраивается одним вызовом `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — включает или отключает параметр AutoShow для поля.
- `isTop` — значение `true` сохраняет элементы с наивысшим рейтингом, а `false` — с наименьшим.
- `count` — количество сохраняемых элементов, например 10 для классического отчета «Топ-10».
- `rankBy` — нулевой индекс поля данных, значения которого определяют рейтинг элементов. Передайте значение -1, чтобы ранжировать элементы по самому полю.
Рейтинг может определяться полем значений или самим полем. Ниже показаны два типичных варианта.

### **Ранжирование по полю значений**
Ранжируйте элементы поля строки с помощью обычного поля значений, например «Sum of Sales». В следующем примере создается сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображаются два лучших вида спорта по объему продаж. Значение `rankBy` равно 0, поскольку «Sum of Sales» является полем данных с индексом 0.

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Ранжирование по самому полю**
Поле также можно ранжировать по его собственным значениям — передайте значение -1 в качестве `rankBy`. Для этого варианта дополнительное поле данных не требуется; поле необходимо разместить в области строк или столбцов. В следующем примере показаны три вида спорта, занимающих нижние позиции в рейтинге. При сохранении этой настройки атрибут `rankBy` исключается из XML сводной таблицы, поскольку -1 является значением по умолчанию для этого формата, а метод `getTop10AutoShowSettings().getRankBy()` возвращает значение -1.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Чтение текущих параметров (Top10AutoShowSettings)**
Метод `PivotField.getTop10AutoShowSettings()` возвращает объект `PivotFieldTop10AutoShowSettings`, предоставляющий доступ к текущим параметрам AutoShow, сохраненным в поле. Используйте его, чтобы проверить, как существующая рабочая книга или только что настроенная сводная таблица будет отображать свои элементы. Этот метод также применяется к рабочим книгам, загруженным из файла.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Геттеры `isAutoShow()`, `isTop()`, `getAutoShowCount()` и `getRankBy()` соответствуют классическим атрибутам AutoShow, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому считанные значения учитываются всеми версиями Excel.

## **Примечание**

{{% alert color="primary" %}}
- Прямые геттеры `PivotField` — `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` и `getAutoShowField()` — помечены как устаревшие. Вместо них используйте объект, возвращаемый методом `getTop10AutoShowSettings()`: `isAutoShow()` заменяется на `getTop10AutoShowSettings().isAutoShow()`, `isAscendShow()` — на `getTop10AutoShowSettings().isTop()`, `getAutoShowCount()` — на `getTop10AutoShowSettings().getAutoShowCount()`, а `getAutoShowField()` — на `getTop10AutoShowSettings().getRankBy()`. Сам метод `top10AutoShow()` является поддерживаемым способом изменения этих параметров.
- `top10AutoShow()` работает с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не размещены в основной части сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр «Топ-10» (FilterTop10)**
Современные версии Excel представляют «Топ-10» в виде фильтра значений в меню поля («Фильтры значений», «Топ-10…»). В Aspose.Cells этот фильтр реализуется методом `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, который возвращает созданный объект `PivotFilter`:
- `valueFieldIndex` — нулевой индекс поля данных, агрегированные значения которого определяют рейтинг элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.COUNT` оставляет фиксированное количество элементов (вариант «Элементы» в диалоговом окне). `PivotFilterType.PERCENT` оставляет заданный процент элементов, поэтому `itemCount` сам по себе является процентом: значение 30 оставляет верхние 30 процентов. `PivotFilterType.SUM` ранжирует элементы по накопленному объему значений.
- `isTop` — значение `true` для варианта «Топ», `false` — для варианта «Низ».
- `itemCount` — число N в выражении «Топ-N»; его единица измерения зависит от `type`.

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` и `filterTop10()` — два отдельных механизма. AutoShow записывает классический атрибут `autoShow` для поля сводной таблицы и поддерживается всеми версиями Excel, начиная с Excel 97. `filterTop10()` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. При открытии рабочей книги в более старой версии Excel сводная таблица с современным фильтром отображает все элементы. Для документов, которые должны проходить цикл сохранения и повторного открытия в устаревших инструментах, предпочтителен `top10AutoShow()`; для современных рабочих книг предпочтителен `filterTop10()`, поскольку он сочетается с другими фильтрами значений.
{{% /alert %}}

## **Связанные статьи**
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Добавление полей строки и столбца в сводную таблицу](/cells/ru/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Группировка полей в сводной таблице](/cells/ru/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/nodejs-java/refresh-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}