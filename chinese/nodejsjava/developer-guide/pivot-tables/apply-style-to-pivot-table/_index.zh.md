---
title: 向数据透视表应用样式
linktitle: 向数据透视表应用样式
description: 了解如何在 Aspose.Cells for Node.js via Java 中向数据透视表应用内置和自定义样式，涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells Node.js via Java pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持同时应用旧版的数据透视自动格式（适用于 `.xls` 文件）和现代的命名或自定义数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。您应调用的 API 取决于工作簿保存到的文件格式，而非加载时的格式。

{{% /alert %}}

## **简介**

Aspose.Cells 为数据透视表公开了两套并行的样式 API。它们之间的选择取决于工作簿保存到的文件格式，而非读取时的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，在这种情况下适用的是现代样式 API。

对于旧版 `.xls` 输出，请使用 `PivotTable.autoFormatType` 属性结合 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举。此 API 对应于经典 Excel 为数据透视表提供的自动格式选择器。

对于现代 `.xlsx`、`.xlsm` 和 `.xlsb` 输出，可使用两种风格的样式 API：

- `PivotTable.pivotTableStyleType` 用于选择内置的命名样式之一（浅色和深色主题，包括 Excel 2017 中新增的样式）。这些预设是只读的。
- `PivotTable.pivotTableStyleName` 用于选择您通过 `Worksheets.getTableStyles().addPivotTableStyle(...)` 自行定义的自定义样式。当您希望修改预设所提供的颜色、边框或字体时，必须使用自定义样式。

此外，`PivotTable.formatAll(Style)` 是一个快捷方式，它将单个 `Style` 对象应用于数据透视表的每一个单元格，覆盖通过上述任一样式名称 API 设置的内容。当无论底层主题如何都需要统一外观时，此功能非常有用。

## **应用旧版 XLS 预设自动格式**

`PivotTable.autoFormatType` 接受来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举的值。可用值为 `Report1` 至 `Report10`、`Classic` 以及 `Table1` 至 `Table10`。

{{% alert color="primary" %}}

`autoFormatType` 仅在工作簿保存为 `.xls` 时生效。当同一工作簿保存为 `.xlsx`、`.xlsm` 或 `.xlsb` 时，Excel 将忽略此属性并回退到 `pivotTableStyleType` 和 `pivotTableStyleName` 设置。

{{% /alert %}}

以下示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.Report5`，并将结果保存为 `.xls`。

{{% alert color="primary" %}}

**为什么没有列字段？** Report 系列自动格式（`Report1` 到 `Report10`、`Table1` 到 `Table10`）是在经典 Excel 中为**单维度数据透视表**设计的——只有行字段和值，没有为列字段标题提供内置样式。如果透视表需要列字段，请改用下方场景 2 中的现代 `PivotTableStyleType` 预设样式，它们专为现代 Excel 的二维布局而设计。

{{% /alert %}}

```javascript
let workbook = new AsposeCells.Workbook();

// 获取第一个工作表
let sheet = workbook.getWorksheets().get(0);

// 填充源数据,包含标题行(Fruit、Year、Amount)
// 以及 9 行数据,涵盖 2020 年和 2021 年的葡萄、蓝莓、猕猴桃、樱桃
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

// 在目标单元格 E3 处添加一个数据透视表,命名为 "Pivot1",使用源数据区域 A1:C10
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// 分配字段:Fruit -> 行,Year -> 列,Amount -> 数据
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// 应用旧的 XLS 预设自动格式 "Report5"
// 注意:此属性仅在保存为 .xls 时有意义。
// 当保存为 .xlsx/.xlsm/.xlsb 时,Excel 会忽略 AutoFormatType,
// 而使用 PivotTableStyleType / PivotTableStyleName 指定的内容。
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// 将工作簿保存为旧的 .xls 格式
workbook.save("output.xls");
```

## **应用现代的命名预设数据透视表样式**

`PivotTable.pivotTableStyleType` 接受来自 `Aspose.Cells.PivotTableStyleType` 枚举的值。该枚举涵盖浅色主题 `PivotTableStyleLight1` 至 `PivotTableStyleLight28` 以及深色主题 `PivotTableStyleDark1` 至 `PivotTableStyleDark28`。Excel 2017 中新增的样式（浅色和深色主题的第二波）可通过同一枚举访问。

对于任何现代文件格式，推荐使用此 API。与旧版自动格式不同，此处选择的样式能够被 Excel 准确地呈现，并在其他 Office 工具中往返转换时保持不变。

以下示例使用相同的 Fruit/Year/Amount 数据，创建一个相同的数据透视表，应用 `PivotTableStyleDark1`，并将工作簿保存为 `.xlsx`。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 表头行：水果 / 年份 / 数量
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 行数据：水果 / 年份 / 数量
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

// 在 E3 位置添加一个名为 "Pivot1" 的数据透视表，数据源为 A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 配置透视字段：水果 -> 行区域，年份 -> 列区域，数量 -> 数据区域
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// 应用一个现代化的 Excel 2007+ 命名预设透视表样式。
// 对于 .xlsx / .xlsm / .xlsb 文件，应使用 PivotTableStyleType 枚举（AutoFormatType
// 在这些格式中会被 Excel 忽略）。PivotTableStyleDark1 属于暗色主题系列
// （PivotTableStyleDark1..PivotTableStyleDark28），同一枚举也包含较新的 Excel 2017
// 浅色/暗色主题（PivotTableStyleLight1..Light28 / Dark1..Dark28）。
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// 另存为现代 .xlsx 格式——PivotTableStyleType 仅对此类格式有效。
workbook.save("output.xlsx");
```

