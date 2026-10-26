---
title: Add Pivot Table Row and Column Fields in Aspose.Cells for Python via .NET
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.set_subtotals in Aspose.Cells for Python via .NET.
linktitle: Row and Column Fields
keywords: Aspose.Cells, Python via .NET, pivot table, row field, column field, PivotField, set_subtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding a Field to the Row or Column Region**
The `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` method moves a base field from the source data into one of the four pivot regions. The `field_type` argument accepts one of the following `PivotFieldType` values.
- `ROW` — fields placed vertically on the left
- `COLUMN` — fields placed horizontally across the top
- `DATA` — fields whose values are aggregated
- `PAGE` — fields used as report filters
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

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get(0, 0).put_value("Category")
worksheet.cells.get(0, 1).put_value("Item")
worksheet.cells.get(0, 2).put_value("Year")
worksheet.cells.get(0, 3).put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **Scenario 2 — Suppressing All Subtotals (None)**
Calling `set_subtotals(PivotFieldSubtotalType.NONE, True)` removes every subtotal row from the pivot, leaving only the field rows and the grand total at the bottom. This is useful when you want the raw grouped data without any summary rows.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells.get(0, j).put_value(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
]
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells.get(i + 1, j).put_value(data[i][j])
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [PivotFieldSubtotalType.SUM, PivotFieldSubtotalType.COUNT, PivotFieldSubtotalType.AVERAGE, PivotFieldSubtotalType.MAX, PivotFieldSubtotalType.MIN, PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
You are not limited to a single subtotal type. Each `set_subtotals` call operates independently on one type, so calling the method twice — once with `SUM` and once with `AVERAGE` — produces a custom subset of two subtotal rows for each `Category` group.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get("A1").put_value("Category")
worksheet.cells.get("B1").put_value("Item")
worksheet.cells.get("C1").put_value("Year")
worksheet.cells.get("D1").put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_table = pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **Recap**
The three scenarios differ in one thing only: the set_subtotals calls. Everything else — the dataset, the fields, and the areas they are assigned to — is identical, which is what makes the layouts directly comparable.
- **Placing fields.** `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` moves a source column into a region. Within one region the order of the calls is the display order, so the first call becomes the outermost group. Subtotals need two or more fields in the same region: with a single field there is nothing between the groups to subtotal.
- **Scenario 1 — automatic subtotals.** Leaving set_subtotals uncalled leaves the choice to Excel, which applies its own default subtotal to numeric fields. Calling set_subtotals with `PivotFieldSubtotalType.AUTOMATIC` records that choice explicitly instead of leaving it implicit.
- **Scenario 2 — no subtotals.** set_subtotals with `PivotFieldSubtotalType.NONE` switches the default subtotal off, so the pivot keeps the field rows and the grand total but drops the subtotal rows Excel would otherwise insert between them.
- **Scenario 3 — a chosen subset.** Each call toggles exactly one subtotal type, and calls accumulate rather than reset one another. Calling it once with `PivotFieldSubtotalType.SUM` and once with `PivotFieldSubtotalType.AVERAGE` therefore leaves both enabled, and the pivot renders a Sum subtotal, an Average subtotal, and a grand total.

{{% alert color="primary" %}}
Nothing about subtotals is specific to the row region. The same set_subtotals calls on a field taken from `PivotTable.ColumnFields` produce the same three layouts on the column axis, because the setting belongs to the pivot field rather than to the axis it sits on.
{{% /alert %}}

## **Related Articles**
- [Page Fields in Pivot Tables](/cells/python-net/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Python via .NET](/cells/python-net/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}