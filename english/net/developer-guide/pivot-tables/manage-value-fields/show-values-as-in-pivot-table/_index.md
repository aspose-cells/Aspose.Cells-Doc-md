---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for .NET.
linktitle: Show Values As
keywords: Aspose.Cells, pivot table, show values as, data display format, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `Sum` or `Count`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for .NET, `PivotFieldDataDisplayFormat` selects the secondary calculation. The read-only `PivotField.ShowValuesSetting` property returns a `PivotShowValuesSetting` object, whose writable `CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, and `BaseItemIndex` properties configure the behavior; the convenience method `PivotField.ShowValuesAs(...)` applies the same four settings in one call. Apply these settings to a data or value field obtained from `PivotTable.DataFields`.

## **PivotFieldDataDisplayFormat Enumeration Members**
The data field keeps its aggregate function, such as Sum or Count, while Show Values As transforms only how the aggregated value is displayed.
Besides writing the `PivotShowValuesSetting` properties directly (see the last section), a one-call convenience method applies the same configuration:

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
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
`ShowValuesAs(...)` writes the `PivotShowValuesSetting` properties (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — the method and the property object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.ShowValuesAs` method with `PivotFieldDataDisplayFormat.PercentageOfTotal` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `PivotItemPositionType.Previous`, `0`) are placeholders the format ignores, as the parameter table above notes.

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

## **Get and Configure PivotField.ShowValuesSetting**
Read the current configuration through `PivotField.ShowValuesSetting`: the read-only property returns the field’s `PivotShowValuesSetting` object, whose four properties describe the active Show Values As calculation. To change the configuration, call the `PivotField.ShowValuesAs` method — it writes all four settings in one call, so you never need to assign the properties one by one.
The `PivotShowValuesSetting` object exposes the four properties `ShowValuesAs` writes:
- `CalculationType` selects the `PivotFieldDataDisplayFormat` secondary calculation.
- `BaseFieldIndex` specifies the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `BaseItemPositionType` determines how the base item is positioned relative to the current item and accepts `PivotItemPositionType.Next`, `PivotItemPositionType.Previous`, or `PivotItemPositionType.Custom`.
- `BaseItemIndex` specifies the zero-based base item index and is used when `BaseItemPositionType` is `Custom`.
After calling `ShowValuesAs`, call `PivotTable.CalculateData()` again so the pivot body is recalculated and rerendered with the updated configuration.

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

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/net/manage-value-fields/)
- [Working with Data Display Formats of DataField in Pivot Table](/cells/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Refreshing Pivot Table](/cells/net/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}