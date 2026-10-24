---
title: Изменение макета полей страницы в сводной таблице
description: Узнайте, как управлять макетом области полей страницы в сводной таблице с помощью Aspose.Cells for Python via .NET, включая настройку порядка отображения, количества полей страницы до переноса и порядка полей страницы в верхней части сводной таблицы.
linktitle: Изменение макета полей страницы в сводной таблице
keywords: Aspose.Cells, библиотека Python via .NET, электронная таблица, сводная таблица, поле страницы, порядок полей страницы, количество полей страницы до переноса, перемещение поля страницы
type: docs
weight: 191
url: /ru/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Эта статья продолжает тему **Добавление поля страницы в сводную таблицу**. В ней показано, как управлять макетом области полей страницы — полосой элементов управления фильтрами в верхней части сводной таблицы, — включая порядок отображения, количество полей до переноса и изменение их порядка.
{{% /alert %}}

## **Введение**
Сводная таблица в Microsoft Excel предоставляет отдельную **область полей страницы**, расположенную над основной частью таблицы, содержащей строки, столбцы и данные. Эта область отображается в виде полосы раскрывающихся элементов управления фильтрами — по одному на каждое поле страницы. Именно с их помощью конечные пользователи применяют такие критерии, как год или регион, для фильтрации сводной таблицы. Aspose.Cells for Python via .NET моделирует эту область с помощью коллекции `pivot_table.page_fields` и предоставляет три свойства, управляющих визуальным макетом полосы:
- `pivot_table.page_field_order` (значение типа `PrintOrderType`) определяет, размещаются ли дополнительные поля страницы *рядом* с существующими или *под ними*.
- `pivot_table.page_field_wrap_count` задает количество полей страницы, размещаемых в каждой строке или столбце до переноса.
- `pivot_table.page_fields.move(curr_index, dest_index)` изменяет порядок полей страницы, не меняя режим упорядочивания.
В этой статье рассматриваются три примера кода, демонстрирующие каждую из этих операций на общем наборе данных, чтобы можно было сравнить полученные макеты друг с другом.

## **Исходные данные**
| Фрукт   | Год | Регион | Сумма |
|---------|-----|--------|-------|
| Яблоко  | 2022 | Север  | 150   |
| Яблоко  | 2023 | Север  | 180   |
| Банан   | 2022 | Юг     | 120   |
| Банан   | 2023 | Юг     | 140   |
| Вишня   | 2022 | Восток | 200   |
| Вишня   | 2023 | Восток | 220   |
| Виноград | 2022 | Запад | 90    |
| Виноград | 2023 | Запад | 110   |
Во всех примерах кода все восемь строк заполнены в одинаковом порядке, поэтому исходные данные не различаются между сценариями — изменяются только свойства макета полей страницы.

## **Пример 1. Сначала по горизонтали, затем по вертикали**
В первом сценарии два поля страницы (`Year`, `Region`) настраиваются так, чтобы они отображались **друг рядом с другом в одной строке** в верхней части сводной таблицы. Мы назначаем `Fruit` оси строк, размещаем `Year` первым, а `Region` вторым на оси страницы (порядок вызовов `add_field_to_area` определяет начальный индекс), добавляем `Amount` (`Sum`) как поле данных, а затем задаем `page_field_order` значение `PrintOrderType.OVER_THEN_DOWN` и `page_field_wrap_count = 2`. При `OverThenDown` и количестве полей до переноса, равном 2, два поля страницы располагаются горизонтально друг рядом с другом в одной строке в верхней части сводной таблицы, поэтому полоса занимает одну строку шириной в два поля.