## **定义并应用自定义数据透视表样式**

无法修改内置预设。每当您需要覆盖颜色、边框或字体时，都必须定义一个自定义数据透视样式。该工作流程包含三个步骤：

1. 通过 `Worksheets.getTableStyles().addPivotTableStyle(String name)` 向工作簿的 `TableStyles` 集合添加一个自定义样式。这将返回新创建样式的索引。
2. 通过 `TableStyle.tableStyleElements.add(TableStyleElementType)` 添加元素（例如 `WholeTable` 或 `GrandTotalRow`）来配置该样式，然后通过 `TableStyleElement.setElementStyle(Style)` 为每个元素分配一个 `Style`。
3. 通过将 `PivotTable.pivotTableStyleName` 设置为该样式的名称，将自定义样式应用于数据透视表。此处不要使用 `pivotTableStyleType`，因为该属性用于选择内置预设。

{{% alert color="primary" %}}

`pivotTableStyleName` 和 `pivotTableStyleType` 不能互换使用。对于内置预设，请使用 `pivotTableStyleType`；对于通过 `addPivotTableStyle` 定义的自定义样式，请使用 `pivotTableStyleName`。同时设置两者是无害的，但只有与预期来源匹配的那个才会被呈现。

{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。

以下示例定义一个自定义数据透视样式，在 `WholeTable` 上设置细黑色边框，在 `GrandTotalRow` 上设置粗体红色字体，然后通过 `pivotTableStyleName` 应用该样式并保存为 `.xlsx`。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 填充源数据：表头行 + 9 行数据 (A1:C10)
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

// 添加数据源为 A1:C10 的数据透视表，锚定在 E3，命名为 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// 步骤 1：注册一个新的自定义数据透视表样式并获取其索引
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// 步骤 2：添加 WholeTable 元素，并在四边应用细的黑色边框
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// 步骤 3：添加 GrandTotalRow 元素，并应用粗体红色字体
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// 步骤 4：通过名称应用自定义样式（不要使用 PivotTableStyleType，它是用于内置预设样式的）
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **使用 FormatAll 将单个样式应用于每个数据透视表单元格**

`PivotTable.formatAll(Style)` 是一个快捷方式，它将单个 `Style` 对象应用于数据透视表的每一个单元格，包括数据区域、行和列标题以及总计。之前通过 `pivotTableStyleType` 或 `pivotTableStyleName` 设置的内容都将被覆盖。

{{% alert color="primary" %}}

`formatAll` 会覆盖 `pivotTableStyleType` 和 `pivotTableStyleName`。仅当整个数据透视表需要统一且独立于主题的外观时才使用它。

{{% /alert %}}

以下示例创建一个具有黄色纯色填充、粗体深蓝色字体以及四边细黑色边框的 `Style`，然后使用 `formatAll` 应用它，并保存为 `.xlsx`。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 填充源数据：表头行（第1行）+ 9个数据行（第2-10行）
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

// 添加数据透视表：源数据区域 A1:C10，目标单元格 E3，名称 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 创建一个将被强制应用到数据透视表每个单元格的样式
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);

// 应用 FormatAll：将此单个样式强制应用到数据透视表的每个单元格，
// 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);

// 以现代 .xlsx 格式保存工作簿
workbook.save("output.xlsx");
```

## **我应该使用哪个样式 API？**

样式 API 的选择取决于您要保存到的文件格式。请参考下表以快速查阅。

| 目标文件格式 | 要使用的 API | 备注 |
|---|---|---|
| `.xls`（旧版） | `PivotTable.autoFormatType` | 取值来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType`（例如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。在保存为现代格式时被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `PivotTable.pivotTableStyleType` | 取值来自 `Aspose.Cells.PivotTableStyleType`（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | 在内置预设不够用时使用。通过 `TableStyleElement.setElementStyle(...)` 进行配置。 |
| 任何格式（统一覆盖） | `PivotTable.formatAll(Style)` | 快捷方式，覆盖整个数据透视表上的所有其他样式设置。 |

如有疑问，请保存为 `.xlsx`，并对内置主题使用 `pivotTableStyleType`，对自定义主题使用 `pivotTableStyleName`。

{{< app/cells/assistant language="javascript" >}}