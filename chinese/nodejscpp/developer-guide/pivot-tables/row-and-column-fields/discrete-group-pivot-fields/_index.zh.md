---
title: 数据透视表字段项的离散分组
linktitle: 离散分组
description: 了解如何使用 Aspose.Cells for Node.js via C++ 中的 DiscreteGroupItem 和 PivotFieldGroupOptions.DiscreteGroupItems 将数据透视表字段项分组到自定义命名组（例如水果和蔬菜）。
keywords: Aspose.Cells, 数据透视表, 离散分组, DiscreteGroupItem, PivotFieldGroupOptions, 分组数据透视表项, 自定义分组, PivotField.Group, Node.js, Excel 数据透视表
type: docs
weight: 90
url: /zh/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 自动分组根据数据类型收集项，例如将日期划分为月份和季度，或将数字划分为范围。离散分组解决相反的问题，将特定的、无关联的项收集到自定义命名组中，例如将产品划分为水果和蔬菜，将商店划分为地区，或将账户划分为区域。Aspose.Cells for Node.js via C++ 通过 `DiscreteGroupItem` 类和 `PivotFieldGroupOptions.discreteGroupItems` 属性提供离散分组。
- `DiscreteGroupItem` 是一个组名以及属于该组的项。可以通过两种方式标识这些项：按名称（`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`）或按在源数据中的零基位置（`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`）。两种形式产生相同的结果。
- 离散分组通过将选项传递给 `pivotField.group(pivotFieldGroupOptions)`，应用于数据透视表行区或列区的字段。

## **按项名称分组数据透视表字段项**
以下示例构建一个小的销售列表（产品、日期和金额），并基于该列表创建数据透视表，其中 `product` 位于行区，`date` 位于列区，`amount` 位于数据区，然后通过项名称定义两个自定义组：水果（grape、cherry）和蔬菜（carrot、potato）。结果显示两级行布局，外层为组名，内部嵌套原始项，从而可以按自定义组和单个项读取趋势。

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

在调用 `calculateData()` 后，数据透视表的行区显示水果（grape 50、cherry 80）和蔬菜（carrot 60、potato 70），总计为 260，列标签保留四个日期（2/5/2021、3/8/2022、4/10/2023、5/16/2024）。

## **按项索引分组数据透视表字段项**
当项名称较长或已本地化时，`DiscreteGroupItem` 的第二个构造函数通过索引来标识项。索引是项在源数据中出现顺序的零基位置，而非字母顺序。在上面的示例数据中，grape 为项 0，carrot 为项 1，potato 为项 2，cherry 为项 3，因此水果为 `{ 0, 3 }`，蔬菜为 `{ 1, 2 }`。结果与基于名称的示例相同。

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

## **注意**

{{% alert color="primary" %}}
- 未分配到任何自定义组的项不会丢失。它们保持在数据透视表中，与自定义组处于同一级别，各自作为单项条目存在。在上面的示例中，仅定义水果组时，carrot 和 potato 会作为独立条目出现在行区，位于水果组旁边。
- `PivotFieldGroupOptions.newPivotField` 属性控制离散分组的布局。默认值为 true，表示将分组字段作为新的外层字段添加在原字段旁边，形成上述的两级布局（`rowFields` 增长到 2）。将其设为 false 则替换原字段，行区仅显示单层，仅包含组名及其聚合值，水果 130（50 + 80）和蔬菜 130（60 + 70）。
- `DiscreteGroupItem` 的基于名称和基于索引的构造函数可以在同一个 `PivotFieldGroupOptions.discreteGroupItems` 数组中混合使用。
{{% /alert %}}

## **相关文章**
- [在数据透视表中分组字段](/cells/zh/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [在数据透视表中添加行和列字段](/cells/zh/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [按标签或数值过滤数据透视表](/cells/zh/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [为数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}