```python
import os
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)
workbook = ac.Workbook()
worksheets = workbook.worksheets
pivot_data_sheet = worksheets.add("PivotData")
pivot_data_cells = pivot_data_sheet.cells
# Headers (row 0)
pivot_data_cells.get(0, 0).put_value("Fruit")
pivot_data_cells.get(0, 1).put_value("Year")
pivot_data_cells.get(0, 2).put_value("Region")
pivot_data_cells.get(0, 3).put_value("Amount")
# Row 1: Apple, 2022, North, 150
pivot_data_cells.get(1, 0).put_value("Apple")
pivot_data_cells.get(1, 1).put_value(2022)
pivot_data_cells.get(1, 2).put_value("North")
pivot_data_cells.get(1, 3).put_value(150)
# Row 2: Apple, 2023, North, 180
pivot_data_cells.get(2, 0).put_value("Apple")
pivot_data_cells.get(2, 1).put_value(2023)
pivot_data_cells.get(2, 2).put_value("North")
pivot_data_cells.get(2, 3).put_value(180)
# Row 3: Banana, 2022, South, 120
pivot_data_cells.get(3, 0).put_value("Banana")
pivot_data_cells.get(3, 1).put_value(2022)
pivot_data_cells.get(3, 2).put_value("South")
pivot_data_cells.get(3, 3).put_value(120)
# Row 4: Banana, 2023, South, 140
pivot_data_cells.get(4, 0).put_value("Banana")
pivot_data_cells.get(4, 1).put_value(2023)
pivot_data_cells.get(4, 2).put_value("South")
pivot_data_cells.get(4, 3).put_value(140)
# Row 5: Cherry, 2022, East, 200
pivot_data_cells.get(5, 0).put_value("Cherry")
pivot_data_cells.get(5, 1).put_value(2022)
pivot_data_cells.get(5, 2).put_value("East")
pivot_data_cells.get(5, 3).put_value(200)
# Row 6: Cherry, 2023, East, 220
pivot_data_cells.get(6, 0).put_value("Cherry")
pivot_data_cells.get(6, 1).put_value(2023)
pivot_data_cells.get(6, 2).put_value("East")
pivot_data_cells.get(6, 3).put_value(220)
# Row 7: Grape, 2022, West, 90
pivot_data_cells.get(7, 0).put_value("Grape")
pivot_data_cells.get(7, 1).put_value(2022)
pivot_data_cells.get(7, 2).put_value("West")
pivot_data_cells.get(7, 3).put_value(90)
# Row 8: Grape, 2023, West, 110
pivot_data_cells.get(8, 0).put_value("Grape")
pivot_data_cells.get(8, 1).put_value(2023)
pivot_data_cells.get(8, 2).put_value("West")
pivot_data_cells.get(8, 3).put_value(110)
# Add PivotTableReport sheet
pivot_table_sheet = worksheets.add("PivotTableReport")
pivot_tables = pivot_table_sheet.pivot_tables
# Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
# Add fields
pivot_table.add_field_to_area(PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(PivotFieldType.PAGE, 1)  # Year
pivot_table.add_field_to_area(PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(PivotFieldType.DATA, 3)  # Amount
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM
# Configure page field area layout: place page fields across first, wrap after every 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2
# Refresh and calculate
pivot_table.calculate_data()
# Save
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```

