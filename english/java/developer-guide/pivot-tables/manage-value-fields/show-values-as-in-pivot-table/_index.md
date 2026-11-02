---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for Java.
linktitle: Show Values As
keywords: Aspose.Cells, pivot table, show values as, data display format, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `Sum` or `Count`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for Java, `PivotFieldDataDisplayFormat` selects the secondary calculation. The read-only `PivotField.getShowValuesSetting()` getter returns a `PivotShowValuesSetting` object, whose `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)`, and `setBaseItemIndex(...)` methods configure the behavior; the convenience method `PivotField.showValuesAs(...)` applies the same four settings in one call. Apply these settings to a data or value field obtained from `PivotTable.getDataFields()`.

## **PivotFieldDataDisplayFormat Enumeration Members**
The data field keeps its aggregate function, such as Sum or Count, while Show Values As transforms only how the aggregated value is displayed.
Besides using the `PivotShowValuesSetting` setters directly (see the last section), a one-call convenience method applies the same configuration:

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `displayFormat` | The `PivotFieldDataDisplayFormat` secondary calculation to apply. | Always. |
| `baseField` | Zero-based index of the base field among the pivot table's base fields (for example, the index of the row field the base item belongs to). | Only the six base-relative formats below (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignored by every other format. |
| `baseItemPositionType` | How the base item is chosen relative to the current item: `PivotItemPositionType.PREVIOUS`, `NEXT`, or `CUSTOM`. | Only the three base-item formats (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignored by every other format. |
| `baseItem` | Zero-based index of the base item. | Only when `baseItemPositionType` is `CUSTOM` (the item index picks the exact base item); ignored for `PREVIOUS` / `NEXT` and by every non-base format — pass `0`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `NORMAL` | No secondary calculation; the aggregated value is displayed as is (default). | — |
| `DIFFERENCE_FROM` | Displays the value as a difference from the value of a base item in a base field. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` only with `CUSTOM`) |
| `PERCENTAGE_OF` | Displays the value as a percentage of the value of a base item in a base field. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` only with `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Displays the value as the percentage difference from the value of a base item in a base field. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` only with `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Displays the value as a running total for successive items of a base field. | `baseField` (the field whose item order drives the accumulation) |
| `PERCENTAGE_OF_ROW` | Displays the value as a percentage of the row total. | — |
| `PERCENTAGE_OF_COLUMN` | Displays the value as a percentage of the column total. | — |
| `PERCENTAGE_OF_TOTAL` | Displays the value as a percentage of the grand total. | — |
| `INDEX` | Displays the value using the Excel index formula ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Displays the value as a percentage of its parent row total (for nested row fields). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Displays the value as a percentage of its parent column total (for nested column fields). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Displays the value as a percentage of its parent total. | `baseField` (the parent field whose total is the reference) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Displays the value as a percentage of a running total in a base field. | `baseField` (the accumulation field) |
| `RANK_SMALLEST_TO_LARGEST` | Ranks the value from smallest (1) to largest. | — |
| `RANK_LARGEST_TO_SMALLEST` | Ranks the value from largest (1) to smallest. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` sets exactly the four `PivotShowValuesSetting` values through `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)`, and `setBaseItemIndex(...)` — the method and the property object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.showValuesAs(...)` method with `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `PivotItemPositionType.PREVIOUS`, `0`) are placeholders the format ignores, as the parameter table above notes.

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Get and Configure PivotField.getShowValuesSetting**
Read the current configuration through `PivotField.getShowValuesSetting()`: the read-only getter returns the field’s `PivotShowValuesSetting` object, whose four properties describe the active Show Values As calculation. To change the configuration, call the `PivotField.showValuesAs(...)` method — it writes all four settings in one call, so you never need to set the properties one by one.
The `PivotShowValuesSetting` object exposes the four properties `showValuesAs(...)` writes:
- `getCalculationType()` / `setCalculationType(...)` selects the `PivotFieldDataDisplayFormat` secondary calculation.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` specifies the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` determines how the base item is positioned relative to the current item and accepts `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS`, or `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` specifies the zero-based base item index and is used when `BaseItemPositionType` is `CUSTOM`.
After calling `showValuesAs(...)`, call `PivotTable.calculateData()` again so the pivot body is recalculated and rerendered with the updated configuration.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/java/manage-value-fields/)
- [Refreshing Pivot Table](/cells/java/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}