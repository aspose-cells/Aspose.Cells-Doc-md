---
title: Add Filter Fields to a Pivot Table in Aspose.Cells for .NET
description: Learn how to add and configure filter fields in pivot tables using Aspose.Cells for Python via Java, including adding filter fields, single-select filtering, and multi-select filtering.
keywords: Aspose.Cells, Python, Java, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /python-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonjava
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
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Set up the header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# Add a pivot table anchored at cell E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Refresh and calculate the pivot table data
pivotTable.calculateData()

# Save the workbook
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### Adding a Filter Field with page_fields.add

When you already work with a `PivotField` instance, you can pass it directly to `PivotTable.page_fields.add`. The pivot table and filter field are constructed exactly as in the previous scenario; only the final filter-area registration is replaced with the lower-level API call.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data). Below we obtain the Year PivotField from the
#   BaseFields collection and pass it to PageFields.Add — the
#   low-level alternative to AddFieldToArea. The result is
#   functionally identical to Scenario 1a.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Headers
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# Add pivot table at E3 covering A1:C10
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Low-level approach: grab the existing Year PivotField from BaseFields
# and register it in the Page area via PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Single-Select Filtering (Showing One Filter Item)**

In the default single-select behavior, the filter field renders as a single dropdown and the `PivotField.current_page_item` integer selects which filter item drives the pivot body. Assigning a specific index picks that one item; assigning the special sentinel `0x7FFD` (decimal 32765) clears the filter so every filter item is summarized at once. Single-select is the default; you do not need to enable it explicitly.

### Showing All Items

Setting `current_page_item` to the magic value `0x7FFD` is equivalent to clearing the filter: the pivot body summarizes every filter item as if no filter were applied.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Create a new workbook
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

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
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# Create pivot table at E3
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.calculateData()

# Clear the page filter so every item in the page field is visible.
# 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
# equivalent to selecting "(All)" in Excel's page-field dropdown.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Showing One Specific Item

Setting `current_page_item` to a real index picks just that one filter item. The index is the position of the item in the filter field's sorted item list, so for example `1` selects the second item after sorting.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Create workbook
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# Add pivot table at E3
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = second item in sorted order (e.g. "2021")

# Refresh and calculate pivot table
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Multi-Select Filtering**

Multi-select filtering turns the filter dropdown into a checkbox list and lets the end user pick several filter items simultaneously. Aspose.Cells exposes two properties that work together. `PivotField.is_multiple_item_selection_allowed` must be set to `True` before the multi-select UI takes effect at all. After it is enabled, `PivotItem.is_hidden` controls which items appear in the checkbox list, so you can either show every item or whitelist only specific items.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data, Year→Page via AddFieldToArea).
#   Below we apply multi-select filtering on the page field.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

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
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Part A — select ALL items (make every item visible)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Part B — select only specific items by source value
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **Note:** When using multi-select filtering through `PivotItem.is_hidden`, **at least one `PivotItem` must remain visible** (`is_hidden == False`). If every item is hidden, Excel either crashes when opening the file or renders a blank pivot. Always verify that your multi-select whitelist includes at least one item from your source data.

## **Which API and Which Mode Should I Use?**

The table below summarizes when to use each API and mode so you can pick the right combination without reading every scenario in detail.

| Scenario / Use Case | Recommended API | Property Used | Notes |
|---|---|---|---|
| Add a filter field by source-column name (most common) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/a | High-level, one-line. Use this unless you need a `PivotField` reference. |
| Add a filter field when you already have a `PivotField` object | `PivotTable.page_fields.add(PivotField)` | n/a | Use when the field object was obtained elsewhere or needs to be reused. |
| Filter to a single filter item (default mode) | `PivotField.current_page_item` | set to a specific index | For example, `1` shows the second item in the sorted list. |
| Show all items / clear the filter | `PivotField.current_page_item` | set to `0x7FFD` | The magic value `0x7FFD` (decimal 32765) is the sentinel for "all items". |
| Enable multi-select UI in Excel | `PivotField.is_multiple_item_selection_allowed` | set to `True` | Required before any `is_hidden` calls take effect. |
| Hide / show individual items in a multi-select list | `PivotItem.is_hidden` | set per item | At least one item must remain visible (`is_hidden == False`). |

{{% alert color="primary" %}}
Always remember the visibility constraint when configuring multi-select filtering. If every `PivotItem` in a multi-select filter field is hidden, Excel crashes on open or renders a blank pivot. Build your whitelist against your source data so at least one item stays visible, and your saved workbooks will open reliably on every machine.
{{% /alert %}}



{{< app/cells/assistant language="python" >}}
