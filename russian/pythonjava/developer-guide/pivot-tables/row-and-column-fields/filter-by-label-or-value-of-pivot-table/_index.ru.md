---
title: Фильтрация сводных таблиц по метке или значению
description: Aspose.Cells for Python via Java поддерживает широкие возможности фильтрации сводных таблиц. В этой статье объясняется, как фильтровать данные сводной таблицы с помощью фильтров по меткам, фильтров по дате, фильтров по значениям, фильтров «первые 10», а также путём скрытия и отображения элементов сводной таблицы.
linktitle: Фильтрация сводных таблиц по метке или значению
keywords: Aspose.Cells, библиотека Python via Java, электронная таблица, сводная таблица, фильтр, фильтр по метке, фильтр по значению, фильтр по дате, фильтр «первые 10», элемент сводной таблицы, скрытие элемента сводной таблицы
type: docs
weight: 10
url: /ru/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells предоставляет пять практических стратегий фильтрации данных, отображаемых в сводной таблице. Можно применять фильтры по меткам к текстовым полям строк или столбцов, использовать фильтры по дате, когда поле содержит только ячейки с датой и временем или пустые значения, применять фильтры по значениям к агрегированным числам, использовать фильтры «первые 10» для ранжирования по полю значений, а также вручную скрывать и отображать отдельные элементы сводной таблицы с помощью свойства `is_hidden`. Каждая стратегия реализована через специализированные API классов `PivotField` и `PivotItem`.
{{% /alert %}}

## **Введение**
Сводные таблицы — это мощный аналитический инструмент, однако необработанные сводки часто содержат значительно больше информации, чем требуется для представления. Фильтрация является основным механизмом сужения сводной таблицы до строк, столбцов или значений, важных для конкретного отчёта. Aspose.Cells for Python via Java повторяет возможности фильтрации, доступные в Microsoft Excel, предоставляя их программно, чтобы формирование отчётов могло быть полностью автоматизировано.
В данной статье рассматриваются следующие стратегии фильтрации:
1. **Фильтр по метке** — фильтрует элементы поля строки или столбца на основе их текстовых меток.
2. **Фильтр по дате** — фильтрует поля строк или столбцов, которые содержат только значения даты и времени (или пустые значения).
3. **Фильтр по значению** — фильтрует элементы на основе агрегированных значений поля данных.
4. **Фильтр «первые 10»** — показывает только верхние или нижние N элементов, ранжированных по полю значений.
5. **Скрытие/отображение элементов сводной таблицы** — позволяет вручную управлять видимостью каждого отдельного элемента в поле.
Каждый подход использует свой метод класса `PivotField` или свойство класса `PivotItem`. После применения любого фильтра необходимо вызвать `refresh_data()` и `calculate_data()` для сводной таблицы, чтобы кэшированные данные и вычисленные значения отражали новое состояние фильтра.

