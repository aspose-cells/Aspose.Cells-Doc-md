---
title: 在 Aspose.Cells for Node.js via Java 中为数据透视表应用样式
linktitle: 在 Aspose.Cells for Node.js via Java 中为数据透视表应用样式
description: 了解如何在 Aspose.Cells for Node.js via Java 中为数据透视表应用内置和自定义样式,涵盖传统 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 formatAll 快捷方式。
keywords: Aspose.Cells Node.js via Java 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持同时应用传统的数据透视表自动格式(用于 `.xls` 文件)和现代的命名或自定义数据透视表样式(用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件)。应调用的 API 取决于工作簿保存到的文件格式,而非加载时的格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供两套并行的样式 API。两者之间的选择由工作簿保存到的文件格式决定,而非读取时的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`,此时将应用现代样式 API,而非传统 API。
- `PivotTable.pivotTableStyleType` 用于选择内置的命名样式之一(浅色和深色主题,包括 Excel 2017 中新增的样式)。这些预设为只读。
- `PivotTable.pivotTableStyleName` 用于选择您通过 `Worksheets.getTableStyles().addPivotTableStyle(...)` 自行定义的自定义样式。当您希望修改预置样式之外的颜色、边框或字体时,必须使用自定义样式。
此外,`PivotTable.formatAll(Style)` 是一个快捷方式,可将单个 `Style` 对象应用于数据透视表的每个单元格,从而覆盖通过上述任一样式名称 API 所设置的内容。当需要统一外观而不考虑底层主题时,此方法非常有用。

## **应用传统 XLS 预设自动格式**
`PivotTable.autoFormatType` 接受来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举的值。可用值包括 `Report1` 至 `Report10`、`Classic` 以及 `Table1` 至 `Table10`。
以下示例加载一个新工作簿,填入 Fruit/Year/Amount 示例数据,添加一个数据透视表,应用 `PivotTableAutoFormatType.Report5`,并将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为什么没有列字段?**Report 系列的自动格式(`Report1` 至 `Report10`、`Table1` 至 `Table10`)是经典 Excel 中为**单维数据透视表**设计的,仅包含行字段和值——它们没有为列字段标题提供内置样式。如果您的数据透视表需要列字段,请改用[场景 2](#apply-a-modern-named-preset-pivot-table-style) 中的现代 `PivotTableStyleType` 预设,这些预设专为现代 Excel 使用的二维布局而设计。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// 获取第一个工作表
let sheet = workbook.getWorksheets().get(0);
// 填充源数据，包括表头行（Fruit、Year、Amount）
// 以及 9 行数据，涵盖 2020 和 2021 年的葡萄、蓝莓、猕猴桃、樱桃
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
// 在目标单元格 E3 添加一个名为 的数据透视表，源数据范围为 A1:C10
let pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// 分配字段：Fruit -> 行，Amount -> 数据
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// 应用旧版 XLS 预设自动格式 "Report5"
// 注意：此属性仅在保存为 .xls 格式时有效。
// 当保存为 .xlsx/.xlsm/.xlsb 格式时，Excel 会忽略 AutoFormatType，
// 而使用 PivotTableStyleType / PivotTableStyleName 所指定的样式。
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);
// 将工作簿保存为旧版 .xls 格式
workbook.save("output.xls");
```

