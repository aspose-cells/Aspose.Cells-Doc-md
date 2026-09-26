---
title: Add Pivot Table Row and Column Fields in Aspose.Cells for Go via C++
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Go via C++.
linktitle: Row and Column Fields
keywords: Aspose.Cells, Go, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /go-cpp/pivot-table-add-row-and-column-fields/
---

## **Adding a Field to the Row or Column Region**
The `PivotTable.AddFieldToArea(PivotFieldType fieldType, U16String fieldName)` method moves a base field from the source data into one of the four pivot regions. The `fieldType` argument accepts one of the following `PivotFieldType` values.
- `Row` — fields placed vertically on the left
- `Column` — fields placed horizontally across the top
- `Data` — fields whose values are aggregated
- `Page` — fields used as report filters
Field nesting order matters. Adding `Category` to the row region first and then `Item` produces a pivot whose outer grouping is `Category` and whose inner grouping is `Item`. Reversing the order reverses the hierarchy.

## **Pivot Field Subtotals**
The `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` method controls which subtotal rows appear for a pivot field. Each call toggles a single subtotal type independently. Passing `shown = true` displays the subtotal, while `shown = false` hides it. Because each call only affects one type, calling the method multiple times with different `subtotalType` values builds a custom subset of subtotals.
The `PivotFieldSubtotalType` enum defines the available subtotal kinds.
- `Automatic` — Aspose.Cells chooses the default selection (typically `Sum` for numeric fields)
- `None` — suppress every subtotal row
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Subtotals only render when there are two or more pivot fields in the row region (or in the column region). A single field has nothing meaningful to subtotal between, so `SetSubtotals` calls have no visible effect in that case. This article therefore places two row fields (`Category` outer, `Item` inner) in every example so the subtotal boundary between each `Category` group is visible.
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**
When you do not call `SetSubtotals` at all, Aspose.Cells applies the `Automatic` selection to numeric fields. The following example explicitly confirms this behavior by calling `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` on the outer `Category` row field.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RowAndColumnFields.go" >}}

## **Scenario 2 — Suppressing All Subtotals (None)**
Calling `SetSubtotals(PivotFieldSubtotalType.None, true)` removes every subtotal row from the pivot, leaving only the field rows and the grand total at the bottom. This is useful when you want the raw grouped data without any summary rows.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RowAndColumnFields-1.go" >}}

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
You are not limited to a single subtotal type. Each `SetSubtotals` call operates independently on one type, so calling the method twice — once with `Sum` and once with `Average` — produces a custom subset of two subtotal rows for each `Category` group.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RowAndColumnFields-2.go" >}}

## **Recap**

## **Related Articles**
- [Page Fields in Pivot Tables](/cells/go-cpp/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Go via C++](/cells/go-cpp/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/go-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="go" >}}