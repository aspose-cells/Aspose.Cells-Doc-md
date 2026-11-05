---
title: Добавление условного форматирования к сводной таблице
linktitle: Добавление условного форматирования к сводной таблице
description: Добавление условного форматирования к сводной таблице в Aspose.Cells for Python via Java — привязать правило к области данных с помощью applyTo и области PivotConditionFormatScopeType, либо определить цель с помощью addCellArea и getPivotAreas, затем присоединить правила и стили через getFormatConditions().addCondition.
keywords: Aspose.Cells for Python via Java, сводная таблица, условное форматирование, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /ru/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на родительской и соседней страницах, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это управляемый правилами аналог, позволяющий выделять каждую сумму более 200, затенять средние пятьдесят процентов или помечать элементы с наименьшим рейтингом, и выделение будет следовать за значениями при каждом перерасчёте или обновлении сводной таблицы.

{{% alert color="primary" %}}
Не вызывайте `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` или `FormatConditionCollection.addArea(CellArea)` у объекта `PivotConditionalFormat.getFormatConditions()` условного форматирования сводной таблицы. Эти два перегруженных метода унаследованы из обычного API условного форматирования листа и не работают для сводных таблиц — область ячеек никогда не преобразуется в область сводной таблицы, поэтому запрос беззвучно игнорируется. Всегда определяйте область непосредственно на объекте `PivotConditionalFormat` (`applyTo`, `addCellArea` или `getPivotAreas()`) и добавляйте правило с помощью одного из перегруженных методов `addCondition`.
{{% /alert %}}

## **Применить правило с областью (как в интерфейсе Excel)**
Первый способ позиционирует правило так же, как это делает пользовательский интерфейс Excel. Ячейка сводной таблицы задаётся её нулевыми координатами листа, а область `PivotConditionFormatScopeType` сообщает Aspose.Cells, насколько далеко правило должно распространяться от этой ячейки:
- `PivotConditionFormatScopeType.DATA` — все ячейки‑значения, которые создает сводная таблица, включая общие итоги.
- `PivotConditionFormatScopeType.FIELD` — ячейки‑значения, принадлежащие полю, которое идентифицирует данная ячейка, исключая общие итоги. Ячейка должна быть ячейкой поля, например меткой строкового поля; передача ячейки‑значения вызывает исключение.
- `PivotConditionFormatScopeType.SELECTION` — только ячейки‑значения на пересечении, выбранном ячейкой, обычно одна ячейка‑значение.
Ниже пример, который создаёт сводную таблицу продаж фруктов с левым верхним углом в E3, привязывает условный формат к ячейке F4 (строка 3, столбец 5) с областью `DATA` и выделяет каждую сумму более 200 жирным белым на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и общем итоге 750 правило закрашивает F4, F5 и F7 — разрешённая область охватывает весь столбец данных F4:F7, и только ячейки, прошедшие проверку, подсвечиваются.

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

Привязка того же правила к метке строкового поля E4 (строка 3, столбец 4) с областью `FIELD` приводит к области F4:F6 — тот же столбец данных без строки общего итога, поскольку область теперь описывает поле `Fruit`, а не всю область значений. Область `SELECTION`, привязанная к F4, приводит к только F4.

## **Определить область вручную**
Второй способ пропускает выбор области и явно задает её на `PivotConditionalFormat`.

### **Прямоугольник листа с помощью addCellArea()**
`addCellArea(CellArea)` фиксирует указанный прямоугольник как цель правила. Координаты задаются нул‑базовыми координатами листа, и область точно соответствует переданному прямоугольнику — без расширения до столбца данных и без логики общих итогов. Используйте этот метод, когда интересующие ячейки представляют известный фиксированный прямоугольник текущего расположения сводной таблицы.

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

### **Семантическая область сводной таблицы с помощью getPivotAreas()**
Коллекция `getPivotAreas()` использует ту же модель семантических областей, которую применяет соседняя страница для статических стилей. Создайте `PivotArea`, выберите поле или область с помощью `PivotArea.select(...)` или `PivotArea.selectField(...)` и добавьте её через `getPivotAreas().addPivotArea(PivotArea)`. Семантическая область остаётся привязанной к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и смещении макета. Перегруженный метод `getPivotAreas().add(PivotArea)` всё ещё компилируется, но помечен как устаревший — предпочтительно использовать `addPivotArea`.

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
Каждый вызов `PivotTable.getConditionalFormats().add()` добавляет один `PivotConditionalFormat` к сводной таблице. Условия, их формулы и стили сохраняются вместе с рабочей книгой — при повторном открытии файла в приведённом ниже примере отображаются то же правило со своими типами, операторами и формулами, а `PivotConditionalFormat.getCellAreas()` сообщает те же области. Записи, которым никогда не было присвоено условие, отбрасываются при сохранении рабочей книги, так же как Excel удаляет условный формат без правила.

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
- [Форматировать часть сводной таблицы](/cells/ru/python-java/format-part-of-pivot-table/)
- [Топ‑10 отображений или фильтров в сводной таблице](/cells/ru/python-java/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}