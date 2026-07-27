---
title: Apply Styles to Pivot Tables in Aspose.Cells for .NET
linktitle: Apply Pivot Table Styles
description: Learn how to apply built-in and custom styles to pivot tables in Aspose.Cells for Python via Java, covering legacy XLS autoformats, modern Excel 2007+ named styles, custom pivot table styles, and the FormatAll shortcut.
keywords: Aspose.Cells Python via Java pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells supports applying both legacy pivot autoformats (intended for `.xls` files) and modern named or custom pivot table styles (intended for `.xlsx`, `.xlsm`, and `.xlsb` files). The API you should call depends on the file format the workbook is saved to, not the format it was loaded from.

{{% /alert %}}

## **Introduction**

Aspose.Cells exposes two parallel style APIs for pivot tables. The decision between them is driven by the file format you save the workbook to, not by the format you read it from. A workbook loaded from an `.xls` file can be re-saved as `.xlsx`, and in that case the modern style API applies rather than the legacy one.

For legacy `.xls` output, use the `pivotTable.setAutoFormatType(int)` method together with the `com.aspose.cells.pivot.PivotTableAutoFormatType` enumeration. This API corresponds to the autoformat picker that classic Excel offered for pivot tables.

For modern `.xlsx`, `.xlsm`, and `.xlsb` output, two flavors of style API are available:

- `pivotTable.setPivotTableStyleType(int)` selects one of the built-in named styles (light and dark themes, including the styles added in Excel 2017). These presets are read-only.
- `pivotTable.setPivotTableStyleName(String)` selects a custom style you define yourself through `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Custom styles are required whenever you want to modify colors, borders, or fonts beyond what the presets offer.

In addition, `pivotTable.formatAll(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot, overriding whatever is set through either of the style-name APIs above. This is useful when a uniform appearance is required regardless of the underlying theme.

## **Apply a Legacy XLS Preset Autoformat**

The `setAutoFormatType` method on a pivot table accepts a value from the `com.aspose.cells.pivot.PivotTableAutoFormatType` enumeration. The available values are `REPORT_1` through `REPORT_10`, `CLASSIC`, and `TABLE_1` through `TABLE_10`.

{{% alert color="primary" %}}

{{% /alert %}}

The following example loads a fresh workbook, populates the Fruit/Year/Amount sample data, adds a pivot table, applies `PivotTableAutoFormatType.REPORT_5`, and saves the result as `.xls`.

{{% alert color="primary" %}}

**Why no column fields?** Report-series autoformats (`Report1` through `Report10`, `Table1` through `Table10`) were designed in classic Excel for **single-dimension pivot tables** with row fields and values only — they have no built-in styling for column-field headers. If your pivot needs column fields, use the modern `PivotTableStyleType` presets from [Scenario 2](#apply-a-modern-named-preset-pivot-table-style) instead, which are designed for the two-dimensional layout modern Excel uses.

{{% /alert %}}
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# Scenario 1: Apply a legacy XLS preset autoformat
# API in use: PivotTable.AutoFormatType
# Target file format: .xls (legacy)
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Create a new workbook
workbook = Workbook()

# Get the first worksheet
sheet = workbook.getWorksheets().get(0)

# Populate the source data with header row (Fruit, Year, Amount)
# and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")

sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)

sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)

sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)

sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)

sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)

sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)

sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)

sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)

sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)

# Add a pivot table at destination cell E3, named "Pivot1", using source range A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Apply the legacy XLS preset autoformat "Report5"
# Note: This property is only meaningful when saving as .xls.
# When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
# and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# Save the workbook in legacy .xls format
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **Apply a Modern Named Preset Pivot Table Style**

This is the recommended API for any modern file format. Unlike the legacy autoformat, the style selected here is rendered faithfully by Excel and survives round-trips through other Office tooling.

## **Define and Apply a Custom Pivot Table Style**

The built-in presets cannot be modified. Whenever you need to override colors, borders, or fonts, you must define a custom pivot style. The workflow has three steps:

1. Add a custom style to the workbook's `TableStyles` collection via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. This returns the index of the newly created style.
2. Configure the style by adding elements (such as `WHOLE_TABLE` or `GRAND_TOTAL_ROW`) through `tableStyle.getTableStyleElements().add(TableStyleElementType)`, then assign a `Style` to each element via `tableStyleElement.setElementStyle(Style)`.
3. Apply the custom style to the pivot by calling `pivotTable.setPivotTableStyleName(String)` with the style's name. Do not use `setPivotTableStyleType` here, since that method selects built-in presets.

{{% alert color="primary" %}}

`setPivotTableStyleName` and `setPivotTableStyleType` are not interchangeable. Use `setPivotTableStyleType` for built-in presets, and `setPivotTableStyleName` for custom styles you have defined through `addPivotTableStyle`. Setting both is harmless, but only the one matching the intended source is rendered.

{{% /alert %}}

The available `TableStyleElementType` values include `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS`, and `PAGE_FIELD_VALUES`.

The following example defines a custom pivot style with a thin black border on `WHOLE_TABLE` and a bold red font on `GRAND_TOTAL_ROW`, then applies it via `setPivotTableStyleName` and saves as `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Populate source data: header row + 9 data rows (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

# Add pivot table sourced from A1:C10, anchored at E3, named "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Step 1: register a new custom pivot table style and capture its index
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# Step 2: add a WholeTable element and apply thin black borders on all four sides
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# Step 3: add a GrandTotalRow element and apply bold red font
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Apply One Style to Every Pivot Cell with FormatAll**

`pivotTable.formatAll(Style)` is a shortcut that applies a single `Style` object to every cell of the pivot table, including the data area, row and column headers, and totals. Whatever was previously set through `setPivotTableStyleType` or `setPivotTableStyleName` is overridden.

{{% alert color="primary" %}}

`formatAll` overrides both `setPivotTableStyleType` and `setPivotTableStyleName`. Use it only when a uniform, theme-independent appearance is required across the entire pivot.

{{% /alert %}}

The following example creates a `Style` with a yellow solid fill, a bold dark-blue font, and thin black borders on all sides, then applies it with `formatAll` and saves as `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# Scenario 4: Apply a single Style to every pivot table cell using FormatAll
# API in use: PivotTable.FormatAll(Style)
# Target format: .xlsx
# GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)

# Add pivot table: source range A1:C10, destination cell E3, name "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Build a Style that will be forced onto every cell of the pivot table
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# Apply FormatAll: forces this single style onto every cell of the pivot table,
# overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.formatAll(style)

# Save the workbook in the modern .xlsx format
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Which Style API Should I Use?**

The choice of style API depends on the file format you are saving to. Use the table below as a quick reference.

| Target file format | API to use | Notes |
|---|---|---|
| `.xls` (legacy) | `pivotTable.setAutoFormatType(int)` | Values from `com.aspose.cells.pivot.PivotTableAutoFormatType` (e.g. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignored when saving as modern formats. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, built-in style) | `pivotTable.setPivotTableStyleType(int)` | Values from `com.aspose.cells.PivotTableStyleType` (light/dark themes, including Excel 2017 additions). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, custom style) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Use when the built-in presets are not enough. Configure via `tableStyleElement.setElementStyle(Style)`. |
| Any format (uniform override) | `pivotTable.formatAll(Style)` | Shortcut that overrides every other style setting across the entire pivot. |

When in doubt, save as `.xlsx` and use `setPivotTableStyleType` for built-in themes, or `setPivotTableStyleName` for custom themes.

{{< app/cells/assistant language="python" >}}
