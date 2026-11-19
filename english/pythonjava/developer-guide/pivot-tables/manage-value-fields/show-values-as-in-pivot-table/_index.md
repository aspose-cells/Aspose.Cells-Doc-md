---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for Python via Java.
linktitle: Show Values As
keywords: Aspose.Cells, pivot table, show values as, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `SUM` or `COUNT`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for Python via Java, the `PivotShowValuesAsType` enumeration selects the secondary calculation. The read-only `PivotField.getShowValuesSetting()` method returns a `PivotShowValuesSetting` object, whose `setShowValuesAs(...)`, `setBaseFieldIndex(...)`, and `setBaseItemIndex(...)` methods configure the behavior; the convenience method `PivotField.showValuesAs(...)` applies the same settings in one call. Apply these settings to a data or value field obtained from `PivotTable.getDataFields()`.

## **PivotShowValuesAsType Enumeration Members**
The data field keeps its aggregate function, such as `SUM` or `COUNT`, while Show Values As transforms only how the aggregated value is displayed.
Besides using the `PivotShowValuesSetting` setters directly (see the last section), a one-call convenience method applies the same configuration. It comes in two forms — one addressing the base field and base item by index, one by name:

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
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
`showValuesAs(...)` writes the `PivotShowValuesSetting` values through `setShowValuesAs`, `setBaseFieldIndex`, and `setBaseItemIndex` — the method and the setting object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.showValuesAs` method with `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `0`) are placeholders the format ignores, as the parameter table above notes.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Get and Configure PivotField.getShowValuesSetting()**
Read the current configuration through `PivotField.getShowValuesSetting()`: the read-only method returns the field’s `PivotShowValuesSetting` object, whose properties describe the active Show Values As calculation. To change the configuration, call the `PivotField.showValuesAs` method — it writes all settings in one call, so you never need to set the properties one by one.
The `PivotShowValuesSetting` object exposes the state that `showValuesAs` writes:
- `getShowValuesAs()` returns the `PivotShowValuesAsType` secondary calculation, while `setShowValuesAs(...)` changes it.
- `getBaseFieldIndex()` and `setBaseFieldIndex(...)` specify the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `getBaseItemIndex()` and `setBaseItemIndex(...)` specify the base item: a zero-based index of a specific pivot item, or one of the two sentinels — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) for the preceding item, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) for the succeeding one. It is used by the base-item formats.
- `getBaseFieldName()` and `getBaseItemCaption()` are read-only views that report the resolved base field name and base item caption; for example, after selecting the previous-item sentinel, `getBaseItemCaption()` returns `(previous)`.
After calling `showValuesAs`, call `PivotTable.calculateData()` again so the pivot body is recalculated and rerendered with the updated configuration.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/python-java/manage-value-fields/)
- [Refreshing Pivot Table](/cells/python-java/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}