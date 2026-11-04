---
title: Format Part of a Pivot Table
description: Format part of a pivot table in Aspose.Cells for Python via .NET by applying styles to semantic PivotArea regions or CellArea rectangles through PivotTable.format, with formats stored in PivotTable.pivot_formats and preserved when the pivot table is refreshed.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Python via .NET, pivot table, format, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
`PivotTable.format_all` applies a single style to the entire pivot table and is covered on the parent page. It does not distinguish between labels, values, totals, or particular regions of the report.
In practice, only a portion of a pivot table usually needs to stand out. Common targets include the labels belonging to one row field, the value cells produced by one field, the grand-total row, or an arbitrary rectangle such as the first two item rows.
Applying a style directly to the worksheet cells of a pivot table is not equivalent. Excel stores pivot-table formatting as semantic `PivotArea` regions rather than as ordinary cell-style records. A pivot-area format stays attached to a region such as a field's labels or data values, and it is re-resolved when the pivot table is recalculated, refreshed, or expanded. A style written directly to a cell, on the other hand, belongs to that cell position and is not tracked by the pivot model.
Aspose.Cells exposes the complete `PivotTable.format` overload family so that both kinds of formatting are available:
- `format(PivotArea, Style)` anchors a style to a semantic region that is built with `PivotArea.select` or `PivotArea.select_field`.
- `format(CellArea, Style)` anchors a style to a worksheet rectangle inside the pivot table.
- `format(int row, int column, Style)` targets one cell.
- `format_all(Style)` formats the whole pivot table.

## **Format a Pivot Area**
The semantic-area workflow is the recommended approach when a highlight must follow a field or a region of the report.
1. Create a `PivotArea` with `PivotArea(pivot_table)`. The object describes a semantic region that belongs to that specific pivot table.
1. Select a field by its zero-based position on a given axis with `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` selects both the labels and the data of the field.
   - `PivotTableSelectionType.LABEL_ONLY` selects only the field's labels.
   - `PivotTableSelectionType.DATA_ONLY` selects only the field's data cells.
1. Select a field by name with `PivotArea.select_field(PivotFieldType axis_type, string field_name)`. When a row field is selected by name, the region resolves to the value cells produced by that field's items.
1. Create a `Style` with `Workbook.create_style()`, configure its font, foreground color, and solid background pattern, and pass the style to `PivotTable.format(area, style)`.
1. Each call to the `PivotArea` overload appends one `PivotTableFormat` entry to `PivotTable.pivot_formats`.
1. Field-anchored formats are painted when the pivot data is calculated. Therefore, call `PivotTable.calculate_data()` after applying the formats so that the styles become visible.
The following example builds a small fruit-sales pivot table, styles the `Fruit` row labels with `PivotArea.select` and `PivotTableSelectionType.LABEL_ONLY`, styles the value cells produced by that same row field with `PivotArea.select_field`, and then recalculates the pivot table so both styles are painted.

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **Format a Cell Area of the Pivot Table**
Use `PivotTable.format(CellArea, Style)` when the region of interest is a plain worksheet rectangle rather than a semantic pivot region.
A `CellArea` is described by the `start_row`, `start_column`, `end_row`, and `end_column` properties. The values are zero-based worksheet coordinates, and the end coordinates identify the last row and column that are included in the rectangle, so the area covers the cells from the start position through the end position inclusive.
Unlike a field-anchored format, a `CellArea` format is applied to the cells immediately. Another call to `calculate_data()` is not needed for the style to appear.
A `CellArea` rectangle may contain label cells and value cells together. The next section describes how Aspose.Cells and Excel represent that rectangle internally.
The following example formats the rectangle `E4:F5` of the pivot table with an italic, light-blue style and saves the workbook without any further recalculation.

```python
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **How Pivot Areas and Cell Areas Map**
Excel stores pivot-table formatting as `pivotArea` records rather than as ordinary worksheet cell-style records. The same model is used by Aspose.Cells, so a formatting request is translated into pivot areas when it is recorded.
The relationship between the `CellArea` supplied by the user and the pivot areas stored internally is many-to-many in both directions.
- One `CellArea` may produce several pivot areas. If the rectangle spans both label cells and value cells, it is decomposed into separate label and data rules, because the pivot model treats label formatting and data formatting independently.
- One pivot area may resolve to several disjoint `CellArea` instances. A semantic region such as a grand-total row, or a field whose items are not contiguous, can cover multiple rectangles. This is why `PivotArea.get_cell_areas()` returns a collection instead of a single rectangle.
Every format operation performed through `PivotTable.format` is recorded in `PivotTable.pivot_formats`. Each `PivotTableFormat` entry exposes the associated `PivotArea` and the `Style` that is applied to it. The `PivotArea` overload adds exactly one entry per call, while a `CellArea` that contains different semantic regions can add multiple entries.
To distinguish the stored regions, each `PivotArea` exposes the `only_label` and `only_data` flags. The example below formats a single rectangle that covers both labels and values, inspects `PivotTable.pivot_formats`, and prints the `CellArea` coordinates that each stored pivot area resolves to.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
Because the formats are stored as pivot areas rather than as ordinary cell styles, they survive recalculation and refresh. When the pivot table is refreshed with `PivotTable.refresh_data`, recalculated with `calculate_data`, or saved and reloaded, every stored pivot area re-resolves to the current position of its region and its style is re-applied.
{{% /alert %}}

Use a `PivotArea` built with `select` or `select_field` when a highlight must remain attached to a field or a semantic region across refreshes, and use a `CellArea` when formatting a fixed rectangle in the current pivot-table layout is sufficient. The single-cell `format(int row, int column, Style)` overload targets an individual cell. Use `format_all`, covered on the parent page, when the entire pivot table should be restyled at once.

## **Related Articles**
- [Applying Style to Pivot Table](/cells/python-net/apply-style-to-pivot-table/)
- [Adding Pivot Table Row and Column Fields](/cells/python-net/pivot-table-add-row-and-column-fields/)
- [Managing Value Fields in Pivot Table](/cells/python-net/manage-value-fields/)
- [Refreshing Pivot Table](/cells/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}