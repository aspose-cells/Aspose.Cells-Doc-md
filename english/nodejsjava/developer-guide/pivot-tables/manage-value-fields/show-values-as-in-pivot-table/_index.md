---
title: Show Values As in Pivot Table
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for Node.js via Java.
linktitle: Show Values As
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, pivot table, show values as, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `SUM` or `COUNT`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for Node.js via Java, the `PivotShowValuesAsType` enumeration selects the secondary calculation. The read-only `PivotField.getShowValuesSetting()` method returns a `PivotShowValuesSetting` object, whose `setShowValuesAs()`, `setBaseFieldIndex()`, and `setBaseItemIndex()` methods configure the behavior; the convenience method `PivotField.showValuesAs(...)` applies the same settings in one call. Apply these settings to a data or value field obtained from `PivotTable.getDataFields()`.

## **PivotShowValuesAsType Enumeration Members**
The data field keeps its aggregate function, such as SUM or COUNT, while Show Values As transforms only how the aggregated value is displayed.
Besides using the `PivotShowValuesSetting` setters directly (see the last section), a one-call convenience method applies the same configuration. It comes in two forms — one addressing the base field and base item by index, one by name:

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

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `showValuesAsType` | The `PivotShowValuesAsType` secondary calculation to apply. | Always. |
| `baseField` | Zero-based index of the base field among the pivot table's base fields (for example, the index of the row field the base item belongs to), or — in the name form — the name of the base field. | The eight base-relative formats below (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); pass `0` (or `null` in the name form) for every other format. |
| `baseItem` | Zero-based index of the base item, with two sentinels: -1 selects the preceding item and -2 the succeeding one (the package root does not export the `PivotShowValuesSetting` constants — pass the literal values). The name form takes the caption of the base item instead, and `null` when the selected format needs no base item. | Only the three base-item formats (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) evaluate the base item; the five field-relative formats (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, both ranks) ignore it — pass `0` or `null`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `NORMAL` | No secondary calculation; the aggregated value is displayed as is (default). | — |
| `DIFFERENCE_FROM` | Displays the value as a difference from the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `PERCENTAGE_OF` | Displays the value as a percentage of the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `PERCENTAGE_DIFFERENCE_FROM` | Displays the value as the percentage difference from the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `RUNNING_TOTAL_IN` | Displays the value as a running total for successive items of a base field. | `baseField` (the field whose item order drives the accumulation) |
| `PERCENTAGE_OF_ROW` | Displays the value as a percentage of the row total. | — |
| `PERCENTAGE_OF_COLUMN` | Displays the value as a percentage of the column total. | — |
| `PERCENTAGE_OF_TOTAL` | Displays the value as a percentage of the grand total. | — |
| `INDEX` | Displays the value using the Excel index formula ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Displays the value as a percentage of its parent row total (for nested row fields). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Displays the value as a percentage of its parent column total (for nested column fields). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Displays the value as a percentage of its parent total. | `baseField` (the parent field whose total is the reference) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Displays the value as a percentage of a running total in a base field. | `baseField` (the accumulation field) |
| `RANK_SMALLEST_TO_LARGEST` | Ranks the value from smallest (1) to largest. | `baseField` (the field whose items define the ranking scope) |
| `RANK_LARGEST_TO_SMALLEST` | Ranks the value from largest (1) to smallest. | `baseField` (the field whose items define the ranking scope) |

{{% alert color="primary" %}}
`showValuesAs(...)` writes the `PivotShowValuesSetting` state through `setShowValuesAs()`, `setBaseFieldIndex()`, and `setBaseItemIndex()` — the method and the property object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.showValuesAs()` method with `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `0`) are placeholders the format ignores, as the parameter table above notes.

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

## **Get and Configure PivotField.getShowValuesSetting()**
Read the current configuration through `PivotField.getShowValuesSetting()`: the read-only method returns the field’s `PivotShowValuesSetting` object, whose settings describe the active Show Values As calculation. To change the configuration, call the `PivotField.showValuesAs()` method — it writes all settings in one call, so you never need to set them one by one.
The `PivotShowValuesSetting` object exposes the state `showValuesAs()` writes:
- `getShowValuesAs()` / `setShowValuesAs()` selects the `PivotShowValuesAsType` secondary calculation.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` specifies the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `getBaseItemIndex()` / `setBaseItemIndex()` specifies the base item: a zero-based index of a specific pivot item, or one of the two sentinel values — -1 for the preceding item, -2 for the succeeding one (the package root does not export the named constants). It is used by the base-item formats.
- `getBaseFieldName()` and `getBaseItemCaption()` are read-only views that report the resolved base field name and base item caption; for example, after selecting the previous-item sentinel, `getBaseItemCaption()` returns `(previous)`.
After calling `showValuesAs()`, call `PivotTable.calculateData()` again so the pivot body is recalculated and rerendered with the updated configuration.

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

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/nodejs-java/manage-value-fields/)
- [Refreshing Pivot Table](/cells/nodejs-java/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}