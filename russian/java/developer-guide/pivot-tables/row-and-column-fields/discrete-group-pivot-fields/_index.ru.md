---
title: Дискретная группировка элементов поля сводной таблицы
linktitle: Дискретная группировка
description: Узнайте, как группировать элементы поля сводной таблицы в пользовательские группы с заданными именами, например «фрукты» и «овощи», с помощью DiscreteGroupItem и PivotFieldGroupOptions.DiscreteGroupItems в Aspose.Cells for Java.
keywords: Aspose.Cells for Java, сводная таблица, дискретная группировка, DiscreteGroupItem, PivotFieldGroupOptions, группировка элементов поля сводной таблицы, пользовательские группы, PivotField.group, Java, сводная таблица Excel
type: docs
weight: 90
url: /ru/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Автоматическая группировка объединяет элементы по типам данных, например даты — по месяцам и кварталам, а числа — по диапазонам. Дискретная группировка решает обратную задачу, объединяя конкретные несвязанные элементы в пользовательские группы с заданными именами: продукты объединяются в группы «фрукты» и «овощи», магазины — по регионам, а счета — по зонам. Aspose.Cells предоставляет дискретную группировку с помощью класса `DiscreteGroupItem` и свойства `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- `DiscreteGroupItem` представляет собой название группы и принадлежащие ей элементы. Элементы можно идентифицировать двумя способами: по именам (`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`) или по их позициям в исходных данных, начиная с нуля (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Обе формы дают одинаковый результат.
- Дискретная группировка применяется к полю в области строк или столбцов сводной таблицы путем передачи параметров группировки в метод `PivotField.group(PivotFieldGroupOptions)`.

## **Группировка элементов поля сводной таблицы по именам**
В следующем примере создается небольшой список продаж (продукт, дата и сумма), а на его основе — сводная таблица, в которой `product` находится в области строк, `date` — в области столбцов, а `amount` — в области данных. Затем определяются две пользовательские группы по именам элементов: «фрукты» (виноград, вишня) и «овощи» (морковь, картофель). В результате отображается двухуровневая компоновка строк: внешний уровень содержит названия групп, а под ними вложены исходные элементы. Благодаря этому можно анализировать тенденции отдельно для каждой пользовательской группы и каждого элемента.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

После вызова `calculateData()` в области строк сводной таблицы отображаются фрукты (виноград 50, вишня 80) и овощи (морковь 60, картофель 70). Общий итог составляет 260, а метки столбцов по-прежнему содержат четыре даты (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Группировка элементов поля сводной таблицы по индексам**
Если имена элементов являются длинными или локализованными, второй конструктор `DiscreteGroupItem` позволяет идентифицировать элементы по индексу. Индексы — это позиции элементов в порядке их появления в исходных данных, а не в алфавитном порядке; нумерация начинается с нуля. В приведенных выше данных виноград имеет индекс 0, морковь — индекс 1, картофель — индекс 2, а вишня — индекс 3; следовательно, фрукты — `{ 0, 3 }`, а овощи — `{ 1, 2 }`. Результат совпадает с результатом примера группировки по именам.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Примечание**

{{% alert color="primary" %}}
- Элементы, не включенные ни в одну пользовательскую группу, не теряются. Они остаются в сводной таблице на том же уровне, что и пользовательские группы, причем каждый элемент образует отдельную запись. В примере выше, если определить только группу «фрукты», морковь и картофель останутся в области строк как самостоятельные записи рядом с группой «фрукты».
- Свойство `PivotFieldGroupOptions.getNewPivotField()` управляет компоновкой дискретной группировки. По умолчанию значение свойства — `true`: сгруппированное поле добавляется как новое внешнее поле рядом с исходным, что создает показанную выше двухуровневую компоновку (`getRowFields()` увеличивается до 2). Установите значение `false` с помощью `setNewPivotField(false)`, чтобы заменить исходное поле. Тогда в области строк останется единственный уровень, содержащий только названия групп и агрегированные значения: фрукты — 130 (50 + 80) и овощи — 130 (60 + 70).
- Конструкторы `DiscreteGroupItem`, основанные на именах и индексах, можно комбинировать в одном массиве `getDiscreteGroupItems()`.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей в сводной таблице](/cells/ru/java/group-pivot-fields-in-the-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/java/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/java/filter-by-label-or-value-of-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/java/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}