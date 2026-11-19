---
title: Фильтрация сводных таблиц по подписи или значению
linktitle: Фильтрация сводных таблиц по подписи или значению
description: Aspose.Cells for .NET поддерживает широкие возможности фильтрации сводных таблиц. В этой статье объясняется, как фильтровать данные сводной таблицы с помощью фильтров по подписи, фильтров по дате, фильтров по значению, фильтров «первые 10», а также путём скрытия и отображения элементов сводной таблицы.
keywords: Aspose.Cells, библиотека .NET, электронная таблица, сводная таблица, фильтр, фильтр по подписи, фильтр по значению, фильтр по дате, фильтр «первые 10», элемент сводной таблицы, скрытие элемента сводной таблицы
type: docs
weight: 10
url: /ru/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет пять практических стратегий фильтрации данных, отображаемых в сводной таблице. Можно применять фильтры по подписи к текстовым полям строк или столбцов, использовать фильтры по дате, когда поле содержит только ячейки с датой и временем или пустые значения, применять фильтры по значению к агрегированным числам, использовать фильтры «первые 10» для ранжирования по полю значения, а также вручную скрывать и отображать отдельные элементы сводной таблицы с помощью свойства `IsHidden`. Каждая стратегия реализована через специальные API классов `PivotField` и `PivotItem`.
{{% /alert %}}

## **Введение**
Сводные таблицы — мощный инструмент анализа, однако необработанные итоги часто содержат значительно больше информации, чем требуется представить. Фильтрация — основной механизм сужения сводной таблицы до строк, столбцов или значений, важных для конкретного отчёта. Aspose.Cells for .NET воспроизводит возможности фильтрации, доступные в Microsoft Excel, и предоставляет их программно, чтобы формирование отчётов можно было полностью автоматизировать.
В этой статье рассмотрены следующие стратегии фильтрации:
1. **Фильтр по подписи** — фильтрует элементы поля строки или столбца на основе их текстовых подписей.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, содержащие только значения даты и времени (или пустые значения).
3. **Фильтр по значению** — фильтрует элементы на основе агрегированных значений поля данных.
4. **Фильтр «первые 10»** — отображает только верхние или нижние N элементов, ранжированных по полю значения.
5. **Скрытие / отображение элементов сводной таблицы** — управление видимостью каждого отдельного элемента в поле.
Каждый подход использует отдельный метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `PivotCache.Refresh()` для сводной таблицы, чтобы кэшированные данные и вычисленные значения отражали новое состояние фильтра.

## **Фильтр по подписи**
Фильтр по подписи позволяет фильтровать элементы поля строки или столбца, сравнивая их текстовые подписи с шаблоном. Это полезно, когда требуется отобразить только товары, названия которых начинаются с определённой буквы, содержат конкретное слово или соответствуют другому критерию, основанному на подписи.
Aspose.Cells предоставляет фильтрацию по подписи через метод `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`. Аргумент `filterType` задаёт режим сравнения (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и так далее). Аргументы `label1` и `label2` содержат текст для сравнения — передавайте `string.Empty` для `label2`, когда требуется сравнение с одним значением (например, «начинается с» или «содержит»).
В следующем примере загружается рабочая книга, содержащая существующую сводную таблицу, применяется фильтр по подписи так, чтобы оставались видимыми только элементы, подписи которых начинаются с указанного префикса, сводная таблица обновляется и результат сохраняется.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string fileName = "sample.xlsx";
string prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.Worksheets[0];
// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];
// Retrieve the first row PivotField
PivotField rowField = pivotTable.RowFields[0];
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook back to disk
workbook.Save(fileName);
```

## **Фильтр по дате**
Фильтры по дате позволяют сузить сводную таблицу по критериям, основанным на дате, таким как сегодня, прошлая неделя, этот месяц, следующий квартал или конкретный диапазон дат. Это специализированные фильтры, которые работают только для полей, содержащих информацию о дате и времени.

{{% alert color="primary" %}}
Фильтр по дате работает только тогда, когда область строк или столбцов содержит исключительно ячейки с датой и временем или пустые значения. Если базовое поле содержит данные других типов, например числа или текст, фильтр по дате не даст ожидаемого результата. Убедитесь, что поле отформатировано как дата и что все значения являются допустимыми экземплярами `DateTime` или пустыми ячейками, прежде чем применять этот фильтр.
Aspose.Cells предоставляет фильтрацию по дате через метод `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`. Перечисление `PivotFilterType` содержит специальные значения для дат, такие как `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра передаётся одно или два значения `DateTime` (для `Between` передаются начальная и конечная даты).
В следующем примере загружается рабочая книга со сводной таблицей, у которой область строк содержит поле даты, применяется фильтр по дате, ограничивающий видимые элементы конкретным диапазоном дат, сводная таблица обновляется, и рабочая книга сохраняется.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";
if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.Worksheets[0];
// Access the pivot table by index
var pivotTable = worksheet.PivotTables[0];
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.RowFields[0];
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.PivotCache.Refresh();
// Persist the workbook
workbook.Save(outputPath);
```

## **Фильтр по значению**
Фильтры по значению работают с агрегированными значениями, которые сводная таблица вычисляет в области данных. Вместо сопоставления текстовых подписей они сравнивают числовые итоги с пороговым значением. Типичные сценарии использования включают отображение только товаров, сумма продаж которых превышает целевое значение, или только регионов, количество транзакций в которых попадает в заданный диапазон.
Aspose.Cells предоставляет фильтрацию по значению через метод `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Параметр `valueFieldIndex` указывает, какое поле данных должно оцениваться (используйте `pivotTable.DataFields.IndexOf(dataField)` или выполните итерацию по коллекции, чтобы найти позицию). Параметр `filterType` принимает такие значения, как `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Два аргумента типа `double` задают пороговое значение (или значения).
В следующем примере загружается рабочая книга со сводной таблицей, применяется фильтр по значению, который оставляет только элементы, агрегированные продажи которых превышают числовой порог, сводная таблица обновляется, и рабочая книга сохраняется.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];
var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}
pivotTable.PivotCache.Refresh();
workbook.Save("output.xlsx");
```

