---
title: Поля значений в Aspose.Cells for Python via Java
linktitle: Поля значений в Aspose.Cells for Python via Java
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять итоговую функцию с помощью PivotField.Function и размещать поле значений на оси строк или столбцов в Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, сводная таблица, поле значений, PivotField, PivotField.Function, поле данных, PivotTable.ValuesField, Сумма, Среднее
type: docs
weight: 230
url: /ru/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Добавление поля в область данных
Добавление базового поля в область данных (значений) — это первый шаг в формировании того, как сводная таблица агрегирует исходные данные. Aspose.Cells предоставляет перегрузку `PivotTable.addFieldToArea(PivotFieldType, string)`, которая принимает константу `PivotFieldType.DATA` и имя исходного столбца. После добавления поля в область данных API предоставляет его через коллекцию `PivotTable.DataFields` в порядке добавления полей. По умолчанию числовой исходный столбец обобщается с помощью `ConsolidationFunction.SUM`, а для нечислового столбца по умолчанию используется `COUNT`.
## Изменение итоговой функции
Каждое поле, помещённое в область данных, внутренне оборачивается как экземпляр `PivotField`, и его свойство `Function` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `Function` позволяет переключаться между доступными агрегатами, включая `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` и `VARP`.
{{% alert color="primary" %}}
Изменение `Function` влияет только на агрегат, исходный столбец при этом не изменяется.
{{% /alert %}}
Таким образом, можно оставить одно поле данных как `SUM`, добавив второе поле данных, ссылающееся на тот же исходный столбец, но использующее `COUNT` или `AVERAGE`, всё в рамках одной сводной таблицы.
## Размещение полей значений на оси строк или столбцов
Когда сводная таблица содержит два или более полей данных, Aspose.Cells предоставляет дополнительное виртуальное поле `PivotTable.ValuesField`. Это виртуальное поле представляет собой агрегат всех полей данных, находящихся в области данных. Его можно перетащить в область строк или столбцов как базовое поле сводной таблицы, что полезно для расположения нескольких мер бок о бок.
{{% alert color="primary" %}}
`PivotTable.ValuesField` не работает, если полей значений нет или присутствует только одно такое поле.
{{% /alert %}}
Приведённые ниже сценарии демонстрируют три полноценных примера, в которых каждая из описанных выше возможностей раскрывается на одной и той же структуре сводной таблицы.
## Сценарий 1 — перетаскивание базового поля в область значений
Этот сценарий показывает, как поместить одно базовое поле (`Amount`) в область данных существующей сводной таблицы. Общая структура сводной таблицы размещает `Category` и `Item` на оси строк, а `Year` — на оси столбцов. После выполнения операции `Amount` появляется в области данных и по умолчанию вычисляется как `Sum` поля `Amount`.
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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## Сценарий 2 — изменение итоговой функции
Этот сценарий начинается с той же структуры сводной таблицы, что и в сценарии 1, но добавляет поле `Amount` в область данных дважды. Оба поля данных ссылаются на один и тот же исходный столбец, однако для второго поля с помощью сеттера `PivotField.Function` задаётся переопределение, в результате чего оно становится `Count` вместо `Sum` по умолчанию.
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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
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
## Сценарий 3 — размещение полей значений на оси строк или столбцов
При наличии двух полей данных `PivotTable.ValuesField` становится доступным для использования. Этот сценарий перетаскивает это агрегатное виртуальное поле в область столбцов, чтобы каждая мера в области данных отображалась как отдельный блок столбцов рядом с `Year`.
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

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```
В совокупности эти три сценария охватывают все аспекты работы с полями значений в Aspose.Cells for Python via Java — от единственного поля данных с `Sum` по умолчанию до сводной таблицы с несколькими мерами, в которой виртуальное поле `ValuesField` управляет расположением по оси строк или столбцов.
## Связанные статьи
- [Поля строк и столбцов сводной таблицы в Aspose.Cells for Python via Java](/cells/ru/python-java/row-and-column-fields/)
- [Поля страниц в сводных таблицах](/cells/ru/python-java/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Python via Java](/cells/ru/python-java/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/python-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python" >}}
