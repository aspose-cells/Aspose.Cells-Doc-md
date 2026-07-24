---
title: Applying Styles to Pivot Tables
description: Learn how to apply built-in and custom styles to pivot tables in Aspose.Cells for Python via .NET, covering legacy XLS autoformats, modern Excel 2007+ named styles, custom pivot table styles, and the FormatAll shortcut.
keywords: Aspose.Cells Python via .NET pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /python-net/apply-style-to-pivot-table/
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

`auto_format_type` is only honored when the workbook is saved as `.xls`. When the same workbook is saved as `.xlsx`, `.xlsm`, or `.xlsb`, Excel ignores this property and falls back to the `pivot_table_style_type` and `pivot_table_style_name` settings.

{{% /alert %}}

The following example loads a fresh workbook, populates the Fruit/Year/Amount sample data, adds a pivot table, applies `PivotTableAutoFormatType.REPORT_5`, and saves the result as `.xls`.

<!-- CODE_BLOCK:0:Apply a legacy XLS preset autoformat using pivot_table.auto_format_type = PivotTableAutoFormatType.REPORT_5, then save as .xls. The code imports aspose.cells and aspose.cells.pivot, creates a new Workbook, populates cells A1:C10 with a header row (Fruit, Year, Amount) plus 9 data rows containing grape/blueberry/kiwi/cherry across years 2020 and 2021 with sample amounts, adds a pivot table at E3 named "Pivot1" with source "A1:C10", assigns Fruit to the Row area, Year to the Column area, Amount to the Data area, sets pivot_table.auto_format_type = PivotTableAutoFormatType.REPORT_5, and saves the workbook as output.xls. The code must begin with the required import statements (import aspose.cells, import aspose.cells.pivot) followed by a leading comment indicating the scenario, the API in use, and the target format, plus the GitHub reference comment line "For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET". -->

## **Apply a Modern Named Preset Pivot Table Style**

`PivotTable.pivot_table_style_type` accepts a value from the `aspose.cells.PivotTableStyleType` enumeration. The enumeration covers light themes `PIVOT_TABLE_STYLE_LIGHT_1` through `PIVOT_TABLE_STYLE_LIGHT_28` and dark themes `PIVOT_TABLE_STYLE_DARK_1` through `PIVOT_TABLE_STYLE_DARK_28`. The styles added in Excel 2017 (the second wave of light and dark themes) are reachable through the same enumeration.

This is the recommended API for any modern file format. Unlike the legacy autoformat, the style selected here is rendered faithfully by Excel and survives round-trips through other Office tooling.

The following example uses the same Fruit/Year/Amount data, creates an identical pivot table, applies `PIVOT_TABLE_STYLE_DARK_1`, and saves the workbook as `.xlsx`.

<!-- CODE_BLOCK:1:Apply a modern Excel 2007+ named preset style using pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1, then save as .xlsx. The code imports aspose.cells, creates a new Workbook, populates cells A1:C10 with the identical Fruit/Year/Amount sample data (header row plus 9 data rows), adds a pivot table at E3 named "Pivot1" with source "A1:C10", assigns Fruit to the Row area, Year to the Column area, Amount to the Data area, sets pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1 (note this enum is in the aspose.cells namespace, not aspose.cells.pivot), and saves the workbook as output.xlsx. The code must begin with the required import statements followed by a leading comment indicating the scenario, the API in use, and the target format, plus the GitHub reference comment line. -->

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

<!-- CODE_BLOCK:2:Define a custom pivot table style with add_pivot_table_style, add WholeTable and GrandTotalRow elements with set_element_style, apply via pivot_table_style_name, then save as .xlsx. The code imports aspose.cells, creates a new Workbook, populates cells A1:C10 with the Fruit/Year/Amount sample data (header row plus 9 data rows), adds a pivot table at E3 named "Pivot1" with source "A1:C10", assigns Fruit to the Row area, Year to the Column area, Amount to the Data area. It then calls workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle") to add a custom style and captures the returned index. It retrieves the TableStyle from workbook.worksheets.table_styles[style_index], adds a WholeTable element via table_style.table_style_elements.add(TableStyleElementType.WHOLE_TABLE) and captures its index, creates a Style via workbook.create_style(), configures thin black borders on all four sides (Top, Bottom, Left, Right) using style.borders[BorderType.TOP_BORDER].color = Color.BLACK and CellBorderType.THIN for each, and calls set_element_style(style) on the WholeTable element. It then adds a GrandTotalRow element similarly, creates another Style, sets style.font.is_bold = True and style.font.color = Color.RED, and calls set_element_style(style) on the GrandTotalRow element. Finally it sets pivot_table.pivot_table_style_name = "CustomPivotStyle" (not pivot_table_style_type) and saves the workbook as output.xlsx. The code must begin with the required import statements followed by a leading comment indicating the scenario, the API in use, and the target format, plus the GitHub reference comment line. -->

## **Apply One Style to Every Pivot Cell with FormatAll**

`PivotTable.format_all(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot table, including the data area, row and column headers, and totals. Whatever was previously set through `pivot_table_style_type` or `pivot_table_style_name` is overridden.

{{% alert color="primary" %}}

`format_all` overrides both `pivot_table_style_type` and `pivot_table_style_name`. Use it only when a uniform, theme-independent appearance is required across the entire pivot.

{{% /alert %}}

The following example creates a `Style` with a yellow solid fill, a bold dark-blue font, and thin black borders on all sides, then applies it with `format_all` and saves as `.xlsx`.

<!-- CODE_BLOCK:3:Apply a single Style to every pivot table cell using pivot_table.format_all, then save as .xlsx. The code imports aspose.cells, creates a new Workbook, populates cells A1:C10 with the Fruit/Year/Amount sample data (header row plus 9 data rows), adds a pivot table at E3 named "Pivot1" with source "A1:C10", assigns Fruit to the Row area, Year to the Column area, Amount to the Data area. It then creates a Style via workbook.create_style(), configures a yellow solid fill via style.foreground_color = Color.YELLOW and style.pattern = BackgroundType.SOLID, sets a bold dark-blue font via style.font.is_bold = True and style.font.color = Color.DARK_BLUE, and adds thin black borders on all four sides (Top, Bottom, Left, Right) using CellBorderType.THIN. It then calls pivot_table.format_all(style) to override any prior style settings, and saves the workbook as output.xlsx. The code must begin with the required import statements followed by a leading comment indicating the scenario, the API in use, and the target format, plus the GitHub reference comment line. -->

## **Which Style API Should I Use?**

The choice of style API depends on the file format you are saving to. Use the table below as a quick reference.

| Target file format | API to use | Notes |
|---|---|---|
| `.xls` (legacy) | `PivotTable.auto_format_type` | Values from `aspose.cells.pivot.PivotTableAutoFormatType` (e.g. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignored when saving as modern formats. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, built-in style) | `PivotTable.pivot_table_style_type` | Values from `aspose.cells.PivotTableStyleType` (light/dark themes, including Excel 2017 additions). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, custom style) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Use when the built-in presets are not enough. Configure via `table_style_element.set_element_style(...)`. |
| Any format (uniform override) | `PivotTable.format_all(Style)` | Shortcut that overrides every other style setting across the entire pivot. |

When in doubt, save as `.xlsx` and use `pivot_table_style_type` for built-in themes, or `pivot_table_style_name` for custom themes.

## **Related Articles**

- [Refreshing Pivot Tables in Aspose.Cells for Python via .NET](/cells/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}