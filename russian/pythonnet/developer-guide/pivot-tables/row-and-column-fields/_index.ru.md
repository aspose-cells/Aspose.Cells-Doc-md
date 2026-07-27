---
title: Добавить поля строк и столбцов сводной таблицы в Aspose.Cells для .NET
linktitle: Поля строк и столбцов
description: Узнайте, как добавлять базовые поля в области строк и столбцов сводной таблицы и управлять промежуточными итогами полей сводки с помощью PivotField.set_subtotals в Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, сводная таблица, поле строки, поле столбца, PivotField, set_subtotals, PivotFieldSubtotalType, промежуточные итоги
type: docs
weight: 220
url: /ru/python-net/pivot-table-add-row-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Добавление поля в область строк или столбцов**

Метод `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` перемещает базовое поле из исходных данных в одну из четырёх областей сводной таблицы. Аргумент `field_type` принимает одно из следующих значений `PivotFieldType`.

- `ROW` — поля, размещаемые вертикально слева
- `COLUMN` — поля, размещаемые горизонтально сверху
- `DATA` — поля, значения которых агрегируются
- `PAGE` — поля, используемые в качестве фильтров отчёта

После добавления полей вы можете получить к ним доступ через свойства `PivotTable.row_fields` и `PivotTable.column_fields`. Каждое свойство возвращает коллекцию `PivotFieldCollection`. Поле с индексом 0 в `row_fields` является самым внешним полем строки, а последующие индексы представляют поля, вложенные внутрь него. То же соглашение об индексации применяется к `column_fields`.

Порядок вложенности полей имеет значение. Добавление `Category` в область строк первым, а затем `Item` создаёт сводную таблицу, в которой внешняя группировка — `Category`, а внутренняя — `Item`. Изменение порядка на противоположный меняет иерархию.

## **Промежуточные итоги полей сводки**

Метод `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` управляет тем, какие строки промежуточных итогов отображаются для поля сводки. Каждый вызов независимо переключает один тип промежуточного итога. Передача `shown = True` отображает промежуточный итог, тогда как `shown = False` скрывает его. Поскольку каждый вызов затрагивает только один тип, многократный вызов метода с разными значениями `subtotal_type` позволяет сформировать настраиваемое подмножество промежуточных итогов.

Перечисление `PivotFieldSubtotalType` определяет доступные виды промежуточных итогов.

- `AUTOMATIC` — Aspose.Cells выбирает вариант по умолчанию (как правило, `SUM` для числовых полей)
- `NONE` — подавить все строки промежуточных итогов
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Промежуточные итоги отображаются только при наличии двух или более полей сводки в области строк (или в области столбцов). У одного поля нет ничего значимого для подведения промежуточного итога, поэтому вызовы `set_subtotals` в этом случае не дают видимого эффекта. Поэтому в этой статье во всех примерах размещаются два поля строк (`Category` внешнее, `Item` внутреннее), чтобы граница промежуточного итога между каждой группой `Category` была видна.
{{% /alert %}}

## **Сценарий 1 — автоматические (по умолчанию) промежуточные итоги**

Если `set_subtotals` вообще не вызывается, Aspose.Cells применяет выбор `AUTOMATIC` к числовым полям. Следующий пример явно подтверждает это поведение, вызывая `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` на внешнем поле строки `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.AUTOMATIC, True)

pivot_table.calculate_data()

workbook.save("output_automatic.xlsx")
```

## **Сценарий 2 — подавление всех промежуточных итогов (None)**

Вызов `set_subtotals(PivotFieldSubtotalType.NONE, True)` удаляет все строки промежуточных итогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Это полезно, когда требуются необработанные сгруппированные данные без каких-либо строк итогов.

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
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
for st in [ac.PivotFieldSubtotalType.SUM, ac.PivotFieldSubtotalType.COUNT, ac.PivotFieldSubtotalType.AVERAGE, ac.PivotFieldSubtotalType.MAX, ac.PivotFieldSubtotalType.MIN, ac.PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()

workbook.save("output_none.xlsx")
```

## **Сценарий 3 — настраиваемое подмножество промежуточных итогов (Sum + Average)**

Вы не ограничены одним типом промежуточного итога. Каждый вызов `set_subtotals` действует независимо на один тип, поэтому двукратный вызов метода — один раз с `SUM` и один раз с `AVERAGE` — формирует настраиваемое подмножество из двух строк промежуточных итогов для каждой группы `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells["A1"].put_value("Category")
worksheet.cells["B1"].put_value("Item")
worksheet.cells["C1"].put_value("Year")
worksheet.cells["D1"].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(ac.PivotFieldSubtotalType.AVERAGE, True)

pivot_table.calculate_data()

workbook.save("output_custom.xlsx")
```

## **Резюме**

Три приведённых выше сценария используют один и тот же набор данных и структуру сводной таблицы. Единственное различие между ними — вызов `set_subtotals`, применяемый к внешнему полю строки `Category`. Помните о правиле двух полей: у одного поля в области нет ничего, между чем можно подвести промежуточный итог, поэтому всегда размещайте как минимум два поля в области строк или столбцов, если хотите, чтобы `set_subtotals` дал видимый эффект.

## **Связанные статьи**

- [Поля страниц в сводных таблицах](/cells/ru/python-net/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Python via .NET](/cells/ru/python-net/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
