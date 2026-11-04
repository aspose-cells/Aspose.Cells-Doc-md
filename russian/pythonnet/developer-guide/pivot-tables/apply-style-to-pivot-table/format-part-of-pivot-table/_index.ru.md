---
title: Форматирование части сводной таблицы
description: Форматировать часть сводной таблицы в Aspose.Cells for Python via .NET, применяя стили к семантическим областям PivotArea или прямоугольникам CellArea через PivotTable.format; форматы сохраняются в PivotTable.pivot_formats и сохраняются при обновлении сводной таблицы.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Python via .NET, сводная таблица, формат, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /ru/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
`PivotTable.format_all` применяет один стиль ко всей сводной таблице и описан на родительской странице. Он не различает подписи, значения, итоговые строки или отдельные области отчёта. На практике обычно требуется выделить лишь часть сводной таблицы. Часто выделяют подписи, принадлежащие одному полю строк, ячейки‑значения, сформированные одним полем, итоговую строку или произвольный прямоугольник, например первые две строки элементов. Применение стиля непосредственно к ячейкам листа, содержащим сводную таблицу, не эквивалентно. Excel сохраняет форматирование сводной таблицы как семантические регионы `PivotArea`, а не как обычные записи стилей ячеек. Формат, привязанный к области Pivot, остаётся связанным с регионом, таким как подписи поля или значения данных, и пересчитывается при перерасчёте, обновлении или расширении сводной таблицы. Стиль, записанный напрямую в ячейку, привязан к конкретному положению ячейки и не отслеживается моделью сводной таблицы. Aspose.Cells предоставляет полный набор перегрузок `PivotTable.format`, чтобы поддерживать оба типа форматирования:
- `format(PivotArea, Style)` привязывает стиль к семантической области, созданной через `PivotArea.select` или `PivotArea.select_field`.
- `format(CellArea, Style)` привязывает стиль к прямоугольнику листа внутри сводной таблицы.
- `format(int row, int column, Style)` нацеливает одну ячейку.
- `format_all(Style)` форматирует всю сводную таблицу.

## **Форматирование области Pivot**
Работа с семантической областью рекомендуется, когда выделение должно следовать за полем или регионом отчёта.
1. Создайте объект `PivotArea` с помощью `PivotArea(pivot_table)`. Этот объект описывает семантическую область, принадлежащую указанной сводной таблице.  
2. Выберите поле по его нулевой позиции на заданной оси с помощью `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` выбирает как подписи, так и данные поля.  
   - `PivotTableSelectionType.LABEL_ONLY` выбирает только подписи поля.  
   - `PivotTableSelectionType.DATA_ONLY` выбирает только ячейки данных поля.  
3. Выберите поле по имени с помощью `PivotArea.select_field(PivotFieldType axis_type, string field_name)`. При выборе поля строк по имени область разрешается в ячейки‑значения, созданные элементами этого поля.  
4. Создайте объект `Style` через `Workbook.create_style()`, задайте шрифт, цвет переднего плана и сплошной фон, затем передайте стиль в `PivotTable.format(area, style)`.  
5. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `PivotTable.pivot_formats`.  
6. Форматы, привязанные к полям, отображаются при расчёте данных сводной таблицы. Поэтому после применения форматов вызовите `PivotTable.calculate_data()`, чтобы стили стали видимыми.  
Следующий пример создает небольшую сводную таблицу продаж фруктов, оформляет подписи строк `Fruit` с помощью `PivotArea.select` и `PivotTableSelectionType.LABEL_ONLY`, оформляет ячейки‑значения того же поля с помощью `PivotArea.select_field`, а затем пересчитывает сводную таблицу, чтобы оба стиля отобразились.

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **Форматирование области ячеек сводной таблицы**
Используйте `PivotTable.format(CellArea, Style)`, когда интересующая область представлена простым прямоугольником листа, а не семантической областью сводной таблицы. `CellArea` описывается свойствами `start_row`, `start_column`, `end_row` и `end_column`. Значения являются нулевыми координатами листа, а конечные координаты указывают последнюю включаемую строку и столбец, поэтому область охватывает ячейки от начального до конечного положения включительно. В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам немедленно; дополнительный вызов `calculate_data()` не требуется для отображения стиля. Прямоугольник `CellArea` может содержать одновременно подписи и значения. В следующем разделе объясняется, как Aspose.Cells и Excel представляют такой прямоугольник внутренне. Пример ниже форматирует прямоугольник `E4:F5` сводной таблицы курсивным светло‑синим стилем и сохраняет рабочую книгу без дополнительного пересчёта.

```python
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **Соответствие областей Pivot и Cell**
Excel сохраняет форматирование сводных таблиц как записи `pivotArea`, а не как обычные записи стилей ячеек листа. Та же модель используется в Aspose.Cells, поэтому запрос на форматирование преобразуется в области Pivot при записи. Соотношение между `CellArea`, предоставленным пользователем, и внутренними областями Pivot является многократным в обеих направлениях.
- Одна `CellArea` может породить несколько областей Pivot. Если прямоугольник охватывает как подписи, так и значения, он разбивается на отдельные правила для подписей и данных, поскольку модель Pivot обрабатывает их независимо.  
- Одна область Pivot может разрешаться в несколько несвязанных экземпляров `CellArea`. Семантическая область, такая как строка итогов или поле, элементы которого не подряд, может покрывать несколько прямоугольников. Поэтому `PivotArea.get_cell_areas()` возвращает коллекцию, а не один прямоугольник.  
Каждая операция форматирования, выполненная через `PivotTable.format`, фиксируется в `PivotTable.pivot_formats`. Каждая запись `PivotTableFormat` раскрывает связанный `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за вызов, тогда как `CellArea`, содержащий разные семантические регионы, может добавить несколько записей. Чтобы различать сохранённые области, каждый `PivotArea` предоставляет флаги `only_label` и `only_data`. Пример ниже форматирует один прямоугольник, покрывающий одновременно подписи и значения, проверяет `PivotTable.pivot_formats` и выводит координаты `CellArea`, к которым каждый сохранённый регион Pivot разрешается.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
Поскольку форматы сохраняются как области Pivot, а не как обычные стили ячеек, они сохраняются при пересчёте и обновлении. Когда сводная таблица обновляется с помощью `PivotTable.refresh_data`, пересчитывается через `calculate_data` или сохраняется и повторно загружается, каждая сохранённая область Pivot переопределяется к текущему положению своего региона, и стиль повторно применяется.
{{% /alert %}}

Используйте `PivotArea`, построенный через `select` или `select_field`, когда выделение должно оставаться привязанным к полю или семантической области при обновлениях, и используйте `CellArea`, когда достаточно форматировать фиксированный прямоугольник текущего макета сводной таблицы. Перегрузка `format(int row, int column, Style)` работает с отдельной ячейкой. Применяйте `format_all`, описанный на родительской странице, когда требуется переоформить всю сводную таблицу целиком.

## **Сопутствующие статьи**
- [Применение стиля к сводной таблице](/cells/ru/python-net/apply-style-to-pivot-table/)
- [Добавление полей строк и столбцов сводной таблицы](/cells/ru/python-net/pivot-table-add-row-and-column-fields/)
- [Управление полями значений в сводной таблице](/cells/ru/python-net/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}