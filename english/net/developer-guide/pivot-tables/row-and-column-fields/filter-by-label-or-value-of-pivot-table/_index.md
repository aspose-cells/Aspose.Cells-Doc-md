---
title: Filtering Pivot Tables by Label or Value
linktitle: Filtering by Label or Value
description: Aspose.Cells for .NET supports comprehensive pivot table filtering capabilities. This article explains how to filter pivot table data using label filters, date filters, value filters, top 10 filters, and by hiding or unhiding pivot items.
keywords: Aspose.Cells, .NET library, spreadsheet, pivot table, filter, label filter, value filter, date filter, top 10 filter, pivot item, hide pivot item
type: docs
weight: 10
url: /net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides five practical strategies for filtering the data displayed in a pivot table. You can apply label filters to text-based row or column fields, use date filters when the field contains only date-time cells or blanks, apply value filters against aggregated numbers, use top 10 filters to rank by a value field, or manually hide and unhide individual pivot items using the `IsHidden` property. Each strategy is exposed through dedicated APIs on the `PivotField` and `PivotItem` classes.

{{% /alert %}}

## **Introduction**

Pivot tables are powerful analytical tools, but raw summaries often contain far more information than you need to present. Filtering is the primary mechanism for narrowing a pivot table down to the rows, columns, or values that matter for a specific report. Aspose.Cells for .NET mirrors the filtering capabilities that are available in Microsoft Excel, exposing them programmatically so that report generation can be fully automated.

The following filtering strategies are covered in this article:

1. **Label Filter** — filters row or column field items based on their text labels.
2. **Date Filter** — filters row or column fields that contain only date-time values (or blanks).
3. **Value Filter** — filters items based on the aggregated values of a data field.
4. **Top 10 Filter** — shows only the top or bottom N items ranked by a value field.
5. **Hide / Unhide Pivot Items** — manually controls the visibility of each individual item in a field.

Each approach uses a different method on the `PivotField` class or a property on the `PivotItem` class. After applying any filter, you must call `PivotCache.Refresh()` on the pivot table so that the cached data and calculated values reflect the new filter state.

## **Label Filter**

A label filter allows you to filter the items of a row or column field by comparing their text captions against a pattern. This is useful when you want to display only products whose names start with a specific letter, contain a particular word, or match some other caption-based criterion.

Aspose.Cells exposes label filtering through the `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)` method. The `filterType` argument selects the comparison mode (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, and so on). The `label1` and `label2` arguments supply the comparison text — pass `string.Empty` for `label2` when you only need a single-value match (e.g. starts-with or contains).

The following example loads a workbook containing an existing pivot table, applies a label filter so that only items whose captions begin with a specified prefix remain visible, refreshes the pivot table, and saves the result.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string fileName = "sample.xlsx";
string prefix = "B";

// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);

// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.Worksheets[0];

// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];

// Retrieve the first row PivotField
PivotField rowField = pivotTable.RowFields[0];

// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);

// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.PivotCache.Refresh();

// Save the workbook back to disk
workbook.Save(fileName);
```

## **Date Filter**

Date filters let you narrow a pivot table by date-based criteria such as today, last week, this month, next quarter, or a specific date range. They are specialized filters that work only against fields that store date-time information.

{{% alert color="primary" %}}

The date filter only works when the row or column area contains only date-time cells or blank values. If the underlying field contains other data types such as numbers or text, the date filter will not produce the expected result. Make sure the field is formatted as a date and that all values are valid `DateTime` instances or empty cells before applying this filter.

{{% /alert %}}

Aspose.Cells exposes date filtering through the `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)` method. The `PivotFilterType` enumeration contains dedicated date values such as `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, and `Between`. Depending on the chosen filter type, you pass one or two `DateTime` values (for `Between`, you pass the start and end dates).

The following example loads a workbook with a pivot table whose row area contains a date field, applies a date filter that restricts the visible items to a particular date range, refreshes the pivot table, and saves the workbook.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";

if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}

// Load the existing workbook that contains the pivot table
var workbook = new Workbook(inputPath);

// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.Worksheets[0];

// Access the pivot table by index
var pivotTable = worksheet.PivotTables[0];

// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.RowFields[0];

// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Apply the date filter on the pivot field
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);

// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.PivotCache.Refresh();

// Persist the workbook
workbook.Save(outputPath);
```

## **Value Filter**

Value filters operate on the aggregated values that a pivot table calculates in its data area. Instead of matching text labels, they compare numeric totals against a threshold. Typical use cases include showing only products whose sum of sales exceeds a target amount or only regions whose count of transactions falls within a range.

Aspose.Cells exposes value filtering through the `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` method. The `valueFieldIndex` parameter specifies which data field should be evaluated (use `pivotTable.DataFields.IndexOf(dataField)` or iterate the collection to find the position). The `filterType` parameter uses values such as `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, and `ValueLessThanOrEqual`. The two `double` arguments supply the threshold value(s).

The following example loads a workbook with a pivot table, applies a value filter that keeps only items whose aggregated sales exceed a numeric threshold, refreshes the pivot table, and saves the workbook.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];

var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];

// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}

pivotTable.PivotCache.Refresh();

workbook.Save("output.xlsx");
```

## **Top 10 Filter**

The top 10 filter is a specialized form of value filter that retains only the highest or lowest N items based on a chosen value field. It is commonly used for ranking reports such as "top 10 products by revenue" or "bottom 5 regions by sales count".

{{% alert color="primary" %}}

The top 10 filter is only effective when the pivot table has one or more value pivot fields in the data area. Without at least one value field, there is no aggregated measure to rank the items against, and the filter cannot be applied.

{{% /alert %}}

Aspose.Cells exposes top 10 filtering through the `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)` method. The `itemCount` parameter defines how many items to retain, `filterType` controls how the value is computed (typically `Sum`, but also `Count` and `Percent`), `isTop` indicates whether to keep the top items (true) or the bottom items (false), and `valueFieldIndex` is the index of the data field used to rank items.

The following example loads a workbook with a pivot table that contains a value field, applies a top 10 filter to keep only the highest 10 items by the sum of sales, refreshes the pivot table, and saves the workbook.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Load the existing workbook that contains the pivot table
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.Worksheets[0];

// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];

// Confirm there is at least one value PivotField in the data area
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];

// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.RowFields[0];

// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;

// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);

// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.PivotCache.Refresh();

// Save the workbook
workbook.Save(outputPath);
```

## **Filter by Hiding or Unhiding Pivot Items**

In addition to the structured filter APIs, Aspose.Cells allows you to control the visibility of each individual pivot item directly. By iterating through the `PivotItems` collection of a `PivotField` and toggling the `IsHidden` property, you can selectively suppress specific items without applying a formula-based filter. Setting `IsHidden = true` hides the item from the pivot table; setting `IsHidden = false` unhides it and makes it visible again.

This approach is useful when the filtering rule is irregular or item-specific, such as hiding a small number of named categories that should not appear in a particular report. The example below loads a pivot table, hides a specific item by name, demonstrates how to unhide it, refreshes the pivot table, and saves the workbook.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.Worksheets[0];

// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.PivotTables[0];

// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.RowFields[0];

// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];

    // Hide pivot items that match a specific name/criterion
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }

    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}

// Refresh and recalculate the pivot table so changes take effect
pivotTable.PivotCache.Refresh();

// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.Save("output_pivot_filtered.xlsx");
```

## **Summary**

Aspose.Cells for .NET provides a complete set of pivot table filtering capabilities that match those found in Microsoft Excel. Label, date, and value filters cover the most common analytical scenarios, while the top 10 filter handles ranking reports. When the filtering rule is irregular, the `PivotItem.IsHidden` property offers a flexible, item-level fallback. Combining these strategies — for example, applying a label filter and then hiding specific items — allows you to build precisely targeted pivot table reports entirely from code.

## Related Articles

- [Insert Pivot Table](/cells/net/create-pivot-table/)
- [Add Pivot Table Row and Column Fields in Aspose.Cells for .NET](/cells/net/pivot-table-add-row-column-fields/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for .NET](/cells/net/add-filter-field-in-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for .NET](/cells/net/pivot-table-manage-value-fields/)
- [Refresh Pivot Tables and Pivot Caches in Aspose.Cells for .NET](/cells/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}