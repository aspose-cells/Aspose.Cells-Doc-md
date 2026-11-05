---
title: Добавление условного форматирования к сводной таблице
linktitle: Добавление условного форматирования к сводной таблице
description: Добавление условного форматирования к сводной таблице в Aspose.Cells for Python via .NET, привязка правила к региону данных с помощью apply_to и области PivotConditionFormatScopeType, или определение цели с add_cell_area и pivot_areas, затем прикрепление правил и стилей через format_conditions.add_condition.
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, сводная таблица, условное форматирование, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /ru/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на основной странице и на соседней странице, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это правило‑ориентированный аналог: подсветить каждую сумму более 200, затенить средние пятьдесят процентов или отметить позиции с наименьшим рейтингом — и подсветка будет следовать за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells условное форматирование сводных таблиц находится в коллекции `pivot_table.conditional_formats`. Каждая запись представляет собой объект `PivotConditionalFormat`, который независимо отвечает на два вопроса:
- **Где применяется правило?** Целевая область определяется либо через `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)`, что соответствует выбору области в пользовательском интерфейсе Excel, либо через `add_cell_area(cell_area: CellArea)` и коллекцию `pivot_areas`, где область указывается явно.  
- **Что проверяется в правиле?** Одна или несколько условий добавляются в `format_conditions` с помощью `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)`, и каждый условный объект несёт собственный `style`.

{{% alert color="primary" %}}
Не вызывайте `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` или `format_conditions.add_area(cell_area: CellArea)` у объекта `format_conditions` условного формата сводной таблицы. Эти два перегруженных метода унаследованы из обычного API условного форматирования листа и не работают для сводных таблиц — область ячейки никогда не преобразуется в область сводной таблицы, поэтому запрос молча игнорируется. Всегда определяйте регион непосредственно на объекте `pivot_conditional_format` (`apply_to`, `add_cell_area` или `pivot_areas`) и добавляйте правило через одну из перегрузок `add_condition`.
{{% /alert %}}

## **Применить правило с областью (способ Excel UI)**
Первый способ размещает правило так же, как это делает пользовательский интерфейс Excel. Ячейка сводной таблицы задаётся её нулевыми координатами листа, а область `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко правило должно распространяться от этой ячейки:
- `PivotConditionFormatScopeType.DATA` — все ячейки‑значения, которые создаёт сводная таблица, включая итоги.
- `PivotConditionFormatScopeType.FIELD` — ячейки‑значения, принадлежащие полю, которое определяет данная ячейка, без итогов. Ячейка должна быть полевой (например, метка строки‑поля); передача ячейки‑значения вызывает исключение.
- `PivotConditionFormatScopeType.SELECTION` — только те ячейки‑значения, которые находятся на пересечении выбранного диапазона, как правило, одна ячейка‑значение.
Пример ниже создаёт сводную таблицу продаж фруктов, левый верхний угол которой находится в E3, привязывает условный формат к ячейке F4 (строка 3, столбец 5) с областью `PivotConditionFormatScopeType.DATA` и подсвечивает каждую сумму больше 200 жирным белым шрифтом на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и общем итоге 750 правило закрасит F4, F5 и F7 — разрешённый регион охватывает весь столбец данных F4:F7, и лишь ячейки, попадающие под условие, освещаются.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

Привязка того же правила к метке поля‑строки E4 (строка 3, столбец 4) с областью `PivotConditionFormatScopeType.FIELD` приводит к региону F4:F6 — тот же столбец данных без строки общего итога, поскольку область теперь относится к полю `Fruit`, а не ко всей области значений. Область `PivotConditionFormatScopeType.SELECTION`, привязанная к F4, разрешается только в F4.

## **Определить область вручную**
Второй способ пропускает выбор области и явно задаёт её в объекте `PivotConditionalFormat`.

### **Прямоугольник листа с add_cell_area**
`add_cell_area(cell_area: CellArea)` сохраняет указанный прямоугольник в качестве цели правила. Координаты — нулевые координаты листа, и регион точно соответствует заданному прямоугольнику — без расширения до столбца данных и без логики итогов. Используйте этот метод, когда интересующие ячейки образуют известный фиксированный прямоугольник текущего макета сводной таблицы.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
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
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **Семантическая область сводной таблицы с pivot_areas**
`pivot_areas` — тот же семантический‑региональный механизм, который используется на соседней странице для статических стилей. Создайте объект `PivotArea`, выберите поле или регион с помощью `select` или `select_field` и добавьте его через `pivot_areas.add_pivot_area(pivot_area)`. Семантическая область остаётся привязана к своему полю, поэтому условный формат будет следовать за полем при обновлении сводной таблицы и изменении её макета. Перегрузка `pivot_areas.add(pivot_area)` всё ещё компилируется, но помечена как устаревшая — предпочтительно использовать `add_pivot_area`.

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
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Rule - grey text for amounts below 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **Где хранятся правила и как они сохраняются при перезагрузке**
Каждый вызов `pivot_table.conditional_formats.add()` добавляет один `PivotConditionalFormat` в сводную таблицу. Условия, их формулы и стили сохраняются вместе с рабочей книгой — повторное открытие файла в примере ниже показывает то же правило с его типом, оператором и формулой без изменения, а `get_cell_areas()` возвращает те же регионы. Записи, которым никогда не было присвоено условие, отбрасываются при сохранении рабочей книги, аналогично тому, как Excel удаляет условный формат без правила.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/python-net/apply-style-to-pivot-table/)
- [Форматирование части сводной таблицы](/cells/ru/python-net/format-part-of-pivot-table/)
- [Показать топ‑10 или отфильтровать в сводной таблице](/cells/ru/python-net/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}