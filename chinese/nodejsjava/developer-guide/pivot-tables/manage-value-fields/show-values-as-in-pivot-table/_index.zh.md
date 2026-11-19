---
title: 在数据透视表中显示为
linktitle: 在数据透视表中显示为
description: 使用 Aspose.Cells for Node.js via Java 将数据透视表数据字段的值显示为总计的百分比、相对基准项的差异、运行总计、排名等。
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, 数据透视表, 显示值为, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /zh/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用诸如 `SUM` 或 `COUNT` 的聚合函数对每个数据字段进行聚合。Excel 的 **显示值为** 功能用从聚合结果派生的二次计算替代每个显示的结果，例如，总计的百分比、运行总计、相对于选定基准项的差异或排名，从而无需辅助公式或计算列即可进行比较分析。  
常见用法包括占比分析（行、列或总计的百分比）、使用期间字段的运行总计进行累积报告、使用相对于基准项的差异或百分比差异进行方差分析，以及对值进行从最小到最大或从最大到最小的排名。  
在 Aspose.Cells for Node.js via Java 中，`PivotShowValuesAsType` 枚举用于选择二次计算。只读的 `PivotField.getShowValuesSetting()` 方法返回 `PivotShowValuesSetting` 对象，可通过其 `setShowValuesAs()`、`setBaseFieldIndex()` 和 `setBaseItemIndex()` 方法配置行为；便捷方法 `PivotField.showValuesAs(...)` 在一次调用中应用相同的设置。将这些设置应用于通过 `PivotTable.getDataFields()` 获取的数据或值字段。

## **PivotShowValuesAsType 枚举成员**
数据字段保留其聚合函数，如 SUM 或 COUNT，而 “显示值为” 只改变聚合值的显示方式。  
除了直接使用 `PivotShowValuesSetting` 的设置器（参见最后一节），还有一种一次调用的便捷方法可应用相同的配置。该方法有两种形式——一种通过索引指定基字段和基项，另一种通过名称指定。

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `showValuesAsType` | 要应用的 `PivotShowValuesAsType` 二次计算。 | 始终。 |
| `baseField` | 数据透视表基字段中的零基索引（例如，基项所属的行字段的索引），或者在名称形式下为基字段的名称。 | 以下八种基于字段的格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`）时必需；对其他所有格式请传入 `0`（名称形式下请传 `null`）。 |
| `baseItem` | 基项的零基索引，附带两个哨兵值：-1 选择前一个项，-2 选择后一个项（包根未导出 `PivotShowValuesSetting` 常量——请直接使用文字值）。名称形式则使用基项的标题，当所选格式不需要基项时传 `null`。 | 仅在三种基项格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）中需要评估基项；五种基于字段的格式（`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、两种排名）会忽略它——请传 `0` 或 `null`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `NORMAL` | 无二次计算；聚合值按原样显示（默认）。 | — |
| `DIFFERENCE_FROM` | 显示为相对于基字段中基项值的差异。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `PERCENTAGE_OF` | 显示为相对于基字段中基项值的百分比。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `PERCENTAGE_DIFFERENCE_FROM` | 显示为相对于基字段中基项值的百分比差异。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `RUNNING_TOTAL_IN` | 显示为基字段中连续项的运行总计。 | `baseField`（决定累加顺序的字段） |
| `PERCENTAGE_OF_ROW` | 显示为行总计的百分比。 | — |
| `PERCENTAGE_OF_COLUMN` | 显示为列总计的百分比。 | — |
| `PERCENTAGE_OF_TOTAL` | 显示为总计的百分比。 | — |
| `INDEX` | 使用 Excel 的 INDEX 公式 ((value * total) / (row total * column total)) 显示值。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 显示为其父行总计的百分比（用于嵌套行字段）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 显示为其父列总计的百分比（用于嵌套列字段）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 显示为其父总计的百分比。 | `baseField`（父字段，其总计作为参考） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 显示为基字段中运行总计的百分比。 | `baseField`（累加字段） |
| `RANK_SMALLEST_TO_LARGEST` | 按从最小（1）到最大进行排名。 | `baseField`（定义排名范围的字段） |
| `RANK_LARGEST_TO_SMALLEST` | 按从最大（1）到最小进行排名。 | `baseField`（定义排名范围的字段） |

{{% alert color="primary" %}}
`showValuesAs(...)` 通过 `setShowValuesAs()`、`setBaseFieldIndex()` 和 `setBaseItemIndex()` 写入 `PivotShowValuesSetting` 状态——该方法和属性对象是配置相同状态的两种方式，映射 Excel “显示值为” 对话框中的基字段和基项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.showValuesAs()` 方法并传入 `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL`，可将每个数据字段单元格（包括总计）转换为其在总计中的占比。显示的数字因此为完整结果集的比例。此格式仅将每个值与总计进行比较，无需基字段或基项——尾随参数（`0`, `0`）是该格式忽略的占位符，如上表所示。

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **获取并配置 PivotField.getShowValuesSetting()**
通过 `PivotField.getShowValuesSetting()` 读取当前配置：该只读方法返回字段的 `PivotShowValuesSetting` 对象，其设置描述了当前的 “显示值为” 计算。要更改配置，调用 `PivotField.showValuesAs()` 方法——它一次性写入所有设置，无需逐个设置。
- `getShowValuesAs()` / `setShowValuesAs()` 选择 `PivotShowValuesAsType` 二次计算。
- `getBaseFieldIndex()` / `setBaseFieldIndex()` 指定基字段在数据透视表字段中的零基索引。基于字段的格式会使用该索引。
- `getBaseItemIndex()` / `setBaseItemIndex()` 指定基项：具体的基项零基索引，或两个哨兵值之一——-1 表示前一个项，-2 表示后一个项（包根未导出命名常量）。基项格式会使用它。
- `getBaseFieldName()` 和 `getBaseItemCaption()` 为只读视图，报告已解析的基字段名称和基项标题；例如，在选择前项哨兵后，`getBaseItemCaption()` 返回 `(previous)`。
调用 `showValuesAs()` 后，再次调用 `PivotTable.calculateData()`，以便重新计算并重新渲染数据透视表主体，使其使用更新的配置。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **相关文档**
- [在数据透视表中管理值字段](/cells/zh/nodejs-java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}