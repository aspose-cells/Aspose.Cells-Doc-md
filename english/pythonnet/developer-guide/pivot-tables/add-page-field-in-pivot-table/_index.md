---
title: Add Filter Fields to a Pivot Table in Aspose.Cells for Python via .NET
description: Learn how to add and configure filter fields in pivot tables using Aspose.Cells for Python via .NET, including adding filter fields, single-select filtering, and multi-select filtering.
keywords: Aspose.Cells, Python via .NET, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /python-net/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Add Filter Fields
---


{{% alert color="primary" %}}
Aspose.Cells supports the full lifecycle of filter fields in pivot tables. You can add a filter field through a high-level convenience API or through the lower-level `page_fields` collection, and you can drive the filter in single-select mode, clear it to show every filter item, or switch the field to multi-select so users can pick several filter items at once through the checkbox UI in Excel.
{{% /alert %}}

## **Introduction**

A filter field is a pivot field that controls *which subset* of the source data the pivot body displays. End users see it as a dropdown at the top of a rendered pivot in Excel, and selecting one of the available filter items rebuilds the pivot body so that only the records belonging to that filter item are summarized. A pivot field becomes a filter field when it is registered as `PivotFieldType.PAGE` rather than `PivotFieldType.ROW`, `PivotFieldType.COLUMN`, or `PivotFieldType.DATA`.

## **Adding a Filter Field**

### Adding a Filter Field with add_field_to_area

The following example builds a small Fruit / Year / Amount dataset, places a pivot table at cell E3 with `Fruit` on the row area, `Amount` on the data area, and `Year` on the filter area, refreshes the pivot, and saves the workbook.

```python
import aspose.cells as ac

# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Set up the header row
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Populate 9 rows of sample data: Fruit, Year, Amount
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# Add a pivot table anchored at cell E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# Refresh and calculate the pivot table data
pivot_table.calculate_data()

# Save the workbook
workbook.save("pageFieldSample.xlsx")
```

### Adding a Filter Field with page_fields.add

When you already work with a `PivotField` instance, you can pass it directly to `PivotTable.page_fields.add`. The pivot table and filter field are constructed exactly as in the previous scenario; only the final filter-area registration is replaced with the lower-level API call.

```python
import aspose.cells as ac

# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data). Below we obtain the Year PivotField from the
#   BaseFields collection and pass it to PageFields.Add — the
#   low-level alternative to AddFieldToArea. The result is
#   functionally identical to Scenario 1a.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Headers
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# Sample data (9 rows)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# Add pivot table at E3 covering A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Fruit -> Row, Amount -> Data (Year will go to Page below)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Low-level approach: grab the existing Year PivotField from BaseFields
# and register it in the Page area via PageFields.Add(PivotField).
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# Refresh so the new page field is reflected in the saved workbook
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Single-Select Filtering (Showing One Filter Item)**

In the default single-select behavior, the filter field renders as a single dropdown and the `PivotField.current_page_item` integer selects which filter item drives the pivot body. Assigning a specific index picks that one item; assigning the special sentinel `0x7FFD` (decimal 32765) clears the filter so every filter item is summarized at once. Single-select is the default; you do not need to enable it explicitly.

### Showing All Items

Setting `current_page_item` to the magic value `0x7FFD` is equivalent to clearing the filter: the pivot body summarizes every filter item as if no filter were applied.

```python
import aspose.cells as ac

# Create a new workbook
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Populate Fruit/Year/Amount data
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# Create pivot table at E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.calculate_data()

# Clear the page filter so every item in the page field is visible.
# 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
# equivalent to selecting "(All)" in Excel's page-field dropdown.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### Showing One Specific Item

Setting `current_page_item` to a real index picks just that one filter item. The index is the position of the item in the filter field's sorted item list, so for example `1` selects the second item after sorting.

```python
import aspose.cells as ac

# Create workbook
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Add sample data (Fruit/Year/Amount)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# Add pivot table at E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Add fields: Fruit→Row, Amount→Data, Year→Page
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# Page-field-specific operations
pivot_table.page_fields[0].current_page_item = 1  # 1 = second item in sorted order (e.g. "2021")

# Refresh and calculate pivot table
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Multi-Select Filtering**

Multi-select filtering turns the filter dropdown into a checkbox list and lets the end user pick several filter items simultaneously. Aspose.Cells exposes two properties that work together. `PivotField.is_multiple_item_selection_allowed` must be set to `True` before the multi-select UI takes effect at all. After it is enabled, `PivotItem.is_hidden` controls which items appear in the checkbox list, so you can either show every item or whitelist only specific items.

```python
import aspose.cells as ac

# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data, Year→Page via AddFieldToArea).
#   Below we apply multi-select filtering on the page field.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Sample data: Fruit | Year | Amount
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — Enable multi-select on the page field
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# Part A — select ALL items (make every item visible)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# Part B — select only specific items by source value
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **Note:** When using multi-select filtering through `PivotItem.is_hidden`, **at least one `PivotItem` must remain visible** (`is_hidden == False`). If every item is hidden, Excel either crashes when opening the file or renders a blank pivot. Always verify that your multi-select whitelist includes at least one item from your source data.

## **Which API and Which Mode Should I Use?**

The table below summarizes when to use each API and mode so you can pick the right combination without reading every scenario in detail.

| Scenario / Use Case | Recommended API | Property Used | Notes |
|---|---|---|---|
| Add a filter field by source-column name (most common) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | High-level, one-line. Use this unless you need a `PivotField` reference. |
| Add a filter field when you already have a `PivotField` object | `PivotTable.page_fields.add(PivotField)` | n/a | Use when the field object was obtained elsewhere or needs to be reused. |
| Filter to a single filter item (default mode) | `PivotField.current_page_item` | set to a specific index | For example, `1` shows the second item in the sorted list. |
| Show all items / clear the filter | `PivotField.current_page_item` | set to `0x7FFD` | The magic value `0x7FFD` (decimal 32765) is the sentinel for "all items". |
| Enable multi-select UI in Excel | `PivotField.is_multiple_item_selection_allowed` | set to `True` | Required before any `is_hidden` calls take effect. |
| Hide / show individual items in a multi-select list | `PivotItem.is_hidden` | set per item | At least one item must remain visible (`is_hidden == False`). |

{{% alert color="primary" %}}
Always remember the visibility constraint when configuring multi-select filtering. If every `PivotItem` in a multi-select filter field is hidden, Excel crashes on open or renders a blank pivot. Build your whitelist against your source data so at least one item stays visible, and your saved workbooks will open reliably on every machine.
{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}