## **Пример 2. Сначала по вертикали, затем по горизонтали**
В этом примере мы размещаем `Fruit` на оси строк, `Year` и `Region` — на оси страницы (`Year` первым), а `Amount` (`Sum`) — как поле данных, точно как в примере 1. Затем мы задаем `page_field_order` значение `PrintOrderType.DOWN_THEN_OVER`, а `page_field_wrap_count` — `2`. При `DownThenOver` и количестве полей до переноса, равном 2, два поля страницы располагаются вертикально одно под другим: `Year` сверху, а `Region` непосредственно под ним, образуя один столбец в верхней части сводной таблицы. Поэтому полоса занимает две строки шириной в одно поле, в отличие от примера 1.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report = workbook.worksheets.add("PivotTableReport")
headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells.get(0, c).put_value(headers[c])
data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]
for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells.get(r + 1, c).put_value(data[r][c])
idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]
pivot_table.add_field_to_area(PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(PivotFieldType.DATA, 3)
pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2
pivot_table.calculate_data()
workbook.save("pageFieldLayout_downThenOver.xlsx")
```

## **Пример 3. Перемещение поля страницы**
В третьем сценарии сохраняются этот набор данных и распределение полей, задается нейтральный макет (`OverThenDown` с количеством полей до переноса `2`), а затем демонстрируется операция `page_fields.move`. Вызов `move(0, 1)` перемещает поле страницы с индексом 0 (`Year`) на позицию 1, а поле страницы, ранее находившееся на позиции 1 (`Region`), сдвигается на позицию 0. После этого вызова `Region` становится первым полем страницы, а `Year` — вторым. Режим переноса и упорядочивания не изменяется, поэтому полоса по-прежнему отображается горизонтально — изменяется только порядок двух раскрывающихся списков.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Year")
data_sheet.cells.get("C1").put_value("Region")
data_sheet.cells.get("D1").put_value("Amount")
data_sheet.cells.get("A2").put_value("Apple")
data_sheet.cells.get("B2").put_value(2022)
data_sheet.cells.get("C2").put_value("North")
data_sheet.cells.get("D2").put_value(150)
data_sheet.cells.get("A3").put_value("Apple")
data_sheet.cells.get("B3").put_value(2023)
data_sheet.cells.get("C3").put_value("North")
data_sheet.cells.get("D3").put_value(180)
data_sheet.cells.get("A4").put_value("Banana")
data_sheet.cells.get("B4").put_value(2022)
data_sheet.cells.get("C4").put_value("South")
data_sheet.cells.get("D4").put_value(120)
data_sheet.cells.get("A5").put_value("Banana")
data_sheet.cells.get("B5").put_value(2023)
data_sheet.cells.get("C5").put_value("South")
data_sheet.cells.get("D5").put_value(140)
data_sheet.cells.get("A6").put_value("Cherry")
data_sheet.cells.get("B6").put_value(2022)
data_sheet.cells.get("C6").put_value("East")
data_sheet.cells.get("D6").put_value(200)
data_sheet.cells.get("A7").put_value("Cherry")
data_sheet.cells.get("B7").put_value(2023)
data_sheet.cells.get("C7").put_value("East")
data_sheet.cells.get("D7").put_value(220)
data_sheet.cells.get("A8").put_value("Grape")
data_sheet.cells.get("B8").put_value(2022)
data_sheet.cells.get("C8").put_value("West")
data_sheet.cells.get("D8").put_value(90)
data_sheet.cells.get("A9").put_value("Grape")
data_sheet.cells.get("B9").put_value(2023)
data_sheet.cells.get("C9").put_value("West")
data_sheet.cells.get("D9").put_value(110)
pivot_sheet = workbook.worksheets.add("PivotTableReport")
pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]
pivot_table.add_field_to_area(PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(PivotFieldType.DATA, 3)
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2
pivot_table.page_fields.move(0, 1)
pivot_table.calculate_data()
workbook.save("pageFieldLayout_move.xlsx")
```

## **Связанные статьи**
- [Добавление поля страницы в сводную таблицу](/cells/ru/python-net/add-page-field-in-pivot-table/) — родительская страница, на которой описывается добавление полей страницы в сводную таблицу.
- [Поля строк и столбцов в сводной таблице](/cells/ru/python-net/row-and-column-fields/) — рассматривает распределение полей по осям строк и столбцов и дополняет работу с осью страницы, показанную здесь.
- [Управление полями значений в сводной таблице](/cells/ru/python-net/manage-value-fields/) — описывает настройку области данных (значений), включая агрегацию `Sum`, используемую в этой статье.
- [Обновление сводной таблицы](/cells/ru/python-net/refresh-pivot-table/) — объясняет, как использовать `refresh_data` и `calculate_data`, необходимые после изменения порядка полей страницы.
- [Применение стиля к сводной таблице](/cells/ru/python-net/apply-style-to-pivot-table/) — показывает, как форматировать отображенную сводную таблицу после создания макета полосы полей страницы.

{{< app/cells/assistant language="python-net" >}}