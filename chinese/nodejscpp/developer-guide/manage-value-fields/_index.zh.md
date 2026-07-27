---
title: Aspose.Cells for Node.js via C++ 中的值字段
linktitle: Aspose.Cells for Node.js via C++ 中的值字段
description: 了解如何在 Aspose.Cells for Node.js via C++ 中将基础字段添加到数据透视表的数据区域，使用 PivotField.Function 更改汇总函数，以及将值字段绘制到行或列轴上。
keywords: Aspose.Cells, Node.js, C++, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /zh/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

值字段是每个数据透视表的核心，是对源数据进行数值汇总的聚合字段。在 Aspose.Cells for Node.js via C++ 中，通过 `PivotTable.addFieldToArea` 将基础字段添加到数据区域来填充数据透视表的数据区域，添加到该区域的每个字段都可以拥有自己的汇总函数。当存在两个或更多数据字段时，Aspose.Cells 会公开一个特殊的聚合字段 `PivotTable.ValuesField`，它可以作为基础字段绘制到行或列轴上，从而让您更精细地控制值字段在布局中的显示方式。

## 将字段添加到数据区域

将基础字段添加到数据（值）区域是塑造数据透视表如何聚合源数据的第一步。Aspose.Cells 公开了 `PivotTable.addFieldToArea(PivotFieldType, string)` 重载方法，该方法接受常量 `PivotFieldType.Data` 和源列名称。一旦字段被添加到数据区域，API 会通过 `PivotTable.DataFields` 集合按字段添加的顺序将其公开。默认情况下，数值型源列使用 `ConsolidationFunction.Sum` 进行汇总，而非数值列默认为 `Count`。

## 更改汇总函数

放置在数据区域中的每个字段在内部都被包装为 `PivotField` 实例，其 `Function` 属性返回 `ConsolidationFunction` 枚举中的一个值。同一个 `Function` setter 允许您在可用的聚合函数之间切换，包括 `Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var` 和 `Varp`。

{{% alert color="primary" %}}
更改 `Function` 仅影响聚合结果，源列不会发生变化。
{{% /alert %}}

因此，您可以在单个数据透视表中保留一个数据字段为 `Sum`，同时添加另一个针对同一源列但使用 `Count` 或 `Average` 的数据字段。

## 将值字段绘制到行或列轴

当数据透视表包含两个或更多数据字段时，Aspose.Cells 会公开一个额外的虚拟字段 `PivotTable.ValuesField`。此虚拟字段表示数据区域中每个数据字段的聚合。您可以将其作为基础数据透视字段拖到行或列区域，这对于并排布局多个度量值非常有用。

{{% alert color="primary" %}}
`PivotTable.ValuesField` 在没有或只有一个值字段时不起作用。
{{% /alert %}}

以下场景逐步演示了三个端到端示例，针对相同的数据透视结构展示上述每项功能。

## 场景 1 — 将基础字段拖入值区域

本场景演示如何将单个基础字段（`Amount`）放入现有数据透视表的数据区域。共享的数据透视结构将 `Category` 和 `Item` 放在行轴上，将 `Year` 放在列轴上。操作完成后，`Amount` 出现在数据区域中，默认按 `Sum of Amount` 进行计算。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 中的表头
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// 使用嵌套循环根据 j 分支填充 A2:D9 的数据行
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

// 在 F3 添加名为 PivotTable1 的数据透视表
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

本场景从与场景 1 相同的数据透视结构开始，但将 `Amount` 字段添加到数据区域两次。两个数据字段都引用同一个源列，但是通过 `PivotField.Function` setter 覆盖第二个字段，使其变为 `Count` 而不是默认的 `Sum`。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
    for (let j = 0; j <= 3; j++)
    {
        if (j == 0)
        {
            worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
        }
        else if (j == 1)
        {
            let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
            worksheet.getCells().get(i, j).putValue(items[i - 1]);
        }
        else if (j == 2)
        {
            let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
            worksheet.getCells().get(i, j).putValue(years[i - 1]);
        }
        else
        {
            let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
            worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
        }
    }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```

## 场景 3 — 将值字段绘制到行或列轴

当存在两个数据字段时，`PivotTable.ValuesField` 就变得可用。本场景将该聚合虚拟字段拖到列区域，使数据区域中的每个度量值作为其自己的列块显示在 `Year` 旁边。

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

这三个场景涵盖了 Aspose.Cells for Node.js via C++ 中值字段操作的各个方面，从默认 `Sum` 的单个数据字段，到由虚拟 `ValuesField` 控制行或列轴布局的多度量数据透视表。

## 相关文章

- [Aspose.Cells for Node.js via C++ 中的数据透视表行和列字段](/cells/zh/nodejs-cpp/row-and-column-fields/)
- [数据透视表中的页面字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Node.js via C++ 中刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)
- [对数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}