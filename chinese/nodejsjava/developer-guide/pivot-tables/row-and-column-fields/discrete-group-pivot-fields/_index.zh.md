---
title: 数据透视字段项的离散分组
linktitle: 离散分组
description: 了解如何使用 DiscreteGroupItem 和 PivotFieldGroupOptions.getDiscreteGroupItems()，在 Aspose.Cells for Node.js via Java 中将数据透视字段项归入自定义命名组，例如水果组和蔬菜组。
keywords: Aspose.Cells, 数据透视表, 离散分组, DiscreteGroupItem, PivotFieldGroupOptions, 对数据透视字段项进行分组, 自定义组, PivotField.group, Aspose.Cells for Node.js via Java, Excel 数据透视表
type: docs
weight: 90
url: /zh/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的应用场景**
- 自动分组按数据类型对项进行归类，例如将日期归入月份和季度，或将数字归入数值范围。离散分组解决的是相反的问题：将特定的、互不相关的项归入自定义命名组，例如将产品归入水果组和蔬菜组、将商店归入区域组或将账户归入分区组。Aspose.Cells 通过 `DiscreteGroupItem` 类和 `PivotFieldGroupOptions.getDiscreteGroupItems()` 属性提供离散分组功能。
- `DiscreteGroupItem` 表示一个组名称以及归属于该组的项。项可以通过两种方式标识：按名称标识（`new DiscreteGroupItem("fruit", ["grape", "cherry"])`），或按其在源数据中从零开始的位置标识（`new DiscreteGroupItem("fruit", [0, 3])`）。两种形式产生的结果相同。
- 若要对数据透视表行区域或列区域中的字段应用离散分组，请将选项传递给 `PivotField.group(PivotFieldGroupOptions)`。

## **按项名称对数据透视字段项进行分组**
以下示例创建一个小型销售列表（产品、日期和金额），并据此创建数据透视表，其中 `product` 位于行区域，`date` 位于列区域，`amount` 位于数据区域。随后按项名称定义两个自定义组：水果组（葡萄、樱桃）和蔬菜组（胡萝卜、土豆）。结果呈现两级行布局：组名称位于外层级别，原始项嵌套在其下，从而可按自定义组和项分别分析趋势。

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

调用 `calculateData()` 后，数据透视表的行区域显示 `fruit`（`grape` 50、`cherry` 80）和 `vegetable`（`carrot` 60、`potato` 70），总计为 260；列标签仍保留四个日期（2/5/2021、3/8/2022、4/10/2023、5/16/2024）。

## **按项索引对数据透视字段项进行分组**
当项名称较长或经过本地化时，可使用 `DiscreteGroupItem` 的第二个构造函数，通过索引标识项。索引是项在源数据中按出现顺序排列的、从零开始的位置，而不是按字母顺序排列的位置。在上述示例数据中，`grape` 是项 0，`carrot` 是项 1，`potato` 是项 2，`cherry` 是项 3，因此 `fruit` 为 `{ 0, 3 }`，`vegetable` 为 `{ 1, 2 }`。结果与基于名称的示例完全相同。

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

## **注意**

{{% alert color="primary" %}}
- 未分配给任何自定义组的项不会丢失。这些项仍保留在数据透视表中，与自定义组处于同一层级，每项均作为独立的单项条目存在。在上述示例中，仅定义 `fruit` 组时，`carrot` 和 `potato` 仍作为独立条目保留在行区域中，与 `fruit` 组并列。
- `PivotFieldGroupOptions.getNewPivotField()` 属性控制离散分组的布局。其默认值为 true，该设置会在原始字段旁将分组字段添加为新的外层字段，从而生成上述两级布局（`getRowFields()` 增至 2）。调用 `PivotFieldGroupOptions.setNewPivotField(false)` 将其设置为 false，以替换原始字段；此时行区域仅显示一个层级，其中只包含组名称及其汇总值，即 `fruit` 130（50 + 80）和 `vegetable` 130（60 + 70）。
- `DiscreteGroupItem` 基于名称的构造函数和基于索引的构造函数可以在同一个 `getDiscreteGroupItems()` 数组中混用。
{{% /alert %}}

## **相关文章**
- [在数据透视表中对数据透视字段进行分组](/cells/zh/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [在数据透视表中添加行和列字段](/cells/zh/nodejs-java/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [为数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}