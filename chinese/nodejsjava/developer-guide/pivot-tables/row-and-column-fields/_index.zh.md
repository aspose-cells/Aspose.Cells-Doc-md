---
title: 通过 Java 在 Aspose.Cells for Node.js 中将行和列字段添加到数据透视表
linktitle: 通过 Java 在 Aspose.Cells for Node.js 中将行和列字段添加到数据透视表
description: 了解如何使用 PivotField.setSubtotals 在 Aspose.Cells for Node.js via Java 中将基字段添加到数据透视表的行区域和列区域，并控制数据透视字段的小计
keywords: Aspose.Cells, Node.js, Java, 数据透视表, 行字段, 列字段, PivotField, setSubtotals, PivotFieldSubtotalType, 小计
type: docs
weight: 220
url: /zh/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **向行区域或列区域添加字段**
`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` 方法将基字段从源数据移动到四个数据透视区域之一。`fieldType` 参数接受以下 `PivotFieldType` 值之一。
- `ROW` — 垂直放置在左侧的字段
- `COLUMN` — 水平放置在顶部的字段
- `DATA` — 对值进行聚合的字段
- `PAGE` — 用作报表筛选器的字段
字段的嵌套顺序很重要。先将 `Category` 添加到行区域，再将 `Item` 添加到行区域，会生成一个外层分组为 `Category`、内层分组为 `Item` 的数据透视表。反转顺序会反转层次结构。

## **数据透视字段小计**
`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` 方法控制数据透视字段显示哪些小计行。每次调用都会独立切换一种小计类型。传入 `shown = true` 会显示小计，而 `shown = false` 则会隐藏小计。由于每次调用仅影响一种类型，因此使用不同的 `subtotalType` 值多次调用该方法，可以构建自定义的小计子集。
`PivotFieldSubtotalType` 枚举定义了可用的小计类型。
- `AUTOMATIC` — Aspose.Cells 选择默认选项（数值字段通常为 `SUM`）
- `NONE` — 禁止所有小计行
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
仅当行区域（或列区域）中存在两个或更多数据透视字段时，才会呈现小计。单个字段没有可在其间进行小计计算的内容，因此此时调用 `setSubtotals` 不会产生可见效果。因此，本文中的每个示例都在行区域中放置两个行字段（外层为 `Category`，内层为 `Item`），以便显示各 `Category` 组之间的小计边界。
{{% /alert %}}

## **场景 1 — 自动（默认）小计**
如果完全不调用 `setSubtotals`，Aspose.Cells 会将 `AUTOMATIC` 选项应用于数值字段。以下示例通过在外层 `Category` 行字段上调用 `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)`，显式确认此行为。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **场景 2 — 禁止所有小计（无）**
调用 `setSubtotals(PivotFieldSubtotalType.NONE, true)` 会从数据透视表中移除所有小计行，仅保留字段行和底部的总计。当您希望获取原始分组数据且不包含任何汇总行时，此方法非常有用。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **场景 3 — 自定义小计子集（求和 + 平均值）**
您不必局限于单个小计类型。每次 `setSubtotals` 调用都会独立作用于一种类型，因此调用该方法两次——一次使用 `SUM`，一次使用 `AVERAGE`——即可为每个 `Category` 组生成由两行小计组成的自定义子集。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **回顾**

这三种场景仅在 `setSubtotals` 调用上存在差异；其余部分——数据集、字段及其分配区域——均相同，这也使得各布局之间具有直接可比性。
- **字段放置。** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` 将源列移入某一区域。在同一个区域内，调用的顺序即为显示顺序，因此首次调用对应最外层分组。子总计功能要求同一区域内至少包含两个字段：单个字段情况下，组与组之间无任何数据可供计算子总计。
- **场景一——自动子总计。** 若不调用 `setSubtotals`，则将选择权交由 Excel 自行决定，Excel 会对数值型字段应用其默认的子总计方式；而调用 `setSubtotals` 并传入 `AsposeCells.PivotFieldSubtotalType.AUTOMATIC`，则显式记录了该选择，而非依赖隐式默认行为。
- **场景二——无子总计。** 调用 `setSubtotals` 并传入 `AsposeCells.PivotFieldSubtotalType.NONE` 会禁用默认子总计，这样数据透视表会保留字段行和总计行，但不再插入 Excel 默认会在其间插入的子总计行。
- **场景三——指定子总计集合。** 每次调用仅切换一种子总计类型，且多次调用会累积效果而非相互覆盖。例如，先以 `AsposeCells.PivotFieldSubtotalType.SUM` 调用一次，再以 `AsposeCells.PivotFieldSubtotalType.AVERAGE` 调用一次，则二者将同时生效，数据透视表将渲染“求和”子总计、“平均值”子总计及总计行。

{{% alert color="primary" %}}
子总计设置并非仅限于行区域。对从 `PivotTable.ColumnFields` 获取的字段执行相同的 `setSubtotals` 调用，可在列轴上生成相同的三种布局，因为该设置属于数据透视字段本身，而非其所在的轴。
{{% /alert %}}
## **相关文章**
- [数据透视表中的页面字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)
- [使用 Aspose.Cells for Node.js via Java 刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}