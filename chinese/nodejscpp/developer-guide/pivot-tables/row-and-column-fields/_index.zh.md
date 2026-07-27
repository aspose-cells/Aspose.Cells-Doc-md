---
title: 在 Aspose.Cells for .NET 中添加数据透视表的行字段和列字段
linktitle: 行字段和列字段
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /zh/nodejs-cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **向行或列区域添加字段**

`PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` 方法将一个基础字段从源数据移动到四个透视区域之一。`fieldType` 参数接受以下 `PivotFieldType` 值之一。

- `Row` — 垂直放置在左侧的字段
- `Column` — 水平放置在顶部的字段
- `Data` — 其值被聚合的字段
- `Page` — 用作报表筛选器的字段

添加字段后，您可以通过 `PivotTable.RowFields` 和 `PivotTable.ColumnFields` 属性访问它们。每个属性返回一个 `PivotFieldCollection`。`RowFields` 索引 0 处的字段是最外层的行字段，后续索引表示嵌套在其内部的字段。相同的索引约定也适用于 `ColumnFields`。

字段的嵌套顺序很重要。先向行区域添加 `Category`，然后再添加 `Item`，会产生一个外部分组为 `Category`、内部分组为 `Item` 的透视表。反转该顺序则会反转层级结构。

## **透视字段小计**

`PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` 方法控制透视字段显示哪些小计行。每次调用都会独立切换一种小计类型。传递 `shown = true` 将显示小计，而传递 `shown = false` 则会隐藏它。由于每次调用只影响一种类型，因此使用不同的 `subtotalType` 值多次调用该方法可以构建自定义的小计子集。

`PivotFieldSubtotalType` 枚举定义了可用的小计种类。

- `Automatic` — Aspose.Cells 选择默认选项（通常对数值字段为 `Sum`）
- `None` — 抑制所有小计行
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
小计仅在行区域（或列区域）中存在两个或更多透视字段时才会呈现。单个字段之间没有可供小计的有意义内容，因此在这种情况下 `SetSubtotals` 调用没有可见效果。因此本文在每个示例中都放置两个行字段（外层 `Category`，内层 `Item`），以便每个 `Category` 组之间的小计边界可见。
{{% /alert %}}

## **场景 1 — 自动（默认）小计**

当您根本不调用 `SetSubtotals` 时，Aspose.Cells 会将 `Automatic` 选择应用于数值字段。以下示例通过对外部 `Category` 行字段调用 `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` 来显式确认此行为。

```javascript
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

## **场景 2 — 抑制所有小计 (None)**

调用 `SetSubtotals(PivotFieldSubtotalType.None, true)` 会从透视表中移除所有小计行，仅保留字段行和底部总计。当您希望查看不带任何汇总行的原始分组数据时，这非常有用。

```javascript
const AsposeCells = require("aspose.cells");

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

## **场景 3 — 自定义小计子集 (Sum + Average)**

您不仅限于单一的小计类型。每次 `SetSubtotals` 调用都独立作用于一种类型，因此使用 `Sum` 和 `Average` 各调用一次该方法，可以为每个 `Category` 组生成两个小计行的自定义子集。

```javascript
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
## **总结**

上述三个场景共享相同的数据集和透视表结构。它们之间唯一的区别是应用于外部 `Category` 行字段的 `SetSubtotals` 调用。请记住两个字段的规则：区域中只有一个字段时没有内容可供小计，因此当您希望 `SetSubtotals` 产生可见效果时，请始终在行或列区域中放置至少两个字段。

## **相关文章**

- [透视表中的页面字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Node.js via C++ 中刷新透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)
- [对透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
