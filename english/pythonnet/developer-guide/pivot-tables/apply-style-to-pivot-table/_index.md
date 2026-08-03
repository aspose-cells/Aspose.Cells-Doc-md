---
title: Apply Styles to Pivot Tables in Aspose.Cells for Python via .NET
linktitle: Apply Pivot Table Styles
description: Learn how to apply built-in and custom styles to pivot tables in Aspose.Cells for Python via .NET, covering legacy XLS autoformats, modern Excel 2007+ named styles, custom pivot table styles, and the FormatAll shortcut.
keywords: Aspose.Cells Python via .NET pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells supports applying both legacy pivot autoformats (intended for `.xls` files) and modern named or custom pivot table styles (intended for `.xlsx`, `.xlsm`, and `.xlsb` files). The API you should call depends on the file format the workbook is saved to, not the format it was loaded from.

{{% /alert %}}

## **Introduction**

Aspose.Cells exposes two parallel style APIs for pivot tables. The decision between them is driven by the file format you save the workbook to, not by the format you read it from. A workbook loaded from an `.xls` file can be re-saved as `.xlsx`, and in that case the modern style API applies rather than the legacy one.

For legacy `.xls` output, use the `PivotTable.auto_format_type` property together with the `aspose.cells.pivot.PivotTableAutoFormatType` enumeration. This API corresponds to the autoformat picker that classic Excel offered for pivot tables.

For modern `.xlsx`, `.xlsm`, and `.xlsb` output, two flavors of style API are available:

