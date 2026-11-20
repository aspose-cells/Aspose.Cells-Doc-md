---
title: Дискретная группировка элементов полей сводной таблицы
linktitle: Дискретная группировка
description: Узнайте, как группировать элементы полей сводной таблицы в пользовательские группы с именами, например фрукты и овощи, с помощью классов DiscreteGroupItem и свойства PivotFieldGroupOptions.DiscreteGroupItems в Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, сводная таблица, дискретная группировка, DiscreteGroupItem, PivotFieldGroupOptions, группировать элементы сводной таблицы, пользовательские группы, PivotField.Group, Node.js, сводная таблица Excel
type: docs
weight: 90
url: /ru/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Автоматическая группировка собирает элементы по типу данных, например даты — в месяцы и кварталы, а числа — в диапазоны. Дискретная группировка решает обратную задачу, объединяя отдельные, несвязанные элементы в пользовательские группы с именами, например товары — в фрукты и овощи, магазины — в регионы, а счета — в зоны. Aspose.Cells for Node.js via C++ предоставляет дискретную группировку через класс `DiscreteGroupItem` и свойство `PivotFieldGroupOptions.discreteGroupItems`.
- `DiscreteGroupItem` представляет собой имя группы и элементы, принадлежащие ей. Элементы можно указывать двумя способами: по их именам (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) или по их нулевому индексу в исходных данных (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Оба варианта дают одинаковый результат.
- Дискретная группировка применяется к полю в области строк или столбцов сводной таблицы путём передачи опций в `pivotField.group(pivotFieldGroupOptions)`.

## **Группировка элементов поля сводной таблицы по именам**
В следующем примере создаётся небольшой список продаж (товар, дата и сумма), из него формируется сводная таблица с `product` в области строк, `date` в области столбцов и `amount` в области данных, затем определяются две пользовательские группы по именам элементов: фрукты (grape, cherry) и овощи (carrot, potato). Результат отображает двухуровневую структуру строк, где имя группы является внешним уровнем, а исходные элементы вложены под ним, что позволяет анализировать тенденции как по пользовательским группам, так и по отдельным элементам.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

После вызова `calculateData()` область строк сводной таблицы отображает фрукты (grape 50, cherry 80) и овощи (carrot 60, potato 70) с итоговой суммой 260, а подписи столбцов сохраняют четыре даты (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Группировка элементов поля сводной таблицы по индексам элементов**
Когда имена элементов длинные или локализованы, второй конструктор `DiscreteGroupItem` определяет элементы по индексу. Индексы — это нулевые позиции элементов в порядке их появления в исходных данных, а не в алфавитном порядке. В приведённом выше примере данные: grape — элемент 0, carrot — элемент 1, potato — элемент 2 и cherry — элемент 3, поэтому фрукты — `{ 0, 3 }`, а овощи — `{ 1, 2 }`. Результат идентичен примеру, основанному на именах.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Примечание**

{{% alert color="primary" %}}
- Элементы, не отнесённые к какой‑либо пользовательской группе, не исчезают. Они остаются в сводной таблице на том же уровне, что и пользовательские группы, каждый как отдельная одноэлементная запись. В приведённом выше примере, если определена только группа «fruit», то carrot и potato остаются в области строк как отдельные записи рядом с группой фруктов.
- Свойство `PivotFieldGroupOptions.newPivotField` управляет макетом дискретной группировки. По умолчанию оно равно **true**, что добавляет сгруппированное поле как новое внешнее поле рядом с исходным, создавая двухуровневый макет, показанный выше (`rowFields` увеличивается до 2). Установив его в **false**, можно заменить исходное поле, и область строк будет отображать один уровень, содержащий только имена групп с их агрегированными значениями: fruit 130 (50 + 80) и vegetable 130 (60 + 70).
- Конструкторы `DiscreteGroupItem`, основанные на именах и на индексах, могут сочетаться в одном массиве `PivotFieldGroupOptions.discreteGroupItems`.
{{% /alert %}}

## **Related Articles**
- [Группировка полей сводной таблицы](/cells/ru/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}