---
title: 在 Aspose.Cells for .NET 中管理数据透视表的值字段
linktitle: 值字段
description: 了解如何在 Aspose.Cells for Node.js via Java 中将基本字段添加到数据透视表的数据区域，使用 PivotField.Function 更改汇总函数，以及将值字段绘制到行或列轴。
keywords: Aspose.Cells, Node.js via Java, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, 求和, 平均值
type: docs
weight: 230
url: /zh/nodejs-java/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

值字段是每个数据透视表的核心，用于汇总源数据的数值聚合。在 Aspose.Cells for Node.js via Java 中，通过 `PivotTable.addFieldToArea` 向数据透视表的数据区域添加基本字段来填充该区域，并且放置在该区域中的每个字段都可以拥有自己的汇总函数。当存在两个或更多数据字段时，Aspose.Cells 公开了一个特殊的聚合字段 `PivotTable.getValuesField()`，该字段可以作为基本字段绘制到行或列轴上，从而让您更精细地控制值字段在布局中的显示方式。

## 将字段添加到数据区域

将基本字段添加到数据（值）区域是塑造数据透视表如何聚合源数据的第一步。Aspose.Cells 公开了 `PivotTable.addFieldToArea(PivotFieldType, string)` 重载方法，该方法接受常量 `PivotFieldType.DATA` 和源列名称。一旦字段被添加到数据区域，API 会通过 `PivotTable.getDataFields()` 集合按字段添加的顺序将其公开。默认情况下，数值类型的源列使用 `ConsolidationFunction.SUM` 进行汇总，而非数值列则默认为 `COUNT`。

## 更改汇总函数

放置在数据区域中的每个字段在内部都被包装为 `PivotField` 实例，其 `getFunction()` 属性返回 `ConsolidationFunction` 枚举中的某个值。同一个 `setFunction()` 设置器允许您在可用的聚合函数之间切换，包括 `SUM`、`COUNT`、`AVERAGE`、`MAX`、`MIN`、`PRODUCT`、`STD_DEV`、`STD_DEVP`、`VAR` 和 `VARP`。

{{% alert color="primary" %}}
更改 `Function` 仅影响聚合方式，源列不会改变。
{{% /alert %}}

因此，您可以在单个数据透视表中保留一个数据字段使用 `SUM`，同时添加第二个针对同一源列但使用 `COUNT` 或 `AVERAGE` 的数据字段。

## 将值字段绘制到行或列轴

当数据透视表包含两个或更多数据字段时，Aspose.Cells 会公开一个额外的虚拟字段，称为 `PivotTable.getValuesField()`。此虚拟字段代表数据区域中每个数据字段的聚合。您可以将其作为基本数据透视字段拖到行或列区域，这对于并排布置多个度量值非常有用。

{{% alert color="primary" %}}
如果没有值字段或只有一个值字段，`PivotTable.getValuesField()` 无法使用。
{{% /alert %}}

下面的场景将逐步介绍三个端到端示例，针对同一数据透视结构演示上文所述的每项功能。

## 场景 1 — 将基本字段拖入值区域

此场景展示如何将单个基本字段（`Amount`）放入现有数据透视表的数据区域。共享的数据透视结构将 `Category` 和 `Item` 放在行轴上，将 `Year` 放在列轴上。操作完成后，`Amount` 将出现在数据区域中，并默认按 `Amount` 的 `Sum` 进行计算。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 中的表头
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// 使用嵌套循环在 A2:D9 写入数据，根据 j 分支处理
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// 在 F3 位置添加名为 PivotTable1 的数据透视表
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 透视表布局：Category 和 Item 作为行，Year 作为列，Amount 作为数据字段
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## 场景 2 — 更改汇总函数

此场景从与场景 1 相同的数据透视结构开始，但将 `Amount` 字段添加到数据区域两次。两个数据字段引用同一源列，但是使用 `PivotField.setFunction()` 设置器覆盖第二个字段，使其变为 `COUNT` 而不是默认的 `SUM`。

<!-- CODE_BLOCK:1:Build a complete end-to-end sample that imports the Aspose.Cells namespace, then creates a new Workbook instance, gets worksheets.get(0), assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual cells.get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount") twice so that pivotTable.getDataFields() contains two fields. Retrieve the second data field via pivotTable.getDataFields().get(1) and assign countField.setFunction(ConsolidationFunction.COUNT) to change its summary function from the default SUM to COUNT; the first data field remains Sum of Amount. Demonstrate that the setFunction setter can also be assigned ConsolidationFunction.AVERAGE, MAX, MIN, etc. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_function.xlsx"). -->

## 场景 3 — 将值字段绘制到行或列轴

当存在两个数据字段时，`PivotTable.getValuesField()` 便可使用。此场景将该聚合虚拟字段拖到列区域，以便数据区域中的每个度量值都以独立的列块形式出现在 `Year` 旁边。

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that imports the Aspose.Cells namespace, then creates a new Workbook instance, gets worksheets.get(0), assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual cells.get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT) so the second data field becomes COUNT while the first remains SUM. Finally call pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

综上所述，这三个场景涵盖了 Aspose.Cells for Node.js via Java 中值字段操作的方方面面，从使用默认 `SUM` 的单个数据字段，到由虚拟 `ValuesField` 控制行或列轴布局的多度量值数据透视表。

## 相关文章

- [Aspose.Cells for Node.js via Java 中的数据透视表行和列字段](/cells/zh/nodejs-java/row-and-column-fields/)
- [数据透视表中的页面字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Node.js via Java 中刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/)
- [向数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}