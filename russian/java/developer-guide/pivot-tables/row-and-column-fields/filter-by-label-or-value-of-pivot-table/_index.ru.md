---
title: Фильтрация сводных таблиц по метке или значению
linktitle: Фильтрация сводных таблиц по метке или значению
description: Aspose.Cells for Java поддерживает широкий набор возможностей фильтрации сводных таблиц. В этой статье описаны способы фильтрации данных сводных таблиц с помощью фильтров по меткам, датам и значениям, фильтра «10 лучших», а также путем скрытия и восстановления видимости элементов сводной таблицы.
keywords: Aspose.Cells, библиотека для Java, электронная таблица, сводная таблица, фильтрация, фильтр по метке, фильтр по значению, фильтр по дате, фильтр «10 лучших», элемент сводной таблицы, скрытие элемента сводной таблицы
type: docs
weight: 10
url: /ru/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предлагает пять практичных способов фильтрации данных, отображаемых в сводной таблице. Можно применять фильтры по меткам к текстовым полям строк или столбцов, использовать фильтры по датам, если поле содержит только ячейки с датой и временем либо пустые ячейки, применять фильтры по значениям к агрегированным числам, использовать фильтр «10 лучших» для ранжирования по полю значений или вручную скрывать элементы сводной таблицы и восстанавливать их видимость с помощью свойства `IsHidden`. Каждый подход доступен через отдельные API классов `PivotField` и `PivotItem`.
{{% /alert %}}

## **Введение**
Сводные таблицы — мощные аналитические инструменты, однако исходные сводные данные часто содержат значительно больше информации, чем необходимо представить. Фильтрация — основной механизм, позволяющий сузить сводную таблицу до строк, столбцов или значений, важных для конкретного отчета. Aspose.Cells for Java обеспечивает программный доступ к возможностям фильтрации, доступным в Microsoft Excel, что позволяет полностью автоматизировать создание отчетов.
В этой статье рассматриваются следующие стратегии фильтрации:
1. **Фильтр по метке** — фильтрует элементы полей строк или столбцов по их текстовым подписям.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, содержащие только значения даты и времени либо пустые значения.
3. **Фильтр по значению** — фильтрует элементы по агрегированным значениям поля данных.
4. **Фильтр «10 лучших»** — отображает только N элементов с наибольшими или наименьшими значениями по полю значений.
5. **Скрытие и восстановление видимости элементов сводной таблицы** — обеспечивает ручное управление видимостью каждого отдельного элемента поля.
Каждый подход использует отдельный метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `getPivotCache().refresh()` для сводной таблицы, чтобы кэшированные данные и вычисленные значения отражали новое состояние фильтрации.

