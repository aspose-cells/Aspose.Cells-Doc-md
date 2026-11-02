---
title: 在数据透视表中显示值方式
linktitle: 在数据透视表中显示值方式
description: 使用 Aspose.Cells for Go via C++ 将数据透视表数据字段的值显示为总计的百分比、相对于基准项的差异、累计总计、排名等。
keywords: Aspose.Cells for Go via C++, 数据透视表, 显示值方式, 数据展示格式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /zh/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用诸如 `Sum` 或 `Count` 的聚合函数来汇总每个数据字段。Excel 的 **显示值方式** 功能会用二次计算替代每个显示的结果，例如显示为总计的百分比、累计总计、相对于选定基准项的差异或排名，从而无需辅助公式或计算列即可进行比较分析。常见用法包括按行、列或总计的百分比进行占比分析；在周期字段中使用累计总计进行累计报告；通过相对于基准项的差异或百分比差异进行方差分析；以及将数值按从小到大或从大到小进行排名。  
在 Aspose.Cells for Go via C++ 中，`PivotFieldDataDisplayFormat` 用于选择二次计算。`PivotField.GetShowValuesSetting()` 访问器返回 `PivotShowValuesSetting` 对象，其 `SetCalculationType`、`SetBaseFieldIndex`、`SetBaseItemPositionType` 和 `SetBaseItemIndex` 方法配置该行为；便利方法 `PivotField.ShowValuesAs(...)` 在一次调用中应用这四个设置。将这些设置应用于通过 `PivotTable.GetDataFields()` 获取的数据或数值字段。

