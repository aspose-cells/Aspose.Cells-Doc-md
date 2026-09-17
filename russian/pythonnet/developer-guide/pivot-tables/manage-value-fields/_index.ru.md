---
title: Управление полями значений сводной таблицы в Aspose.Cells для .NET
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять функцию итогов с помощью PivotField.function и размещать поле значений на оси строк или столбцов в Aspose.Cells for Python via .NET.
linktitle: Поля значений
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
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field)
pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

## Изменение функции итогов
Каждое поле, размещённое в области данных, внутренне оборачивается как экземпляр `PivotField`, и его свойство `function` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `function` позволяет переключаться между доступными агрегатами, включая `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` и `Varp`.

{{% alert color="primary" %}}
Изменение `function` влияет только на агрегат, исходный столбец не изменяется.
{{% /alert %}}

Таким образом, можно оставить одно поле данных как `Sum`, одновременно добавив второе поле данных, которое ссылается на тот же исходный столбец, но использует `Count` или `Average`, всё в рамках одной сводной таблицы.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
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
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

{{< app/cells/assistant language="python-net" >}}