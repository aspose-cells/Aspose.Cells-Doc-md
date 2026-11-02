---
title: 在数据透视表中显示值方式
description: 使用 Aspose.Cells for .NET，将数据透视表数据字段的值显示为总计的百分比、相对于基准项的差异、累计总计、排名等。
linktitle: Show Values As
keywords: Aspose.Cells, 数据透视表, 显示值方式, 数据显示格式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /zh/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用聚合函数（例如 `Sum` 或 `Count`）对每个数据字段进行汇总。Excel 的 **Show Values As** 功能将每个显示的结果替换为基于该聚合的二次计算——例如，总计的百分比、累计总计、相对于选定基准项的差异或排名——从而无需辅助公式或计算列即可进行比较分析。
典型用法包括占比分析（如行、列或总计的百分比）；使用期间字段的累计总计进行累计报告；使用相对于基准项的差异或百分比差异进行方差分析；以及对数值进行从最小到最大或从最大到最小的排名。
在 Aspose.Cells for .NET 中，`PivotFieldDataDisplayFormat` 用于选择二次计算。只读属性 `PivotField.ShowValuesSetting` 返回一个 `PivotShowValuesSetting` 对象，其可写的 `CalculationType`、`BaseFieldIndex`、`BaseItemPositionType` 和 `BaseItemIndex` 属性用于配置行为；便捷方法 `PivotField.ShowValuesAs(...)` 在一次调用中应用相同的四个设置。将这些设置应用于从 `PivotTable.DataFields` 获取的数据字段或数值字段。

## **PivotFieldDataDisplayFormat 枚举成员**
数据字段保持其聚合函数（如 Sum 或 Count），而 Show Values As 仅改变聚合值的显示方式。除了直接写入 `PivotShowValuesSetting` 属性（参见最后一节），还可以使用一次调用的便捷方法来应用相同的配置：

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `displayFormat` | 要应用的 `PivotFieldDataDisplayFormat` 二次计算。 | 始终必需。 |
| `baseField` | 数据透视表基字段的零基索引（例如，基项所属的行字段的索引）。 | 仅适用于以下六种基准相关格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）；其它格式均忽略。 |
| `baseItemPositionType` | 相对于当前项选择基项的方式：`PivotItemPositionType.Previous`、`.Next` 或 `.Custom`。 | 仅适用于三种基项格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）；其它格式均忽略。 |
| `baseItem` | 基项的零基索引。 | 仅当 `baseItemPositionType` 为 `Custom` 时使用（此时项索引指定具体基项）；`Previous` / `Next` 以及所有非基项格式均忽略——传入 `0`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `Normal` | 无二次计算；聚合值按原样显示（默认）。 | — |
| `DifferenceFrom` | 将数值显示为相对于基字段中基项值的差异。 | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` 仅在 `Custom` 时) |
| `PercentageOf` | 将数值显示为基字段中基项值的百分比。 | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` 仅在 `Custom` 时) |
| `PercentageDifferenceFrom` | 将数值显示为相对于基字段中基项值的百分比差异。 | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` 仅在 `Custom` 时) |
| `RunningTotalIn` | 将数值显示为基字段连续项的累计总计。 | `baseField` (累加所依据的字段) |
| `PercentageOfRow` | 将数值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将数值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将数值显示为总计的百分比。 | — |
| `Index` | 使用 Excel 的 INDEX 公式 ((value * grand total) / (row total * column total)) 显示数值。 | — |
| `PercentageOfParentRowTotal` | 将数值显示为其父行总计的百分比（用于嵌套行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将数值显示为其父列总计的百分比（用于嵌套列字段）。 | — |
| `PercentageOfParentTotal` | 将数值显示为其父总计的百分比。 | `baseField`（作为参照的父字段） |
| `PercentageOfRunningTotalIn` | 将数值显示为基字段累计总计的百分比。 | `baseField` (累加所依据的字段) |
| `RankSmallestToLargest` | 对数值进行从最小（1）到最大排序。 | — |
| `RankLargestToSmallest` | 对数值进行从最大（1）到最小排序。 | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` 写入 `PivotShowValuesSetting` 属性（`CalculationType`、`BaseFieldIndex`、`BaseItemPositionType`、`BaseItemIndex`）——该方法和属性对象是配置相同状态的两种方式，映射了 Excel "Show Values As" 对话框中的基字段和基项选择器。
{{% /alert %}}

## **显示为总计的百分比**
使用 `PivotField.ShowValuesAs` 方法并传入 `PivotFieldDataDisplayFormat.PercentageOfTotal`，可将每个数据字段单元格（包括总计）转换为其在总计中的份额。因此显示的数字表现为完整结果集的比例。该格式仅相对于总计进行测量，无需基字段或基项——尾随参数（`0`、`PivotItemPositionType.Previous`、`0`）为该格式所忽略的占位符，如上表所示。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **获取并配置 PivotField.ShowValuesSetting**
通过 `PivotField.ShowValuesSetting` 读取当前配置：只读属性返回字段的 `PivotShowValuesSetting` 对象，其四个属性描述了当前的 Show Values As 计算。要更改配置，调用 `PivotField.ShowValuesAs` 方法——它一次调用即可写入全部四个设置，无需逐个赋值。
`PivotShowValuesSetting` 对象公开了 `ShowValuesAs` 写入的四个属性：
- `CalculationType` 选择 `PivotFieldDataDisplayFormat` 二次计算。
- `BaseFieldIndex` 指定基字段在数据透视表字段中的零基索引。用于基准相关格式。
- `BaseItemPositionType` 确定基项相对于当前项的位置，可接受 `PivotItemPositionType.Next`、`PivotItemPositionType.Previous` 或 `PivotItemPositionType.Custom`。
- `BaseItemIndex` 指定零基的基项索引，仅在 `BaseItemPositionType` 为 `Custom` 时使用。
调用 `ShowValuesAs` 后，再次调用 `PivotTable.CalculateData()`，使数据透视表主体重新计算并使用更新的配置重新渲染。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **相关文章**
- [管理数据透视表中的值字段](/cells/zh/net/manage-value-fields/)
- [使用数据透视表中 DataField 的数据显示格式](/cells/zh/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [刷新数据透视表](/cells/zh/net/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}