## **Фильтр по метке**
Фильтр по метке позволяет фильтровать элементы поля строки или столбца путём сравнения их текстовых подписей с шаблоном. Это полезно, когда требуется отобразить только те продукты, названия которых начинаются с определённой буквы, содержат конкретное слово или соответствуют другому критерию, основанному на подписи.
Aspose.Cells предоставляет фильтрацию по меткам через метод `PivotField.filter_by_label(PivotFilterType, str)`. Перечисление `PivotFilterType` включает такие значения, как `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` и другие. Второй аргумент задаёт строку метки, используемую для сравнения.
В следующем примере загружается рабочая книга, содержащая существующую сводную таблицу, применяется фильтр по метке, чтобы остались видны только элементы, подписи которых начинаются с указанного префикса, сводная таблица обновляется и результат сохраняется.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the first row PivotField
rowField = pivotTable.getRowFields().get(0)
# Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook back to disk
workbook.save(fileName)
jpype.shutdownJVM()
```

## **Фильтр по дате**
Фильтры по дате позволяют сузить сводную таблицу по критериям, основанным на дате, таким как сегодня, прошлая неделя, этот месяц, следующий квартал или конкретный диапазон дат. Это специализированные фильтры, которые работают только с полями, содержащими информацию о дате и времени.

{{% alert color="primary" %}}
Фильтр по дате работает только тогда, когда область строк или столбцов содержит только ячейки с датой и временем либо пустые значения. Если базовое поле содержит другие типы данных, такие как числа или текст, фильтр по дате не даст ожидаемого результата. Перед применением этого фильтра убедитесь, что поле отформатировано как дата и что все значения являются допустимыми экземплярами `DateTime` или пустыми ячейками.
Aspose.Cells предоставляет фильтрацию по дате через метод `PivotField.filter_by_date(PivotFilterType, values)`. Перечисление `PivotFilterType` содержит специальные значения для дат, такие как `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` и `Between`. В зависимости от выбранного типа фильтра передаётся одно или два значения `DateTime` (для `Between` передаются начальная и конечная даты).
В следующем примере загружается рабочая книга со сводной таблицей, в области строк которой находится поле даты, применяется фильтр по дате, ограничивающий видимые элементы определённым диапазоном дат, сводная таблица обновляется и рабочая книга сохраняется.
{{% /alert %}}

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"
if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")
# Load the existing workbook that contains the pivot table
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
dateField = pivotTable.getRowFields().get(0)
# Define the date criterion for the Between filter
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)
# Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate)
# Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh()
# Persist the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Фильтр по значению**
Фильтры по значениям работают с агрегированными значениями, которые сводная таблица вычисляет в области данных. Вместо сопоставления текстовых меток они сравнивают числовые итоги с пороговым значением. Типичные варианты использования включают отображение только тех продуктов, сумма продаж которых превышает целевую сумму, или только тех регионов, количество транзакций в которых попадает в определённый диапазон.
Aspose.Cells предоставляет фильтрацию по значениям через метод `PivotField.filter_by_value(value_field, filter_type, values)`. Параметр `filter_type` использует такие значения, как `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` и `ValueLessThanOrEqual`. Параметр `value_field` указывает, какое поле данных должно оцениваться, а последний аргумент (или аргументы) задаёт пороговое значение (или значения).
В следующем примере загружается рабочая книга со сводной таблицей, применяется фильтр по значению, который оставляет только элементы, агрегированные продажи которых превышают числовой порог, сводная таблица обновляется и рабочая книга сохраняется.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)
rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break
if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))
pivotTable.getPivotCache().refresh()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Фильтр «первые 10»**
Фильтр «первые 10» — это специализированная форма фильтра по значению, который сохраняет только верхние или нижние N элементов на основе выбранного поля значений. Он часто используется в отчётах с ранжированием, таких как «10 лучших продуктов по выручке» или «5 худших регионов по количеству продаж».

{{% alert color="primary" %}}
Фильтр «первые 10» работает только тогда, когда в области данных сводной таблицы имеется одно или несколько полей значений. Без хотя бы одного поля значений не существует агрегированной меры, по которой можно ранжировать элементы, и фильтр не может быть применён.
Aspose.Cells предоставляет фильтрацию Top 10 через метод `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. Параметр `valueFieldIndex` — это индекс поля данных, по агрегированным значениям которого ранжируются элементы, `filterType` выбирает единицу для `itemCount` (`PivotFilterType.COUNT` сохраняет фиксированное количество элементов, `PivotFilterType.PERCENT` сохраняет процент элементов, поэтому `itemCount` — это сам процент), `isTop` указывает, сохранять верхние элементы (true) или нижние (false), а `itemCount` определяет, сколько элементов или какой процент сохранить.
В следующем примере загружается рабочая книга со сводной таблицей, содержащей поле значений, применяется фильтр «первые 10», чтобы оставить только 10 лучших элементов по сумме продаж, сводная таблица обновляется и рабочая книга сохраняется.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Confirm there is at least one value PivotField in the data area
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.getRowFields().get(0)
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, True, 10)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Фильтрация путём скрытия или отображения элементов сводной таблицы**
Помимо структурированных API фильтрации, Aspose.Cells позволяет напрямую управлять видимостью каждого отдельного элемента сводной таблицы. Перебирая коллекцию `PivotItems` объекта `PivotField` и переключая свойство `is_hidden`, можно выборочно подавлять определённые элементы без применения фильтра на основе формулы. Установка `is_hidden = True` скрывает элемент из сводной таблицы; установка `is_hidden = False` отображает его снова.
Этот подход полезен, когда правило фильтрации является нерегулярным или специфичным для элемента, например при сокрытии небольшого числа именованных категорий, которые не должны отображаться в конкретном отчёте. В примере ниже загружается сводная таблица, скрывается определённый элемент по имени, демонстрируется, как его снова отобразить, сводная таблица обновляется и рабочая книга сохраняется.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem
# Load an existing workbook containing a pivot table
workbook = Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.getWorksheets().get(0)
# Access the pivot table by index (the first pivot table on the sheet)
pivotTable = sheet.getPivotTables().get(0)
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivotField = pivotTable.getRowFields().get(0)
# Iterate through the PivotItems collection of the selected PivotField
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)
    # Hide pivot items that match a specific name/criterion
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setHidden(True)
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.getName() == "Item3":
        item.setHidden(False)
# Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
jpype.shutdownJVM()
```

## **Резюме**
Aspose.Cells for Python via Java предоставляет полный набор возможностей фильтрации сводных таблиц, соответствующий возможностям Microsoft Excel. Фильтры по меткам, дате и значениям охватывают наиболее распространённые аналитические сценарии, тогда как фильтр «первые 10» предназначен для отчётов с ранжированием. Когда правило фильтрации является нерегулярным, свойство `PivotItem.is_hidden` предлагает гибкий резервный вариант на уровне отдельных элементов. Комбинирование этих стратегий — например, применение фильтра по метке с последующим скрытием определённых элементов — позволяет формировать точно нацеленные отчёты сводных таблиц полностью из кода.

{{< app/cells/assistant language="python" >}}