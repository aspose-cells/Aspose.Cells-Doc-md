---
title: Applying Styles to Pivot Tables
description: Learn how to apply built-in and custom styles to pivot tables in Aspose.Cells for Node.js via Java, covering legacy XLS autoformats, modern Excel 2007+ named styles, custom pivot table styles, and the FormatAll shortcut.
keywords: Aspose.Cells Node.js via Java pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /nodejs-java/apply-style-to-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells supports applying both legacy pivot autoformats (intended for `.xls` files) and modern named or custom pivot table styles (intended for `.xlsx`, `.xlsm`, and `.xlsb` files). The API you should call depends on the file format the workbook is saved to, not the format it was loaded from.

{{% /alert %}}

## **Introduction**

Aspose.Cells exposes two parallel style APIs for pivot tables. The decision between them is driven by the file format you save the workbook to, not by the format you read it from. A workbook loaded from an `.xls` file can be re-saved as `.xlsx`, and in that case the modern style API applies rather than the legacy one.

For legacy `.xls` output, use the `PivotTable.autoFormatType` property together with the `Aspose.Cells.Pivot.PivotTableAutoFormatType` enumeration. This API corresponds to the autoformat picker that classic Excel offered for pivot tables.

For modern `.xlsx`, `.xlsm`, and `.xlsb` output, two flavors of style API are available:

- `PivotTable.pivotTableStyleType` selects one of the built-in named styles (light and dark themes, including the styles added in Excel 2017). These presets are read-only.
- `PivotTable.pivotTableStyleName` selects a custom style you define yourself through `Worksheets.getTableStyles().addPivotTableStyle(...)`. Custom styles are required whenever you want to modify colors, borders, or fonts beyond what the presets offer.

