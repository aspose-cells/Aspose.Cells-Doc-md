---
title: Add Filter Fields to a Pivot Table in Aspose.Cells for Go via C++
description: Learn how to add and configure filter fields in pivot tables using Aspose.Cells for Go via C++, including adding filter fields, single-select filtering, and multi-select filtering.
keywords: Aspose.Cells, Go, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /go-cpp/add-page-field-in-pivot-table/
linktitle: Add Filter Fields
---

{{% alert color="primary" %}}
Aspose.Cells supports the full lifecycle of filter fields in pivot tables. You can add a filter field through a high-level convenience API or through the lower-level `PageFields` collection, and you can drive the filter in single-select mode, clear it to show every filter item, or switch the field to multi-select so users can pick several filter items at once through the checkbox UI in Excel.
{{% /alert %}}

## **Introduction**
A filter field is a pivot field that controls *which subset* of the source data the pivot body displays. End users see it as a dropdown at the top of a rendered pivot in Excel, and selecting one of the available filter items rebuilds the pivot body so that only the records belonging to that filter item are summarized. A pivot field becomes a filter field when it is registered as `PivotFieldType.Page` rather than `PivotFieldType.Row`, `PivotFieldType.Column`, or `PivotFieldType.Data`.

## **Adding a Filter Field**

### Adding a Filter Field with AddFieldToArea
The following example builds a small Fruit / Year / Amount dataset, places a pivot table at cell E3 with `Fruit` on the row area, `Amount` on the data area, and `Year` on the filter area, refreshes the pivot, and saves the workbook.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPageFieldInPivotTable.go" >}}

### Adding a Filter Field with PageFields.Add
When you already work with a `PivotField` instance, you can pass it directly to `PivotTable.PageFields.Add`. The pivot table and filter field are constructed exactly as in the previous scenario; only the final filter-area registration is replaced with the lower-level API call.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPageFieldInPivotTable-1.go" >}}

## **Single-Select Filtering (Showing One Filter Item)**
In the default single-select behavior, the filter field renders as a single dropdown and the `PivotField.CurrentPageItem` integer selects which filter item drives the pivot body. Assigning a specific index picks that one item; assigning the special sentinel `0x7FFD` (decimal 32765) clears the filter so every filter item is summarized at once. Single-select is the default; you do not need to enable it explicitly.

### Showing All Items
Setting `CurrentPageItem` to the magic value `0x7FFD` is equivalent to clearing the filter: the pivot body summarizes every filter item as if no filter were applied.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPageFieldInPivotTable-2.go" >}}

### Showing One Specific Item
Setting `CurrentPageItem` to a real index picks just that one filter item. The index is the position of the item in the filter field's sorted item list, so for example `1` selects the second item after sorting.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPageFieldInPivotTable-3.go" >}}

## **Multi-Select Filtering**
Multi-select filtering turns the filter dropdown into a checkbox list and lets the end user pick several filter items simultaneously. Aspose.Cells exposes two properties that work together. `PivotField.IsMultipleItemSelectionAllowed` must be set to `true` before the multi-select UI takes effect at all. After it is enabled, `PivotItem.IsHidden` controls which items appear in the checkbox list, so you can either show every item or whitelist only specific items.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPageFieldInPivotTable-4.go" >}}

> **Note:** When using multi-select filtering through `PivotItem.IsHidden`, **at least one `PivotItem` must remain visible** (`IsHidden == false`). If every item is hidden, Excel either crashes when opening the file or renders a blank pivot. Always verify that your multi-select whitelist includes at least one item from your source data.

## **Which API and Which Mode Should I Use?**
The table below summarizes when to use each API and mode so you can pick the right combination without reading every scenario in detail.
| Scenario / Use Case | Recommended API | Property Used | Notes |
|---|---|---|---|
| Add a filter field by source-column name (most common) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | High-level, one-line. Use this unless you need a `PivotField` reference. |
| Add a filter field when you already have a `PivotField` object | `PivotTable.PageFields.Add(PivotField)` | n/a | Use when the field object was obtained elsewhere or needs to be reused. |
| Filter to a single filter item (default mode) | `PivotField.CurrentPageItem` | set to a specific index | For example, `1` shows the second item in the sorted list. |
| Show all items / clear the filter | `PivotField.CurrentPageItem` | set to `0x7FFD` | The magic value `0x7FFD` (decimal 32765) is the sentinel for "all items". |
| Enable multi-select UI in Excel | `PivotField.IsMultipleItemSelectionAllowed` | set to `true` | Required before any `IsHidden` calls take effect. |
| Hide / show individual items in a multi-select list | `PivotItem.IsHidden` | set per item | At least one item must remain visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Always remember the visibility constraint when configuring multi-select filtering. If every `PivotItem` in a multi-select filter field is hidden, Excel crashes on open or renders a blank pivot. Build your whitelist against your source data so at least one item stays visible, and your saved workbooks will open reliably on every machine.
{{% /alert %}}

{{< app/cells/assistant language="go" >}}