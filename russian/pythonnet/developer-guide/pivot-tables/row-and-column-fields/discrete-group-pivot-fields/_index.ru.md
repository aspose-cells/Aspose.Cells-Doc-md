---
title: Дискретная группировка элементов поля сводной таблицы
linktitle: Дискретная группировка
description: Узнайте, как с помощью DiscreteGroupItem и pivot_field_group_options.discrete_group_items группировать элементы поля сводной таблицы в пользовательские группы с заданными именами, например «фрукты» и «овощи», в Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, сводная таблица, дискретная группировка, DiscreteGroupItem, PivotFieldGroupOptions, группировка элементов сводной таблицы, пользовательские группы, PivotField.group, Python, сводная таблица Excel
type: docs
weight: 90
url: /ru/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Автоматическая группировка объединяет элементы в зависимости от типа данных: например, даты — по месяцам и кварталам, а числа — по диапазонам. Дискретная группировка решает обратную задачу: объединяет заданные несвязанные элементы в пользовательские группы с определенными именами, например продукты — в группы «фрукты» и «овощи», магазины — по регионам, а счета — по зонам. В Aspose.Cells дискретная группировка реализована с помощью класса `DiscreteGroupItem` и свойства `pivot_field_group_options.discrete_group_items`.
- Класс `DiscreteGroupItem` представляет собой имя группы и элементы, входящие в нее. Элементы можно идентифицировать двумя способами: по именам (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) или по индексам элементов в исходных данных с нуля (`DiscreteGroupItem("fruit", [0, 3])`). Оба варианта дают одинаковый результат.
- Дискретная группировка применяется к полю в области строк или столбцов сводной таблицы путем передачи параметров группировки в `pivot_field.group(PivotFieldGroupOptions)`.

## **Группировка элементов поля сводной таблицы по именам**
В следующем примере создается небольшая таблица продаж (продукт, дата и сумма), на основе которой формируется сводная таблица. В ней `product` размещается в области строк, `date` — в области столбцов, а `amount` — в области данных. Затем по именам элементов определяются две пользовательские группы: `fruit` (`grape`, `cherry`) и `vegetables` (`carrot`, `potato`). В результате формируется двухуровневая структура строк: на внешнем уровне отображается имя группы, а под ним вложены исходные элементы. Такая структура позволяет отслеживать тенденции по каждой пользовательской группе и каждому элементу.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

После вызова `calculate_data()` в области строк сводной таблицы отображаются `fruit` (`grape` — 50, `cherry` — 80) и `vegetable` (`carrot` — 60, `potato` — 70), а общий итог составляет 260. Подписи столбцов по-прежнему содержат четыре даты (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Группировка элементов поля сводной таблицы по индексам**
При длинных или локализованных именах элементов второй конструктор `DiscreteGroupItem` позволяет определить их по индексам. Индексы соответствуют позициям элементов в исходных данных: нумерация начинается с нуля, а позиции определяются порядком появления элементов, а не алфавитным порядком. В приведенных выше данных элементу `grape` соответствует индекс 0, `carrot` — индекс 1, `potato` — индекс 2, а `cherry` — индекс 3. Поэтому для `fruit` используются индексы `{ 0, 3 }`, а для `vegetable` — `{ 1, 2 }`. Результат совпадает с результатом при группировке по именам.

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **Примечание**

{{% alert color="primary" %}}
- Элементы, не включенные ни в одну пользовательскую группу, не удаляются. Они остаются в сводной таблице на том же уровне, что и пользовательские группы, и отображаются как отдельные записи, содержащие по одному элементу. Если определить только группу `fruit`, элементы `carrot` и `potato` останутся в области строк как самостоятельные записи рядом с группой `fruit`.
- Свойство `pivot_field_group_options.new_pivot_field` определяет компоновку дискретной группировки. По умолчанию для него задано значение `True`, при котором сгруппированное поле добавляется как новое поле внешнего уровня рядом с исходным полем и формирует показанную выше двухуровневую структуру (число полей в `row_fields` увеличивается до 2). Установите для него значение `False`, чтобы заменить исходное поле. Тогда в области строк будет отображаться единственный уровень, содержащий только имена групп и их агрегированные значения: `fruit` — 130 (50 + 80), `vegetable` — 130 (60 + 70).
- Конструкторы `DiscreteGroupItem`, принимающие имена и индексы, можно сочетать в одном списке `discrete_group_items`.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей сводной таблицы](/cells/ru/python-net/group-pivot-fields-in-the-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/python-net/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-net/filter-by-label-or-value-of-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/python-net/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}