---
title: Дискретная группировка элементов поля сводной таблицы
linktitle: Дискретная группировка
description: Узнайте, как группировать элементы поля сводной таблицы в пользовательские группы с заданными именами, например «фрукты» и «овощи», с помощью DiscreteGroupItem и PivotFieldGroupOptions.DiscreteGroupItems в Aspose.Cells for .NET.
keywords: Aspose.Cells, сводная таблица, дискретная группировка, DiscreteGroupItem, PivotFieldGroupOptions, группировка элементов сводной таблицы, пользовательские группы, PivotField.Group, C#, сводная таблица Excel
type: docs
weight: 90
url: /ru/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Автоматическая группировка объединяет элементы по типу данных: например, даты — по месяцам и кварталам, а числа — по диапазонам. Дискретная группировка решает обратную задачу: объединяет конкретные несвязанные элементы в пользовательские группы с заданными именами, например продукты в группы «фрукты» и «овощи», магазины — по регионам, а счета — по зонам. Aspose.Cells обеспечивает дискретную группировку с помощью класса `DiscreteGroupItem` и свойства `PivotFieldGroupOptions.DiscreteGroupItems`.
- `DiscreteGroupItem` представляет собой имя группы и входящие в нее элементы. Элементы можно идентифицировать двумя способами: по именам (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) или по индексам (нумерация с нуля) в исходных данных (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Обе формы дают одинаковый результат.
- Дискретная группировка применяется к полю в области строк или столбцов сводной таблицы путем передачи объекта параметров в метод `PivotField.Group(PivotFieldGroupOptions)`.

## **Группировка элементов поля сводной таблицы по именам элементов**
В следующем примере создается небольшой список продаж (продукт, дата и сумма) и на его основе формируется сводная таблица, в которой `product` размещается в области строк, `date` — в области столбцов, а `amount` — в области данных. Затем по именам элементов создаются две пользовательские группы: «фрукты» (виноград, вишня) и «овощи» (морковь, картофель). В результате формируется двухуровневая структура строк: имя группы занимает внешний уровень, а исходные элементы располагаются под соответствующей группой. Это позволяет анализировать тенденции отдельно по каждой пользовательской группе и каждому элементу.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

После `CalculateData()` в области строк сводной таблицы отображаются фрукты (виноград 50, вишня 80) и овощи (морковь 60, картофель 70), а общий итог равен 260; в подписях столбцов по-прежнему отображаются четыре даты (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Группировка элементов поля сводной таблицы по индексам элементов**
Если имена элементов являются длинными или локализованными, второй конструктор `DiscreteGroupItem` позволяет идентифицировать элементы по индексу. Индексы соответствуют позициям элементов в исходных данных (нумерация с нуля) в порядке их появления, а не в алфавитном порядке. В приведенных выше данных виноград имеет индекс 0, морковь — индекс 1, картофель — индекс 2, а вишня — индекс 3, поэтому элементы группы «фрукты» имеют индексы `{ 0, 3 }`, а элементы группы «овощи» — `{ 1, 2 }`. Результат совпадает с результатом примера с группировкой по именам.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Примечание**

{{% alert color="primary" %}}
- Элементы, не включенные ни в одну пользовательскую группу, не теряются. Они остаются в сводной таблице на том же уровне, что и пользовательские группы, каждый в виде отдельной записи, состоящей из одного элемента. В приведенном выше примере, если определить только группу «фрукты», морковь и картофель останутся в области строк как отдельные записи рядом с группой «фрукты».
- Свойство `PivotFieldGroupOptions.NewPivotField` управляет компоновкой дискретной группировки. По умолчанию его значение равно true. В этом случае сгруппированное поле добавляется как новое внешнее поле рядом с исходным, что формирует двухуровневую структуру, показанную выше (`RowFields` увеличивается до 2). Установите для него значение false, чтобы вместо этого заменить исходное поле. Тогда область строк будет содержать только один уровень с именами групп и их агрегированными значениями: фрукты — 130 (50 + 80) и овощи — 130 (60 + 70).
- Конструкторы `DiscreteGroupItem`, предназначенные для указания элементов по именам и индексам, можно комбинировать в одном массиве `DiscreteGroupItems`.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей сводной таблицы](/cells/ru/net/group-pivot-fields-in-the-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/net/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/net/filter-by-label-or-value-of-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/net/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}