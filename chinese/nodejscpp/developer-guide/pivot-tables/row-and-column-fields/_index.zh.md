---
title: 在 Aspose.Cells for Node.js via C++ 中添加数据透视表行字段和列字段
linktitle: 在 Aspose.Cells for Node.js via C++ 中添加数据透视表行字段和列字段
description: 了解如何使用 PivotField.SetSubtotals 在 Aspose.Cells for Node.js via C++ 中将基础字段添加到数据透视表的行区域和列区域，并控制数据透视字段的小计。
keywords: Aspose.Cells, Node.js, C++, 数据透视表, 行字段, 列字段, PivotField, SetSubtotals, PivotFieldSubtotalType, 小计
type: docs
weight: 220
url: /zh/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **将字段添加到行区域或列区域**
`PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` 方法将基础字段从源数据移动到数据透视表的四个区域之一。`fieldType` 参数接受以下 `PivotFieldType` 值之一。
- `Row` — 垂直放置在左侧的字段
- `Column` — 水平放置在顶部的字段
- `Data` — 对其值进行聚合的字段
- `Page` — 用作报表筛选字段
字段的嵌套顺序很重要。先将 `Category` 添加到行区域，然后再添加 `Item`，会生成外层分组为 `Category`、内层分组为 `Item` 的数据透视表。按相反顺序添加会颠倒层级结构。

## **数据透视字段小计**
`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` 方法控制数据透视字段显示哪些小计行。每次调用都会独立切换一种小计类型。传入 `shown = true` 将显示小计，而 `shown = false` 将隐藏小计。由于每次调用仅影响一种类型，因此使用不同的 `subtotalType` 值多次调用该方法，可以构建自定义的小计子集。
`PivotFieldSubtotalType` 枚举定义了可用的小计类型。
- `Automatic` — 由 Aspose.Cells 选择默认选项（数值字段通常为 `Sum`）
- `None` — 取消所有小计行
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
仅当行区域（或列区域）中有两个或更多数据透视字段时，才会显示小计。对于单个字段，不存在可供计算小计的层级，因此 `setSubtotals` 调用在这种情况下不会产生可见效果。因此，本文中的每个示例都包含两个行字段（外层为 `Category`，内层为 `Item`），以便清楚显示各 `Category` 组的小计边界。
{{% /alert %}}

## **场景 1 — `Automatic`（默认）小计**
如果完全不调用 `setSubtotals`，Aspose.Cells 会将 `Automatic` 选项应用于数值字段。以下示例在外层 `Category` 行字段上调用 `setSubtotals(PivotFieldSubtotalType.Automatic, true)`，以明确验证这一行为。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **场景 2 — 禁止所有小计（`None`）**
调用 `setSubtotals(PivotFieldSubtotalType.None, true)` 会从数据透视表中移除所有小计行，仅保留字段行以及底部的总计。此功能适用于需要查看不含汇总行的原始分组数据的场景。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **场景 3 — 自定义小计子集（`Sum` + `Average`）**
您并非只能使用一种小计类型。每次 `setSubtotals` 调用都会独立作用于一种类型，因此调用该方法两次——一次使用 `Sum`，另一次使用 `Average`——会为每个 `Category` 组生成包含两行小计的自定义子集。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
let pivotTables = worksheet.getPivotTables();
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **总结**

这三种场景仅有一处不同：setSubtotals 调用。其余所有内容——数据集、字段及其所属区域——完全相同，因此这些布局可以直接比较。
- **放置字段。** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` 将源列移入某个区域。在同一区域内，调用顺序就是显示顺序，因此第一次调用会成为最外层组。子汇总需要同一区域内有两个或更多字段：如果只有一个字段，组与组之间就没有可汇总的内容。
- **方案 1 — 自动子汇总。** 不调用 setSubtotals 会将选择权交给 Excel，由 Excel 对数值字段应用其默认子汇总。使用 `AsposeCells.PivotFieldSubtotalType.Automatic` 调用 setSubtotals 会明确记录该选择，而不是让其保持隐式状态。
- **方案 2 — 无子汇总。** 使用 `AsposeCells.PivotFieldSubtotalType.None` 调用 setSubtotals 会关闭默认子汇总，因此数据透视表会保留字段行和总计，但会移除 Excel 否则会插入这些行之间的子汇总行。
- **方案 3 — 选择指定子集。** 每次调用恰好切换一种子汇总类型，多次调用会累加设置，而不会相互重置。因此，分别使用 `AsposeCells.PivotFieldSubtotalType.Sum` 和 `AsposeCells.PivotFieldSubtotalType.Average` 调用一次后，两种子汇总都会保持启用，数据透视表将呈现 Sum 子汇总、Average 子汇总以及总计。

{{% alert color="primary" %}}
子汇总的任何行为都不是行区域所特有的。对取自 `PivotTable.ColumnFields` 的字段执行相同的 setSubtotals 调用，也会在列轴上生成相同的三种布局，因为该设置属于数据透视字段，而不是字段所在的轴。
{{% /alert %}}
## **相关文章**
- [数据透视表中的页字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Node.js via C++ 中刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}