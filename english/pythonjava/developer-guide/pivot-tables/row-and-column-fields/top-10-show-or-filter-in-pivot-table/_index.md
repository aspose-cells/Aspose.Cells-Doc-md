---
title: Top 10 Show or Filter in Pivot Table
description: Learn how to show only the top or bottom ranked items of a pivot field in Aspose.Cells for Python via Java. This article covers the Excel 97-2003 top10AutoShow method, reading options with Top10AutoShowSettings, and the Excel 2007-365 Top 10 Filter via filterTop10.
linktitle: Top 10 Show or Filter
keywords: Aspose.Cells for Python via Java, pivot table, top 10, auto show, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table that lists every item of a row field can be hard to read when the field has dozens of members. A Top 10 report keeps only the highest or lowest ranked items, which is exactly what ranking reports need — "top 5 products by revenue" or "bottom 3 regions by sales count". Aspose.Cells supports two mechanisms for this, and they correspond to two generations of Microsoft Excel.
- **Excel 97-2003 AutoShow** — the `PivotField.top10AutoShow()` method. This is the classic "Show the top/bottom N items" setting stored directly on the pivot field. It works in every Excel version, old and new, because it is part of the original pivot table format.
- **Excel 2007-365 Top 10 Filter** — the `PivotField.filterTop10()` method. This is the modern Top 10 value filter found under the field menu's Value Filters. It is stored as a `PivotFilter` object attached to the field and offers item-count and percentage based ranking.

## **Top 10 Show in Excel 97-2003 (top10AutoShow)**
The classic AutoShow is configured with a single call to `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — enables or disables the AutoShow setting on the field.
- `isTop` — `True` keeps the highest ranked items (Top), `False` keeps the lowest (Bottom).
- `count` — how many items to keep, for example 10 for a classic Top 10 report.
- `rankBy` — the zero-based index of the **data field** whose values rank the items. Pass -1 to rank the items by the field itself.
The ranking can be driven by a value field or by the field itself. Two natural variants exist, shown below.

### **Rank by a Value Field**
Rank the row field's items by an ordinary value field such as Sum of Sales. The following example builds a pivot table with one row field (`Sport`) and one data field (`Sales`), then shows the top 2 sports by sales. `rankBy` is 0 because "Sum of Sales" is the data field at index 0.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Rank by the Field Itself**
A field can also be ranked by itself — pass -1 as `rankBy`. No extra data field is needed for this variant; the field only has to sit in the row (or column) area. The following example shows the bottom 3 sports ranked by the field itself. When this setting is saved, the `rankBy` attribute is omitted from the pivot table XML because -1 is the format's default value, and `Top10AutoShowSettings.getRankBy()` reads -1 back.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Reading the Current Options (Top10AutoShowSettings)**
The `PivotField.getTop10AutoShowSettings()` method returns a `PivotFieldTop10AutoShowSettings` object that exposes the AutoShow options currently stored on the field. Use it to inspect how an existing workbook, or a pivot table you just configured, will present its items — including workbooks loaded from file.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

The four properties map to the classic AutoShow attributes written into the pivot table XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), so the values read back are the values every Excel version will honor.

## **Note**

{{% alert color="primary" %}}
- The direct `PivotField` accessors `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` and `getAutoShowField()` are marked obsolete. Use the `Top10AutoShowSettings` object instead: `PivotField.isAutoShow()` becomes `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` becomes `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` becomes `Top10AutoShowSettings.getAutoShowCount()`, and `PivotField.getAutoShowField()` becomes `Top10AutoShowSettings.getRankBy()`. The `top10AutoShow()` method itself is the supported way to change the settings.
- `top10AutoShow` works with row and column fields. A field that is only in the page (filter) area cannot be ranked this way because its items are not laid out in the pivot body.
{{% /alert %}}

## **Excel 2007-365: Top 10 Filter (filterTop10)**
Modern Excel versions expose Top 10 as a value filter on the field menu (Value Filters, Top 10...). Aspose.Cells models it with the `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` method, which returns the created `PivotFilter`:
- `valueFieldIndex` — the zero-based index of the data field whose aggregated values rank the items.
- `type` — what `itemCount` means. `PivotFilterType.COUNT` keeps a fixed number of items (the dialog's Items option). `PivotFilterType.PERCENT` keeps a percentage of the items, so `itemCount` is the percentage itself — 30 keeps the top 30 percent. `PivotFilterType.SUM` ranks by cumulative value coverage.
- `isTop` — `True` for Top, `False` for Bottom.
- `itemCount` — the N in Top N; its unit depends on `type`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` and `filterTop10` are two separate features. AutoShow writes the classic `autoShow` attribute set on the pivot field and is honored by all Excel versions back to Excel 97. `filterTop10` writes a modern `PivotFilter` entry, which requires Excel 2007 or later. When a workbook is opened in an older Excel version, a pivot table that uses the modern filter falls back to showing all items. For documents that must round-trip through legacy tooling, prefer `top10AutoShow`; for modern workbooks, prefer `filterTop10` because it composes with the other value filters.
{{% /alert %}}

## **Related Articles**
- [Filtering Pivot Tables by Label or Value](/cells/python-java/filter-by-label-or-value-of-pivot-table/)
- [Add Pivot Table Row and Column Fields](/cells/python-java/pivot-table-add-row-and-column-fields/)
- [Group Pivot Fields in the Pivot Table](/cells/python-java/group-pivot-fields-in-the-pivot-table/)
- [Refresh Pivot Table](/cells/python-java/refresh-pivot-table/)
- [Add Page Field in Pivot Table](/cells/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}