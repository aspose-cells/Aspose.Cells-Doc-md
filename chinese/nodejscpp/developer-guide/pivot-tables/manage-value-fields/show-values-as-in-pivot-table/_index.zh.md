---
title: 在数据透视表中显示值方式
linktitle: 在数据透视表中显示值方式
description: 使用 Aspose.Cells for Node.js via C++ 将数据透视表数据字段值显示为总计的百分比、相对于基项的差异、累计总计、排名等。
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, 数据透视表, 显示值方式, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /zh/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
Excel 的 **显示值为** 功能用二次计算替代每个显示结果，该二次计算基于聚合值，例如总体总计的百分比、累计总计、相对于选定基项的差值或排名，从而无需辅助公式或计算列即可进行比较分析。  
典型用法包括占比分析（行、列或总体总计的百分比）；使用期间字段的累计总计进行累计报告；使用相对于基项的差异或百分比差异对基准项进行差异分析；以及将数值按从小到大或从大到小进行排名。  
在 Aspose.Cells for Node.js via C++，`PivotShowValuesAsType` 枚举用于选择二次计算。只读的 `PivotField.getShowValuesSetting()` 访问器返回 `PivotShowValuesSetting` 对象，其 `setShowValuesAs()`、`setBaseFieldIndex()` 和 `setBaseItemIndex()` 方法用于配置行为；便利方法 `PivotField.showValuesAs(...)` 可在一次调用中应用相同设置。将这些设置应用于从 `PivotTable.getDataFields()` 获取的数据或值字段。

## **PivotShowValuesAsType 枚举成员**
数据字段保留其聚合函数（如 SUM 或 COUNT），而 **显示值为** 仅转换聚合值的显示方式。  
除了直接编写 `PivotShowValuesSetting` 设置（见最后一节），还有一个一次性调用的便利方法可应用相同的配置。它有两种形式——一种通过索引指定基字段和基项，另一种通过名称：

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `showValuesAsType` | 要应用的 `PivotShowValuesAsType` 二次计算。 | 始终。 |
| `baseField` | 基字段在数据透视表基字段中的零基索引（例如基项所属的行字段的索引），或在名称形式中为基字段的名称。 | 以下八种基相对格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、`RankSmallestToLargest`、`RankLargestToSmallest`）需要；其他格式传入 `0`（名称形式传入 `null`）。 |
| `baseItem` | 基项的零基索引，有两个哨兵值：-1 选择前一项，-2 选择后一项（Node.js via C++ 绑定未导出命名常量——请直接传入数值）。名称形式使用基项的标题，若所选格式不需要基项则为 `null`。 | 仅对三种基项格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）评估基项；其余五种基字段相对格式（`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、两种排名）忽略基项——传入 `0` 或 `null`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `Normal` | 无二次计算；聚合值按原样显示（默认）。 | — |
| `DifferenceFrom` | 将值显示为相对于基字段中基项值的差值。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `PercentageOf` | 将值显示为基字段中基项值的百分比。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `PercentageDifferenceFrom` | 将值显示为相对于基字段中基项值的百分比差异。 | `baseField` + `baseItem`（索引或标题，或前/后哨兵） |
| `RunningTotalIn` | 将值显示为基字段中后续项的累计总计。 | `baseField`（决定累计顺序的字段） |
| `PercentageOfRow` | 将值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将值显示为总体总计的百分比。 | — |
| `Index` | 使用 Excel 的 INDEX 公式 ((值 * 总计) / (行总计 * 列总计)) 显示值。 | — |
| `PercentageOfParentRowTotal` | 将值显示为其父行总计的百分比（用于嵌套的行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将值显示为其父列总计的百分比（用于嵌套的列字段）。 | — |
| `PercentageOfParentTotal` | 将值显示为父总计的百分比。 | `baseField`（父字段的总计作为参考） |
| `PercentageOfRunningTotalIn` | 将值显示为基字段中累计总计的百分比。 | `baseField`（累计字段） |
| `RankSmallestToLargest` | 对数值进行从最小（1）到最大排名。 | `baseField`（其项定义排名范围的字段） |
| `RankLargestToSmallest` | 对数值进行从最大（1）到最小排名。 | `baseField`（其项定义排名范围的字段） |

{{% alert color="primary" %}}
`showValuesAs(...)` 写入 `PivotShowValuesSetting` 设置（`getShowValuesAs()`/`setShowValuesAs()`、`getBaseFieldIndex()`/`setBaseFieldIndex()` 和 `getBaseItemIndex()`/`setBaseItemIndex()`）——该方法与属性对象是配置相同状态的两种方式，映射了 Excel “显示值为” 对话框中的基字段和基项选择器。
{{% /alert %}}

## **将值显示为总体总计的百分比**
使用 `PivotShowValuesAsType.PercentageOfTotal` 调用 `PivotField.showValuesAs()` 方法，可将每个数据字段单元格（包括总体总计）转换为其在总体总计中的占比。因此显示的数字为完整结果集的比例。此格式仅相对于总体总计进行度量，无需基字段或基项——尾随参数（`0`,`0`）为该格式忽略的占位符，正如上表所述。

```javascript
const AsposeCells = require("aspose.cells.node");
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
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **获取并配置 PivotField.getShowValuesSetting()**
通过 `PivotField.getShowValuesSetting()` 读取当前配置：只读访问器返回字段的 `PivotShowValuesSetting` 对象，该对象的设置描述了活动的显示值为计算。要更改配置，调用 `PivotField.showValuesAs()` 方法——一次调用写入所有设置，因而无需逐个设置。
`PivotShowValuesSetting` 对象公开 `showValuesAs()` 所写入的状态：
- `getShowValuesAs()` 和 `setShowValuesAs()` 用于选择 `PivotShowValuesAsType` 二次计算。
- `getBaseFieldIndex()` 和 `setBaseFieldIndex()` 指定基字段在数据透视表字段中的零基索引。该索引用于基相对格式。
- `getBaseItemIndex()` 和 `setBaseItemIndex()` 指定基项：特定透视项的零基索引，或两个哨兵值之一——-1 代表前一项，-2 代表后一项（绑定未导出命名常量）。该索引用于基项格式。
- `getBaseFieldName()` 和 `getBaseItemCaption()` 为只读视图，报告解析后的基字段名称和基项标题；例如，选择前项哨兵后，`getBaseItemCaption()` 返回 `(previous)`。
调用 `showValuesAs()` 后，再次调用 `PivotTable.calculateData()`，使数据透视表主体重新计算并使用更新的配置重新渲染。

```javascript
const AsposeCells = require("aspose.cells.node");
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
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
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
- [在数据透视表中管理值字段](/cells/zh/nodejs-cpp/manage-value-fields/)
- [刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}