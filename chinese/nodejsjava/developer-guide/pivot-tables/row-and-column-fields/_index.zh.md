---
title: 在 Aspose.Cells for .NET 中添加数据透视表的行字段和列字段
linktitle: 行字段和列字段
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /zh/nodejs-java/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


行和列字段是数据透视表的构建块。放置在行区域的字段在数据透视表的左侧垂直显示,而放置在列区域的字段在顶部水平显示。本文演示如何以编程方式将基础字段添加到这些区域,以及如何使用 `PivotField.setSubtotals` 方法控制在字段组之间呈现的小计。

## **将字段添加到行或列区域**

`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` 方法将基础字段从源数据移动到四个数据透视区域之一。`fieldType` 参数接受以下 `PivotFieldType` 值之一。

- `ROW` — 在左侧垂直放置的字段
- `COLUMN` — 在顶部水平放置的字段
- `DATA` — 其值进行聚合的字段
- `PAGE` — 用作报表筛选器的字段

添加字段后,可以通过 `PivotTable.getRowFields()` 和 `PivotTable.getColumnFields()` 属性访问它们。每个属性返回一个 `PivotFieldCollection`。`RowFields` 中索引 0 处的字段是最外层的行字段,后续索引表示嵌套在其中的字段。相同的索引约定也适用于 `ColumnFields`。

字段嵌套顺序很重要。先将 `Category` 添加到行区域,然后添加 `Item`,生成的数据透视表的外部分组为 `Category`,内部分组为 `Item`。颠倒顺序则会颠倒层次结构。

## **数据透视字段小计**

`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` 方法控制为数据透视字段显示哪些小计行。每次调用独立切换单个小计类型。传递 `shown = true` 显示小计,而 `shown = false` 则隐藏它。由于每次调用仅影响一种类型,因此使用不同的 `subtotalType` 值多次调用该方法可以构建自定义小计子集。

`PivotFieldSubtotalType` 枚举定义了可用的小计类型。

- `AUTOMATIC` — Aspose.Cells 选择默认选项(通常对数值字段为 `SUM`)
- `NONE` — 抑制所有小计行
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
仅当行区域(或列区域)中有两个或更多数据透视字段时,小计才会呈现。单个字段之间没有有意义的内容可以小计,因此在这种情况下 `setSubtotals` 调用没有可见效果。因此,本文在每个示例中放置两个行字段(`Category` 外层,`Item` 内层),以便每个 `Category` 组之间的小计边界可见。
{{% /alert %}}

## **场景 1 — 自动(默认)小计**

当您完全不调用 `setSubtotals` 时,Aspose.Cells 会将 `AUTOMATIC` 选择应用于数值字段。以下示例通过对外部 `Category` 行字段调用 `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` 来明确确认此行为。

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

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **场景 2 — 抑制所有小计(无)**

调用 `setSubtotals(PivotFieldSubtotalType.NONE, true)` 会从数据透视表中删除所有小计行,仅保留字段行和底部的总计。当您希望获得原始分组数据而不包含任何汇总行时,这非常有用。

```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **场景 3 — 自定义小计子集(总和 + 平均值)**

您不仅限于单一小计类型。每次 `setSubtotals` 调用独立作用于一个类型,因此调用该方法两次(一次使用 `SUM`,一次使用 `AVERAGE`)会为每个 `Category` 组生成两个小计行的自定义子集。

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

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
## **回顾**

上述三个场景共享相同的数据集和数据透视表结构。它们之间唯一的区别是对外部 `Category` 行字段应用的 `setSubtotals` 调用。请记住两个字段的规则:区域中的单个字段之间没有内容可以小计,因此当您希望 `setSubtotals` 具有可见效果时,请始终在行或列区域中放置至少两个字段。

## **相关文章**

- [Page Fields in Pivot Tables](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Node.js via Java](/cells/zh/nodejs-java/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/zh/nodejs-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
