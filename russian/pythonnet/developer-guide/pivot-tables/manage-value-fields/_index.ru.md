---
title: Управление полями значений сводной таблицы в Aspose.Cells для .NET
linktitle: Поля значений
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять функцию итогов с помощью PivotField.function и размещать поле значений на оси строк или столбцов в Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, сводная таблица, поле значений, PivotField, PivotField.function, поле данных, PivotTable.values_field, Sum, Average
type: docs
weight: 230
url: /ru/python-net/manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Добавление поля в область данных
Добавление базового поля в область данных (значений) — это первый шаг в формировании того, как сводная таблица агрегирует исходные данные. Aspose.Cells предоставляет метод `PivotTable.add_field_to_area(PivotFieldType, str)`, перегрузку, которая принимает константу `PivotFieldType.DATA` и имя исходного столбца. Как только поле добавлено в область данных, API предоставляет к нему доступ через коллекцию `PivotTable.data_fields` в порядке добавления полей. По умолчанию числовой исходный столбец агрегируется с помощью `ConsolidationFunction.SUM`, а для нечислового столбца по умолчанию используется `Count`.

```python
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Заголовки в A1:D1
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

# Строки данных A2:D9 с использованием вложенных циклов с ветвлением по j
for i in range(1, 9):
    for j in range(4):
        if j == 0:
            worksheet.cells[i, j].put_value("Fruit" if i <= 4 else "Vegetable")
        elif j == 1:
            if i == 1 or i == 2:
                worksheet.cells[i, j].put_value("Apple")
            elif i == 3 or i == 4:
                worksheet.cells[i, j].put_value("Banana")
            elif i == 5 or i == 6:
                worksheet.cells[i, j].put_value("Carrot")
            else:
                worksheet.cells[i, j].put_value("Daikon")
        elif j == 2:
            worksheet.cells[i, j].put_value(2020 + ((i - 1) % 2))
        elif j == 3:
            if i == 1:
                worksheet.cells[i, j].put_value(100)
            elif i == 2:
                worksheet.cells[i, j].put_value(150)
            elif i == 3:
                worksheet.cells[i, j].put_value(80)
            elif i == 4:
                worksheet.cells[i, j].put_value(90)
            elif i == 5:
                worksheet.cells[i, j].put_value(50)
            elif i == 6:
                worksheet.cells[i, j].put_value(60)
            elif i == 7:
                worksheet.cells[i, j].put_value(40)
            else:
                worksheet.cells[i, j].put_value(45)

# Добавить сводную таблицу в F3 с именем PivotTable1
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]

# Расположение сводной таблицы: Category и Item в строках, Year в столбцах, Amount как поле данных
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## Изменение функции итогов
Каждое поле, размещённое в области данных, внутренне оборачивается как экземпляр `PivotField`, и его свойство `function` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `function` позволяет переключаться между доступными агрегатами, включая `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` и `Varp`.
{{% alert color="primary" %}}
Изменение `function` влияет только на агрегат, исходный столбец не изменяется.
{{% /alert %}}
Таким образом, можно оставить одно поле данных как `Sum`, одновременно добавив второе поле данных, которое ссылается на тот же исходный столбец, но использует `Count` или `Average`, всё в рамках одной сводной таблицы.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")

pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

count_field = pivot_table.data_fields[1]
count_field.function = ac.ConsolidationFunction.COUNT

pivot_table.calculate_data()

workbook.save("output_function.xlsx")
```

## Размещение полей значений на оси строк или столбцов
Когда сводная таблица содержит два или более полей данных, Aspose.Cells предоставляет дополнительное виртуальное поле под названием `PivotTable.values_field`. Это виртуальное поле представляет агрегат всех полей данных, находящихся в области данных. Его можно перетащить в область строк или столбцов как базовое поле сводной таблицы, что удобно для расположения нескольких мер бок о бок.
{{% alert color="primary" %}}
`PivotTable.values_field` не работает, если полей значений нет или имеется только одно.
{{% /alert %}}
Приведённые ниже сценарии последовательно рассматривают три полноценных примера, демонстрирующих каждую из описанных выше возможностей на основе одной и той же структуры сводной таблицы.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ac.ConsolidationFunction.COUNT

# Построить поля значений по оси столбцов.
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, pivot_table.values_field)

pivot_table.calculate_data()

workbook.save("output_plot.xlsx")
```

{{< app/cells/assistant language="python-net" >}}