## **应用现代命名预设数据透视表样式**
`PivotTable.setPivotTableStyleType(int)` 用于选择 Excel 2007 为数据透视表引入的内置命名样式之一。`PivotTableStyleType` 枚举包含三个主题系列：从 `PIVOT_TABLE_STYLE_LIGHT1` 到 `PIVOT_TABLE_STYLE_LIGHT28` 的浅色系列、从 `PIVOT_TABLE_STYLE_MEDIUM1` 到 `PIVOT_TABLE_STYLE_MEDIUM28` 的中等系列，以及从 `PIVOT_TABLE_STYLE_DARK1` 到 `PIVOT_TABLE_STYLE_DARK_28` 的深色系列。它还定义了 `None` 和 `Custom`。每个系列中编号较高的成员都是在 Excel 2017 中添加的样式。
这些预设样式为只读。一旦需要更改预设样式未涵盖的颜色、边框或字体，就必须改为定义自定义数据透视表样式，如[场景 3](#define-and-apply-a-custom-pivot-table-style)所示。

{{% alert color="primary" %}}
**为何使用现代预设样式，而不采用报表系列自动格式？** `PivotTableAutoFormatType` 中从 `Report1` 到 `Report10` 以及从 `Table1` 到 `Table10` 的值早于数据透视表列字段的推出，因此不包含列字段标题的样式，Excel 会将这些标题呈现为无样式。`PivotTableStyleType` 预设样式专为现代 Excel 使用的二维布局而设计，并会同时为行字段和列字段标题设置样式。
{{% /alert %}}

本场景沿用场景 1 的 Fruit/Year/Amount 数据集，通过 `PivotFieldType.COLUMN` 将 `Year` 添加到列区域，同时保留 `Fruit` 行字段，使用 `pivotTable.setPivotTableStyleType` 应用深色主题预设样式 `PIVOT_TABLE_STYLE_DARK1`，并将结果保存为 `.xlsx`——这是 `PivotTableStyleType` 能够发挥作用的格式。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **定义并应用自定义数据透视表样式**
无法修改内置预设。当您需要覆盖颜色、边框或字体时,必须定义自定义数据透视表样式。该工作流包含三个步骤:
1. 通过 `Worksheets.getTableStyles().addPivotTableStyle(String name)` 向工作簿的 `TableStyles` 集合添加自定义样式。该方法返回新创建样式的索引。
2. 通过 `TableStyle.tableStyleElements.add(TableStyleElementType)` 添加元素(例如 `WholeTable` 或 `GrandTotalRow`)来配置样式,然后通过 `TableStyleElement.setElementStyle(Style)` 为每个元素分配一个 `Style`。
3. 通过将 `PivotTable.pivotTableStyleName` 设置为样式名称,将自定义样式应用于数据透视表。此处不要使用 `pivotTableStyleType`,因为该属性用于选择内置预设。

{{% alert color="primary" %}}
`pivotTableStyleName` 和 `pivotTableStyleType` 不能互换使用。使用 `pivotTableStyleType` 选择内置预设,使用 `pivotTableStyleName` 选择通过 `addPivotTableStyle` 定义的自定义样式。同时设置两者是无害的,但只有与预期来源匹配的那一个会被渲染。
可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。
以下示例定义了一个自定义数据透视表样式,在 `WholeTable` 上使用细黑边框,在 `GrandTotalRow` 上使用粗体红色字体,然后通过 `pivotTableStyleName` 应用该样式并保存为 `.xlsx`。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// 填充源数据：标题行 + 9 行数据 (A1:C10)
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
// 添加数据透视表，源数据为 A1:C10，锚定在 E3，名称为
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// 步骤 1：注册一个新的自定义数据透视表样式并捕获其索引
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// 步骤 2：添加一个 WholeTable 元素并在四边应用细黑色边框
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.getBlack());
let bottomBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.getBlack());
let leftBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.getBlack());
let rightBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// 步骤 3：添加一个 GrandTotalRow 元素并应用粗体红色字体
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// 步骤 4：按名称应用自定义样式（不要使用 PivotTableStyleType，那是用于内置预设样式的）
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **使用 formatAll 将单一样式应用于每个数据透视表单元格**
`PivotTable.formatAll(Style)` 是一个快捷方式,可将单个 `Style` 对象应用于数据透视表的每个单元格,包括数据区域、行和列标题以及总计。先前通过 `pivotTableStyleType` 或 `pivotTableStyleName` 设置的内容都将被覆盖。

{{% alert color="primary" %}}
`formatAll` 会覆盖 `pivotTableStyleType` 和 `pivotTableStyleName`。仅当需要在整个数据透视表中获得统一且不依赖主题的外观时才使用它。
以下示例创建了一个具有黄色纯色填充、粗体深蓝色字体以及四周细黑边框的 `Style`,然后使用 `formatAll` 应用该样式并保存为 `.xlsx`。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// 填充源数据：表头行（第1行）+ 9行数据（第2-10行）
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
// 添加数据透视表：源数据区域 A1:C10，目标单元格 E3，名称
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// 创建一个将强制应用于数据透视表每个单元格的样式
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.getYellow());
style.setPattern(AsposeCells.BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getDarkBlue());
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setColor(AsposeCells.Color.getBlack());
// 应用 formatAll：强制将此单个样式应用于数据透视表的每个单元格，
// 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);
// 以现代 .xlsx 格式保存工作簿
workbook.save("output.xlsx");
```

## **应该使用哪种样式 API?**
样式 API 的选择取决于您要保存到的文件格式。请使用下表作为快速参考。
| 目标文件格式 | 要使用的 API | 备注 |
|---|---|---|
| `.xls`(传统) | `PivotTable.autoFormatType` | 值来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType`(例如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`)。在保存为现代格式时将被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`(现代,内置样式) | `PivotTable.pivotTableStyleType` | 值来自 `Aspose.Cells.PivotTableStyleType`(浅色/深色主题,包括 Excel 2017 新增内容)。 |
| `.xlsx` / `.xlsm` / `.xlsb`(现代,自定义样式) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | 当内置预设不够用时使用。通过 `TableStyleElement.setElementStyle(...)` 进行配置。 |
| 任何格式(统一覆盖) | `PivotTable.formatAll(Style)` | 快捷方式,可覆盖整个数据透视表中的所有其他样式设置。 |
如有疑问,请保存为 `.xlsx`,并对内置主题使用 `pivotTableStyleType`,对自定义主题使用 `pivotTableStyleName`。

{{< app/cells/assistant language="nodejs-java" >}}