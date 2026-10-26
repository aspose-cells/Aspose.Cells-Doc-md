---
title: Добавление полей строки и столбца сводной таблицы в Aspose.Cells for Python via Java
linktitle: Добавление полей строки и столбца сводной таблицы в Aspose.Cells for Python via Java
description: Узнайте, как добавлять базовые поля в области строк и столбцов сводной таблицы и управлять подытогами полей сводной таблицы с помощью PivotField.setSubtotals в Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, сводная таблица, поле строки, поле столбца, PivotField, setSubtotals, PivotFieldSubtotalType, подытоги
type: docs
weight: 220
url: /ru/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding a Field to the Row or Column Region**
Метод `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` переносит базовое поле из исходных данных в одну из четырех областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`:
- `ROW` — поля, расположенные вертикально слева
- `COLUMN` — поля, расположенные горизонтально в верхней части
- `DATA` — поля, значения которых агрегируются
- `PAGE` — поля, используемые в качестве фильтров отчета
Порядок вложения полей имеет значение. Если сначала добавить `Category` в область строк, а затем `Item`, получится сводная таблица, в которой внешняя группировка — `Category`, а внутренняя — `Item`. Изменение порядка меняет иерархию.

## **Pivot Field Subtotals**
Метод `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` управляет отображением строк подытогов для поля сводной таблицы. Каждый вызов независимо переключает отображение одного типа подытога. Передача `shown = true` отображает подытог, а `shown = false` скрывает его. Поскольку каждый вызов влияет только на один тип, несколько вызовов с разными значениями `subtotalType` позволяют сформировать пользовательское подмножество подытогов.
Перечисление `PivotFieldSubtotalType` определяет доступные типы подытогов.
- `AUTOMATIC` — Aspose.Cells выбирает вариант по умолчанию (обычно `SUM` для числовых полей)
- `NONE` — подавляет все строки подытогов
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
Подытоги отображаются только тогда, когда в области строк (или столбцов) есть два или более поля сводной таблицы. У одного поля нет между чем вычислять содержательный подытог, поэтому в этом случае вызовы `setSubtotals` не имеют видимого эффекта. По этой причине в каждом примере этой статьи используются два поля строки (`Category` — внешнее, `Item` — внутреннее), чтобы была видна граница подытогов между каждой группой `Category`.
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**
Если метод `setSubtotals` не вызывается, Aspose.Cells применяет выбор `AUTOMATIC` к числовым полям. Следующий пример явно подтверждает это поведение, вызывая `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` для внешнего поля строки `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivotTable.calculateData()
workbook.save("output_automatic.xlsx")
jpype.shutdownJVM()
```

## **Scenario 2 — Suppressing All Subtotals (None)**
Вызов `setSubtotals(PivotFieldSubtotalType.NONE, true)` удаляет все строки подытогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Это полезно, если требуются сгруппированные исходные данные без каких-либо итоговых строк.

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.calculateData()
workbook.save("output_none.xlsx")
jpype.shutdownJVM()
```

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
Вы не ограничены одним типом подытога. Каждый вызов `setSubtotals` независимо действует на один тип, поэтому два вызова метода — один с `SUM`, а другой с `AVERAGE` — создают пользовательское подмножество из двух строк подытогов для каждой группы `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable = pivotTables.add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, True)
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, True)
pivotTable.calculateData()
workbook.save("output_custom.xlsx")
jpype.shutdownJVM()
```

## **Recap**
Три сценария различаются только одним: вызовами `setSubtotals`. Всё остальное — набор данных, поля и области, в которые они помещены — идентично, что и делает макеты прямо сравнимыми.
- **Размещение полей.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` перемещает исходный столбец в определённую область. Внутри одной области порядок вызовов определяет порядок отображения, поэтому первый вызов создаёт внешнюю (самую высокую по иерархии) группу. Для вычисления промежуточных итогов необходимо наличие двух или более полей в одной области: при единственном поле между группами нечего суммировать.
- **Сценарий 1 — автоматические промежуточные итоги.** Отсутствие вызова `setSubtotals` оставляет решение за Excel, который применяет собственную настройку промежуточного итога к числовым полям. Вызов `setSubtotals` с параметром `PivotFieldSubtotalType.AUTOMATIC` явно фиксирует это решение, вместо того чтобы оставить его неявным.
- **Сценарий 2 — без промежуточных итогов.** Вызов `setSubtotals` с параметром `PivotFieldSubtotalType.NONE` отключает значение промежуточного итога по умолчанию, поэтому сводная таблица сохраняет строки полей и общий итог, но удаляет строки промежуточных итогов, которые Excel в противном случае вставил бы между ними.
- **Сценарий 3 — выбранный набор.** Каждый вызов переключает ровно один тип промежуточного итога, и вызовы накапливаются, не сбрасывая друг друга. Вызов с параметром `PivotFieldSubtotalType.SUM`, а затем с `PivotFieldSubtotalType.AVERAGE` оставляет оба режима включёнными, и сводная таблица отображает промежуточный итог по сумме, промежуточный итог по среднему и общий итог.

{{% alert color="primary" %}}
Ничего в настройке промежуточных итогов не привязано к строковой области. Те же самые вызовы `setSubtotals`, выполненные для поля, полученного из `PivotTable.ColumnFields`, создают те же три макета на оси столбцов, поскольку настройка относится к самому полю сводной таблицы, а не к оси, на которой оно размещено.
{{% /alert %}}

## **Related Articles**
- [Поля страницы в сводных таблицах](/cells/ru/python-java/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Python via Java](/cells/ru/python-java/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}