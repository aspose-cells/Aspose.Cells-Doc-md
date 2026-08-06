---
title: Modify Page Field Layout in Pivot Table
linktitle: Modify Page Field Layout in Pivot Table
description: Learn how to control the page field area layout in a pivot table using Aspose.Cells for Python via .NET, including setting the display order, wrap count, and field order of the page fields at the top of the pivot table.
keywords: Aspose.Cells, Python via .NET library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This article is a continuation of the **Add Page Field in Pivot Table** topic. It demonstrates how to control the layout of the page field area — the strip of filter controls at the top of a pivot table — including display order, wrap count, and field reordering.

{{% /alert %}}

## **Introduction**

A pivot table in Microsoft Excel exposes a dedicated **page field area** that sits above the row/column/data body of the table. This area is rendered as a strip of dropdown filter controls (one per page field) and is what end-users click to slice the pivot by criteria such as year or region. Aspose.Cells for Python via .NET models this area through the `pivot_table.page_fields` collection and exposes three properties that control how the strip is visually laid out:

- `pivot_table.page_field_order` (a `PrintOrderType` value) decides whether additional page fields are placed *next to* the existing ones or *below* them.
- `pivot_table.page_field_wrap_count` sets how many page fields are placed per row or column before wrapping.
- `pivot_table.page_fields.move(curr_index, dest_index)` reorders the page fields without changing the order mode.

This article walks through three code examples that demonstrate each of these operations on a shared dataset, so that you can compare the resulting layouts side-by-side.

## **Source Data**

All three examples below load these eight rows of sales data into a worksheet named `PivotData`. The data contains two page-field candidates (`Year`, `Region`), one row-field candidate (`Fruit`), and one measure (`Amount`), which makes the page-field strip meaningful to inspect.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

All eight rows are populated in every code example, in identical order, so the source data never differs between scenarios — only the page-field layout properties do.

## **Example 1: Over Then Down**

In the first scenario we configure the two page fields (`Year`, `Region`) to appear **side-by-side in a single row** at the top of the pivot table. We assign `Fruit` to the row axis, place `Year` first and `Region` second on the page axis (the order of `add_field_to_area` calls determines the starting index), add `Amount` (Sum) as the data field, and then set `page_field_order` to `PrintOrderType.OverThenDown` with `page_field_wrap_count = 2`. With `OverThenDown` and a wrap count of 2, the two page fields are laid out horizontally side-by-side in a single row at the top of the pivot table, so the strip occupies one row of width two.

```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# Headers (row 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# Row 1: Apple, 2022, North, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# Row 2: Apple, 2023, North, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# Row 3: Banana, 2022, South, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# Row 4: Banana, 2023, South, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# Row 5: Cherry, 2022, East, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# Row 6: Cherry, 2023, East, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# Row 7: Grape, 2022, West, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# Row 8: Grape, 2023, West, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# Add PivotTableReport sheet
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Add fields
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Year
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Amount
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# Configure page field area layout: place page fields across first, wrap after every 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# Refresh and calculate
pivot_table.calculate_data()

# Save
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```

## **Example 2: Down Then Over**

In this example we place `Fruit` on the row axis, `Year` and `Region` on the page axis (with `Year` first), and `Amount` (Sum) as the data field — exactly as in Example 1. We then set `page_field_order` to `PrintOrderType.DownThenOver` and `page_field_wrap_count` to `2`. With `DownThenOver` and a wrap count of 2, the two page fields are stacked vertically — `Year` on top, `Region` directly below — forming a single column at the top of the pivot table. The strip therefore occupies two rows of width one, in contrast to Example 1.

```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```

## **Example 3: Move a Page Field**

In the third scenario we keep this dataset and field allocation, set a neutral layout (`OverThenDown` with wrap count `2`), and then demonstrate the `page_fields.move` operation. The `move(0, 1)` call moves the page field at index 0 (`Year`) to position 1, and the page field that was at position 1 (`Region`) shifts to position 0. After this call, `Region` is the first page field and `Year` is the second. The wrap and order mode are unchanged, so the strip is still rendered horizontally side-by-side — only the order of the two dropdowns has been swapped.

```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```

## **Related Articles**

- [Add Page Field in Pivot Table](/cells/python-net/add-page-field-in-pivot-table/) — the parent page that introduces how page fields are added to a pivot table.
- [Row and Column Fields in Pivot Table](/cells/python-net/row-and-column-fields/) — covers allocating fields to the row and column axes, complementing the page-axis work shown here.
- [Manage Value Fields in Pivot Table](/cells/python-net/manage-value-fields/) — describes how to configure the data (value) area, including the `Sum` aggregation used in this article.
- [Refresh Pivot Table](/cells/python-net/refresh-pivot-table/) — explains `refresh_data` and `calculate_data`, which are required after reordering page fields.
- [Apply Style to Pivot Table](/cells/python-net/apply-style-to-pivot-table/) — shows how to format the rendered pivot table after the page-field strip has been laid out.

{{< app/cells/assistant language="python-net" >}}