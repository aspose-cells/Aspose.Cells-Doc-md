---
title: Top 10 Show or Filter in Pivot Table
description: Learn how to show only the top or bottom ranked items of a pivot field in Aspose.Cells for Python via .NET. This article covers the Excel 97-2003 top_10_auto_show method, reading options with top_10_auto_show_settings, and the Excel 2007-365 Top 10 Filter via filter_top10.
linktitle: Top 10 Show or Filter
keywords: Aspose.Cells, Python via .NET, pivot table, top 10, auto show, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table that lists every item of a row field can be hard to read when the field has dozens of members. A Top 10 report keeps only the highest or lowest ranked items, which is exactly what ranking reports need — "top 5 products by revenue" or "bottom 3 regions by sales count". Aspose.Cells supports two mechanisms for this, and they correspond to two generations of Microsoft Excel.
- **Excel 97-2003 AutoShow** — the `PivotField.top_10_auto_show()` method. This is the classic "Show the top/bottom N items" setting stored directly on the pivot field. It works in every Excel version, old and new, because it is part of the original pivot table format.
- **Excel 2007-365 Top 10 Filter** — the `PivotField.filter_top10()` method. This is the modern Top 10 value filter found under the field menu's Value Filters. It is stored as a `PivotFilter` object attached to the field and offers item-count and percentage based ranking.

## **Top 10 Show in Excel 97-2003 (top_10_auto_show)**
The classic AutoShow is configured with a single call to `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)`:
- `is_auto_show` — enables or disables the AutoShow setting on the field.
- `is_top` — `True` keeps the highest ranked items (Top), `False` keeps the lowest (Bottom).
- `count` — how many items to keep, for example 10 for a classic Top 10 report.
- `rank_by` — the zero-based index of the **data field** whose values rank the items. Pass -1 to rank the items by the field itself.
The ranking can be driven by a value field or by the field itself. Two natural variants exist, shown below.

### **Rank by a Value Field**
Rank the row field's items by an ordinary value field such as Sum of Sales. The following example builds a pivot table with one row field (`Sport`) and one data field (`Sales`), then shows the top 2 sports by sales. `rank_by` is 0 because "Sum of Sales" is the data field at index 0.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **Rank by the Field Itself**
A field can also be ranked by itself — pass -1 as `rank_by`. No extra data field is needed for this variant; the field only has to sit in the row (or column) area. The following example shows the bottom 3 sports ranked by the field itself. When this setting is saved, the `rank_by` attribute is omitted from the pivot table XML because -1 is the format's default value, and `top_10_auto_show_settings.rank_by` reads -1 back.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **Reading the Current Options (top_10_auto_show_settings)**
The `PivotField.top_10_auto_show_settings` property returns a `PivotFieldTop10AutoShowSettings` object that exposes the AutoShow options currently stored on the field. Use it to inspect how an existing workbook, or a pivot table you just configured, will present its items — including workbooks loaded from file.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

The four properties map to the classic AutoShow attributes written into the pivot table XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), so the values read back are the values every Excel version will honor.

## **Note**

{{% alert color="primary" %}}
- The direct `PivotField` properties `is_auto_show`, `is_ascend_show`, `auto_show_count` and `auto_show_field` are marked obsolete. Use the `top_10_auto_show_settings` object instead: `is_auto_show` becomes `top_10_auto_show_settings.is_auto_show`, `is_ascend_show` becomes `top_10_auto_show_settings.is_top`, `auto_show_count` becomes `top_10_auto_show_settings.auto_show_count`, and `auto_show_field` becomes `top_10_auto_show_settings.rank_by`. The `top_10_auto_show()` method itself is the supported way to change the settings.
- `top_10_auto_show` works with row and column fields. A field that is only in the page (filter) area cannot be ranked this way because its items are not laid out in the pivot body.
{{% /alert %}}

## **Excel 2007-365: Top 10 Filter (filter_top10)**
Modern Excel versions expose Top 10 as a value filter on the field menu (Value Filters, Top 10...). Aspose.Cells models it with the `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)` method, which returns the created `PivotFilter`:
- `value_field_index` — the zero-based index of the data field whose aggregated values rank the items.
- `type` — what `item_count` means. `PivotFilterType.COUNT` keeps a fixed number of items (the dialog's Items option). `PivotFilterType.PERCENT` keeps a percentage of the items, so `item_count` is the percentage itself — 30 keeps the top 30 percent. `PivotFilterType.SUM` ranks by cumulative value coverage.
- `is_top` — `True` for Top, `False` for Bottom.
- `item_count` — the N in Top N; its unit depends on `type`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# For a percentage-based filter instead, keep the top 30 percent of the items:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` and `filter_top10` are two separate features. AutoShow writes the classic `autoShow` attribute set on the pivot field and is honored by all Excel versions back to Excel 97. `filter_top10` writes a modern `PivotFilter` entry, which requires Excel 2007 or later. When a workbook is opened in an older Excel version, a pivot table that uses the modern filter falls back to showing all items. For documents that must round-trip through legacy tooling, prefer `top_10_auto_show`; for modern workbooks, prefer `filter_top10` because it composes with the other value filters.
{{% /alert %}}

## **Related Articles**
- [Filtering Pivot Tables by Label or Value](/cells/python-net/filter-by-label-or-value-of-pivot-table/)
- [Add Pivot Table Row and Column Fields](/cells/python-net/pivot-table-add-row-and-column-fields/)
- [Group Pivot Fields in the Pivot Table](/cells/python-net/group-pivot-fields-in-the-pivot-table/)
- [Refresh Pivot Table](/cells/python-net/refresh-pivot-table/)
- [Add Page Field in Pivot Table](/cells/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}