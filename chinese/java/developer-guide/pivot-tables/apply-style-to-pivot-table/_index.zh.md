---
title: 在 Aspose.Cells for Java 中为数据透视表应用样式
linktitle: 应用数据透视表样式
description: 学习如何在 Aspose.Cells for Java 中为数据透视表应用内置和自定义样式，包括传统 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 formatAll 快捷方式。
keywords: Aspose.Cells Java 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持同时应用传统的数据透视表自动格式（适用于 `.xls` 文件）和现代命名或自定义数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。您应该调用的 API 取决于工作簿保存到的文件格式，而不是读取的格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供了两个并行的样式 API。它们之间的选择取决于工作簿保存到的文件格式，而不是读取的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，在这种情况下应用的是现代样式 API，而不是传统样式 API。
- `PivotTable.PivotTableStyleType` 从内置命名样式中选择一种（明色和暗色主题，包括 Excel 2017 中新增的样式）。这些预设是只读的。
- `PivotTable.PivotTableStyleName` 选择您通过 `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)` 自行定义的自定义样式。当您希望修改预设无法提供的颜色、边框或字体时，必须使用自定义样式。
此外，`PivotTable.formatAll(Style)` 是一个快捷方式，可将单个 `Style` 对象应用于数据透视表的每一个单元格，覆盖通过上述任一样式名称 API 设置的内容。当需要统一外观而不受底层主题影响时，此方法非常有用。

