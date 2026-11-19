---
title: Фильтрация сводных таблиц по метке или значению
description: Aspose.Cells for Node.js via Java поддерживает комплексные возможности фильтрации сводных таблиц. В этой статье объясняется, как фильтровать данные сводной таблицы с помощью фильтров по меткам, фильтров по датам, фильтров по значениям, топ-10 фильтров, а также путём скрытия или отображения элементов сводной таблицы.
linktitle: Фильтрация сводных таблиц по метке или значению
url: /ru/nodejs-java/filter-by-label-or-value-of-pivot-table/
keywords: Aspose.Cells, библиотека Node.js via Java, электронная таблица, сводная таблица, фильтр, фильтр по метке, фильтр по значению, фильтр по дате, топ-10 фильтр, элемент сводной таблицы, скрыть элемент сводной таблицы
type: docs
weight: 10
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет пять практических стратегий фильтрации данных, отображаемых в сводной таблице. Можно применять фильтры по меткам к текстовым полям строк или столбцов, использовать фильтры по датам, когда поле содержит только ячейки с датой и временем либо пустые значения, применять фильтры по значениям к агрегированным числам, использовать топ-10 фильтры для ранжирования по полю значения либо вручную скрывать и отображать отдельные элементы сводной таблицы с помощью свойства `IsHidden`. Каждая стратегия предоставляется через специализированные API классов `PivotField` и `PivotItem`.
{{% /alert %}}

## **Введение**
Сводные таблицы — это мощный аналитический инструмент, однако необработанные сводки зачастую содержат значительно больше информации, чем требуется представить. Фильтрация является основным механизмом сужения сводной таблицы до строк, столбцов или значений, важных для конкретного отчёта. Aspose.Cells for Node.js via Java дублирует возможности фильтрации, доступные в Microsoft Excel, предоставляя их программно, чтобы формирование отчётов можно было полностью автоматизировать.
В данной статье рассматриваются следующие стратегии фильтрации:
1. **Фильтр по метке** — фильтрует элементы поля строки или столбца на основе их текстовых меток.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, содержащие только значения даты и времени (или пустые значения).
3. **Фильтр по значению** — фильтрует элементы на основе агрегированных значений поля данных.
4. **Топ-10 фильтр** — отображает только верхние или нижние N элементов, ранжированных по полю значения.
5. **Скрытие/отображение элементов сводной таблицы** — вручную управляет видимостью каждого отдельного элемента в поле.
Каждый подход использует различный метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `getPivotCache().refresh()` для сводной таблицы, чтобы кешированные данные и вычисленные значения отражали новое состояние фильтра.