## **PivotFieldDataDisplayFormat 枚举成员**
数据字段保留其聚合函数（如 Sum 或 Count），而 **显示值方式** 仅改变聚合值的显示方式。除了直接写入 `PivotShowValuesSetting` 的值（请参见最后一节），也可以使用一次调用的便利方法来完成相同配置：

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `displayFormat` | 要应用的 `PivotFieldDataDisplayFormat` 二次计算。 | 始终。 |
| `baseField` | 基字段的零基索引，指在数据透视表的基字段中的位置（例如，基项所属的行字段的索引）。 | 仅适用于以下六种基准相关格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）；其它格式均忽略。 |
| `baseItemPositionType` | 基项相对于当前项的选择方式：`PivotItemPositionType.Previous`、`.Next` 或 `.Custom`。 | 仅适用于三种基项格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）；其它格式均忽略。 |
| `baseItem` | 基项的零基索引。 | 仅当 `baseItemPositionType` 为 `Custom` 时使用（此时项索引指定确切的基项）；`Previous` / `Next` 以及所有非基项格式忽略此参数 — 传入 `0`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `Normal` | 无二次计算；聚合值按原样显示（默认）。 | — |
| `DifferenceFrom` | 将值显示为相对于基字段中基项值的差异。 | `baseField` + `Previous`/`Next`/`Custom`（仅在 `Custom` 时使用 `baseItem`） |
| `PercentageOf` | 将值显示为相对于基字段中基项值的百分比。 | `baseField` + `Previous`/`Next`/`Custom`（仅在 `Custom` 时使用 `baseItem`） |
| `PercentageDifferenceFrom` | 将值显示为相对于基字段中基项值的百分比差异。 | `baseField` + `Previous`/`Next`/`Custom`（仅在 `Custom` 时使用 `baseItem`） |
| `RunningTotalIn` | 将值显示为基字段中连续项的累计总计。 | `baseField`（决定累计顺序的字段） |
| `PercentageOfRow` | 将值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将值显示为总计的百分比。 | — |
| `Index` | 使用 Excel 索引公式 ((value * 总计) / (行总计 * 列总计)) 显示值。 | — |
| `PercentageOfParentRowTotal` | 将值显示为其父行总计的百分比（适用于嵌套行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将值显示为其父列总计的百分比（适用于嵌套列字段）。 | — |
| `PercentageOfParentTotal` | 将值显示为其父总计的百分比。 | `baseField`（作为参照的父字段） |
| `PercentageOfRunningTotalIn` | 将值显示为基字段中累计总计的百分比。 | `baseField`（累计字段） |
| `RankSmallestToLargest` | 将值按从最小（1）到最大进行排名。 | — |
| `RankLargestToSmallest` | 将值按从最大（1）到最小进行排名。 | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` 写入 `PivotShowValuesSetting` 值（`CalculationType`、`BaseFieldIndex`、`BaseItemPositionType`、`BaseItemIndex`）——该方法和设置对象是配置同一状态的两种方式，映射到 Excel “显示值方式” 对话框中的基字段和基项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.ShowValuesAs` 并传入 `PivotFieldDataDisplayFormat.PercentageOfTotal`，即可把每个数据字段单元格（包括总计）转换为其在总计中的占比。显示的数字因此是完整结果集的比例。此格式仅相对于总计进行衡量，无需基字段或基项——后置参数 (`0`、`PivotItemPositionType.Previous`、`0`) 仅是占位符，格式本身会忽略它们，如上表所示。

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load or create a workbook with source data
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	dataSheet, _ := worksheets.Get_Int(0)
	cells, _ := dataSheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"}
	amounts := []int{10, 20, 30, 40, 50, 60}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		amountCell.PutValue_Int(int32(amounts[i]))
	}
	// Add a pivot table on a new worksheet
	pivotSheetIndex, _ := worksheets.Add()
	pivotSheet, _ := worksheets.Get_Int(pivotSheetIndex)
	pivotTables, _ := pivotSheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=Sheet1!A1:B7", 2, 2)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Show the Amount data field as a percentage of the grand total with the
	// one-call method; PercentageOfTotal takes no base item, so the trailing
	// base arguments (0, Previous, 0) are placeholders the format ignores
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_PercentageOfTotal,
		int32(0),
		PivotItemPositionType_Previous,
		int32(0),
	)
	pivotTable.CalculateData()
	// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
	workbook.Save_String("ShowValuesAsPercentageOfTotal.xlsx")
}
```

## **获取并配置 PivotField.ShowValuesSetting**
通过 `PivotField.GetShowValuesSetting()` 读取当前配置：该访问器返回字段的 `PivotShowValuesSetting` 对象，其四个 getter 方法描述当前的 “显示值方式” 计算。若需更改配置，调用 `PivotField.ShowValuesAs` 方法——一次调用即可写入全部四个设置，无需逐一设置。  
`PivotShowValuesSetting` 对象公开了 `ShowValuesAs` 写入的四个值：
- `GetCalculationType()` / `SetCalculationType()` 选择 `PivotFieldDataDisplayFormat` 二次计算。
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` 指定基字段在透视字段集合中的零基索引。基准相关格式会使用此索引。
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` 决定基项相对于当前项的位置，可接受 `PivotItemPositionType.Next`、`PivotItemPositionType.Previous` 或 `PivotItemPositionType.Custom`。
- `GetBaseItemIndex()` / `SetBaseItemIndex()` 指定零基的基项索引，仅在位置类型为 `Custom` 时使用。
在调用 `ShowValuesAs` 之后，重新调用 `PivotTable.CalculateData()`，使透视表主体重新计算并使用更新后的配置重新渲染。

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("ShowValuesAsPercentageOfTotal.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	// Read the current show-values settings
	settings, _ := dataField.GetShowValuesSetting()
	calculationType, _ := settings.GetCalculationType()
	baseFieldIndex, _ := settings.GetBaseFieldIndex()
	baseItemPositionType, _ := settings.GetBaseItemPositionType()
	baseItemIndex, _ := settings.GetBaseItemIndex()
	fmt.Println("CalculationType:", calculationType)
	fmt.Println("BaseFieldIndex:", baseFieldIndex)
	fmt.Println("BaseItemPositionType:", baseItemPositionType)
	fmt.Println("BaseItemIndex:", baseItemIndex)
	// Switch to a base-item calculation with the one-call method: difference
	// from the value of the previous item in the row field
	rowFields, _ := pivotTable.GetRowFields()
	rowField, _ := rowFields.Get_Int(0)
	baseIndex, _ := rowField.GetBaseIndex()
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_DifferenceFrom,
		baseIndex,
		PivotItemPositionType_Previous,
		0,
	)
	pivotTable.CalculateData()
	// Note: the percentage number format saved by the previous example still
	// clings to the data field cells; the underlying values are now differences
	// Re-read the applied configuration
	updatedSettings, _ := dataField.GetShowValuesSetting()
	updatedCalculationType, _ := updatedSettings.GetCalculationType()
	fmt.Println("CalculationType now:", updatedCalculationType)
	workbook.Save_String("ShowValuesAsDifferenceFrom.xlsx")
}
```

## **相关文章**
- [在数据透视表中对透视字段进行分组](/cells/zh/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [数据透视表中前 10 项的显示或过滤](/cells/zh/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [更新切片器](/cells/zh/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}