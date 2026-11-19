---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for Python via .NET.
linktitle: Show Values As
keywords: Aspose.Cells, pivot table, show values as, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `SUM` or `COUNT`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for Python via .NET, the `PivotShowValuesAsType` enumeration selects the secondary calculation. The read-only `PivotField.show_values_setting` property returns a `PivotShowValuesSetting` object, whose writable `show_values_as`, `base_field_index`, and `base_item_index` properties configure the behavior; the convenience method `PivotField.show_values_as(...)` applies the same settings in one call. Apply these settings to a data or value field obtained from `PivotTable.data_fields`.

## **PivotShowValuesAsType Enumeration Members**
The data field keeps its aggregate function, such as `SUM` or `COUNT`, while Show Values As transforms only how the aggregated value is displayed.
Besides writing the `PivotShowValuesSetting` properties directly (see the last section), a one-call convenience method applies the same configuration. It comes in two forms — one addressing the base field and base item by index, one by name:

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `show_values_as_type` | The `PivotShowValuesAsType` secondary calculation to apply. | Always. |
| `base_field` | Zero-based index of the base field among the pivot table's base fields (for example, the index of the row field the base item belongs to), or — in the name form — the name of the base field. | The eight base-relative formats below (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); pass `0` (or `None` in the name form) for every other format. |
| `base_item` | Zero-based index of the base item, with two sentinels: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) selects the preceding item and `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) the succeeding one. The name form takes the caption of the base item instead, and `None` when the selected format needs no base item. | Only the three base-item formats (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) evaluate the base item; the five field-relative formats (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, both ranks) ignore it — pass `0` or `None`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `NORMAL` | No secondary calculation; the aggregated value is displayed as is (default). | — |
| `DIFFERENCE_FROM` | Displays the value as a difference from the value of a base item in a base field. | `base_field` + `base_item` (an index or caption, or the previous/next sentinel) |
| `PERCENTAGE_OF` | Displays the value as a percentage of the value of a base item in a base field. | `base_field` + `base_item` (an index or caption, or the previous/next sentinel) |
| `PERCENTAGE_DIFFERENCE_FROM` | Displays the value as the percentage difference from the value of a base item in a base field. | `base_field` + `base_item` (an index or caption, or the previous/next sentinel) |
| `RUNNING_TOTAL_IN` | Displays the value as a running total for successive items of a base field. | `base_field` (the field whose item order drives the accumulation) |
| `PERCENTAGE_OF_ROW` | Displays the value as a percentage of the row total. | — |
| `PERCENTAGE_OF_COLUMN` | Displays the value as a percentage of the column total. | — |
| `PERCENTAGE_OF_TOTAL` | Displays the value as a percentage of the grand total. | — |
| `INDEX` | Displays the value using the Excel index formula ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Displays the value as a percentage of its parent row total (for nested row fields). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Displays the value as a percentage of its parent column total (for nested column fields). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Displays the value as a percentage of its parent total. | `base_field` (the parent field whose total is the reference) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Displays the value as a percentage of a running total in a base field. | `base_field` (the accumulation field) |
| `RANK_SMALLEST_TO_LARGEST` | Ranks the value from smallest (1) to largest. | `base_field` (the field whose items define the ranking scope) |
| `RANK_LARGEST_TO_SMALLEST` | Ranks the value from largest (1) to smallest. | `base_field` (the field whose items define the ranking scope) |

{{% alert color="primary" %}}
`show_values_as(...)` writes the `PivotShowValuesSetting` properties (`show_values_as`, `base_field_index`, `base_item_index`) — the method and the property object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.show_values_as` method with `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `0`) are placeholders the format ignores, as the parameter table above notes.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
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
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Get and Configure PivotField.show_values_setting**
Read the current configuration through `PivotField.show_values_setting`: the read-only property returns the field’s `PivotShowValuesSetting` object, whose properties describe the active Show Values As calculation. To change the configuration, call the `PivotField.show_values_as` method — it writes all settings in one call, so you never need to assign the properties one by one.
The `PivotShowValuesSetting` object exposes the state `show_values_as` writes:
- `show_values_as` selects the `PivotShowValuesAsType` secondary calculation.
- `base_field_index` specifies the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `base_item_index` specifies the base item: a zero-based index of a specific pivot item, or one of the two sentinels — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) for the preceding item, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) for the succeeding one. It is used by the base-item formats.
- `base_field_name` and `base_item_caption` are read-only views that report the resolved base field name and base item caption; for example, after selecting the previous-item sentinel, `base_item_caption` reads `(previous)`.
After calling `show_values_as`, call `PivotTable.calculate_data()` again so the pivot body is recalculated and rerendered with the updated configuration.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/python-net/manage-value-fields/)
- [Refreshing Pivot Table](/cells/python-net/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}