## **Фильтр по метке**
Фильтр по метке позволяет фильтровать элементы поля строки или столбца путём сравнения их текстовых заголовков с шаблоном. Это полезно, когда требуется отобразить только товары, названия которых начинаются с определённой буквы, содержат конкретное слово или соответствуют другому критерию, основанному на заголовке.
Aspose.Cells предоставляет фильтрацию по меткам через метод `PivotField.filterByLabel(PivotFilterType, string)`. Перечисление `PivotFilterType` содержит такие значения, как `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и другие. Второй аргумент задаёт строку метки, используемую для сравнения.
В следующем примере загружается рабочая книга, содержащая существующую сводную таблицу, применяется фильтр по метке, чтобы остались видны только элементы, заголовки которых начинаются с указанного префикса, сводная таблица обновляется, и результат сохраняется.

```javascript
const AsposeCells = require("aspose.cells");
let fileName = "sample.xlsx";
let prefix = "B";
// Load the existing workbook containing a pivot table
let workbook = new AsposeCells.Workbook(fileName);
// Access the worksheet by index (first worksheet)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
let rowField = pivotTable.getRowFields().get(0);
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(AsposeCells.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Фильтр по дате**
Фильтры по датам позволяют сузить сводную таблицу по критериям на основе дат, таким как сегодня, прошлая неделя, этот месяц, следующий квартал или конкретный диапазон дат. Это специализированные фильтры, которые работают только с полями, хранящими информацию о дате и времени.

{{% alert color="primary" %}}
Фильтр по дате работает только в том случае, если область строки или столбца содержит только ячейки с датой и временем либо пустые значения. Если базовое поле содержит другие типы данных, такие как числа или текст, фильтр по дате не даст ожидаемого результата. Перед применением этого фильтра убедитесь, что поле отформатировано как дата и что все значения являются допустимыми экземплярами `DateTime` или пустыми ячейками.
Aspose.Cells предоставляет фильтрацию по датам через метод `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. Перечисление `PivotFilterType` содержит специализированные значения дат, такие как `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра передаётся одно или два значения `DateTime` (для `Between` передаются начальная и конечная даты).
В следующем примере загружается рабочая книга со сводной таблицей, в области строк которой находится поле даты, применяется фильтр по дате, ограничивающий видимые элементы определённым диапазоном дат, сводная таблица обновляется, и рабочая книга сохраняется.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
var pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
let dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Фильтр по значению**
Фильтры по значениям работают с агрегированными значениями, которые сводная таблица вычисляет в области данных. Вместо сопоставления текстовых меток они сравнивают числовые итоги с пороговым значением. Типичные случаи использования включают отображение только тех товаров, сумма продаж которых превышает целевую сумму, или только тех регионов, количество транзакций в которых попадает в диапазон.
Aspose.Cells предоставляет фильтрацию по значениям через метод `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. Параметр `filterType` использует значения, такие как `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Параметр `valueField` задаёт, какое поле данных должно оцениваться, а последний аргумент (или аргументы) указывает пороговое значение (или значения).
В следующем примере загружается рабочая книга со сводной таблицей, применяется фильтр по значениям, оставляющий только те элементы, агрегированные продажи которых превышают числовой порог, сводная таблица обновляется, и рабочая книга сохраняется.

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);
var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.VALUE_GREATER_THAN, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Топ-10 фильтр**
Топ-10 фильтр — это специализированная форма фильтра по значениям, которая сохраняет только верхние или нижние N элементов на основе выбранного поля значения. Он часто используется в отчётах ранжирования, таких как «топ-10 товаров по выручке» или «5 худших регионов по числу продаж».

{{% alert color="primary" %}}
Топ-10 фильтр эффективен только тогда, когда сводная таблица имеет одно или несколько полей значений в области данных. Без хотя бы одного поля значения нет агрегированной меры для ранжирования элементов, и фильтр не может быть применён.
Aspose.Cells предоставляет фильтрацию Top 10 через метод `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. Параметр `valueFieldIndex` — это индекс поля данных, по агрегированным значениям которого ранжируются элементы, `filterType` выбирает единицу для `itemCount` (`PivotFilterType.COUNT` сохраняет фиксированное количество элементов, `PivotFilterType.PERCENT` сохраняет процент элементов, поэтому `itemCount` — это сам процент), `isTop` указывает, сохранять верхние элементы (true) или нижние (false), а `itemCount` определяет, сколько элементов или какой процент сохранить.
В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значения, применяется топ-10 фильтр, чтобы оставить только 10 наибольших элементов по сумме продаж, сводная таблица обновляется, и рабочая книга сохраняется.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
let rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
let valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Фильтрация путём скрытия или отображения элементов сводной таблицы**
Помимо структурированных API фильтрации, Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Перебирая коллекцию `PivotItems` объекта `PivotField` и переключая свойство `IsHidden`, можно выборочно подавлять определённые элементы без применения формульного фильтра. Установка `IsHidden = true` скрывает элемент из сводной таблицы; установка `IsHidden = false` отображает его снова, делая видимым.
Этот подход полезен, когда правило фильтрации является нерегулярным или специфичным для элемента, например, при сокрытии небольшого числа именованных категорий, которые не должны появляться в конкретном отчёте. Пример ниже загружает сводную таблицу, скрывает определённый элемент по имени, демонстрирует, как его отобразить, обновляет сводную таблицу и сохраняет рабочую книгу.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
let sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
let pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
let pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3") {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Резюме**
Aspose.Cells for Node.js via Java предоставляет полный набор возможностей фильтрации сводных таблиц, аналогичный тем, что есть в Microsoft Excel. Фильтры по меткам, датам и значениям охватывают наиболее распространённые аналитические сценарии, а топ-10 фильтр обрабатывает отчёты ранжирования. Когда правило фильтрации нерегулярно, свойство `PivotItem.IsHidden` предлагает гибкий резервный вариант на уровне элементов. Комбинирование этих стратегий — например, применение фильтра по меткам с последующим сокрытием определённых элементов — позволяет создавать точные целевые отчёты сводных таблиц полностью из кода.

{{< app/cells/assistant language="nodejs-java" >}}