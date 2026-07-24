---
title: Row and Column Fields in Aspose.Cells for Python via .NET
linktitle: Row and Column Fields
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.set_subtotals in Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, pivot table, row field, column field, PivotField, set_subtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /python-net/pivot-table-row-and-column-fields/
---

Row and column fields are the building blocks of a pivot table. A field placed in the row region appears vertically on the left of the pivot, while a field placed in the column region appears horizontally across the top. This article shows how to add base fields to those regions programmatically and how to control the subtotals that render between field groups by using the `PivotField.set_subtotals` method.

## **Adding a Field to the Row or Column Region**

The `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` method moves a base field from the source data into one of the four pivot regions. The `field_type` argument accepts one of the following `PivotFieldType` values.

- `ROW` — fields placed vertically on the left
- `COLUMN` — fields placed horizontally across the top
- `DATA` — fields whose values are aggregated
- `PAGE` — fields used as report filters

After fields are added, you can access them through the `PivotTable.row_fields` and `PivotTable.column_fields` properties. Each property returns a `PivotFieldCollection`. The field at index 0 of `row_fields` is the outermost row field, and subsequent indices represent fields nested inside it. The same indexing convention applies to `column_fields`.

Field nesting order matters. Adding `Category` to the row region first and then `Item` produces a pivot whose outer grouping is `Category` and whose inner grouping is `Item`. Reversing the order reverses the hierarchy.

## **Pivot Field Subtotals**

The `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` method controls which subtotal rows appear for a pivot field. Each call toggles a single subtotal type independently. Passing `shown = True` displays the subtotal, while `shown = False` hides it. Because each call only affects one type, calling the method multiple times with different `subtotal_type` values builds a custom subset of subtotals.

The `PivotFieldSubtotalType` enum defines the available subtotal kinds.

- `AUTOMATIC` — Aspose.Cells chooses the default selection (typically `SUM` for numeric fields)
- `NONE` — suppress every subtotal row
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Subtotals only render when there are two or more pivot fields in the row region (or in the column region). A single field has nothing meaningful to subtotal between, so `set_subtotals` calls have no visible effect in that case. This article therefore places two row fields (`Category` outer, `Item` inner) in every example so the subtotal boundary between each `Category` group is visible.
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**

When you do not call `set_subtotals` at all, Aspose.Cells applies the `AUTOMATIC` selection to numeric fields. The following example explicitly confirms this behavior by calling `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` on the outer `Category` row field.

<!-- CODE_BLOCK:0:Complete top-level Python program that imports the necessary modules (import aspose.cells; from aspose.cells.pivot import PivotFieldType, PivotFieldSubtotalType), creates a new Workbook, renames worksheets[0] to 'Data', writes a header row at A1:D1 (Category, Item, Year, Amount) and eight data rows at A2:D9 using put_value with the shared dataset (Fruit/Apple with year 2020 amount 100, Fruit/Apple 2021 150, Fruit/Banana 2020 80, Fruit/Banana 2021 90, Vegetable/Carrot 2020 50, Vegetable/Carrot 2021 60, Vegetable/Daikon 2020 40, Vegetable/Daikon 2021 45) where Year and Amount are ints and Category and Item are strings, adds a pivot table covering A1:D9 placed at cell F3 named 'PivotTable1' via worksheet.pivot_tables.add, adds Category to the Row region first, then Item to the Row region second (so Category is outer and Item is inner), adds Year to the Column region, adds Amount to the Data region (all four via pivot_table.add_field_to_area(PivotFieldType.X, 'name')), retrieves the outer row field via category_field = pivot_table.row_fields[0], explicitly calls category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True) using the 2-arg overload, then calls pivot_table.refresh_data() and pivot_table.calculate_data() and saves the workbook as output_automatic.xlsx. Expected output: the pivot renders a default subtotal row for each Category group (Fruit and Vegetable) between the inner Item rows and the next Category. -->

## **Scenario 2 — Suppressing All Subtotals (None)**

Calling `set_subtotals(PivotFieldSubtotalType.NONE, True)` removes every subtotal row from the pivot, leaving only the field rows and the grand total at the bottom. This is useful when you want the raw grouped data without any summary rows.

<!-- CODE_BLOCK:1:Complete top-level Python program identical in structure to Scenario 1 (same import statements at the top, same Workbook creation, same worksheets[0] rename to 'Data', same eight-row shared dataset written to A1:D9 via put_value, same PivotTable1 constructed at cell F3 over A1:D9, same four fields added with Category outer and Item inner in the Row region, Year in the Column region, and Amount in the Data region) except that the set_subtotals call is changed to category_field.set_subtotals(PivotFieldSubtotalType.NONE, True) on the outer Category row field to suppress every subtotal row, followed by refresh_data() and calculate_data(), and the workbook is saved as output_none.xlsx. Expected output: the pivot renders Category and Item rows but no subtotal row between category groups — only the grand total row remains at the bottom. -->

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**

You are not limited to a single subtotal type. Each `set_subtotals` call operates independently on one type, so calling the method twice — once with `SUM` and once with `AVERAGE` — produces a custom subset of two subtotal rows for each `Category` group.

<!-- CODE_BLOCK:2:Complete top-level Python program identical in structure to Scenario 1 (same import statements at the top, same Workbook creation, same worksheets[0] rename to 'Data', same eight-row shared dataset written to A1:D9 via put_value, same PivotTable1 constructed at cell F3 over A1:D9, same four fields added with Category outer and Item inner in the Row region, Year in the Column region, and Amount in the Data region) except that it makes TWO independent set_subtotals calls on the outer Category row field using the 2-arg overload — first category_field.set_subtotals(PivotFieldSubtotalType.SUM, True), then a separate category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True) call (NOT an array, NOT a single call with both types) — to produce a custom subset of two subtotals, followed by refresh_data() and calculate_data(), and the workbook is saved as output_custom.xlsx. Expected output: the pivot renders TWO subtotal rows per Category group — one SUM subtotal and one AVERAGE subtotal — between the inner Item rows and the next Category. -->

## **Recap**

The three scenarios above share the same dataset and pivot table structure. The only difference between them is the `set_subtotals` call applied to the outer `Category` row field. Remember the two-fields rule: a single field in a region has nothing to subtotal between, so always place at least two fields in the row or column region when you want `set_subtotals` to have a visible effect.

## **Related Articles**

- [Page Fields in Pivot Tables](/cells/python-net/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Python via .NET](/cells/python-net/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python" >}}