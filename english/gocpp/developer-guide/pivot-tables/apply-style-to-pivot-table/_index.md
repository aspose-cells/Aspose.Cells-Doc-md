---
title: Apply Styles to Pivot Tables in Aspose.Cells for Go via C++
description: Learn how to apply built-in and custom styles to pivot tables in Aspose.Cells for Go via C++, covering legacy XLS autoformats, modern Excel 2007+ named styles, custom pivot table styles, and the FormatAll shortcut.
linktitle: Apply Pivot Table Styles
keywords: Aspose.Cells Go pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /go-cpp/apply-style-to-pivot-table/
---

{{% alert color="primary" %}}
Aspose.Cells supports applying both legacy pivot autoformats (intended for `.xls` files) and modern named or custom pivot table styles (intended for `.xlsx`, `.xlsm`, and `.xlsb` files). The API you should call depends on the file format the workbook is saved to, not the format it was loaded from.
{{% /alert %}}

## **Introduction**
Aspose.Cells exposes two parallel style APIs for pivot tables. The decision between them is driven by the file format you save the workbook to, not by the format you read it from. A workbook loaded from an `.xls` file can be re-saved as `.xlsx`, and in that case the modern style API applies rather than the legacy one.
- `PivotTable.PivotTableStyleType` selects one of the built-in named styles (light and dark themes, including the styles added in Excel 2017). These presets are read-only.
- `PivotTable.PivotTableStyleName` selects a custom style you define yourself through `Worksheets.TableStyles.AddPivotTableStyle(...)`. Custom styles are required whenever you want to modify colors, borders, or fonts beyond what the presets offer.
In addition, `PivotTable.FormatAll(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot, overriding whatever is set through either of the style-name APIs above. This is useful when a uniform appearance is required regardless of the underlying theme.

## **Apply a Legacy XLS Preset Autoformat**
`PivotTable.AutoFormatType` accepts a value from the `Aspose.Cells.Pivot.PivotTableAutoFormatType` enumeration. The available values are `Report1` through `Report10`, `Classic`, and `Table1` through `Table10`.
The following example loads a fresh workbook, populates the Fruit/Year/Amount sample data, adds a pivot table, applies `PivotTableAutoFormatType.Report5`, and saves the result as `.xls`.

{{% alert color="primary" %}}
**Why no column fields?** Report-series autoformats (`Report1` through `Report10`, `Table1` through `Table10`) were designed in classic Excel for **single-dimension pivot tables** with row fields and values only — they have no built-in styling for column-field headers. If your pivot needs column fields, use the modern `PivotTableStyleType` presets from [Scenario 2](#apply-a-modern-named-preset-pivot-table-style) instead, which are designed for the two-dimensional layout modern Excel uses.
{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyStyleToPivotTable.go" >}}

## **Apply a Modern Named Preset Pivot Table Style**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyStyleToPivotTable-1.go" >}}

## **Define and Apply a Custom Pivot Table Style**
The built-in presets cannot be modified. Whenever you need to override colors, borders, or fonts, you must define a custom pivot style. The workflow has three steps:
1. Add a custom style to the workbook's `TableStyles` collection via `Worksheets.TableStyles.AddPivotTableStyle(string name)`. This returns the index of the newly created style.
2. Configure the style by adding elements (such as `WholeTable` or `GrandTotalRow`) through `TableStyle.TableStyleElements.Add(TableStyleElementType)`, then assign a `Style` to each element via `TableStyleElement.SetElementStyle(Style)`.
3. Apply the custom style to the pivot by setting `PivotTable.PivotTableStyleName` to the style's name. Do not use `PivotTableStyleType` here, since that property selects built-in presets.

{{% alert color="primary" %}}
`PivotTableStyleName` and `PivotTableStyleType` are not interchangeable. Use `PivotTableStyleType` for built-in presets, and `PivotTableStyleName` for custom styles you have defined through `AddPivotTableStyle`. Setting both is harmless, but only the one matching the intended source is rendered.
{{% /alert %}}

The available `TableStyleElementType` values include `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels`, and `PageFieldValues`.
The following example defines a custom pivot style with a thin black border on `WholeTable` and a bold red font on `GrandTotalRow`, then applies it via `PivotTableStyleName` and saves as `.xlsx`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyStyleToPivotTable-2.go" >}}

## **Apply One Style to Every Pivot Cell with FormatAll**
`PivotTable.FormatAll(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot table, including the data area, row and column headers, and totals. Whatever was previously set through `PivotTableStyleType` or `PivotTableStyleName` is overridden.

{{% alert color="primary" %}}
`FormatAll` overrides both `PivotTableStyleType` and `PivotTableStyleName`. Use it only when a uniform, theme-independent appearance is required across the entire pivot.
{{% /alert %}}

The following example creates a `Style` with a yellow solid fill, a bold dark-blue font, and thin black borders on all sides, then applies it with `FormatAll` and saves as `.xlsx`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyStyleToPivotTable-3.go" >}}

## **Which Style API Should I Use?**
The choice of style API depends on the file format you are saving to. Use the table below as a quick reference.
| Target file format | API to use | Notes |
|---|---|---|
| `.xls` (legacy) | `PivotTable.AutoFormatType` | Values from `Aspose.Cells.Pivot.PivotTableAutoFormatType` (e.g. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignored when saving as modern formats. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, built-in style) | `PivotTable.PivotTableStyleType` | Values from `Aspose.Cells.PivotTableStyleType` (light/dark themes, including Excel 2017 additions). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, custom style) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Use when the built-in presets are not enough. Configure via `TableStyleElement.SetElementStyle(...)`. |
| Any format (uniform override) | `PivotTable.FormatAll(Style)` | Shortcut that overrides every other style setting across the entire pivot. |
When in doubt, save as `.xlsx` and use `PivotTableStyleType` for built-in themes, or `PivotTableStyleName` for custom themes.

{{< app/cells/assistant language="go" >}}