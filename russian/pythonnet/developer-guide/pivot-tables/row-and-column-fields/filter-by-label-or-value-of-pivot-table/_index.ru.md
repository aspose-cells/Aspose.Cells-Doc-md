---
title: Фильтрация сводных таблиц по подписи или значению
linktitle: Фильтрация сводных таблиц по подписи или значению
description: Aspose.Cells for Python via .NET поддерживает комплексные возможности фильтрации сводных таблиц. В этой статье объясняется, как фильтровать данные сводной таблицы с помощью фильтров по подписям, фильтров по датам, фильтров по значениям, фильтров топ-10, а также путём скрытия и отображения элементов сводной таблицы.
keywords: Aspose.Cells, Python via .NET library, spreadsheet, pivot table, filter, label filter, value filter, date filter, top 10 filter, pivot item, hide pivot item
type: docs
weight: 10
url: /ru/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет пять практических стратегий фильтрации данных, отображаемых в сводной таблице. Вы можете применять фильтры по подписям к текстовым полям строк или столбцов, использовать фильтры по датам, когда поле содержит только ячейки с датой и временем или пустые значения, применять фильтры по значениям к агрегированным числовым данным, использовать фильтры топ-10 для ранжирования по полю значений или вручную скрывать и отображать отдельные элементы сводной таблицы с помощью свойства `is_hidden`. Каждая стратегия реализована через специализированные API классов `PivotField` и `PivotItem`.

{{% /alert %}}

## **Введение**

Сводные таблицы — это мощный инструмент анализа, однако необработанные сводные данные часто содержат значительно больше информации, чем требуется для представления. Фильтрация является основным механизмом сужения сводной таблицы до строк, столбцов или значений, которые важны для конкретного отчёта. Aspose.Cells for Python via .NET воспроизводит возможности фильтрации, доступные в Microsoft Excel, предоставляя их программно, чтобы генерация отчётов могла быть полностью автоматизирована.

В данной статье рассматриваются следующие стратегии фильтрации:

1. **Фильтр по подписи** — фильтрует элементы поля строк или столбцов на основе их текстовых подписей.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, содержащие только значения даты и времени (или пустые значения).
3. **Фильтр по значению** — фильтрует элементы на основе агрегированных значений поля данных.
4. **Фильтр топ-10** — отображает только топ-N или нижних N элементов, ранжированных по полю значений.
5. **Скрытие и отображение элементов сводной таблицы** — ручное управление видимостью каждого отдельного элемента в поле.

Каждый подход использует отдельный метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `refresh_data()` и `calculate_data()` для сводной таблицы, чтобы кэшированные данные и вычисленные значения отражали новое состояние фильтра.

## **Фильтр по подписи**

Фильтр по подписи позволяет фильтровать элементы поля строк или столбцов путём сравнения их текстовых подписей с шаблоном. Это полезно, когда требуется отобразить только товары, названия которых начинаются с определённой буквы, содержат конкретное слово или соответствуют другому критерию, основанному на подписи.

Aspose.Cells предоставляет фильтрацию по подписям через метод `PivotField.filter_by_label(PivotFilterType, label_string)`. Перечисление `PivotFilterType` включает значения, такие как `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и другие. Второй аргумент задаёт строку подписи, используемую для сравнения.

В следующем примере загружается рабочая книга, содержащая существующую сводную таблицу, применяется фильтр по подписи, чтобы были видны только элементы, подписи которых начинаются с указанного префикса, обновляется сводная таблица и сохраняется результат.

```python
import aspose.cells as ac

fileName = "sample.xlsx"
prefix = "B"

# Load the existing workbook containing a pivot table
workbook = ac.Workbook(fileName)

# Access the worksheet by index (first worksheet)
worksheet = workbook.worksheets[0]

# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]

# Retrieve the first row PivotField
row_field = pivot_table.row_fields[0]

# Apply the label filter — show only row items whose labels begin with the supplied prefix
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")

# Refresh and recalculate the pivot table data so the filter takes effect
pivot_table.pivot_cache.refresh()

# Save the workbook back to disk
workbook.save(fileName)
```

## **Фильтр по дате**

Фильтры по дате позволяют сузить сводную таблицу по критериям, основанным на датах, таким как сегодня, прошлая неделя, этот месяц, следующий квартал или конкретный диапазон дат. Это специализированные фильтры, которые работают только с полями, содержащими информацию о дате и времени.

{{% alert color="primary" %}}

Фильтр по дате работает только тогда, когда область строк или столбцов содержит исключительно ячейки с датой и временем или пустые значения. Если базовое поле содержит данные других типов, такие как числа или текст, фильтр по дате не даст ожидаемого результата. Перед применением этого фильтра убедитесь, что поле отформатировано как дата и что все значения являются допустимыми экземплярами `DateTime` или пустыми ячейками.

{{% /alert %}}

Aspose.Cells предоставляет фильтрацию по датам через метод `PivotField.filter_by_date(PivotFilterType, *date_times)`. Перечисление `PivotFilterType` содержит специализированные значения дат, такие как `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра передаётся одно или два значения `DateTime` (для `Between` передаются начальная и конечная даты).

