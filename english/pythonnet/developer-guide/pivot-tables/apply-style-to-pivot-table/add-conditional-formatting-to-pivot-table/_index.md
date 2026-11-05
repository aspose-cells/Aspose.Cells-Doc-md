---
title: Add Conditional Formatting to a Pivot Table
description: Add conditional formatting to a pivot table in Aspose.Cells for Python via .NET - anchor a rule to the data region with apply_to and a PivotConditionFormatScopeType scope, or define the target with add_cell_area and pivot_areas, then attach rules and styles through format_conditions.add_condition.
linktitle: Add Conditional Formatting to a Pivot Table
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, pivot table, conditional formatting, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
The styles described on the parent page and on the sibling page are static - a `PivotArea` or `CellArea` region is painted once and keeps its style no matter what the values are. Conditional formatting is the rule-driven counterpart - highlight every amount above 200, shade the middle fifty percent, or flag the bottom-ranked items - and the highlight follows the values whenever the pivot table is recalculated or refreshed.
In Aspose.Cells, pivot-table conditional formatting lives in the `pivot_table.conditional_formats` collection. Each entry is a `PivotConditionalFormat` that answers two questions independently:
- **Where does the rule apply?** The target region is defined either through `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)`, which mirrors the scope picker of the Excel user interface, or through `add_cell_area(cell_area: CellArea)` and the `pivot_areas` collection, which name the region explicitly.
- **What does the rule test?** One or more conditions are added to `format_conditions` with `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)`, and each condition carries its own `style`.

{{% alert color="primary" %}}
Do not call `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` or `format_conditions.add_area(cell_area: CellArea)` on the `format_conditions` object of a pivot conditional format. These two overloads are inherited from the ordinary worksheet conditional-formatting API and do not work for pivot tables - the cell area is never converted to a pivot area, so the request is silently ignored. Always define the region on the `pivot_conditional_format` itself (`apply_to`, `add_cell_area`, or `pivot_areas`) and add the rule with one of the `add_condition` overloads.
{{% /alert %}}

## **Apply a Rule with a Scope (the Excel UI Way)**
The first way positions the rule the way the Excel user interface does. A cell of the pivot table is named by its zero-based worksheet coordinates, and a `PivotConditionFormatScopeType` scope tells Aspose.Cells how far the rule should reach from that cell:
- `PivotConditionFormatScopeType.DATA` - all value cells that the pivot table produces, including grand totals.
- `PivotConditionFormatScopeType.FIELD` - the value cells that belong to the field the cell identifies, excluding grand totals. The cell must be a field cell such as a row-field label; passing a value cell throws an exception.
- `PivotConditionFormatScopeType.SELECTION` - only the value cells at the intersection that the cell selects, typically a single value cell.
The example below builds a fruit-sales pivot table whose top-left corner is at E3, anchors a conditional format at cell F4 (row 3, column 5) with the `PivotConditionFormatScopeType.DATA` scope, and highlights every amount greater than 200 in bold white on red. With the values Apple 220, Banana 330, Cherry 200, and the grand total 750, the rule paints F4, F5, and F7 - the resolved region is the whole data column F4:F7, and only the cells whose value passes the rule light up.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

Anchoring the same rule at the row-field label E4 (row 3, column 4) with the `PivotConditionFormatScopeType.FIELD` scope resolves to F4:F6 instead - the same data column without the grand-total row - because the scope now describes the `Fruit` field rather than the whole values area. The `PivotConditionFormatScopeType.SELECTION` scope anchored at F4 resolves to F4 alone.

## **Define the Region Manually**
The second way skips the scope picker and names the region explicitly on the `PivotConditionalFormat`.

### **A worksheet rectangle with add_cell_area**
`add_cell_area(cell_area: CellArea)` records the given rectangle as the target of the rule. The coordinates are zero-based worksheet coordinates, and the region is exactly the rectangle supplied - no expansion to the data column and no grand-total logic. Use it when the interesting cells are a known fixed rectangle of the current pivot layout.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
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
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **A semantic pivot region with pivot_areas**
`pivot_areas` is the same semantic-region model that the sibling page uses for static styles. Build a `PivotArea`, select a field or region with `select` or `select_field`, and add it with `pivot_areas.add_pivot_area(pivot_area)`. A semantic region stays attached to its field, so the conditional format follows the field when the pivot table is refreshed and the layout shifts. The `pivot_areas.add(pivot_area)` overload still compiles but is marked obsolete - prefer `add_pivot_area`.

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
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Rule - grey text for amounts below 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **Where the Rules Are Stored and How They Survive a Reload**
Every `pivot_table.conditional_formats.add()` call appends one `PivotConditionalFormat` to the pivot table. The conditions, their formulas, and their styles are saved with the workbook - reopening the file in the example below shows the same rule with its type, operator, and formula intact, and `get_cell_areas()` reports the same regions. Entries that never received a condition are dropped when the workbook is saved, the same way Excel discards a conditional format that has no rule.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Related Articles**
- [Applying Style to Pivot Table](/cells/python-net/apply-style-to-pivot-table/)
- [Format Part of a Pivot Table](/cells/python-net/format-part-of-pivot-table/)
- [Top 10 Show or Filter in Pivot Table](/cells/python-net/top-10-show-or-filter-in-pivot-table/)
- [Filtering Pivot Tables by Label or Value](/cells/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}