- `PivotTable.pivot_table_style_type` selects one of the built-in named styles (light and dark themes, including the styles added in Excel 2017). These presets are read-only.
- `PivotTable.pivot_table_style_name` selects a custom style you define yourself through `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Custom styles are required whenever you want to modify colors, borders, or fonts beyond what the presets offer.

In addition, `PivotTable.format_all(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot, overriding whatever is set through either of the style-name APIs above. This is useful when a uniform appearance is required regardless of the underlying theme.

## **Apply a Legacy XLS Preset Autoformat**

`PivotTable.auto_format_type` accepts a value from the `aspose.cells.pivot.PivotTableAutoFormatType` enumeration. The available values are `REPORT_1` through `REPORT_10`, `CLASSIC`, and `TABLE_1` through `TABLE_10`.

{{% alert color="primary" %}}

{{% /alert %}}

The following example loads a fresh workbook, populates the Fruit/Year/Amount sample data, adds a pivot table, applies `PivotTableAutoFormatType.REPORT_5`, and saves the result as `.xls`.

{{% alert color="primary" %}}

**Why no column fields?** Report-series autoformats (`Report1` through `Report10`, `Table1` through `Table10`) were designed in classic Excel for **single-dimension pivot tables** with row fields and values only — they have no built-in styling for column-field headers. If your pivot needs column fields, use the modern `PivotTableStyleType` presets from [Scenario 2](#apply-a-modern-named-preset-pivot-table-style) instead, which are designed for the two-dimensional layout modern Excel uses.

{{% /alert %}}
```python
import aspose.cells as ac

# Scenario 1: Apply a legacy XLS preset autoformat
# API in use: PivotTable.AutoFormatType
# Target file format: .xls (legacy)
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Create a new workbook
workbook = ac.Workbook()

# Get the first worksheet
sheet = workbook.worksheets[0]

# Populate the source data with header row (Fruit, Year, Amount)
# and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")

sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)

sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)

sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)

sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)

sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)

sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)

sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)

sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)

sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)

# Add a pivot table at destination cell E3, named "Pivot1", using source range A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# Assign fields: Fruit -> Rows, Amount -> Data
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Apply the legacy XLS preset autoformat "Report5"
# Note: This property is only meaningful when saving as .xls.
# When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
# and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# Save the workbook in legacy .xls format
workbook.save("output.xls")
```

## **Apply a Modern Named Preset Pivot Table Style**

This is the recommended API for any modern file format. Unlike the legacy autoformat, the style selected here is rendered faithfully by Excel and survives round-trips through other Office tooling.

## **Define and Apply a Custom Pivot Table Style**

The built-in presets cannot be modified. Whenever you need to override colors, borders, or fonts, you must define a custom pivot style. The workflow has three steps:

1. Add a custom style to the workbook's `table_styles` collection via `workbook.worksheets.table_styles.add_pivot_table_style(name)`. This returns the index of the newly created style.
2. Configure the style by adding elements (such as `WHOLE_TABLE` or `GRAND_TOTAL_ROW`) through `table_style.table_style_elements.add(TableStyleElementType)`, then assign a `Style` to each element via `table_style_element.set_element_style(Style)`.
3. Apply the custom style to the pivot by setting `PivotTable.pivot_table_style_name` to the style's name. Do not use `pivot_table_style_type` here, since that property selects built-in presets.

{{% alert color="primary" %}}

`pivot_table_style_name` and `pivot_table_style_type` are not interchangeable. Use `pivot_table_style_type` for built-in presets, and `pivot_table_style_name` for custom styles you have defined through `add_pivot_table_style`. Setting both is harmless, but only the one matching the intended source is rendered.

{{% /alert %}}

The available `TableStyleElementType` values include `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS`, and `PAGE_FIELD_VALUES`.

The following example defines a custom pivot style with a thin black border on `WHOLE_TABLE` and a bold red font on `GRAND_TOTAL_ROW`, then applies it via `pivot_table_style_name` and saves as `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Populate source data: header row + 9 data rows (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

# Add pivot table sourced from A1:C10, anchored at E3, named "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Step 1: register a new custom pivot table style and capture its index
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]

# Step 2: add a WholeTable element and apply thin black borders on all four sides
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)

# Step 3: add a GrandTotalRow element and apply bold red font
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **Apply One Style to Every Pivot Cell with FormatAll**

`PivotTable.format_all(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot table, including the data area, row and column headers, and totals. Whatever was previously set through `pivot_table_style_type` or `pivot_table_style_name` is overridden.

{{% alert color="primary" %}}

`format_all` overrides both `pivot_table_style_type` and `pivot_table_style_name`. Use it only when a uniform, theme-independent appearance is required across the entire pivot.

{{% /alert %}}

The following example creates a `Style` with a yellow solid fill, a bold dark-blue font, and thin black borders on all sides, then applies it with `format_all` and saves as `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# Scenario 4: Apply a single Style to every pivot table cell using FormatAll
# API in use: PivotTable.FormatAll(Style)
# Target format: .xlsx
# GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# Add pivot table: source range A1:C10, destination cell E3, name "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# Build a Style that will be forced onto every cell of the pivot table
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# Apply FormatAll: forces this single style onto every cell of the pivot table,
# overriding any PivotTableStyleType / PivotTableStyleName previously set
pivot_table.format_all(style)

# Save the workbook in the modern .xlsx format
workbook.save("output.xlsx")
```

## **Which Style API Should I Use?**

The choice of style API depends on the file format you are saving to. Use the table below as a quick reference.

| Target file format | API to use | Notes |
|---|---|---|
| `.xls` (legacy) | `PivotTable.auto_format_type` | Values from `aspose.cells.pivot.PivotTableAutoFormatType` (e.g. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignored when saving as modern formats. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, built-in style) | `PivotTable.pivot_table_style_type` | Values from `aspose.cells.PivotTableStyleType` (light/dark themes, including Excel 2017 additions). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, custom style) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Use when the built-in presets are not enough. Configure via `table_style_element.set_element_style(...)`. |
| Any format (uniform override) | `PivotTable.format_all(Style)` | Shortcut that overrides every other style setting across the entire pivot. |

When in doubt, save as `.xlsx` and use `pivot_table_style_type` for built-in themes, or `pivot_table_style_name` for custom themes.

{{< app/cells/assistant language="python-net" >}}