В следующем примере загружается рабочая книга со сводной таблицей, область строк которой содержит поле даты, применяется фильтр по дате, ограничивающий видимые элементы определённым диапазоном дат, обновляется сводная таблица и сохраняется рабочая книга.

```python
from datetime import datetime

input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"

if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)

# Load the existing workbook that contains the pivot table
workbook = ac.Workbook(input_path)

# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.worksheets[0]

# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]

# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
date_field = pivot_table.row_fields[0]

# Define the date criterion for the Between filter
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# Apply the date filter on the pivot field
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# Refresh and recalculate the pivot table so the filter takes effect
pivot_table.pivot_cache.refresh()

# Persist the workbook
workbook.save(output_path)
```

## **Фильтр по значению**

Фильтры по значениям работают с агрегированными значениями, которые сводная таблица вычисляет в области данных. Вместо сопоставления текстовых подписей они сравнивают числовые итоги с пороговым значением. Типичные варианты использования включают отображение только товаров, сумма продаж которых превышает целевую сумму, или только регионов, количество транзакций которых находится в определённом диапазоне.

Aspose.Cells предоставляет фильтрацию по значениям через метод `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. Параметр `PivotFilterType` использует значения, такие как `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Параметр `value_field` указывает, какое поле данных должно оцениваться, а последний аргумент (или аргументы) задаёт пороговое значение (или значения).

В следующем примере загружается рабочая книга со сводной таблицей, применяется фильтр по значению, который оставляет только элементы, агрегированные продажи которых превышают числовой порог, обновляется сводная таблица и сохраняется рабочая книга.

```python
import aspose.cells as ac

workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break

if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivot_table.pivot_cache.refresh()

workbook.save("output.xlsx")
```

## **Фильтр топ-10**

Фильтр топ-10 является специализированной формой фильтра по значению, который сохраняет только верхние или нижние N элементов на основе выбранного поля значений. Он часто используется для отчётов ранжирования, таких как «топ-10 товаров по выручке» или «5 регионов с наименьшим количеством продаж».

{{% alert color="primary" %}}

Фильтр топ-10 эффективен только тогда, когда в области данных сводной таблицы присутствует одно или несколько полей значений. Без хотя бы одного поля значений нет агрегированной меры для ранжирования элементов, и фильтр не может быть применён.

{{% /alert %}}

Aspose.Cells предоставляет фильтрацию топ-10 через метод `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)`. Параметр `item_count` определяет, сколько элементов следует оставить, `is_top` указывает, сохранять ли верхние элементы (True) или нижние (False), `value_field` ссылается на поле данных, используемое для ранжирования, а `PivotFilterType` управляет способом вычисления значения (обычно `Sum`, а также `Count` и `Percent`).

В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значений, применяется фильтр топ-10, чтобы оставить только 10 верхних элементов по сумме продаж, обновляется сводная таблица и сохраняется рабочая книга.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)

# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.worksheets[0]

# Access the pivot table by index
pivotTable = worksheet.pivot_tables[0]

# Confirm there is at least one value PivotField in the data area
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.row_fields[0]

# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0

# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.pivot_cache.refresh()

# Save the workbook
workbook.save(outputPath)
```

## **Фильтрация путём скрытия или отображения элементов сводной таблицы**

В дополнение к структурированным API-интерфейсам фильтрации Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Перебирая коллекцию `PivotItems` поля `PivotField` и переключая свойство `is_hidden`, можно выборочно исключать определённые элементы без применения формульного фильтра. Установка `is_hidden = True` скрывает элемент из сводной таблицы; установка `is_hidden = False` отображает его снова, делая видимым.

Этот подход полезен, когда правило фильтрации является нерегулярным или специфичным для элемента, например, при скрытии небольшого числа именованных категорий, которые не должны отображаться в конкретном отчёте. Пример ниже загружает сводную таблицу, скрывает определённый элемент по имени, демонстрирует, как отобразить его, обновляет сводную таблицу и сохраняет рабочую книгу.

```python
import aspose.cells as ac

# Load an existing workbook containing a pivot table
workbook = ac.Workbook("pivot_table_sample.xlsx")

# Access the first worksheet which contains the pivot table
sheet = workbook.worksheets[0]

# Access the pivot table by index (the first pivot table on the sheet)
pivot_table = sheet.pivot_tables[0]

# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivot_field = pivot_table.row_fields[0]

# Iterate through the PivotItems collection of the selected PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # Hide pivot items that match a specific name/criterion
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.name == "Item3":
        item.is_hidden = False

# Refresh and recalculate the pivot table so changes take effect
pivot_table.pivot_cache.refresh()

# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
```

## **Заключение**

Aspose.Cells for Python via .NET предоставляет полный набор возможностей фильтрации сводных таблиц, соответствующих тем, что имеются в Microsoft Excel. Фильтры по подписям, датам и значениям охватывают наиболее распространённые аналитические сценарии, а фильтр топ-10 применяется для отчётов ранжирования. Когда правило фильтрации является нерегулярным, свойство `PivotItem.is_hidden` предлагает гибкий резервный вариант на уровне элементов. Комбинирование этих стратегий — например, применение фильтра по подписи с последующим скрытием определённых элементов — позволяет формировать точно нацеленные отчёты сводных таблиц исключительно из кода.
{{< app/cells/assistant language="python-net" >}}