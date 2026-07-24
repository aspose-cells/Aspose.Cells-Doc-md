---
title: Row and Column Fields in Aspose.Cells for Node.js via C++
linktitle: Row and Column Fields
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /nodejs-cpp/pivot-table-row-and-column-fields/
---

Row and column fields are the building blocks of a pivot table. A field placed in the row region appears vertically on the left of the pivot, while a field placed in the column region appears horizontally across the top. This article shows how to add base fields to those regions programmatically and how to control the subtotals that render between field groups by using the `PivotField.SetSubtotals` method.

## **Adding a Field to the Row or Column Region**

The `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` method moves a base field from the source data into one of the four pivot regions. The `fieldType` argument accepts one of the following `PivotFieldType` values.

- `Row` — fields placed vertically on the left
- `Column` — fields placed horizontally across the top
- `Data` — fields whose values are aggregated
- `Page` — fields used as report filters

After fields are added, you can access them through the `PivotTable.RowFields` and `PivotTable.ColumnFields` properties. Each property returns a `PivotFieldCollection`. The field at index 0 of `RowFields` is the outermost row field, and subsequent indices represent fields nested inside it. The same indexing convention applies to `ColumnFields`.

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

<!-- CODE_BLOCK:0:Complete top-level JavaScript program that begins with the required imports for Aspose.Cells for Node.js via C++, creates a new Workbook, renames Worksheets[0] to "Data", writes a header row at A1:D1 (Category, Item, Year, Amount) and eight data rows at A2:D9 using putValue with the shared dataset (Fruit/Apple with year 2020 amount 100, Fruit/Apple 2021 150, Fruit/Banana 2020 80, Fruit/Banana 2021 90, Vegetable/Carrot 2020 50, Vegetable/Carrot 2021 60, Vegetable/Daikon 2020 40, Vegetable/Daikon 2021 45) where Year and Amount are ints and Category and Item are strings, adds a pivot table covering A1:D9 placed at cell F3 named "PivotTable1" via worksheet.pivotTables.add, adds Category to the Row region first, then Item to the Row region second (so Category is outer and Item is inner), adds Year to the Column region, adds Amount to the Data region (all four via pivotTable.addFieldToArea(PivotFieldType.X, "name")), retrieves the outer row field via PivotField categoryField = pivotTable.rowFields[0], explicitly calls categoryField.setSubtotals(PivotFieldSubtotalType.Automatic, true) using the 2-arg overload, then calls pivotTable.refreshData() and pivotTable.calculateData() and saves the workbook as output_automatic.xlsx. Expected output: the pivot renders a default subtotal row for each Category group (Fruit and Vegetable) between the inner Item rows and the next Category. -->

## **Scenario 2 — Suppressing All Subtotals (None)**

Calling `SetSubtotals(PivotFieldSubtotalType.None, true)` removes every subtotal row from the pivot, leaving only the field rows and the grand total at the bottom. This is useful when you want the raw grouped data without any summary rows.

<!-- CODE_BLOCK:1:Complete top-level JavaScript program identical in structure to Scenario 1 (same required imports at the top, same Workbook creation, same Worksheets[0] rename to "Data", same eight-row shared dataset written to A1:D9 via putValue, same PivotTable1 constructed at cell F3 over A1:D9, same four fields added with Category outer and Item inner in the Row region, Year in the Column region, and Amount in the Data region) except that the setSubtotals call is changed to categoryField.setSubtotals(PivotFieldSubtotalType.None, true) on the outer Category row field to suppress every subtotal row, followed by refreshData() and calculateData(), and the workbook is saved as output_none.xlsx. Expected output: the pivot renders Category and Item rows but no subtotal row between category groups — only the grand total row remains at the bottom. -->

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**

You are not limited to a single subtotal type. Each `SetSubtotals` call operates independently on one type, so calling the method twice — once with `Sum` and once with `Average` — produces a custom subset of two subtotal rows for each `Category` group.

<!-- CODE_BLOCK:2:Complete top-level JavaScript program identical in structure to Scenario 1 (same required imports at the top, same Workbook creation, same Worksheets[0] rename to "Data", same eight-row shared dataset written to A1:D9 via putValue, same PivotTable1 constructed at cell F3 over A1:D9, same four fields added with Category outer and Item inner in the Row region, Year in the Column region, and Amount in the Data region) except that it makes TWO independent setSubtotals calls on the outer Category row field using the 2-arg overload — first categoryField.setSubtotals(PivotFieldSubtotalType.Sum, true), then a separate categoryField.setSubtotals(PivotFieldSubtotalType.Average, true) call (NOT an array, NOT a single call with both types) — to produce a custom subset of two subtotals, followed by refreshData() and calculateData(), and the workbook is saved as output_custom.xlsx. Expected output: the pivot renders TWO subtotal rows per Category group — one Sum subtotal and one Average subtotal — between the inner Item rows and the next Category. -->

## **Recap**

The three scenarios above share the same dataset and pivot table structure. The only difference between them is the `SetSubtotals` call applied to the outer `Category` row field. Remember the two-fields rule: a single field in a region has nothing to subtotal between, so always place at least two fields in the row or column region when you want `SetSubtotals` to have a visible effect.

## **Related Articles**

- [Page Fields in Pivot Tables](/cells/nodejs-cpp/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Node.js via C++](/cells/nodejs-cpp/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}