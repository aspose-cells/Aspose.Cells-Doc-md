---
title: Show Values As in Pivot Table in Aspose.Cells for C++
description: Display pivot table data field values as a percentage of the total, a difference from a base item, running totals, ranks, and more with Aspose.Cells for C++.
linktitle: Show Values As
keywords: Aspose.Cells, C++, pivot table, show values as, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table normally aggregates each data field with an aggregate function such as `Sum` or `Count`. Excel’s **Show Values As** feature replaces each displayed result with a secondary calculation derived from that aggregate—for example, a percentage of the grand total, a running total, a difference from a chosen base item, or a rank—so you can perform comparative analysis without helper formulas or calculated columns.
Typical uses include share-of-total analysis, including percentages of a row, column, or grand total; cumulative reporting using a running total in a period field; variance analysis against a benchmark item using difference from or percentage difference from a base item; and ranking values from smallest to largest or largest to smallest.
In Aspose.Cells for C++, the `PivotShowValuesAsType` enumeration selects the secondary calculation. The `PivotField.GetShowValuesSetting()` accessor returns a `PivotShowValuesSetting` object, whose `SetShowValuesAs`, `SetBaseFieldIndex`, and `SetBaseItemIndex` methods configure the behavior; the convenience method `PivotField.ShowValuesAs(...)` applies the same settings in one call. Apply these settings to a data or value field obtained from `PivotTable.GetDataFields()`.

## **PivotShowValuesAsType Enumeration Members**
The data field keeps its aggregate function, such as Sum or Count, while Show Values As transforms only how the aggregated value is displayed.
Besides writing the `PivotShowValuesSetting` values directly (see the last section), a one-call convenience method applies the same configuration. It comes in two forms — one addressing the base field and base item by index, one by name:

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| Parameter | Meaning | When It Is Required |
| --- | --- | --- |
| `showValuesAsType` | The `PivotShowValuesAsType` secondary calculation to apply. | Always. |
| `baseField` | Zero-based index of the base field among the pivot table's base fields (for example, the index of the row field the base item belongs to), or — in the name form — the name of the base field. | The eight base-relative formats below (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); pass `0` (or an empty `U16String` in the name form) for every other format. |
| `baseItem` | Zero-based index of the base item, with two sentinel values: -1 selects the preceding item and -2 the succeeding one (the C++ API defines no named constants for the sentinels — pass the literal values). The name form takes the caption of the base item instead, and an empty `U16String` when the selected format needs no base item. | Only the three base-item formats (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) evaluate the base item; the five field-relative formats (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, both ranks) ignore it — pass `0` or an empty `U16String`. |

| Calculation Type | Behavior | Base Item Parameters |
| --- | --- | --- |
| `Normal` | No secondary calculation; the aggregated value is displayed as is (default). | — |
| `DifferenceFrom` | Displays the value as a difference from the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `PercentageOf` | Displays the value as a percentage of the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `PercentageDifferenceFrom` | Displays the value as the percentage difference from the value of a base item in a base field. | `baseField` + `baseItem` (an index or caption, or the previous/next sentinel) |
| `RunningTotalIn` | Displays the value as a running total for successive items of a base field. | `baseField` (the field whose item order drives the accumulation) |
| `PercentageOfRow` | Displays the value as a percentage of the row total. | — |
| `PercentageOfColumn` | Displays the value as a percentage of the column total. | — |
| `PercentageOfTotal` | Displays the value as a percentage of the grand total. | — |
| `Index` | Displays the value using the Excel index formula ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Displays the value as a percentage of its parent row total (for nested row fields). | — |
| `PercentageOfParentColumnTotal` | Displays the value as a percentage of its parent column total (for nested column fields). | — |
| `PercentageOfParentTotal` | Displays the value as a percentage of its parent total. | `baseField` (the parent field whose total is the reference) |
| `PercentageOfRunningTotalIn` | Displays the value as a percentage of a running total in a base field. | `baseField` (the accumulation field) |
| `RankSmallestToLargest` | Ranks the value from smallest (1) to largest. | `baseField` (the field whose items define the ranking scope) |
| `RankLargestToSmallest` | Ranks the value from largest (1) to smallest. | `baseField` (the field whose items define the ranking scope) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` writes the `PivotShowValuesSetting` values (`ShowValuesAs`, `BaseFieldIndex`, and `BaseItemIndex`) — the method and the settings object are two ways to configure the same state, mirroring the base field and base item pickers in Excel's Show Values As dialog.
{{% /alert %}}

## **Show Values as Percentage of Total**
Call the `PivotField.ShowValuesAs` method with `PivotShowValuesAsType::PercentageOfTotal` to convert every data-field cell, including the grand total, into its share of the grand total. The displayed numbers therefore read as proportions of the complete result set. This format measures every value against the grand total only, so it needs no base field or base item — the trailing arguments (`0`, `0`) are placeholders the format ignores, as the parameter table above notes.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Get and Configure PivotField.ShowValuesSetting**
Read the current configuration through `PivotField.GetShowValuesSetting()`: the accessor returns the field’s `PivotShowValuesSetting` object, whose getter methods describe the active Show Values As calculation. To change the configuration, call the `PivotField.ShowValuesAs` method — it writes all settings in one call, so you never need to set the values one by one.
The `PivotShowValuesSetting` object exposes the state `ShowValuesAs` writes:
- `GetShowValuesAs()` / `SetShowValuesAs()` select the `PivotShowValuesAsType` secondary calculation.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` specify the zero-based index of the base field within the pivot fields. It is used by the base-relative formats.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` specify the base item: a zero-based index of a specific pivot item, or one of the two sentinel values — -1 for the preceding item, -2 for the succeeding one (the C++ API defines no named constants for the sentinels). It is used by the base-item formats.
- `GetBaseFieldName()` and `GetBaseItemCaption()` are read-only views that report the resolved base field name and base item caption; for example, after selecting the previous-item sentinel, `GetBaseItemCaption()` returns `(previous)`.
After calling `ShowValuesAs`, call `PivotTable.CalculateData()` again so the pivot body is recalculated and rerendered with the updated configuration.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Related Articles**
- [Managing Value Fields in Pivot Table](/cells/cpp/manage-value-fields/)
- [Refreshing Pivot Table](/cells/cpp/refresh-pivot-table/)
- [Applying Style to Pivot Table](/cells/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}