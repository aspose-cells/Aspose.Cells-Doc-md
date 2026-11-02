---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for Python via .NET.
linktitle: Show Values As
keywords: Aspose.Cells for Python via .NET, pivot table, show values as, data display format, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `SUM` or `COUNT`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for Python via .NET, `PivotFieldDataDisplayFormat` selects the secondary calculation. The read-only `PivotField.show_values_setting` property returns a `PivotShowValuesSetting` object, whose writable `calculation_type`, `base_field_index`, `base_item_position_type`, and `base_item_index` properties configure the behavior; the convenience method `PivotField.show_values_as(...)` applies the same four settings in one call. Apply these settings to a data or value field obtained from `PivotTable.data_fields`.

## **PivotFieldDataDisplayFormat Enumeration Members**
The data field keeps its aggregate function, such as `SUM` or `COUNT`, while Show Values As transforms only how the aggregated value is displayed.
Besides writing the `PivotShowValuesSetting` properties directly (see the last section), a one-call convenience method applies the same configuration:

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `display_format` | The `PivotFieldDataDisplayFormat` secondary calculation to apply. | Always. |
| `base_field` | Zero-based index of the base field among the pivot table's base fields (for example, the index of the row field the base item belongs to). | Only the six base-relative formats below (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignored by every other format. |
| `base_item_position_type` | How the base item is chosen relative to the current item: `PivotItemPositionType.PREVIOUS`, `.NEXT`, or `.CUSTOM`. | Only the three base-item formats (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignored by every other format. |
| `base_item` | Zero-based index of the base item. | Only when `base_item_position_type` is `CUSTOM` (the item index picks the exact base item); ignored for `PREVIOUS` / `NEXT` and by every non-base format — pass `0`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `NORMAL` | No secondary calculation; the aggregated value is displayed as is (default). | — |
| `DIFFERENCE_FROM` | Displays the value as a difference from the value of a base item in a base field. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` only with `CUSTOM`) |
| `PERCENTAGE_OF` | Displays the value as a percentage of the value of a base item in a base field. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` only with `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Displays the value as the percentage difference from the value of a base item in a base field. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` only with `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Displays the value as a running total for successive items of a base field. | `base_field` (the field whose item order drives the accumulation) |
| `PERCENTAGE_OF_ROW` | Displays the value as a percentage of the row total. | — |
| `PERCENTAGE_OF_COLUMN` | Displays the value as a percentage of the column total. | — |
| `PERCENTAGE_OF_TOTAL` | Displays the value as a percentage of the grand total. | — |
| `INDEX` | Displays the value using the Excel index formula ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Displays the value as a percentage of its parent row total (for nested row fields). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Displays the value as a percentage of its parent column total (for nested column fields). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Displays the value as a percentage of its parent total. | `baseField` (the parent field whose total is the reference) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Displays the value as a percentage of a running total in a base field. | `base_field` (the accumulation field) |
| `RANK_SMALLEST_TO_LARGEST` | Ranks the value from smallest (1) to largest. | — |
| `RANK_LARGEST_TO_SMALLEST` | Ranks the value from largest (1) to smallest. | — |

{{% alert color="primary" %}}
`show_values_as(...)` writes the `PivotShowValuesSetting` properties (`calculation_type`, `base_field_index`, `base_item_position_type`, `base_item_index`) — the method and the property object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.show_values_as` method with `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `PivotItemPositionType.PREVIOUS`, `0`) are placeholders the format ignores, as the parameter table above notes.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Get and Configure PivotField.show_values_setting**
Read the current configuration through `PivotField.show_values_setting`: the read-only property returns the field’s `PivotShowValuesSetting` object, whose four properties describe the active Show Values As calculation. To change the configuration, call the `PivotField.show_values_as` method — it writes all four settings in one call, so you never need to assign the properties one by one.
The `PivotShowValuesSetting` object exposes the four properties `show_values_as` writes:
- `calculation_type` selects the `PivotFieldDataDisplayFormat` secondary calculation.
- `base_field_index` specifies the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `base_item_position_type` determines how the base item is positioned relative to the current item and accepts `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS`, or `PivotItemPositionType.CUSTOM`.
- `base_item_index` specifies the zero-based base item index and is used when `base_item_position_type` is `CUSTOM`.
After calling `show_values_as`, call `PivotTable.calculate_data()` again so the pivot body is recalculated and rerendered with the updated configuration.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/python-net/manage-value-fields/)
- [Refreshing Pivot Table](/cells/python-net/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}