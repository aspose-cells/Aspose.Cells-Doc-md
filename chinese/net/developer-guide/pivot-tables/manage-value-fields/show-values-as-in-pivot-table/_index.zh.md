---
title: 数据透视表中的值显示方式
linktitle: 数据透视表中的值显示方式
description: 使用 Aspose.Cells for .NET，将数据透视表的数据字段值显示为占总计的百分比、与基准项的差异、累计总计、排名等。
keywords: Aspose.Cells, 数据透视表, 值显示方式, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /zh/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常通过 `Sum` 或 `Count` 等聚合函数对每个数据字段进行汇总。Excel 的**值显示方式**功能会将每个显示结果替换为基于该聚合值计算得出的二次计算结果，例如占总计的百分比、累计总计、与所选基准项的差异或排名，从而无需使用辅助公式或计算列即可完成比较分析。
典型用途包括占比分析，例如显示占行总计、列总计或总计的百分比；在期间字段中使用累计总计来生成累计报告；基于基准项使用“与基准项的差异”或“与基准项的百分比差异”进行差异分析；以及按从小到大或从大到小的顺序对值进行排名。
在 Aspose.Cells for .NET 中，`PivotShowValuesAsType` 枚举用于选择二次计算。只读属性 `PivotField.ShowValuesSetting` 返回 `PivotShowValuesSetting` 对象，该对象的可写属性 `ShowValuesAs`、`BaseFieldIndex` 和 `BaseItemIndex` 用于配置行为；便捷方法 `PivotField.ShowValuesAs(...)` 通过一次调用应用相同的设置。请将这些设置应用于从 `PivotTable.DataFields` 获取的数据字段或值字段。

## **`PivotShowValuesAsType` 枚举成员**
数据字段保留其聚合函数，例如 `Sum` 或 `Count`，而“值显示方式”仅改变聚合值的显示方式。
除直接写入 `PivotShowValuesSetting` 属性外（请参阅最后一节），还提供了一种单次调用即可应用相同配置的便捷方法。该方法包含两个重载：一个通过索引指定基准字段和基准项，另一个通过名称指定。

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| 参数 | 含义 | 何时需要 |
| --- | --- | --- |
| `showValuesAsType` | 要应用的 `PivotShowValuesAsType` 二次计算。 | 始终需要。 |
| `baseField` | 基准字段在数据透视表各基准字段中的从零开始的索引（例如基准项所属行字段的索引），或者在字符串重载中指定基准字段的名称。 | 以下八种基于基准的格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、`RankSmallestToLargest`、`RankLargestToSmallest`）；对于其他所有格式，请传入 `0`（或在字符串重载中传入 `null`）。 |
| `baseItem` | 基准项的从零开始的索引，另有两个哨兵值：`PivotShowValuesSetting.PreviousPivotItem` (-1) 用于选择前一项，`PivotShowValuesSetting.NextPivotItem` (-2) 用于选择后一项。字符串重载接受基准项的标题，而不是索引；当所选格式不需要基准项时，传入 `null`。 | 仅以下三种基于基准项的格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）会使用基准项；以下五种基于字段的格式（`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn` 以及两种排名格式）会忽略该参数——传入 `0` 或 `null`。 |

| 计算类型 | 行为 | 基准项参数 |
| --- | --- | --- |
| `Normal` | 不执行二次计算；按原样显示聚合值（默认值）。 | — |
| `DifferenceFrom` | 将值显示为相对于基准字段中基准项数值的差异。 | `baseField` + `baseItem`（索引或标题，或前一项/后一项哨兵值） |
| `PercentageOf` | 将值显示为占基准字段中基准项数值的百分比。 | `baseField` + `baseItem`（索引或标题，或前一项/后一项哨兵值） |
| `PercentageDifferenceFrom` | 将值显示为相对于基准字段中基准项数值的百分比差异。 | `baseField` + `baseItem`（索引或标题，或前一项/后一项哨兵值） |
| `RunningTotalIn` | 将值显示为基准字段中连续项目的累计总计。 | `baseField`（其项目顺序决定累加顺序的字段） |
| `PercentageOfRow` | 将值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将值显示为总计的百分比。 | — |
| `Index` | 使用 Excel 索引公式显示值（(值 * 总计) / (行总计 * 列总计)）。 | — |
| `PercentageOfParentRowTotal` | 将值显示为其父级行总计的百分比（适用于嵌套行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将值显示为其父级列总计的百分比（适用于嵌套列字段）。 | — |
| `PercentageOfParentTotal` | 将值显示为其父级总计的百分比。 | `baseField`（用作总计参考的父级字段） |
| `PercentageOfRunningTotalIn` | 将值显示为基准字段中累计总计的百分比。 | `baseField`（累加字段） |
| `RankSmallestToLargest` | 按从小到大的顺序对值进行排名（最小值为 1）。 | `baseField`（其项目定义排名作用域的字段） |
| `RankLargestToSmallest` | 按从大到小的顺序对值进行排名（最大值为 1）。 | `baseField`（其项目定义排名作用域的字段） |

{{% alert color="primary" %}}
`ShowValuesAs(...)` 会设置 `PivotShowValuesSetting` 状态（`ShowValuesAs`、`BaseFieldIndex`、`BaseItemIndex`）——该方法与属性对象是配置同一状态的两种方式，对应 Excel“值显示方式”对话框中的基准字段和基准项选择器。
{{% /alert %}}

## **将值显示为占总计的百分比**
调用 `PivotField.ShowValuesAs` 方法并传入 `PivotShowValuesAsType.PercentageOfTotal`，将每个数据字段单元格（包括总计）转换为占总计的比例。因此，显示的数字表示完整结果集中各部分所占的比例。此格式仅以总计为基准衡量每个值，因此不需要基准字段或基准项——末尾参数（`0`、`0`）只是占位参数，该格式会忽略这些参数，如上表中的参数说明所示。

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **获取并配置 PivotField.ShowValuesSetting**
通过 `PivotField.ShowValuesSetting` 读取当前配置：该只读属性返回字段的 `PivotShowValuesSetting` 对象，其属性描述当前生效的“值显示方式”计算类型。若要更改配置，请调用 `PivotField.ShowValuesAs` 方法——该方法通过一次调用写入所有设置，因此无需逐个赋值属性。
`PivotShowValuesSetting` 对象公开由 `ShowValuesAs` 写入的状态：
- `ShowValuesAs` 选择 `PivotShowValuesAsType` 二次计算。
- `BaseFieldIndex` 指定基准字段在数据透视表各字段中的从零开始的索引。该属性用于基于基准的格式。
- `BaseItemIndex` 指定基准项：可以是特定数据透视表项的从零开始的索引，也可以是两个哨兵值之一——`PivotShowValuesSetting.PreviousPivotItem` (-1) 用于选择前一项，`PivotShowValuesSetting.NextPivotItem` (-2) 用于选择后一项。该属性用于基于基准项的格式。
- `BaseFieldName` 和 `BaseItemCaption` 是只读视图，用于返回解析后的基准字段名称和基准项标题；例如，选择前一项哨兵值后，`BaseItemCaption` 的值为 `(previous)`。
调用 `ShowValuesAs` 后，请再次调用 `PivotTable.CalculateData()`，以便使用更新后的配置重新计算并重新呈现数据透视表主体。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **相关文章**
- [管理数据透视表中的值字段](/cells/zh/net/manage-value-fields/)
- [处理数据透视表中 DataField 的数据显示格式](/cells/zh/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [刷新数据透视表](/cells/zh/net/refresh-pivot-table/)
- [对数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}