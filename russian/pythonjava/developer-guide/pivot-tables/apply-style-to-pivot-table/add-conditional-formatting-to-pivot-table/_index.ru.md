---
title: Добавление условного форматирования в сводную таблицу
linktitle: Добавление условного форматирования в сводную таблицу
description: Добавьте условное форматирование в сводную таблицу в Aspose.Cells for Python via Java, привяжите правило к области данных с помощью applyTo и области PivotConditionFormatScopeType, или определите цель с помощью addCellArea и getPivotAreas, затем присоедините правила и стили через getFormatConditions().addCondition.
keywords: Aspose.Cells for Python via Java, сводная таблица, условное форматирование, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /ru/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на родительской странице и на соседней странице, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это основанное на правилах аналогие, которое подсвечивает каждую сумму более 200, затемняет средние пятьдесят процентов или отмечает элементы с самым низким рейтингом, и подсветка следует за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells условное форматирование сводных таблиц находится в коллекции `PivotTable.getConditionalFormats()`. Каждый элемент — это `PivotConditionalFormat`, который отвечает независимо на два вопроса:
- **Где применяется правило?** Целевая область определяется либо через `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)`, что соответствует выбору области в пользовательском интерфейсе Excel, либо через `PivotConditionalFormat.addCellArea(CellArea)` и коллекцию `PivotConditionalFormat.getPivotAreas()`, которые явно задают область.
- **Что проверяется правилом?** Одна или несколько условий добавляются в `PivotConditionalFormat.getFormatConditions()` с помощью `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, и каждое условие содержит собственный `Style`.

{{% alert color="primary" %}}
Не вызывайте `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` или `FormatConditionCollection.addArea(CellArea)` у объекта `PivotConditionalFormat.getFormatConditions()` условного формата сводной таблицы. Эти два перегруженных метода унаследованы от обычного API условного форматирования листа и не работают для сводных таблиц — область ячеек никогда не преобразуется в область сводной таблицы, поэтому запрос безмолвно игнорируется. Всегда определяйте область непосредственно в `PivotConditionalFormat` (`applyTo`, `addCellArea` или `getPivotAreas()`) и добавляйте правило с помощью одного из перегруженных методов `addCondition`.
{{% /alert %}}

## **Применение правила с областью (как в интерфейсе Excel)**
Первый способ позиционирует правило так же, как это делает пользовательский интерфейс Excel. Ячейка сводной таблицы задаётся своими нулевыми координатами листа, а область `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко правило должно распространяться от этой ячейки:
- `PivotConditionFormatScopeType.DATA` — все ячейки со значениями, которые создает сводная таблица, включая общие итоги.
- `PivotConditionFormatScopeType.FIELD` — ячейки со значениями, принадлежащие полю, которое идентифицирует ячейка, исключая общие итоги. Ячейка должна быть ячейкой поля, например меткой строкового поля; передача ячейки со значением вызывает исключение.
- `PivotConditionFormatScopeType.SELECTION` — только ячейки со значениями на пересечении, выбранные этой ячейкой, обычно одна ячейка со значением.
В примере ниже создаётся сводная таблица продаж фруктов, левый верхний угол которой находится в E3, привязывается условный формат к ячейке F4 (строка 3, столбец 5) с областью `DATA` и подсвечивает каждую сумму больше 200 жирным белым шрифтом на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и общем итоге 750 правило окрашивает F4, F5 и F7 — разрешённая область охватывает весь столбец данных F4:F7, и только ячейки, прошедшие проверку, подсвечиваются.

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
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

Привязка того же правила к метке поля строки E4 (строка 3, столбец 4) с областью `FIELD` приводит к области F4:F6 — тот же столбец данных без строки общего итога, потому что область теперь описывает поле `Fruit`, а не всю область значений. Область `SELECTION`, привязанная к F4, охватывает только F4.

## **Определение области вручную**
Второй способ опускает выбор области и явно задаёт её в `PivotConditionalFormat`.

### **Прямоугольник рабочего листа с addCellArea()**
`addCellArea(CellArea)` записывает указанный прямоугольник как целевую область правила. Координаты — нулевые координаты рабочего листа, и область ровно соответствует переданному прямоугольнику — без расширения до столбца данных и без логики общих итогов. Используйте, когда интересующие ячейки известны как фиксированный прямоугольник текущего макета сводной таблицы.

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
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **Семантическая область сводной таблицы с getPivotAreas()**
Коллекция `getPivotAreas()` представляет ту же модель семантических областей, что и на странице со статическими стилями. Создайте `PivotArea`, выберите поле или регион с помощью `PivotArea.select(...)` или `PivotArea.selectField(...)` и добавьте его через `getPivotAreas().addPivotArea(PivotArea)`. Семантическая область остаётся привязанной к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и смещении макета. Перегрузка `getPivotAreas().add(PivotArea)` всё ещё компилируется, но помечена как устаревшая — предпочтительно использовать `addPivotArea`.

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
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Rule - grey text for amounts below 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Где хранятся правила и как они сохраняются при перезагрузке**
Каждый вызов `PivotTable.getConditionalFormats().add()` добавляет один `PivotConditionalFormat` к сводной таблице. Условия, их формулы и стили сохраняются вместе с рабочей книгой — повторное открытие файла в примере ниже показывает то же правило с его типом, оператором и формулой, а `PivotConditionalFormat.getCellAreas()` сообщает те же области. Записи, которым никогда не было присвоено условие, отбрасываются при сохранении рабочей книги, так же как Excel удаляет условный формат без правила.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
jpype.shutdownJVM()
```

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/python-java/apply-style-to-pivot-table/)
- [Форматирование части сводной таблицы](/cells/ru/python-java/format-part-of-pivot-table/)
- [Отображение или фильтрация топ‑10 в сводной таблице](/cells/ru/python-java/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}