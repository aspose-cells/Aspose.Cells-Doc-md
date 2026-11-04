---
title: Форматирование части сводной таблицы
linktitle: Форматирование части сводной таблицы
description: Форматирование части сводной таблицы в Aspose.Cells for Python via Java, применяя стили к семантическим областям PivotArea или прямоугольникам CellArea через PivotTable.format, при этом форматы хранятся в PivotTable.getPivotFormats() и сохраняются при обновлении сводной таблицы.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, сводная таблица, форматирование, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /ru/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
`PivotTable.formatAll` применяет один стиль ко всей сводной таблице и описан на родительской странице. Он не различает метки, значения, итоги или отдельные области отчёта.  
На практике обычно требуется выделить лишь часть сводной таблицы. Частыми целями являются метки, принадлежащие одному полю строк, ячейки‑значения, созданные одним полем, строка итогов или произвольный прямоугольник, например первые две строки элементов.  
Прямое применение стиля к ячейкам рабочего листа сводной таблицы не эквивалентно. Excel хранит форматирование сводных таблиц как семантические области `PivotArea`, а не как обычные записи стилей ячеек. Формат области Pivot остаётся привязанным к региону, например к меткам поля или значениям данных, и переопределяется при пересчёте, обновлении или расширении сводной таблицы. Стиль, записанный непосредственно в ячейку, привязан к её позиции и не отслеживается моделью сводной таблицы.  
Aspose.Cells предоставляет полный набор перегрузок `PivotTable.format`, чтобы поддержать оба типа форматирования:
- `format(PivotArea, Style)` привязывает стиль к семантической области, создаваемой через `PivotArea.select` или `PivotArea.selectField`.
- `format(CellArea, Style)` привязывает стиль к прямоугольнику рабочего листа внутри сводной таблицы.
- `format(int row, int column, Style)` нацеливается на одну ячейку.
- `formatAll(Style)` форматирует всю сводную таблицу.

## **Форматирование области Pivot**
Рабочий процесс с семантическими областями рекомендуется, когда выделение должно следовать за полем или областью отчёта.
1. Создайте `PivotArea` с `PivotArea(pivot_table)`. Объект описывает семантическую область, принадлежащую конкретной сводной таблице.
1. Выберите поле по его нулевому индексу на заданной оси с `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` выбирает как метки, так и данные поля.
   - `PivotTableSelectionType.LABEL_ONLY` выбирает только метки поля.
   - `PivotTableSelectionType.DATA_ONLY` выбирает только ячейки‑данные поля.
1. Выберите поле по имени с `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. При выборе поля строки по имени область разрешается в ячейки‑значения, созданные элементами этого поля.
1. Создайте `Style` через `workbook.createStyle()`, настройте шрифт, цвет переднего плана и сплошной фон, затем передайте стиль в `PivotTable.format(area, style)`.
1. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `PivotTable.getPivotFormats()`.
1. Форматы, привязанные к полю, отрисовываются при вычислении данных сводной таблицы. Поэтому после применения форматов вызовите `PivotTable.calculateData()`, чтобы стили стали видимыми.  
Следующий пример строит небольшую сводную таблицу продаж фруктов, стилизует метки строк `Fruit` с помощью `PivotArea.select` и `PivotTableSelectionType.LABEL_ONLY`, стилизует ячейки‑значения того же поля через `PivotArea.selectField`, а затем пересчитывает сводную таблицу, чтобы оба стиля были отрисованы.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Форматирование области Cell в сводной таблице**
Используйте `PivotTable.format(CellArea, Style)`, когда интересующая область представляет собой обычный прямоугольник рабочего листа, а не семантическую область сводной таблицы.  
`CellArea` описывается свойствами `getStartRow()`, `getStartColumn()`, `getEndRow()` и `getEndColumn()`. Значения — нулевые координаты листа, а конечные координаты указывают последнюю включённую строку и столбец, поэтому область покрывает ячейки от начальной позиции до конечной включительно.  
В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам сразу. Дополнительный вызов `PivotTable.calculateData()` не требуется для появления стиля.  
Прямоугольник `CellArea` может содержать одновременно метки и значения. В следующем разделе описывается, как Aspose.Cells и Excel представляют такой прямоугольник внутри.  
Следующий пример форматирует прямоугольник `E4:F5` сводной таблицы курсивным светло‑синим стилем и сохраняет рабочую книгу без дальнейшего пересчёта.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    CellArea,
    PivotFieldType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **Соответствие между областями Pivot и Cell**
Excel хранит форматирование сводных таблиц как записи `pivotArea`, а не как обычные записи стилей ячеек листа. Тот же механизм использует Aspose.Cells, поэтому запрос на форматирование переводится в области Pivot при сохранении.  
Соотношение между пользовательской `CellArea` и внутренними областями Pivot является многими‑ко‑многим в обоих направлениях.
- Одна `CellArea` может породить несколько областей Pivot. Если прямоугольник охватывает как метки, так и значения, он разбивается на отдельные правила для меток и данных, поскольку модель сводной таблицы обрабатывает форматирование меток и данных независимо.
- Одна область Pivot может разрешаться в несколько разрозненных экземпляров `CellArea`. Семантическая область, например строка итогов или поле, элементы которого не соприкасаются, может покрывать несколько прямоугольников. Поэтому `PivotArea.getCellAreas()` возвращает коллекцию, а не один прямоугольник.  
Каждая операция форматирования через `PivotTable.format` фиксируется в `PivotTable.getPivotFormats()`. Каждая запись `PivotTableFormat` раскрывает связанный `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за вызов, тогда как `CellArea`, содержащий разные семантические регионы, может добавить несколько записей.  
Чтобы различать сохранённые регионы, каждый `PivotArea` предоставляет флаги `getOnlyLabel()` и `getOnlyData()`. Пример ниже форматирует один прямоугольник, охватывающий как метки, так и значения, исследует `PivotTable.getPivotFormats()` и выводит координаты `CellArea`, в которые разрешается каждая сохранённая область Pivot.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Поскольку форматы хранятся как области Pivot, а не как обычные стили ячеек, они сохраняются при пересчёте и обновлении. При обновлении сводной таблицы через `PivotTable.refreshData()`, пересчёте через `PivotTable.calculateData()` или сохранении и повторной загрузке каждая сохранённая область Pivot переопределяется к текущему положению своей области, и стиль применяется заново.
{{% /alert %}}

Используйте `PivotArea`, построенный через `select` или `selectField`, когда выделение должно оставаться привязанным к полю или семантической области после обновлений, а `CellArea` — когда достаточно отформатировать фиксированный прямоугольник в текущем расположении сводной таблицы. Перегрузка `format(int row, int column, Style)` нацеливается на отдельную ячейку. Применяйте `formatAll`, описанный на родительской странице, когда требуется отформатировать всю сводную таблицу одновременно.

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/python-java/apply-style-to-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/python-java/pivot-table-add-row-and-column-fields/)
- [Управление полями значений в сводной таблице](/cells/ru/python-java/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}