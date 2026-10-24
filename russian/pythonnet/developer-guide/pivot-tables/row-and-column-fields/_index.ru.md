---
title: Добавить поля строк и столбцов сводной таблицы в Aspose.Cells для .NET
description: Узнайте, как добавлять базовые поля в области строк и столбцов сводной таблицы и управлять промежуточными итогами полей сводки с помощью PivotField.set_subtotals в Aspose.Cells for Python via .NET.
linktitle: Поля строк и столбцов
keywords: Aspose.Cells, Python via .NET, сводная таблица, поле строки, поле столбца, PivotField, set_subtotals, PivotFieldSubtotalType, промежуточные итоги
type: docs
weight: 220
url: /ru/python-net/pivot-table-add-row-and-column-fields/
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
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get(0, 0).put_value("Category")
worksheet.cells.get(0, 1).put_value("Item")
worksheet.cells.get(0, 2).put_value("Year")
worksheet.cells.get(0, 3).put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **Сценарий 2 — подавление всех промежуточных итогов (None)**
Вызов `set_subtotals(PivotFieldSubtotalType.NONE, True)` удаляет все строки промежуточных итогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Это полезно, когда требуются необработанные сгруппированные данные без каких-либо строк итогов.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells.get(0, j).put_value(headers[j])
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
        worksheet.cells.get(i + 1, j).put_value(data[i][j])
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [PivotFieldSubtotalType.SUM, PivotFieldSubtotalType.COUNT, PivotFieldSubtotalType.AVERAGE, PivotFieldSubtotalType.MAX, PivotFieldSubtotalType.MIN, PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **Сценарий 3 — настраиваемое подмножество промежуточных итогов (Sum + Average)**
Вы не ограничены одним типом промежуточного итога. Каждый вызов `set_subtotals` действует независимо на один тип, поэтому двукратный вызов метода — один раз с `SUM` и один раз с `AVERAGE` — формирует настраиваемое подмножество из двух строк промежуточных итогов для каждой группы `Category`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get("A1").put_value("Category")
worksheet.cells.get("B1").put_value("Item")
worksheet.cells.get("C1").put_value("Year")
worksheet.cells.get("D1").put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **Резюме**

Три сценария различаются только вызовами `set_subtotals`. Всё остальное — набор данных, поля и области, которым они назначены, — одинаково, что делает макеты прямо сравнимыми.
- **Размещение полей.** Вызов `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` перемещает исходный столбец в определённую область. В пределах одной области порядок вызовов определяет порядок отображения, поэтому первый вызов становится наиболее внешней группой. Для вычисления промежуточных итогов требуются два или более полей в одной и той же области: при наличии одного поля между группами просто нет данных для вычисления промежуточных итогов.
- **Сценарий 1 — автоматические промежуточные итоги.** Отсутствие вызова `set_subtotals` оставляет выбор за Excel, который применяет свой собственный промежуточный итог по умолчанию к числовым полям. Вызов `set_subtotals` с `PivotFieldSubtotalType.AUTOMATIC` явно фиксирует этот выбор, вместо того чтобы оставлять его неявным.
- **Сценарий 2 — без промежуточных итогов.** Вызов `set_subtotals` с `PivotFieldSubtotalType.NONE` отключает промежуточный итог по умолчанию, поэтому сводная таблица сохраняет строки полей и итоговый результат, но опускает строки промежуточных итогов, которые Excel в противном случае добавил бы между ними.
- **Сценарий 3 — выбранное подмножество.** Каждый вызов включает или отключает ровно один тип промежуточного итога, причём вызовы накапливаются, а не сбрасывают друг друга. Поэтому вызов один раз с `PivotFieldSubtotalType.SUM`, а затем ещё раз с `PivotFieldSubtotalType.AVERAGE` приведёт к тому, что оба типа останутся включёнными, и сводная таблица отобразит промежуточный итог по сумме, промежуточный итог по среднему значению и общий итог.

{{% alert color="primary" %}}
Ничто в промежуточных итогах не привязано исключительно к строковой области. Те же самые вызовы `set_subtotals` для поля, взятого из `PivotTable.ColumnFields`, создадут те же три макета на оси столбцов, поскольку настройка относится к полю сводной таблицы, а не к оси, на которой оно размещено.
{{% /alert %}}
## **Связанные статьи**

- [Поле страницы в сводных таблицах](/cells/ru/python-net/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells для Python через .NET](/cells/ru/python-net/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python-net" >}}