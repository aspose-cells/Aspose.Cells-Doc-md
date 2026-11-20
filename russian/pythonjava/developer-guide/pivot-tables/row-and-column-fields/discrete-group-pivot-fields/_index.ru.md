---
title: Дискретная группировка элементов поля сводной таблицы
linktitle: Дискретная группировка
description: Узнайте, как группировать элементы поля сводной таблицы в пользовательские группы с заданными именами, например «фрукты» и «овощи», с помощью класса DiscreteGroupItem и метода PivotFieldGroupOptions.getDiscreteGroupItems в Aspose.Cells for Python via Java.
keywords: Aspose.Cells, сводная таблица, дискретная группировка, DiscreteGroupItem, PivotFieldGroupOptions, группировка элементов сводной таблицы, пользовательские группы, PivotField.group, Python via Java, сводная таблица Excel
type: docs
weight: 90
url: /ru/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Автоматическая группировка объединяет элементы по типу данных: даты — по месяцам и кварталам, а числа — по диапазонам. Дискретная группировка решает противоположную задачу: объединяет конкретные несвязанные элементы в пользовательские группы с заданными именами, например группирует продукты в группы «фрукты» и «овощи», магазины — по регионам, а счета — по зонам. Aspose.Cells обеспечивает дискретную группировку с помощью класса `DiscreteGroupItem` и метода `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- `DiscreteGroupItem` представляет собой имя группы и элементы, входящие в нее. Элементы можно определить двумя способами: по именам (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) или по индексам элементов в исходных данных (индексация начинается с нуля) (`DiscreteGroupItem("fruit", [0, 3])`). Обе формы дают одинаковый результат.
- Дискретная группировка применяется к полю в области строк или столбцов сводной таблицы путем передачи объект�� параметров группировки в `PivotField.group(PivotFieldGroupOptions)`.

## **Группировка элементов поля сводной таблицы по именам элементов**
В следующем примере создается небольшой список продаж (продукт, дата и сумма), на основе которого формируется сводная таблица с `product` в области строк, `date` в области столбцов и `amount` в области данных. Затем создаются две пользовательские группы по именам элементов: «фрукты» (виноград, вишня) и «овощи» (морковь, картофель). В результате отображается двухуровневая структура строк: на внешнем уровне находится имя группы, а под ним вложены исходные элементы. Это позволяет анализировать тенденции как по каждой пользовательской группе, так и по каждому элементу.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

После вызова `calculateData()` в области строк сводной таблицы отображаются группы «фрукты» (виноград 50, вишня 80) и «овощи» (морковь 60, картофель 70) с общим итогом 260, а подписи столбцов по-прежнему содержат четыре даты (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Группировка элементов поля сводной таблицы по индексам элементов**
Если имена элементов длинные или локализованные, второй конструктор `DiscreteGroupItem` позволяет определить элементы по индексу. Индекс элемента — это его позиция в порядке появления в исходных данных. Индексация начинается с нуля и не зависит от алфавитного порядка. В приведенных выше данных виноград имеет индекс 0, морковь — индекс 1, картофель — индекс 2, а вишня — индекс 3, поэтому группа «фрукты» обозначается как `{ 0, 3 }`, а группа «овощи» — как `{ 1, 2 }`. Результат совпадает с результатом примера группировки по именам.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **Примечание**

{{% alert color="primary" %}}
- Элементы, не включенные ни в одну пользовательскую группу, не теряются. Они остаются в сводной таблице на том же уровне, что и пользовательские группы, причем каждый образует отдельную запись, состоящую из одного элемента. В примере выше, если определить только группу «фрукты», морковь и картофель останутся в области строк как самостоятельные записи рядом с группой «фрукты».
- Методы `PivotFieldGroupOptions.getNewPivotField()` и `setNewPivotField()` управляют компоновкой дискретной группировки. По умолчанию `getNewPivotField()` возвращает `true`. Это добавляет сгруппированное поле как новое внешнее поле рядом с исходным и формирует показанную выше двухуровневую структуру (количество полей в `getRowFields()` увеличивается до 2). Чтобы заменить исходное поле, вызовите `setNewPivotField(false)`. Тогда в области строк будет отображаться только один уровень с именами групп и их агрегированными значениями: «фрукты» 130 (50 + 80) и «овощи» 130 (60 + 70).
- В одной коллекции `getDiscreteGroupItems()` можно одновременно использовать конструкторы `DiscreteGroupItem`, работающие с именами и индексами.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей в сводной таблице](/cells/ru/python-java/group-pivot-fields-in-the-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/python-java/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/python-java/filter-by-label-or-value-of-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/python-java/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}