## **Фильтр по метке**
Фильтр по метке позволяет фильтровать элементы поля строки или столбца путем сравнения их текстовых подписей с заданным шаблоном. Это полезно, если требуется отобразить только продукты, названия которых начинаются с определенной буквы, содержат конкретное слово или соответствуют другому критерию, основанному на подписях.
Aspose.Cells предоставляет фильтрацию по метке с помощью метода `PivotField.filterByLabel(PivotFilterType, String)`. Перечисление `PivotFilterType` содержит такие значения, как `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и другие. Второй аргумент задает строку метки, используемую для сравнения.
В следующем примере загружается рабочая книга с существующей сводной таблицей и применяется фильтр по метке, который оставляет видимыми только элементы, подписи которых начинаются с указанного префикса. Затем сводная таблица обновляется, а результат сохраняется.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Фильтр по дате**
Фильтры по датам позволяют сузить сводную таблицу с помощью критериев, основанных на датах, например «сегодня», «прошлая неделя», «текущий месяц», «следующий квартал» или определенный диапазон дат. Это специализированные фильтры, работающие только с полями, содержащими сведения о дате и времени.

{{% alert color="primary" %}}
Фильтр по дате работает только тогда, когда область строк или столбцов содержит исключительно ячейки с датой и временем либо пустые ячейки. Если исходное поле содержит данные других типов, например числа или текст, фильтр по дате не даст ожидаемого результата. Перед применением этого фильтра убедитесь, что поле отформатировано как дата и что все значения являются допустимыми экземплярами `DateTime` или пустыми ячейками.
Aspose.Cells предоставляет фильтрацию по дате с помощью метода `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. Перечисление `PivotFilterType` содержит специализированные значения дат, такие как `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра передается одно или два значения `DateTime` (для `Between` передаются даты начала и окончания).
В следующем примере загружается рабочая книга со сводной таблицей, в области строк которой находится поле даты. Применяется фильтр по дате, ограничивающий набор видимых элементов определенным диапазоном дат, после чего сводная таблица обновляется, а рабочая книга сохраняется.
{{% /alert %}}

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Фильтр по значению**
Фильтры по значениям работают с агрегированными значениями, которые сводная таблица вычисляет в области данных. Вместо сопоставления текстовых меток они сравнивают числовые итоги с пороговым значением. Типичные сценарии применения включают отображение только продуктов, сумма продаж которых превышает заданное значение, или только регионов, количество транзакций которых находится в определенном диапазоне.
Aspose.Cells предоставляет фильтрацию по значениям с помощью метода `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Параметр `filterType` использует такие значения, как `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Параметр `valueField` определяет оцениваемое поле данных, а последний аргумент или аргументы задают пороговое значение или значения.
В следующем примере загружается рабочая книга со сводной таблицей и применяется фильтр по значению, который оставляет только элементы, для которых агрегированный показатель продаж превышает заданный числовой порог. Затем сводная таблица обновляется, а рабочая книга сохраняется.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Фильтр «10 лучших»**
Фильтр «10 лучших» — это специализированный вариант фильтра по значениям, который оставляет только N элементов с наибольшими или наименьшими значениями на основе выбранного поля значений. Такой фильтр часто используется при подготовке отчетов с ранжированием, например «10 самых прибыльных продуктов по выручке» или «5 регионов с наименьшим числом продаж».

{{% alert color="primary" %}}
Фильтр «10 лучших» действует только тогда, когда в области данных сводной таблицы есть одно или несколько полей значений. Без хотя бы одного поля значений не существует агрегированной меры, по которой можно ранжировать элементы, поэтому применить фильтр невозможно.
Aspose.Cells предоставляет фильтрацию «10 лучших» с помощью метода `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)`. Параметр `valueFieldIndex` задает индекс поля данных, агрегированные значения которого используются для ранжирования элементов. Параметр `filterType` определяет, как интерпретируется `itemCount` (`PivotFilterType.COUNT` оставляет фиксированное количество элементов, а `PivotFilterType.PERCENT` — процент элементов, поэтому в этом случае `itemCount` задает сам процент). Параметр `isTop` указывает, следует ли оставить элементы с наибольшими (`true`) или наименьшими (`false`) значениями, а `itemCount` определяет, сколько элементов или какой процент элементов следует оставить.
В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значений, и применяется фильтр «10 лучших», чтобы оставить только 10 элементов с наибольшей суммой продаж. Затем сводная таблица обновляется, а рабочая книга сохраняется.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Фильтрация путем скрытия и восстановления видимости элементов сводной таблицы**
Помимо структурированных API фильтрации, Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Перебирая элементы коллекции `PivotItems` поля `PivotField` и изменяя значение свойства `IsHidden`, можно выборочно скрывать определенные элементы без применения фильтра, основанного на формуле. Установка `IsHidden = true` скрывает элемент в сводной таблице; установка `IsHidden = false` восстанавливает его видимость.
Этот подход полезен, когда правило фильтрации является нестандартным или относится к конкретным элементам, например если необходимо скрыть несколько определенных категорий, которые не должны отображаться в конкретном отчете. В приведенном ниже примере загружается рабочая книга со сводной таблицей, скрывается определенный элемент по имени и демонстрируется восстановление его видимости. Затем сводная таблица обновляется, а рабочая книга сохраняется.

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Сводка**
Aspose.Cells for Java предоставляет полный набор возможностей фильтрации сводных таблиц, аналогичный предусмотренным в Microsoft Excel. Фильтры по меткам, датам и значениям охватывают наиболее распространенные аналитические сценарии, а фильтр «10 лучших» используется при подготовке отчетов с ранжированием. Если правило фильтрации нестандартное, свойство `PivotItem.IsHidden` обеспечивает гибкую альтернативу на уровне отдельных элементов. Комбинирование этих подходов — например, применение фильтра по метке с последующим скрытием определенных элементов — позволяет создавать точно нацеленные отчеты на основе сводных таблиц исключительно с помощью кода.

## Связанные статьи
- [Вставка сводной таблицы](/cells/ru/java/create-pivot-table/)
- [Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for Java](/cells/ru/java/pivot-table-add-row-and-column-fields/)
- [Добавление полей фильтра в сводную таблицу в Aspose.Cells for Java](/cells/ru/java/add-page-field-in-pivot-table/)
- [Управление полями значений сводной таблицы в Aspose.Cells for Java](/cells/ru/java/manage-value-fields/)
- [Обновление сводных таблиц и кэшей сводных таблиц в Aspose.Cells for Java](/cells/ru/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}