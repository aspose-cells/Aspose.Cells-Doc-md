---
title: Top 10 Show or Filter in Pivot Table
description: Learn how to show only the top or bottom ranked items of a pivot field in Aspose.Cells for Java. This article covers the Excel 97-2003 Top10AutoShow method, reading options with Top10AutoShowSettings, and the Excel 2007-365 Top 10 Filter via FilterTop10.
linktitle: Top 10 Show or Filter
keywords: Aspose.Cells, Java, pivot table, top 10, auto show, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table that lists every item of a row field can be hard to read when the field has dozens of members. A Top 10 report keeps only the highest or lowest ranked items, which is exactly what ranking reports need — "top 5 products by revenue" or "bottom 3 regions by sales count". Aspose.Cells supports two mechanisms for this, and they correspond to two generations of Microsoft Excel.
- **Excel 97-2003 AutoShow** — the `PivotField.top10AutoShow()` method. This is the classic "Show the top/bottom N items" setting stored directly on the pivot field. It works in every Excel version, old and new, because it is part of the original pivot table format.
- **Excel 2007-365 Top 10 Filter** — the `PivotField.filterTop10()` method. This is the modern Top 10 value filter found under the field menu's Value Filters. It is stored as a `PivotFilter` object attached to the field and offers item-count and percentage based ranking.

## **Top 10 Show in Excel 97-2003 (top10AutoShow)**
The classic AutoShow is configured with a single call to `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — enables or disables the AutoShow setting on the field.
- `isTop` — `true` keeps the highest ranked items (Top), `false` keeps the lowest (Bottom).
- `count` — how many items to keep, for example 10 for a classic Top 10 report.
- `rankBy` — the zero-based index of the **data field** whose values rank the items. Pass -1 to rank the items by the field itself.
The ranking can be driven by a value field or by the field itself. Two natural variants exist, shown below.

### **Rank by a Value Field**
Rank the row field's items by an ordinary value field such as Sum of Sales. The following example builds a pivot table with one row field (`Sport`) and one data field (`Sales`), then shows the top 2 sports by sales. `rankBy` is 0 because "Sum of Sales" is the data field at index 0.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **Rank by the Field Itself**
A field can also be ranked by itself — pass -1 as `rankBy`. No extra data field is needed for this variant; the field only has to sit in the row (or column) area. The following example shows the bottom 3 sports ranked by the field itself. When this setting is saved, the `rankBy` attribute is omitted from the pivot table XML because -1 is the format's default value, and `Top10AutoShowSettings.getRankBy()` reads -1 back.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **Reading the Current Options (Top10AutoShowSettings)**
The `PivotField.getTop10AutoShowSettings()` method returns a `PivotFieldTop10AutoShowSettings` object that exposes the AutoShow options currently stored on the field. Use it to inspect how an existing workbook, or a pivot table you just configured, will present its items — including workbooks loaded from file.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

The four properties map to the classic AutoShow attributes written into the pivot table XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), so the values read back are the values every Excel version will honor.

## **Note**

{{% alert color="primary" %}}
- The direct `PivotField` properties exposed by `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()`, and `getAutoShowField()` are marked obsolete. Use the `Top10AutoShowSettings` object instead: `Top10AutoShowSettings.isAutoShow()` replaces `PivotField.isAutoShow()`, `Top10AutoShowSettings.isTop()` replaces `PivotField.isAscendShow()`, `Top10AutoShowSettings.getAutoShowCount()` replaces `PivotField.getAutoShowCount()`, and `Top10AutoShowSettings.getRankBy()` replaces `PivotField.getAutoShowField()`. The `PivotField.top10AutoShow()` method itself is the supported way to change the settings.
- `top10AutoShow` works with row and column fields. A field that is only in the page (filter) area cannot be ranked this way because its items are not laid out in the pivot body.
{{% /alert %}}

## **Excel 2007-365: Top 10 Filter (filterTop10)**
Modern Excel versions expose Top 10 as a value filter on the field menu (Value Filters, Top 10...). Aspose.Cells models it with the `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` method, which returns the created `PivotFilter`:
- `valueFieldIndex` — the zero-based index of the data field whose aggregated values rank the items.
- `type` — what `itemCount` means. `PivotFilterType.COUNT` keeps a fixed number of items (the dialog's Items option). `PivotFilterType.PERCENT` keeps a percentage of the items, so `itemCount` is the percentage itself — 30 keeps the top 30 percent. `PivotFilterType.SUM` ranks by cumulative value coverage.
- `isTop` — `true` for Top, `false` for Bottom.
- `itemCount` — the N in Top N; its unit depends on `type`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter - keep the top 2 items by "Sum of Sales" (data field index 0)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` and `filterTop10` are two separate features. AutoShow writes the classic `autoShow` attribute set on the pivot field and is honored by all Excel versions back to Excel 97. `filterTop10` writes a modern `PivotFilter` entry, which requires Excel 2007 or later. When a workbook is opened in an older Excel version, a pivot table that uses the modern filter falls back to showing all items. For documents that must round-trip through legacy tooling, prefer `top10AutoShow`; for modern workbooks, prefer `filterTop10` because it composes with the other value filters.
{{% /alert %}}

## **Related Articles**
- [Filtering Pivot Tables by Label or Value](/cells/java/filter-by-label-or-value-of-pivot-table/)
- [Add Pivot Table Row and Column Fields](/cells/java/pivot-table-add-row-and-column-fields/)
- [Group Pivot Fields in the Pivot Table](/cells/java/group-pivot-fields-in-the-pivot-table/)
- [Refresh Pivot Table](/cells/java/refresh-pivot-table/)
- [Add Page Field in Pivot Table](/cells/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}