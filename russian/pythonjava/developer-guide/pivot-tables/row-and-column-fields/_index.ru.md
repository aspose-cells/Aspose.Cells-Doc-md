---
title: Добавить поля строк и столбцов сводной таблицы в Aspose.Cells для .NET
linktitle: Поля строк и столбцов
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ru/python-java/pivot-table-add-row-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Поля строк и столбцов являются строительными блоками сводной таблицы. Поле, помещённое в область строк, отображается вертикально слева от сводной таблицы, тогда как поле, помещённое в область столбцов, отображается горизонтально вверху. В этой статье показано, как программно добавлять базовые поля в эти области и как управлять промежуточными итогами, которые отображаются между группами полей, с помощью метода `PivotField.setSubtotals`.

## **Добавление поля в область строк или столбцов**

Метод `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` перемещает базовое поле из исходных данных в одну из четырёх областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.

- `ROW` — поля, размещаемые вертикально слева
- `COLUMN` — поля, размещаемые горизонтально вверху
- `DATA` — поля, значения которых агрегируются
- `PAGE` — поля, используемые в качестве фильтров отчёта

После добавления полей вы можете получить к ним доступ через методы `PivotTable.getRowFields()` и `PivotTable.getColumnFields()`. Каждый метод возвращает коллекцию `PivotFieldCollection`. Поле с индексом 0 в `RowFields` является самым внешним полем строки, а последующие индексы представляют поля, вложенные в него. Та же самая индексация применяется к `ColumnFields`.

Порядок вложенности полей имеет значение. Если сначала добавить `Category` в область строк, а затем `Item`, получится сводная таблица, в которой внешняя группировка — `Category`, а внутренняя группировка — `Item`. Изменение порядка на противоположный меняет иерархию.

## **Промежуточные итоги полей сводной таблицы**

Метод `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` управляет тем, какие строки промежуточных итогов отображаются для поля сводной таблицы. Каждый вызов переключает один тип промежуточного итога независимо. Передача `shown = true` отображает промежуточный итог, тогда как `shown = false` скрывает его. Поскольку каждый вызов влияет только на один тип, многократный вызов метода с разными значениями `subtotalType` формирует пользовательское подмножество промежуточных итогов.

Перечисление `PivotFieldSubtotalType` определяет доступные виды промежуточных итогов.

- `AUTOMATIC` — Aspose.Cells выбирает вариант по умолчанию (как правило, `SUM` для числовых полей)
- `NONE` — подавляет все строки промежуточных итогов
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Промежуточные итоги отображаются только тогда, когда в области строк (или в области столбцов) присутствуют два или более полей сводной таблицы. Для одного поля нет ничего значимого для расчёта промежуточного итога между группами, поэтому вызовы `setSubtotals` в этом случае не имеют видимого эффекта. Поэтому в этой статье в каждом примере в область строк помещаются два поля (`Category` внешнее, `Item` внутреннее), чтобы граница промежуточного итога между группами `Category` была видна.
{{% /alert %}}

## **Сценарий 1 — Автоматические (по умолчанию) промежуточные итоги**

Если вы вообще не вызываете `setSubtotals`, Aspose.Cells применяет выбор `AUTOMATIC` к числовым полям. Следующий пример явно подтверждает это поведение, вызывая `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` для внешнего поля строки `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, PivotTable, PivotField, PivotFieldType, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

worksheet.getCells().get(0, 0).putValue("Category")
worksheet.getCells().get(0, 1).putValue("Item")
worksheet.getCells().get(0, 2).putValue("Year")
worksheet.getCells().get(0, 3).putValue("Amount")

worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)

worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)

worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)

worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)

worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)

worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)

worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)

worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)

pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output_automatic.xlsx")

jpype.shutdownJVM()
```

## **Сценарий 2 — Подавление всех промежуточных итогов (None)**

Вызов `setSubtotals(PivotFieldSubtotalType.NONE, true)` удаляет все строки промежуточных итогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Это полезно, когда требуются необработанные сгруппированные данные без каких-либо строк итогов.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.getCells().get(0, j).putValue(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80 ],
    ["Fruit",     "Banana", 2021, 90 ],
    ["Vegetable", "Carrot", 2020, 50 ],
    ["Vegetable", "Carrot", 2021, 60 ],
    ["Vegetable", "Daikon", 2020, 40 ],
    ["Vegetable", "Daikon", 2021, 45 ]
]

for i in range(len(data)):
    for j in range(len(data[0])):
        worksheet.getCells().get(i + 1, j).putValue(data[i][j])

pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output_none.xlsx")

jpype.shutdownJVM()
```

## **Сценарий 3 — Пользовательское подмножество промежуточных итогов (Sum + Average)**

Вы не ограничены одним типом промежуточного итога. Каждый вызов `setSubtotals` действует независимо для одного типа, поэтому двойной вызов метода — один раз с `SUM`, а другой раз с `AVERAGE` — формирует пользовательское подмножество из двух строк промежуточных итогов для каждой группы `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableCollection, PivotTable, PivotFieldType, PivotField, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

worksheet.getCells().get("A1").putValue("Category")
worksheet.getCells().get("B1").putValue("Item")
worksheet.getCells().get("C1").putValue("Year")
worksheet.getCells().get("D1").putValue("Amount")

worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)

worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)

worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)

worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)

worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)

worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)

worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)

worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)

pivotTables = worksheet.getPivotTables()
pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Category")
pivotTable.addFieldToArea(PivotFieldType.Row, "Item")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.Sum, True)
categoryField.setSubtotals(PivotFieldSubtotalType.Average, True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output_custom.xlsx")

jpype.shutdownJVM()
## **Резюме**

Три приведённых выше сценария используют один и тот же набор данных и структуру сводной таблицы. Единственное различие между ними — это вызов `setSubtotals`, применяемый к внешнему полю строки `Category`. Помните о правиле двух полей: одно поле в области не даёт ничего значимого для расчёта промежуточного итога между группами, поэтому всегда размещайте как минимум два поля в области строк или столбцов, когда хотите, чтобы `setSubtotals` оказывал видимый эффект.

## **Связанные статьи**

- [Поля страниц в сводных таблицах](/cells/ru/python-java/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Python via Java](/cells/ru/python-java/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/python-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
