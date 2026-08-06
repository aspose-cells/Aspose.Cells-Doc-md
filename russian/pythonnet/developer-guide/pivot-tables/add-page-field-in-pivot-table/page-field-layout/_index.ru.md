---
title: Изменение макета полей страницы в сводной таблице
linktitle: Изменение макета полей страницы в сводной таблице
description: Узнайте, как управлять макетом области полей страницы в сводной таблице с помощью Aspose.Cells for Python via .NET, включая настройку порядка отображения, количества полей в строке или столбце и порядка полей страницы в верхней части сводной таблицы.
keywords: Aspose.Cells, Python via .NET library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /ru/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Эта статья является продолжением темы **Добавление поля страницы в сводную таблицу**. В ней показано, как управлять макетом области полей страницы — полосы элементов управления фильтрами в верхней части сводной таблицы — включая порядок отображения, количество полей в строке или столбце и изменение порядка полей.

{{% /alert %}}

## **Введение**

Сводная таблица в Microsoft Excel предоставляет выделенную **область полей страницы**, которая располагается над областью строк, столбцов и данных таблицы. Эта область отображается в виде полосы раскрывающихся элементов управления фильтрами (по одному на каждое поле страницы) — именно на них пользователь нажимает, чтобы разрезать сводную таблицу по таким критериям, как год или регион. Aspose.Cells for Python via .NET моделирует эту область через коллекцию `pivot_table.page_fields` и предоставляет три свойства, которые управляют визуальным расположением полосы:

- `pivot_table.page_field_order` (значение `PrintOrderType`) определяет, размещаются ли дополнительные поля страницы *рядом* с существующими или *под* ними.
- `pivot_table.page_field_wrap_count` задаёт количество полей страницы, размещаемых в строке или столбце до переноса.
- `pivot_table.page_fields.move(curr_index, dest_index)` изменяет порядок полей страницы без изменения режима упорядочивания.

В этой статье последовательно рассматриваются три примера кода, демонстрирующие каждую из этих операций на общем наборе данных, чтобы можно было сравнить полученные макеты.

## **Исходные данные**

Во всех трёх примерах ниже эти восемь строк данных о продажах загружаются на рабочий лист с именем `PivotData`. Данные содержат два кандидата в поля страницы (`Year`, `Region`), одного кандидата в поле строки (`Fruit`) и один показатель (`Amount`), что делает полосу полей страницы удобной для изучения.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

Все восемь строк заполняются в каждом примере кода в одинаковом порядке, поэтому исходные данные никогда не различаются между сценариями — различаются только свойства макета полей страницы.

## **Пример 1: Слева направо, затем сверху вниз**

В первом сценарии мы настраиваем два поля страницы (`Year`, `Region`) так, чтобы они отображались **рядом в одной строке** в верхней части сводной таблицы. Мы назначаем `Fruit` на ось строк, размещаем `Year` первым и `Region` вторым на оси страницы (порядок вызовов `add_field_to_area` определяет начальный индекс), добавляем `Amount` (Sum) как поле данных, а затем устанавливаем `page_field_order` равным `PrintOrderType.OverThenDown` со значением `page_field_wrap_count = 2`. При `OverThenDown` и количестве полей до переноса равном 2, два поля страницы располагаются горизонтально рядом в одной строке в верхней части сводной таблицы, поэтому полоса занимает одну строку шириной в два поля.

```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# Заголовки (строка 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# Строка 1: Яблоко, 2022, Север, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# Строка 2: Яблоко, 2023, Север, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# Строка 3: Банан, 2022, Юг, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# Строка 4: Банан, 2023, Юг, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# Строка 5: Вишня, 2022, Восток, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# Строка 6: Вишня, 2023, Восток, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# Строка 7: Виноград, 2022, Запад, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# Строка 8: Виноград, 2023, Запад, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# Добавить лист PivotTableReport
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# Создать сводную таблицу из PivotData!A1:D9, размещённую в A1 на PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Добавить поля
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Фрукт
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Год
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Регион
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Сумма
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# Настроить расположение области полей страницы: размещать поля страницы сначала по горизонтали, переносить после каждых 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# Обновить и вычислить
pivot_table.calculate_data()

# Сохранить
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```

## **Пример 2: Сверху вниз, затем слева направо**

В этом примере мы размещаем `Fruit` на оси строк, `Year` и `Region` на оси страницы (с `Year` первым) и `Amount` (Sum) как поле данных — точно так же, как в примере 1. Затем мы устанавливаем `page_field_order` равным `PrintOrderType.DownThenOver`, а `page_field_wrap_count` равным `2`. При `DownThenOver` и количестве полей до переноса равном 2, два поля страницы располагаются вертикально одно под другим — `Year` сверху, `Region` непосредственно под ним — образуя один столбец в верхней части сводной таблицы. Таким образом, полоса занимает две строки шириной в одно поле, в отличие от примера 1.

```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

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
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```

## **Пример 3: Перемещение поля страницы**

В третьем сценарии мы сохраняем этот набор данных и распределение полей, задаём нейтральный макет (`OverThenDown` с количеством полей до переноса равным `2`), а затем демонстрируем операцию `page_fields.move`. Вызов `move(0, 1)` перемещает поле страницы с индексом 0 (`Year`) в позицию 1, а поле страницы, которое находилось в позиции 1 (`Region`), сдвигается в позицию 0. После этого вызова `Region` становится первым полем страницы, а `Year` — вторым. Режим упорядочивания и количество полей до переноса не меняются, поэтому полоса по-прежнему отображается горизонтально рядом — изменён только порядок двух раскрывающихся элементов.

```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```

## **Связанные статьи**

- [Добавление поля страницы в сводную таблицу](/cells/ru/python-net/add-page-field-in-pivot-table/) — родительская страница, на которой рассказывается, как добавлять поля страницы в сводную таблицу.
- [Поля строк и столбцов в сводной таблице](/cells/ru/python-net/row-and-column-fields/) — описывает распределение полей по осям строк и столбцов, дополняя работу с осью страницы, показанную здесь.
- [Управление полями значений в сводной таблице](/cells/ru/python-net/manage-value-fields/) — описывает настройку области данных (значений), включая агрегацию `Sum`, используемую в этой статье.
- [Обновление сводной таблицы](/cells/ru/python-net/refresh-pivot-table/) — объясняет `refresh_data` и `calculate_data`, которые необходимы после изменения порядка полей страницы.
- [Применение стиля к сводной таблице](/cells/ru/python-net/apply-style-to-pivot-table/) — показывает, как форматировать отображаемую сводную таблицу после размещения полосы полей страницы.

{{< app/cells/assistant language="python-net" >}}