In addition, `PivotTable.formatAll(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot, overriding whatever is set through either of the style-name APIs above. This is useful when a uniform appearance is required regardless of the underlying theme.

## **Apply a Legacy XLS Preset Autoformat**

`PivotTable.autoFormatType` accepts a value from the `Aspose.Cells.Pivot.PivotTableAutoFormatType` enumeration. The available values are `Report1` through `Report10`, `Classic`, and `Table1` through `Table10`.

{{% alert color="primary" %}}

`autoFormatType` is only honored when the workbook is saved as `.xls`. When the same workbook is saved as `.xlsx`, `.xlsm`, or `.xlsb`, Excel ignores this property and falls back to the `pivotTableStyleType` and `pivotTableStyleName` settings.

{{% /alert %}}

The following example loads a fresh workbook, populates the Fruit/Year/Amount sample data, adds a pivot table, applies `PivotTableAutoFormatType.Report5`, and saves the result as `.xls`.

<!-- CODE_BLOCK:0:Apply a legacy XLS preset autoformat using pivotTable.autoFormatType = PivotTableAutoFormatType.Report5, then save as .xls. The code creates a new Workbook, populates cells A1:C10 with a header row (Fruit, Year, Amount) plus 9 data rows containing grape/blueberry/kiwi/cherry across years 2020 and 2021 with sample amounts, adds a pivot table at E3 named "Pivot1" with source "A1:C10", assigns Fruit to the Row area, Year to the Column area, Amount to the Data area, sets pivotTable.autoFormatType = PivotTableAutoFormatType.Report5, and saves the workbook as output.xls. The code must begin with the required import statements (var aspose = aspose || {}; ... or const cells = require("aspose.cells");) followed by a leading comment indicating the scenario, the API in use, and the target format, plus the GitHub reference comment line "For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Node.js-via-Java". -->

## **Apply a Modern Named Preset Pivot Table Style**

`PivotTable.pivotTableStyleType` accepts a value from the `Aspose.Cells.PivotTableStyleType` enumeration. The enumeration covers light themes `PivotTableStyleLight1` through `PivotTableStyleLight28` and dark themes `PivotTableStyleDark1` through `PivotTableStyleDark28`. The styles added in Excel 2017 (the second wave of light and dark themes) are reachable through the same enumeration.

This is the recommended API for any modern file format. Unlike the legacy autoformat, the style selected here is rendered faithfully by Excel and survives round-trips through other Office tooling.

The following example uses the same Fruit/Year/Amount data, creates an identical pivot table, applies `PivotTableStyleDark1`, and saves the workbook as `.xlsx`.

<!-- CODE_BLOCK:1:Apply a modern Excel 2007+ named preset style using pivotTable.pivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1, then save as .xlsx. The code creates a new Workbook, populates cells A1:C10 with the identical Fruit/Year/Amount sample data (header row plus 9 data rows), adds a pivot table at E3 named "Pivot1" with source "A1:C10", assigns Fruit to the Row area, Year to the Column area, Amount to the Data area, sets pivotTable.pivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1 (note this enum is in the Aspose.Cells namespace, not Aspose.Cells.Pivot), and saves the workbook as output.xlsx. The code must begin with the required import statements followed by a leading comment indicating the scenario, the API in use, and the target format, plus the GitHub reference comment line. -->

## **Define and Apply a Custom Pivot Table Style**

The built-in presets cannot be modified. Whenever you need to override colors, borders, or fonts, you must define a custom pivot style. The workflow has three steps:

1. Add a custom style to the workbook's `TableStyles` collection via `Worksheets.getTableStyles().addPivotTableStyle(String name)`. This returns the index of the newly created style.
2. Configure the style by adding elements (such as `WholeTable` or `GrandTotalRow`) through `TableStyle.tableStyleElements.add(TableStyleElementType)`, then assign a `Style` to each element via `TableStyleElement.setElementStyle(Style)`.
3. Apply the custom style to the pivot by setting `PivotTable.pivotTableStyleName` to the style's name. Do not use `pivotTableStyleType` here, since that property selects built-in presets.

{{% alert color="primary" %}}

`pivotTableStyleName` and `pivotTableStyleType` are not interchangeable. Use `pivotTableStyleType` for built-in presets, and `pivotTableStyleName` for custom styles you have defined through `addPivotTableStyle`. Setting both is harmless, but only the one matching the intended source is rendered.

{{% /alert %}}

The available `TableStyleElementType` values include `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels`, and `PageFieldValues`.

The following example defines a custom pivot style with a thin black border on `WholeTable` and a bold red font on `GrandTotalRow`, then applies it via `pivotTableStyleName` and saves as `.xlsx`.

<!-- CODE_BLOCK:2:Define a custom pivot table style with addPivotTableStyle, add WholeTable and GrandTotalRow elements with setElementStyle, apply via pivotTableStyleName, then save as .xlsx. The code creates a new Workbook, populates cells A1:C10 with the Fruit/Year/Amount sample data (header row plus 9 data rows), adds a pivot table at E3 named "Pivot1" with source "A1:C10", assigns Fruit to the Row area, Year to the Column area, Amount to the Data area. It then calls workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle") to add a custom style and captures the returned index. It retrieves the TableStyle from workbook.getWorksheets().getTableStyles().get(styleIndex), adds a WholeTable element via tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE) and captures its index, creates a Style via workbook.createStyle(), configures thin black borders on all four sides (Top, Bottom, Left, Right) using style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(com.aspose.cells.Color.getBlack()) and CellBorderType.THIN for each, and calls setElementStyle(style) on the WholeTable element. It then adds a GrandTotalRow element similarly, creates another Style, sets style.getFont().setBold(true) and style.getFont().setColor(com.aspose.cells.Color.getRed()), and calls setElementStyle(style) on the GrandTotalRow element. Finally it sets pivotTable.setPivotTableStyleName("CustomPivotStyle") (not pivotTableStyleType) and saves the workbook as output.xlsx. The code must begin with the required import statements followed by a leading comment indicating the scenario, the API in use, and the target format, plus the GitHub reference comment line. -->

## **Apply One Style to Every Pivot Cell with FormatAll**

`PivotTable.formatAll(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot table, including the data area, row and column headers, and totals. Whatever was previously set through `pivotTableStyleType` or `pivotTableStyleName` is overridden.

{{% alert color="primary" %}}

`formatAll` overrides both `pivotTableStyleType` and `pivotTableStyleName`. Use it only when a uniform, theme-independent appearance is required across the entire pivot.

{{% /alert %}}

The following example creates a `Style` with a yellow solid fill, a bold dark-blue font, and thin black borders on all sides, then applies it with `formatAll` and saves as `.xlsx`.

<!-- CODE_BLOCK:3:Apply a single Style to every pivot table cell using pivotTable.formatAll, then save as .xlsx. The code creates a new Workbook, populates cells A1:C10 with the Fruit/Year/Amount sample data (header row plus 9 data rows), adds a pivot table at E3 named "Pivot1" with source "A1:C10", assigns Fruit to the Row area, Year to the Column area, Amount to the Data area. It then creates a Style via workbook.createStyle(), configures a yellow solid fill via style.setForegroundColor(com.aspose.cells.Color.getYellow()) and style.setPattern(BackgroundType.SOLID), sets a bold dark-blue font via style.getFont().setBold(true) and style.getFont().setColor(com.aspose.cells.Color.getDarkBlue()), and adds thin black borders on all four sides (Top, Bottom, Left, Right) using CellBorderType.THIN. It then calls pivotTable.formatAll(style) to override any prior style settings, and saves the workbook as output.xlsx. The code must begin with the required import statements followed by a leading comment indicating the scenario, the API in use, and the target format, plus the GitHub reference comment line. -->

## **Which Style API Should I Use?**

The choice of style API depends on the file format you are saving to. Use the table below as a quick reference.

| Target file format | API to use | Notes |
|---|---|---|
| `.xls` (legacy) | `PivotTable.autoFormatType` | Values from `Aspose.Cells.Pivot.PivotTableAutoFormatType` (e.g. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignored when saving as modern formats. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, built-in style) | `PivotTable.pivotTableStyleType` | Values from `Aspose.Cells.PivotTableStyleType` (light/dark themes, including Excel 2017 additions). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, custom style) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Use when the built-in presets are not enough. Configure via `TableStyleElement.setElementStyle(...)`. |
| Any format (uniform override) | `PivotTable.formatAll(Style)` | Shortcut that overrides every other style setting across the entire pivot. |

When in doubt, save as `.xlsx` and use `pivotTableStyleType` for built-in themes, or `pivotTableStyleName` for custom themes.

## **Related Articles**

- [Refreshing Pivot Tables in Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="javascript" >}}