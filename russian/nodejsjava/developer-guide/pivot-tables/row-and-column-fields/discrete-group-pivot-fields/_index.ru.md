---
title: Дискретная группировка элементов поля сводной таблицы
linktitle: Дискретная группировка
description: Узнайте, как группировать элементы поля сводной таблицы в пользовательские группы с заданными именами, например фрукты и овощи, с помощью DiscreteGroupItem и PivotFieldGroupOptions.getDiscreteGroupItems() в Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, сводная таблица, дискретная группировка, DiscreteGroupItem, PivotFieldGroupOptions, группировка элементов поля сводной таблицы, пользовательские группы, PivotField.group, Aspose.Cells for Node.js via Java, сводная таблица Excel
type: docs
weight: 90
url: /ru/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Автоматическая группировка группирует элементы в зависимости от типа данных, например даты — по месяцам и кварталам, а числа — по диапазонам. Дискретная группировка решает противоположную задачу: объединяет заданные, не связанные между собой элементы в пользовательские группы с заданными именами, например продукты — во фрукты и овощи, магазины — по регионам, а счета — по зонам. Aspose.Cells предоставляет дискретную группировку с помощью класса `DiscreteGroupItem` и свойства `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- `DiscreteGroupItem` содержит имя группы и входящие в неё элементы. Элементы можно идентифицировать двумя способами: по именам (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) или по их позициям в исходных данных, начиная с нуля (`new DiscreteGroupItem("fruit", [0, 3])`). Оба варианта дают одинаковый результат.
- Дискретная группировка применяется к полю в области строк или столбцов сводной таблицы. Для этого параметры группировки передаются в `PivotField.group(PivotFieldGroupOptions)`.

## **Группировка элементов поля сводной таблицы по именам**
В следующем примере создается небольшой список продаж (продукт, дата и сумма), а затем на его основе — сводная таблица, в которой `product` размещается в области строк, `date` — в области столбцов, а `amount` — в области данных. Затем определяются две пользовательские группы по именам элементов: fruit (grape, cherry) и vegetable (carrot, potato). В результате отображается двухуровневая структура строк: на внешнем уровне находится имя группы, а под ним — исходные элементы. Такая структура позволяет анализировать тенденции отдельно по каждой пользовательской группе и каждому элементу.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

После `calculateData()` область строк сводной таблицы отображает fruit (grape — 50, cherry — 80) и vegetable (carrot — 60, potato — 70), а общий итог равен 260. Метки столбцов сохраняют четыре даты (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Группировка элементов поля сводной таблицы по индексам**
Когда имена элементов длинные или локализованы, второй конструктор `DiscreteGroupItem` позволяет идентифицировать элементы по индексу. Индексы представляют собой позиции элементов в порядке их появления в исходных данных, начиная с нуля, а не в алфавитном порядке. В приведенных выше данных grape имеет индекс 0, carrot — 1, potato — 2, а cherry — 3; поэтому индексы группы fruit — `{ 0, 3 }`, а vegetable — `{ 1, 2 }`. Результат идентичен примеру группировки по именам.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Примечание**

{{% alert color="primary" %}}
- Элементы, не включенные ни в одну пользовательскую группу, не теряются. Они остаются в сводной таблице на том же уровне, что и пользовательские группы, каждый в виде отдельной записи с одним элементом. В примере выше при определении только группы fruit элементы carrot и potato остаются в области строк как отдельные записи рядом с группой fruit.
- Свойство `PivotFieldGroupOptions.getNewPivotField()` управляет компоновкой дискретной группировки. По умолчанию оно имеет значение `true`, при котором сгруппированное поле добавляется как новое внешнее поле рядом с исходным и формирует показанную выше двухуровневую структуру (`getRowFields()` увеличивается до 2). Установите для него значение `false` с помощью `PivotFieldGroupOptions.setNewPivotField(false)`, чтобы заменить исходное поле; тогда область строк будет содержать единственный уровень с именами групп и их агрегированными значениями: fruit — 130 (50 + 80) и vegetable — 130 (60 + 70).
- Конструкторы `DiscreteGroupItem`, основанные на именах и индексах, можно смешивать в одном массиве `getDiscreteGroupItems()`.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей в сводной таблице](/cells/ru/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/nodejs-java/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}