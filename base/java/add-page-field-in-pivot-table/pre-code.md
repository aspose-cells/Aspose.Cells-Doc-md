---
title: Page Fields in Pivot Tables
description: Learn how to add and configure page fields in pivot tables using Aspose.Cells for Java, including adding page fields, single-select filtering, and multi-select filtering.
keywords: Aspose.Cells, Java, pivot table, page field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /java/page-fields/
linktitle: Page Fields
---

{{% alert color="primary" %}}
Aspose.Cells supports the full lifecycle of page fields in pivot tables. You can add a page field through a high-level convenience API or through the lower-level `PageFields` collection, and you can drive the page filter in single-select mode, clear it to show every page item, or switch the field to multi-select so users can pick several page items at once through the checkbox UI in Excel.
{{% /alert %}}

## **Introduction**

A page field is a pivot field that controls *which subset* of the source data the pivot body displays. End users see it as a dropdown at the top of a rendered pivot in Excel, and selecting one of the available page items rebuilds the pivot body so that only the records belonging to that page item are summarized. A pivot field becomes a page field when it is registered as `PivotFieldType.Page` rather than `PivotFieldType.Row`, `PivotFieldType.Column`, or `PivotFieldType.Data`.

A page field can operate in two behaviors. In the default **single-select** behavior only one page item is visible at a time, so the pivot body summarizes exactly one subset. In the **multi-select** behavior the field exposes a checkbox list, and the pivot body summarizes the union of every checked page item. The same source field can be moved back and forth between these behaviors by toggling a single property.

Aspose.Cells for Aspose.Cells for Java exposes two equivalent ways to register a page field. The high-level API is `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")`, which takes the source-column name and adds the field in a single call. The lower-level API is `PivotTable.PageFields.add(PivotField)`, which is used when you already hold a `PivotField` reference and want to add the same field instance to the page area. Both APIs end up populating the same `PageFields` collection, and the remainder of this article demonstrates how to choose between them and how to drive each filtering mode.

## **Adding a Page Field**

There are two ways to register a pivot field in the page area. The high-level call takes the source-column name as a string and is the most common path. The lower-level call accepts an existing `PivotField` instance and is convenient when the same field object must be reused across multiple pivot areas. Both calls place the field into `PivotTable.PageFields`, after which it appears as the page dropdown at the top of the rendered pivot.

### Adding a Page Field with addFieldToArea

The following example builds a small Fruit / Year / Amount dataset, places a pivot table at cell E3 with `Fruit` on the row area, `Amount` on the data area, and `Year` on the page area, refreshes the pivot, and saves the workbook.

<!-- CODE_BLOCK:0:Load or create a workbook, populate a 9-row sample dataset with Fruit, Year, and Amount columns, add a pivot table at E3, use addFieldToArea with PivotFieldType.ROW for Fruit, PivotFieldType.DATA for Amount, and PivotFieldType.PAGE for Year, refresh the pivot, and save the file as pageFieldSample.xlsx -->

### Adding a Page Field with PageFields.add

When you already work with a `PivotField` instance, you can pass it directly to `PivotTable.PageFields.add`. The pivot table and page field are constructed exactly as in the previous scenario; only the final page-area registration is replaced with the lower-level API call.

<!-- CODE_BLOCK:1:Reference the same pivot construction as in Scenario 1a, obtain the Year PivotField from the getBaseFields() collection, pass that PivotField instance to pivotTable.PageFields.add, refresh the pivot, and save the file -->

## **Single-Select Filtering (Showing One Page Item)**

In the default single-select behavior, the page field renders as a single dropdown and the `PivotField.CurrentPageItem` integer selects which page item drives the pivot body. Assigning a specific index picks that one item; assigning the special sentinel `0x7FFD` (decimal 32765) clears the filter so every page item is summarized at once. Single-select is the default; you do not need to enable it explicitly.

### Showing All Items

Setting `CurrentPageItem` to the magic value `0x7FFD` is equivalent to clearing the page filter: the pivot body summarizes every page item as if no filter were applied.

<!-- CODE_BLOCK:2:Reference the same pivot construction as in Scenario 1a, call setCurrentPageItem(0x7FFD) on pivotTable.PageFields[0] with an inline comment explaining that this value represents all items, then save the workbook -->

### Showing One Specific Item

Setting `CurrentPageItem` to a real index picks just that one page item. The index is the position of the item in the page field's sorted item list, so for example `1` selects the second item after sorting.

<!-- CODE_BLOCK:3:Reference the same pivot construction as in Scenario 1a, call setCurrentPageItem(1) on pivotTable.PageFields[0] with an inline comment noting that 1 corresponds to the second sorted item, then save the workbook -->

## **Multi-Select Filtering**

Multi-select filtering turns the page dropdown into a checkbox list and lets the end user pick several page items simultaneously. Aspose.Cells exposes two properties that work together. `PivotField.IsMultipleItemSelectionAllowed` must be set to `true` before the multi-select UI takes effect at all. After it is enabled, `PivotItem.IsHidden` controls which items appear in the checkbox list, so you can either show every item or whitelist only specific items.

The code below enables multi-select on the same Year page field built in Scenario 1a, and then shows two patterns: Part A reveals every page item by leaving `IsHidden` set to `false` for every entry, while Part B whitelists only the source values you choose and hides everything else through a `switch (pivotItems[i].getStringValue())` block.

<!-- CODE_BLOCK:4:Reference the same pivot construction as in Scenario 1a, call setMultipleItemSelectionAllowed(true) on pivotTable.PageFields[0], retrieve the PivotItems collection, then run Part A loop that calls setHidden(false) on every item, followed by Part B loop that uses a switch on getStringValue to whitelist specific source values (for example 2020, grape, and blueberry) and hides all other items, then refresh and save the workbook -->

> **Note:** When using multi-select filtering through `PivotItem.IsHidden`, **at least one `PivotItem` must remain visible** (`IsHidden == false`). If every item is hidden, Excel either crashes when opening the file or renders a blank pivot. Always verify that your multi-select whitelist includes at least one item from your source data.

## **Which API and Which Mode Should I Use?**

The table below summarizes when to use each API and mode so you can pick the right combination without reading every scenario in detail.

| Scenario / Use Case | Recommended API | Property Used | Notes |
|---|---|---|---|
| Add a page field by source-column name (most common) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | High-level, one-line. Use this unless you need a `PivotField` reference. |
| Add a page field when you already have a `PivotField` object | `PivotTable.PageFields.add(PivotField)` | n/a | Use when the field object was obtained elsewhere or needs to be reused. |
| Filter to a single page item (default mode) | `PivotField.CurrentPageItem` | set to a specific index | For example, `1` shows the second item in the sorted list. |
| Show all items / clear the page filter | `PivotField.CurrentPageItem` | set to `0x7FFD` | The magic value `0x7FFD` (decimal 32765) is the sentinel for "all items". |
| Enable multi-select UI in Excel | `PivotField.IsMultipleItemSelectionAllowed` | set to `true` | Required before any `IsHidden` calls take effect. |
| Hide / show individual items in a multi-select list | `PivotItem.IsHidden` | set per item | At least one item must remain visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Always remember the visibility constraint when configuring multi-select filtering. If every `PivotItem` in a multi-select page field is hidden, Excel crashes on open or renders a blank pivot. Build your whitelist against your source data so at least one item stays visible, and your saved workbooks will open reliably on every machine.
{{% /alert %}}



{{< app/cells/assistant language="java" >}}