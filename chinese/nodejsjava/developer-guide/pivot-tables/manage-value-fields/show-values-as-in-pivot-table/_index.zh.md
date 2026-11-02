---
title: 在数据透视表中显示数值方式
description: 使用 Aspose.Cells for Node.js via Java 将数据透视表数据字段值显示为整体百分比、相对于基准项的差异、累计总计、排名等。
linktitle: 显示数值方式
keywords: Aspose.Cells, 数据透视表, 显示数值方式, 数据展示格式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /zh/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用聚合函数（例如 `SUM` 或 `COUNT`）对每个数据字段进行汇总。Excel 的 **显示数值方式** 功能会用基于该聚合的二次计算替换每个显示结果，例如总体百分比、累计总计、相对于选定基准项的差值或排名，从而无需辅助公式或计算列即可进行比较分析。典型的使用场景包括占比分析（包括行、列或整体的百分比）；在周期字段中使用累计总计进行累计报告；使用相对于基准项的差值或百分比差值进行方差分析；以及将数值从最小到最大或从最大到最小进行排名。
在 Aspose.Cells for Node.js via Java 中，`PivotFieldDataDisplayFormat` 选择二次计算。只读的 `PivotField.getShowValuesSetting()` 方法返回一个 `PivotShowValuesSetting` 对象。其 `setCalculationType()`、`setBaseFieldIndex()`、`setBaseItemPositionType()` 和 `setBaseItemIndex()` 方法用于配置行为；便利方法 `PivotField.showValuesAs(...)` 在一次调用中应用相同的四个设置。将这些设置应用于从 `PivotTable.getDataFields()` 获得的数据或数值字段。

## **PivotFieldDataDisplayFormat 枚举成员**
数据字段保留其聚合函数（如 `SUM` 或 `COUNT`），而 **显示数值方式** 只改变聚合值的显示方式。除了直接写入 `PivotShowValuesSetting` 设置（参见最后一节），一次调用的便利方法也会应用相同的配置：

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| 参数 | 含义 | 何时需要 |
| --- | --- | --- |
| `displayFormat` | 要应用的 `PivotFieldDataDisplayFormat` 二次计算。 | 始终。 |
| `baseField` | 在数据透视表的基字段中的零基索引（例如，基项所属的行字段的索引）。 | 仅适用于以下六种基准相关格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`）；其它格式均忽略。 |
| `baseItemPositionType` | 相对于当前项选择基项的方式：`PivotItemPositionType.PREVIOUS`、`.NEXT` 或 `.CUSTOM`。 | 仅适用于三种基项格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）；其它格式均忽略。 |
| `baseItem` | 基项的零基索引。 | 仅当 `baseItemPositionType` 为 `CUSTOM` 时需要（此时项索引指定确切基项）；`PREVIOUS` / `NEXT` 以及所有非基项格式均忽略 —— 传入 `0`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `NORMAL` | 无二次计算；聚合值原样显示（默认）。 | — |
| `DIFFERENCE_FROM` | 显示为相对于基字段中基项的值的差值。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（仅在 `CUSTOM` 时使用 `baseItem`） |
| `PERCENTAGE_OF` | 显示为相对于基字段中基项的值的百分比。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（仅在 `CUSTOM` 时使用 `baseItem`） |
| `PERCENTAGE_DIFFERENCE_FROM` | 显示为相对于基字段中基项的值的百分比差值。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（仅在 `CUSTOM` 时使用 `baseItem`） |
| `RUNNING_TOTAL_IN` | 显示为基字段连续项的累计总计。 | `baseField`（用于驱动累计的字段） |
| `PERCENTAGE_OF_ROW` | 显示为行总计的百分比。 | — |
| `PERCENTAGE_OF_COLUMN` | 显示为列总计的百分比。 | — |
| `PERCENTAGE_OF_TOTAL` | 显示为整体总计的百分比。 | — |
| `INDEX` | 使用 Excel 索引公式 ((value * grand total) / (row total * column total)) 显示值。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 显示为其父行总计的百分比（用于嵌套行字段）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 显示为其父列总计的百分比（用于嵌套列字段）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 显示为其父总计的百分比。 | `baseField`（作为参照的父字段） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 显示为基字段中累计总计的百分比。 | `baseField`（累计字段） |
| `RANK_SMALLEST_TO_LARGEST` | 对值进行从最小 (1) 到最大的排名。 | — |
| `RANK_LARGEST_TO_SMALLEST` | 对值进行从最大 (1) 到最小的排名。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` 写入 `PivotShowValuesSetting` 设置（`setCalculationType()`、`setBaseFieldIndex()`、`setBaseItemPositionType()` 和 `setBaseItemIndex()`）——该方法和设置对象是配置同一状态的两种方式，映射了 Excel “显示数值方式” 对话框中的基字段和基项选择器。
{{% /alert %}}

## **显示数值方式为整体百分比**
使用 `PivotField.showValuesAs()` 方法并传入 `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL`，即可将每个数据字段单元格（包括整体总计）转换为其在整体总计中的占比。显示的数字因此为完整结果集的比例。此格式仅将每个值与整体总计进行比较，因此不需要基字段或基项——尾随参数（`0`、`PivotItemPositionType.PREVIOUS`、`0`）是该格式忽略的占位符，如上表所示。

```javascript
const AsposeCells = require("aspose.cells");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **获取并配置 PivotField.getShowValuesSetting()**
通过 `PivotField.getShowValuesSetting()` 读取当前配置：只读方法返回字段的 `PivotShowValuesSetting` 对象，其四个设置描述了当前的 显示数值方式 计算。要更改配置，调用 `PivotField.showValuesAs()` 方法——它在一次调用中写入所有四个设置，因此无需逐个分配。`PivotShowValuesSetting` 对象公开了 `showValuesAs()` 写入的四个设置：
- `getCalculationType()` / `setCalculationType()` 选择 `PivotFieldDataDisplayFormat` 二次计算。
- `getBaseFieldIndex()` / `setBaseFieldIndex()` 指定基字段在数据透视字段集合中的零基索引。该索引用于基准相关格式。
- `getBaseItemPositionType()` / `setBaseItemPositionType()` 确定基项相对于当前项的位置，可接受 `PivotItemPositionType.NEXT`、`PivotItemPositionType.PREVIOUS` 或 `PivotItemPositionType.CUSTOM`。
- `getBaseItemIndex()` / `setBaseItemIndex()` 指定零基基项索引，仅在 `getBaseItemPositionType()` 为 `CUSTOM` 时使用。
调用 `showValuesAs()` 后，再次调用 `PivotTable.calculateData()`，以便重新计算并重新渲染数据透视表主体，使其使用更新的配置。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **相关文章**
- [管理数据透视表中的数值字段](/cells/zh/nodejs-java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/)
- [对数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}