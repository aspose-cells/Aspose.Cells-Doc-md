---
title: 在 Aspose.Cells for Python via Java 中为数据透视表应用样式
description: 了解如何在 Aspose.Cells for Python via Java 中为数据透视表应用内置和自定义样式，包括传统的 XLS 自动格式、现代的 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
linktitle: 应用数据透视表样式
keywords: Aspose.Cells Python via Java 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持同时应用传统的数据透视自动格式（用于 `.xls` 文件）以及现代的命名或自定义数据透视表样式（用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。您应该调用哪个 API 取决于工作簿保存到的文件格式，而不是它加载时的格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供了两个并行的样式 API。它们之间的选择取决于工作簿保存到的文件格式，而不是从中读取的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，在这种情况下，将应用现代样式 API，而不是传统的 API。
- `pivotTable.setPivotTableStyleType(int)` 用于选择内置的命名样式之一（浅色和深色主题，包括 Excel 2017 中新增的样式）。这些预设是只读的。
- `pivotTable.setPivotTableStyleName(String)` 用于选择您通过 `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)` 自行定义的自定义样式。当您希望修改预设提供的颜色、边框或字体时，必须使用自定义样式。
此外，`pivotTable.formatAll(Style)` 是一个快捷方式，可将单个 `Style` 对象应用于数据透视表的每个单元格，覆盖通过上述任一样式名称 API 设置的内容。当需要无论底层主题如何都呈现统一外观时，这非常有用。

## **应用传统的 XLS 预设自动格式**
数据透视表上的 `setAutoFormatType` 方法接受来自 `com.aspose.cells.pivot.PivotTableAutoFormatType` 枚举的值。可用值为 `REPORT_1` 到 `REPORT_10`、`CLASSIC`，以及 `TABLE_1` 到 `TABLE_10`。
以下示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.REPORT_5`，并将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为什么没有列字段？** Report 系列自动格式（`Report1` 到 `Report10`，`Table1` 到 `Table10`）是为经典 Excel 中的**单维数据透视表**（仅包含行字段和值）设计的——它们没有为列字段标头提供内置样式。如果您的数据透视表需要列字段，请改用 [方案 2](#apply-a-modern-named-preset-pivot-table-style) 中的现代 `PivotTableStyleType` 预设，这些预设是为现代 Excel 使用的二维布局而设计的。
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

## **应用现代命名预设数据透视表样式**

## **定义并应用自定义数据透视表样式**
无法修改内置预设。当您需要覆盖颜色、边框或字体时，必须定义自定义数据透视样式。该工作流包含三个步骤：
1. 通过 `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` 向工作簿的 `TableStyles` 集合添加自定义样式。这将返回新创建样式的索引。
2. 通过 `tableStyle.getTableStyleElements().add(TableStyleElementType)` 添加元素（例如 `WHOLE_TABLE` 或 `GRAND_TOTAL_ROW`）来配置样式，然后通过 `tableStyleElement.setElementStyle(Style)` 为每个元素分配 `Style`。
3. 通过使用样式的名称调用 `pivotTable.setPivotTableStyleName(String)` 将自定义样式应用于数据透视表。此处不要使用 `setPivotTableStyleType`，因为该方法选择的是内置预设。

{{% alert color="primary" %}}
`setPivotTableStyleName` 和 `setPivotTableStyleType` 不能互换使用。对于内置预设，请使用 `setPivotTableStyleType`；对于通过 `addPivotTableStyle` 定义的自定义样式，请使用 `setPivotTableStyleName`。同时设置两者是无害的，但只有与预期来源匹配的那个会被渲染。
{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS` 和 `PAGE_FIELD_VALUES`。
以下示例定义了一个自定义数据透视样式，在 `WHOLE_TABLE` 上使用细黑色边框，在 `GRAND_TOTAL_ROW` 上使用粗体红色字体，然后通过 `setPivotTableStyleName` 应用该样式并保存为 `.xlsx`。

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

## **使用 FormatAll 将一种样式应用于每个数据透视表单元格**
`pivotTable.formatAll(Style)` 是一个快捷方式，可将单个 `Style` 对象应用于数据透视表的每个单元格，包括数据区域、行和列标头以及总计。先前通过 `setPivotTableStyleType` 或 `setPivotTableStyleName` 设置的内容都将被覆盖。

{{% alert color="primary" %}}
`formatAll` 会覆盖 `setPivotTableStyleType` 和 `setPivotTableStyleName`。仅在整个数据透视表需要统一的、与主题无关的外观时才使用它。
{{% /alert %}}

以下示例创建一个 `Style`，具有黄色实心填充、粗体深蓝色字体以及四周的细黑色边框，然后使用 `formatAll` 应用该样式并保存为 `.xlsx`。

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

## **我应该使用哪个样式 API？**
样式 API 的选择取决于您要保存到的文件格式。请使用下表作为快速参考。
| 目标文件格式 | 使用的 API | 备注 |
|---|---|---|
| `.xls`（传统） | `pivotTable.setAutoFormatType(int)` | 取值来自 `com.aspose.cells.pivot.PivotTableAutoFormatType`（例如 `REPORT_1`–`REPORT_10`、`CLASSIC`、`TABLE_1`–`TABLE_10`）。保存为现代格式时将被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `pivotTable.setPivotTableStyleType(int)` | 取值来自 `com.aspose.cells.PivotTableStyleType`（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | 在内置预设不够用时使用。通过 `tableStyleElement.setElementStyle(Style)` 进行配置。 |
| 任何格式（统一覆盖） | `pivotTable.formatAll(Style)` | 快捷方式，可覆盖整个数据透视表上的所有其他样式设置。 |
如有疑问，请保存为 `.xlsx` 并使用 `setPivotTableStyleType` 应用内置主题，或使用 `setPivotTableStyleName` 应用自定义主题。

{{< app/cells/assistant language="python" >}}