## **应用传统 XLS 预设自动格式**
`PivotTable.AutoFormatType` 接受来自 `com.aspose.cells.PivotTableAutoFormatType` 枚举的值。可用值为 `REPORT_1` 至 `REPORT_10`、`CLASSIC` 和 `TABLE_1` 至 `TABLE_10`。
下面的示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.REPORT_5`，并将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为什么没有列字段？** Report 系列自动格式（`Report1` 至 `Report10`、`Table1` 至 `Table10`）是在经典 Excel 中为**单维数据透视表**（仅包含行字段和值）设计的，它们没有针对列字段标题的内置样式。如果您的数据透视表需要列字段，请改用[场景 2](#apply-a-modern-named-preset-pivot-table-style) 中的现代 `PivotTableStyleType` 预设，这些预设为现代 Excel 使用的二维布局而设计。
{{% /alert %}}

```java
import com.aspose.cells.*;
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
Workbook workbook = new Workbook();
// Get the first worksheet
Worksheet sheet = workbook.getWorksheets().get(0);
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// Add a pivot table at destination cell E3, using source range A1:C10
PivotTable pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);
// Save the workbook in legacy .xls format
workbook.save("output.xls");
```

## **应用现代命名预设数据透视表样式**
`PivotTable.setPivotTableStyleType(int)` 用于选择 Excel 2007 为数据透视表引入的内置命名样式之一。`PivotTableStyleType` 枚举提供三个主题系列：从 `PIVOT_TABLE_STYLE_LIGHT1` 到 `PIVOT_TABLE_STYLE_LIGHT28` 的浅色系列、从 `PIVOT_TABLE_STYLE_MEDIUM1` 到 `PIVOT_TABLE_STYLE_MEDIUM28` 的中等色系列，以及从 `PIVOT_TABLE_STYLE_DARK1` 到 `PIVOT_TABLE_STYLE_DARK_28` 的深色系列。它还定义了 `None` 和 `Custom`。每个系列中编号较高的成员是 Excel 2017 中新增的样式。
这些预设样式为只读。一旦您需要更改预设样式未涵盖的颜色、边框或字体，就必须改为定义自定义数据透视表样式，如[方案 3](#define-and-apply-a-custom-pivot-table-style)中所示。

{{% alert color="primary" %}}
**为什么使用现代预设样式，而不采用报表系列自动格式？** `PivotTableAutoFormatType` 的 `Report1` 到 `Report10` 以及 `Table1` 到 `Table10` 值早于数据透视表列字段的出现，因此不包含任何列字段标题样式，Excel 会不应用任何样式来呈现这些标题。`PivotTableStyleType` 预设样式专为现代 Excel 使用的二维布局而设计，可同时为行字段和列字段标题应用样式。
{{% /alert %}}

此方案沿用方案 1 的 Fruit/Year/Amount 数据集，通过 `PivotFieldType.COLUMN` 将 `Year` 添加到列区域，与行字段 `Fruit` 并列；使用 `pivotTable.setPivotTableStyleType` 应用深色主题预设样式 `PIVOT_TABLE_STYLE_DARK1`；然后将结果保存为 `.xlsx`——这是 `PivotTableStyleType` 具有实际意义的文件格式。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);
// Add a pivot table at E3, sourced from A1:C10
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx - this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **定义并应用自定义数据透视表样式**
无法修改内置预设。当您需要覆盖颜色、边框或字体时，必须定义自定义数据透视样式。工作流包含三个步骤：
1. 通过 `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` 向工作簿的 `TableStyles` 集合添加自定义样式。这将返回新创建样式的索引。
2. 通过 `TableStyle.getTableStyleElements().add(TableStyleElementType)` 添加元素（例如 `WholeTable` 或 `GrandTotalRow`）来配置样式，然后通过 `TableStyleElement.setElementStyle(Style)` 为每个元素分配一个 `Style`。
3. 通过将 `PivotTable.PivotTableStyleName` 设置为样式名称，将自定义样式应用于数据透视表。此处不要使用 `PivotTableStyleType`，因为该属性用于选择内置预设。

{{% alert color="primary" %}}
`PivotTableStyleName` 和 `PivotTableStyleType` 不能互换使用。使用 `PivotTableStyleType` 选择内置预设，使用 `PivotTableStyleName` 选择通过 `addPivotTableStyle` 定义的自定义样式。同时设置两者不会产生错误，但只有与预期来源匹配的那一个会被渲染。
可用的 `TableStyleElementType` 值包括 `WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS` 和 `PAGE_FIELD_VALUES`。
下面的示例定义了一个自定义数据透视样式，其中 `WholeTable` 带有细黑色边框，`GrandTotalRow` 带有粗体红色字体，然后通过 `PivotTableStyleName` 应用它并保存为 `.xlsx`。
{{% /alert %}}

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row + 9 data rows (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// Add pivot table sourced from A1:C10, anchored at E3
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Step 1: register a new custom pivot table style and capture its index
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Step 2: add a WholeTable element and apply thin black borders on all four sides
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Step 3: add a GrandTotalRow element and apply bold red font
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **使用 formatAll 将单个样式应用于数据透视表的每个单元格**
`PivotTable.formatAll(Style)` 是一个快捷方式，可将单个 `Style` 对象应用于数据透视表的每一个单元格，包括数据区域、行和列标题以及总计。通过 `PivotTableStyleType` 或 `PivotTableStyleName` 之前设置的任何内容都会被覆盖。

{{% alert color="primary" %}}
`formatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅当需要在整个数据透视表中使用统一的、与主题无关的外观时才使用它。
下面的示例创建了一个具有黄色实心填充、粗体深蓝色字体以及所有边上细黑色边框的 `Style`，然后使用 `formatAll` 应用它并保存为 `.xlsx`。
{{% /alert %}}

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// Add pivot table: source range A1:C10, destination cell E3
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());
// Apply formatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.formatAll(style);
// Save the workbook in the modern .xlsx format
workbook.save("output.xlsx");
```

## **我应该使用哪个样式 API？**
样式 API 的选择取决于您要保存到的文件格式。请参考下表快速查询。
| 目标文件格式 | 要使用的 API | 备注 |
|---|---|---|
| `.xls`（传统） | `PivotTable.AutoFormatType` | 取值来自 `com.aspose.cells.PivotTableAutoFormatType`（例如 `REPORT_1`–`REPORT_10`、`CLASSIC`、`TABLE_1`–`TABLE_10`）。保存为现代格式时将被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `PivotTable.PivotTableStyleType` | 取值来自 `com.aspose.cells.PivotTableStyleType`（明色/暗色主题，包括 Excel 2017 新增内容）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | 当内置预设不够用时使用。通过 `TableStyleElement.setElementStyle(...)` 进行配置。 |
| 任何格式（统一覆盖） | `PivotTable.formatAll(Style)` | 快捷方式，覆盖整个数据透视表上的所有其他样式设置。 |
如有疑问，请保存为 `.xlsx` 并使用 `PivotTableStyleType` 选择内置主题，或使用 `PivotTableStyleName` 选择自定义主题。

{{< app/cells/assistant language="java" >}}