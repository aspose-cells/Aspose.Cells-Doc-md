---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for Python via Java.
linktitle: Show Values As
keywords: Aspose.Cells, pivot table, show values as, data display format, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `Sum` or `Count`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for Python via Java, `PivotFieldDataDisplayFormat` selects the secondary calculation. The read-only `PivotField.getShowValuesSetting()` method returns a `PivotShowValuesSetting` object, whose writable `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType`, and `setBaseItemIndex` methods configure the behavior; the convenience method `PivotField.showValuesAs(...)` applies the same four settings in one call. Apply these settings to a data or value field obtained from `PivotTable.getDataFields()`.

## **PivotFieldDataDisplayFormat Enumeration Members**
The data field keeps its aggregate function, such as Sum or Count, while Show Values As transforms only how the aggregated value is displayed.
Besides setting the `PivotShowValuesSetting` properties directly (see the last section), a one-call convenience method applies the same configuration:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
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
`showValuesAs(...)` writes the `PivotShowValuesSetting` values through `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType`, and `setBaseItemIndex` — the method and the setting object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.showValuesAs` method with `PivotFieldDataDisplayFormat.PercentageOfTotal` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `PivotItemPositionType.Previous`, `0`) are placeholders the format ignores, as the parameter table above notes.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
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
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Get and Configure PivotField.getShowValuesSetting()**
Read the current configuration through `PivotField.getShowValuesSetting()`: the read-only method returns the field’s `PivotShowValuesSetting` object, whose four properties describe the active Show Values As calculation. To change the configuration, call the `PivotField.showValuesAs` method — it writes all four settings in one call, so you never need to assign the properties one by one.
The `PivotShowValuesSetting` object exposes the four properties that `showValuesAs` writes:
- `getCalculationType()` returns the `PivotFieldDataDisplayFormat` secondary calculation, while `setCalculationType(...)` changes it.
- `getBaseFieldIndex()` and `setBaseFieldIndex(...)` specify the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `getBaseItemPositionType()` and `setBaseItemPositionType(...)` determine how the base item is positioned relative to the current item and accept `PivotItemPositionType.Next`, `PivotItemPositionType.Previous`, or `PivotItemPositionType.Custom`.
- `getBaseItemIndex()` and `setBaseItemIndex(...)` specify the zero-based base item index and are used when `BaseItemPositionType` is `Custom`.
After calling `showValuesAs`, call `PivotTable.calculateData()` again so the pivot body is recalculated and rerendered with the updated configuration.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/python-java/manage-value-fields/)
- [Refreshing Pivot Table](/cells/python-java/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}