## **Фильтр «первые 10»**
Фильтр «первые 10» — это специализированная форма фильтра по значению, которая сохраняет только верхние или нижние N элементов на основе выбранного поля значения. Он часто используется в отчётах с ранжированием, например «10 лучших товаров по выручке» или «5 худших регионов по количеству продаж».

{{% alert color="primary" %}}
Фильтр «первые 10» эффективен только тогда, когда в области данных сводной таблицы имеется одно или несколько полей значений. Без хотя бы одного поля значения нет агрегированной меры, по которой можно ранжировать элементы, и фильтр не может быть применён.
Aspose.Cells предоставляет фильтрацию Top 10 через метод `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Параметр `valueFieldIndex` — это индекс поля данных, по агрегированным значениям которого ранжируются элементы, `filterType` выбирает единицу для `itemCount` (`Count` сохраняет фиксированное количество элементов, `Percent` сохраняет процент элементов, поэтому `itemCount` — это сам процент), `isTop` указывает, сохранять верхние элементы (true) или нижние (false), а `itemCount` определяет, сколько элементов или какой процент сохранить.
В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значения, применяется фильтр «первые 10», чтобы оставить только 10 элементов с наибольшей суммой продаж, сводная таблица обновляется, и рабочая книга сохраняется.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load the existing workbook that contains the pivot table
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.Worksheets[0];
// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];
// Confirm there is at least one value PivotField in the data area
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.RowFields[0];
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - valueFieldIndex = 0 — the data field used to rank items
//   - filterType  = PivotFilterType.Count (keep a fixed number of items;
//     PivotFilterType.Percent would interpret 10 as "top 10 percent")
//   - isTop       = true (top N; false would mean bottom N)
//   - itemCount   = 10
rowField.FilterTop10(valueFieldIndex, PivotFilterType.Count, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook
workbook.Save(outputPath);
```

## **Фильтрация путём скрытия или отображения элементов сводной таблицы**
Помимо структурированных API фильтрации, Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Перебирая коллекцию `PivotItems` объекта `PivotField` и переключая свойство `IsHidden`, можно выборочно скрывать определённые элементы без применения фильтра на основе формул. Установка `IsHidden = true` скрывает элемент в сводной таблице; установка `IsHidden = false` отображает его снова.
Этот подход полезен, когда правило фильтрации является нерегулярным или специфичным для элемента, например при необходимости скрыть небольшое число именованных категорий, которые не должны появляться в конкретном отчёте. В примере ниже загружается сводная таблица, скрывается определённый элемент по имени, демонстрируется, как его отобразить, сводная таблица обновляется, и рабочая книга сохраняется.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.Worksheets[0];
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.PivotTables[0];
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.RowFields[0];
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];
    // Hide pivot items that match a specific name/criterion
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.PivotCache.Refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.Save("output_pivot_filtered.xlsx");
```

## **Заключение**
Aspose.Cells for .NET предоставляет полный набор возможностей фильтрации сводных таблиц, соответствующий возможностям Microsoft Excel. Фильтры по подписи, дате и значению охватывают наиболее распространённые аналитические сценарии, а фильтр «первые 10» предназначен для отчётов с ранжированием. Когда правило фильтрации является нерегулярным, свойство `PivotItem.IsHidden` предлагает гибкую альтернативу на уровне отдельных элементов. Сочетание этих стратегий — например, применение фильтра по подписи с последующим скрытием определённых элементов — позволяет полностью из кода формировать точные отчёты на основе сводных таблиц.

## Связанные статьи
- [Добавление полей строк и столбцов в сводную таблицу в Aspose.Cells for .NET](/cells/ru/net/pivot-table-add-row-and-column-fields/)
- [Управление полями значений сводной таблицы в Aspose.Cells for .NET](/cells/ru/net/manage-value-fields/)
- [Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for .NET](/cells/ru/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}