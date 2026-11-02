---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for Go via C++.
linktitle: Show Values As
keywords: Aspose.Cells for Go via C++, pivot table, show values as, data display format, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `Sum` or `Count`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for Go via C++, `PivotFieldDataDisplayFormat` selects the secondary calculation. The `PivotField.GetShowValuesSetting()` accessor returns a `PivotShowValuesSetting` object, whose `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType`, and `SetBaseItemIndex` methods configure the behavior; the convenience method `PivotField.ShowValuesAs(...)` applies the same four settings in one call. Apply these settings to a data or value field obtained from `PivotTable.GetDataFields()`.

## **PivotFieldDataDisplayFormat Enumeration Members**
The data field keeps its aggregate function, such as Sum or Count, while Show Values As transforms only how the aggregated value is displayed.
Besides writing the `PivotShowValuesSetting` values directly (see the last section), a one-call convenience method applies the same configuration:

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `displayFormat` | The `PivotFieldDataDisplayFormat` secondary calculation to apply. | Always. |
| `baseField` | Zero-based index of the base field among the pivot table's base fields (for example, the index of the row field the base item belongs to). | Only the six base-relative formats below (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); ignored by every other format. |
| `baseItemPositionType` | How the base item is chosen relative to the current item: `PivotItemPositionType.Previous`, `.Next`, or `.Custom`. | Only the three base-item formats (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); ignored by every other format. |
| `baseItem` | Zero-based index of the base item. | Only when `baseItemPositionType` is `Custom` (the item index picks the exact base item); ignored for `Previous` / `Next` and by every non-base format — pass `0`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `Normal` | No secondary calculation; the aggregated value is displayed as is (default). | — |
| `DifferenceFrom` | Displays the value as a difference from the value of a base item in a base field. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` only with `Custom`) |
| `PercentageOf` | Displays the value as a percentage of the value of a base item in a base field. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` only with `Custom`) |
| `PercentageDifferenceFrom` | Displays the value as the percentage difference from the value of a base item in a base field. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` only with `Custom`) |
| `RunningTotalIn` | Displays the value as a running total for successive items of a base field. | `baseField` (the field whose item order drives the accumulation) |
| `PercentageOfRow` | Displays the value as a percentage of the row total. | — |
| `PercentageOfColumn` | Displays the value as a percentage of the column total. | — |
| `PercentageOfTotal` | Displays the value as a percentage of the grand total. | — |
| `Index` | Displays the value using the Excel index formula ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Displays the value as a percentage of its parent row total (for nested row fields). | — |
| `PercentageOfParentColumnTotal` | Displays the value as a percentage of its parent column total (for nested column fields). | — |
| `PercentageOfParentTotal` | Displays the value as a percentage of its parent total. | `baseField` (the parent field whose total is the reference) |
| `PercentageOfRunningTotalIn` | Displays the value as a percentage of a running total in a base field. | `baseField` (the accumulation field) |
| `RankSmallestToLargest` | Ranks the value from smallest (1) to largest. | — |
| `RankLargestToSmallest` | Ranks the value from largest (1) to smallest. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` writes the `PivotShowValuesSetting` values (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — the method and the settings object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.ShowValuesAs` method with `PivotFieldDataDisplayFormat.PercentageOfTotal` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `PivotItemPositionType.Previous`, `0`) are placeholders the format ignores, as the parameter table above notes.

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

## **Get and Configure PivotField.ShowValuesSetting**
Read the current configuration through `PivotField.GetShowValuesSetting()`: the accessor returns the field’s `PivotShowValuesSetting` object, whose four getter methods describe the active Show Values As calculation. To change the configuration, call the `PivotField.ShowValuesAs` method — it writes all four settings in one call, so you never need to set the values one by one.
The `PivotShowValuesSetting` object exposes the four values `ShowValuesAs` writes:
- `GetCalculationType()` / `SetCalculationType()` select the `PivotFieldDataDisplayFormat` secondary calculation.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` specify the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` determine how the base item is positioned relative to the current item and accept `PivotItemPositionType.Next`, `PivotItemPositionType.Previous`, or `PivotItemPositionType.Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` specify the zero-based base item index and are used when the position type is `Custom`.
After calling `ShowValuesAs`, call `PivotTable.CalculateData()` again so the pivot body is recalculated and rerendered with the updated configuration.

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

## **Related Articles**
- [Group Pivot Fields in the Pivot Table](/cells/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [Top 10 Show or Filter in Pivot Table](/cells/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Updating Slicer](/cells/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}