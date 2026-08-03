---
title: 在 Aspose.Cells for .NET 中管理数据透视表的值字段
linktitle: 值字段
description: 了解如何在 Aspose.Cells for .NET 中将基础字段添加到数据透视表的数据区域，使用 PivotField.Function 更改汇总函数，以及将值字段绘制到行轴或列轴上。
keywords: Aspose.Cells, .NET, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /zh/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## 将字段添加到数据区域
将基础字段添加到数据（值）区域是塑造数据透视表如何聚合源数据的第一步。Aspose.Cells 公开了 `PivotTable.AddFieldToArea(PivotFieldType, string)` 重载方法，该方法接受常量 `PivotFieldType.Data` 和源列名称。一旦字段被添加到数据区域，就可以通过 `PivotTable.DataFields` 集合按字段添加的顺序访问它。默认情况下，数值类型的源列使用 `ConsolidationFunction.Sum` 进行汇总，而非数值列默认使用 `Count`。
## 更改汇总函数
放置在数据区域中的每个字段在内部都被包装为一个 `PivotField` 实例，其 `Function` 属性返回 `ConsolidationFunction` 枚举中的一个值。相同的 `Function` setter 允许您在可用的聚合之间切换，包括 `Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var` 和 `Varp`。
{{% alert color="primary" %}}
更改 `Function` 仅影响聚合方式，源列不会改变。
{{% /alert %}}
因此，您可以让一个数据字段保持为 `Sum`，同时添加一个针对同一源列但使用 `Count` 或 `Average` 的第二个数据字段，所有这些都在同一个数据透视表中完成。
## 将值字段绘制到行轴或列轴
当数据透视表包含两个或多个数据字段时，Aspose.Cells 会公开一个额外的虚拟字段，称为 `PivotTable.ValuesField`。此虚拟字段表示数据区域中每个数据字段的聚合结果。您可以将其作为基础数据透视字段拖入行区域或列区域，这对于将多个度量值并排布局非常有用。
{{% alert color="primary" %}}
如果没有值字段或只有一个值字段，则 `PivotTable.ValuesField` 无法使用。
{{% /alert %}}
下面的场景演示了三个端到端示例，针对相同的数据透视结构展示了上文描述的每项功能。
## 场景 1 — 将基础字段拖入值区域
本场景演示如何将单个基础字段（`Amount`）放入现有数据透视表的数据区域。共享的数据透视结构将 `Category` 和 `Item` 放在行轴上，将 `Year` 放在列轴上。操作完成后，`Amount` 出现在数据区域中，默认按 `Sum` 进行计算。
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// A1:D1 中的标题行
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

// A2:D9 中的数据行使用嵌套循环，根据 j 进行分支
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.Cells[i, j].PutValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.Cells[i, j].PutValue("Apple");
 else if (i == 3 || i == 4) worksheet.Cells[i, j].PutValue("Banana");
 else if (i == 5 || i == 6) worksheet.Cells[i, j].PutValue("Carrot");
 else worksheet.Cells[i, j].PutValue("Daikon");
 break;
 case 2:
 worksheet.Cells[i, j].PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.Cells[i, j].PutValue(100);
 else if (i == 2) worksheet.Cells[i, j].PutValue(150);
 else if (i == 3) worksheet.Cells[i, j].PutValue(80);
 else if (i == 4) worksheet.Cells[i, j].PutValue(90);
 else if (i == 5) worksheet.Cells[i, j].PutValue(50);
 else if (i == 6) worksheet.Cells[i, j].PutValue(60);
 else if (i == 7) worksheet.Cells[i, j].PutValue(40);
 else worksheet.Cells[i, j].PutValue(45);
 break;
 }
 }
}

// 在 F3 位置添加名为 PivotTable1 的数据透视表
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// 数据透视表布局：Category 和 Item 作为行字段，Year 作为列字段，Amount 作为数据字段
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```
## 场景 2 — 更改汇总函数
本场景从与场景 1 相同的数据透视结构开始，但将 `Amount` 字段两次添加到数据区域。两个数据字段都引用同一个源列，但第二个字段使用 `PivotField.Function` setter 进行重写，使其变为 `Count` 而不是默认的 `Sum`。
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.Cells[i, j].PutValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
 worksheet.Cells[i, j].PutValue(items[i - 1]);
 }
 else if (j == 2)
 {
 int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
 worksheet.Cells[i, j].PutValue(years[i - 1]);
 }
 else
 {
 int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };
 worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");

pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;

pivotTable.CalculateData();

workbook.Save("output_function.xlsx");
```
## 场景 3 — 将值字段绘制到行轴或列轴
当存在两个数据字段时，`PivotTable.ValuesField` 变为可用。本场景将该聚合虚拟字段拖到列区域，以便数据区域中的每个度量值都作为单独的列块显示在 `Year` 旁边。
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

string[] categories = { "Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable" };
string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.Cells[i, j].PutValue(categories[i - 1]);
 else if (j == 1) worksheet.Cells[i, j].PutValue(items[i - 1]);
 else if (j == 2) worksheet.Cells[i, j].PutValue(years[i - 1]);
 else worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.DataFields[1].Function = ConsolidationFunction.Count;

pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);

pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```
这三个场景共同涵盖了 Aspose.Cells for .NET 中值字段操作的各个方面，从使用默认 `Sum` 的单个数据字段，到由虚拟 `ValuesField` 控制行轴或列轴布局的多度量值数据透视表。

{{< app/cells/assistant language="csharp" >}}
