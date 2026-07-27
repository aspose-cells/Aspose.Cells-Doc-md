---
title: 在 Aspose.Cells for .NET 中应用数据透视表样式
linktitle: 应用数据透视表样式
description: 了解如何在 Aspose.Cells for Node.js via C++ 中将内置样式和自定义样式应用于数据透视表，涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells Node.js via C++ pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells 支持应用旧式数据透视表自动格式（适用于 `.xls` 文件）以及现代命名或自定义数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。您应调用的 API 取决于工作簿保存为的文件格式，而不是加载时的文件格式。

{{% /alert %}}

## **简介**

Aspose.Cells 为数据透视表提供两种并行的样式 API。它们之间的选择取决于工作簿保存为的文件格式，而不是读取来源的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，此时应使用现代样式 API，而不是旧式 API。

对于旧式 `.xls` 输出，请使用 `PivotTable.AutoFormatType` 属性以及 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举。该 API 对应于经典 Excel 为数据透视表提供的自动格式选择器。

对于现代 `.xlsx`、`.xlsm` 和 `.xlsb` 输出，提供两种风格的样式 API：

- `PivotTable.PivotTableStyleType` 用于选择内置命名样式之一（浅色和深色主题，包括 Excel 2017 中新增的样式）。这些预设是只读的。
- `PivotTable.PivotTableStyleName` 用于选择您通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...))` 自定义定义的样式。当您想要修改预设之外的颜色、边框或字体时，必须使用自定义样式。

此外，`PivotTable.FormatAll(Style)` 是一个快捷方法，可将单个 `Style` 对象应用于数据透视表的每个单元格，覆盖通过上述任一样式名称 API 设置的内容。当需要统一外观而不受底层主题影响时，此方法非常有用。

## **应用旧式 XLS 预设自动格式**

`PivotTable.AutoFormatType` 接受 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举中的值。可用值包括 `Report1` 到 `Report10`、`Classic` 以及 `Table1` 到 `Table10`。

{{% alert color="primary" %}}

`AutoFormatType` 仅在工作簿保存为 `.xls` 时生效。当同一工作簿保存为 `.xlsx`、`.xlsm` 或 `.xlsb` 时，Excel 会忽略此属性，并回退到 `PivotTableStyleType` 和 `PivotTableStyleName` 设置。

{{% /alert %}}

下面的示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.Report5`，然后将结果保存为 `.xls`。

{{% alert color="primary" %}}

**为什么没有列字段？** Report 系列自动格式（`Report1` 到 `Report10`、`Table1` 到 `Table10`）是在经典 Excel 中为**单维度数据透视表**设计的——只有行字段和值，没有为列字段标题提供内置样式。如果透视表需要列字段，请改用下方场景 2 中的现代 `PivotTableStyleType` 预设样式，它们专为现代 Excel 的二维布局而设计。

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");

// 场景 1：应用旧版 XLS 预设自动格式
// 使用的 API：PivotTable.AutoFormatType
// 目标文件格式：.xls（旧版）
// 如需完整示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET

// 创建一个新的工作簿
const workbook = new AsposeCells.Workbook();

// 获取第一个工作表
const sheet = workbook.getWorksheets().get(0);

// 使用表头行（Fruit、Year、Amount）填充源数据
// 以及覆盖 2020 和 2021 年中 grape、blueberry、kiwi、cherry 的 9 行数据
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

// 在目标单元格 E3 处添加一个名为 "Pivot1" 的数据透视表，使用源区域 A1:C10
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);

// 分配字段：Fruit -> 行，Year -> 列，Amount -> 数据
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 应用旧版 XLS 预设自动格式 "Report5"
// 注意：此属性仅在保存为 .xls 时有效。
// 当保存为 .xlsx/.xlsm/.xlsb 时，Excel 会忽略 AutoFormatType
// 并使用 PivotTableStyleType / PivotTableStyleName 所指定的样式。
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// 以旧版 .xls 格式保存工作簿
workbook.save("output.xls");
```

## **应用现代命名预设数据透视表样式**

`PivotTable.PivotTableStyleType` 接受 `Aspose.Cells.PivotTableStyleType` 枚举中的值。该枚举涵盖浅色主题 `PivotTableStyleLight1` 到 `PivotTableStyleLight28` 以及深色主题 `PivotTableStyleDark1` 到 `PivotTableStyleDark28`。Excel 2017 中新增的样式（浅色和深色主题的第二波）可通过同一枚举访问。

对于任何现代文件格式，这是推荐的 API。与旧式自动格式不同，此处选择的样式可被 Excel 准确呈现，并在其他 Office 工具的往返转换中保留。

下面的示例使用相同的 Fruit/Year/Amount 数据，创建相同的数据透视表，应用 `PivotTableStyleDark1`，并将工作簿保存为 `.xlsx`。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 表头行：水果 / 年份 / 数量
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 行水果 / 年份 / 数量 数据
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

// 在 E3 添加一个名为 "Pivot1" 的数据透视表，数据源为 A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配透视字段：水果 -> 行区域，年份 -> 列区域，数量 -> 数据区域
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 应用现代 Excel 2007+ 的命名预设透视表样式。
// PivotTableStyleType 是 .xlsx / .xlsm / .xlsb 文件的正确 API；AutoFormatType
// 在这些格式下会被 Excel 忽略。PivotTableStyleDark1 属于深色主题系列
// （PivotTableStyleDark1..PivotTableStyleDark28），同一枚举还公开了
// 较新的 Excel 2017 浅色/深色主题（PivotTableStyleLight1..Light28 / Dark1..Dark28）。
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);

// 保存为现代 .xlsx —— 这是 PivotTableStyleType 真正适用的格式。
workbook.save("output.xlsx");
```

## **定义并应用自定义数据透视表样式**

内置预设无法修改。每当您需要覆盖颜色、边框或字体时，都必须定义自定义数据透视样式。工作流包括三个步骤：

1. 通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` 将自定义样式添加到工作簿的 `TableStyles` 集合中。这将返回新创建样式的索引。
2. 通过 `TableStyle.TableStyleElements.Add(TableStyleElementType)` 添加元素（例如 `WholeTable` 或 `GrandTotalRow`），然后通过 `TableStyleElement.SetElementStyle(Style)` 为每个元素分配一个 `Style`，从而配置样式。
3. 通过将 `PivotTable.PivotTableStyleName` 设置为样式的名称，将自定义样式应用于数据透视表。此处不要使用 `PivotTableStyleType`，因为该属性用于选择内置预设。

{{% alert color="primary" %}}

`PivotTableStyleName` 和 `PivotTableStyleType` 不可互换。请将 `PivotTableStyleType` 用于内置预设，将 `PivotTableStyleName` 用于您通过 `AddPivotTableStyle` 定义的自定义样式。同时设置两者无害，但仅会呈现与预期来源匹配的那一个。

{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。

下面的示例定义一个自定义数据透视样式，在 `WholeTable` 上具有细黑色边框，在 `GrandTotalRow` 上具有加粗的红色字体，然后通过 `PivotTableStyleName` 应用它并保存为 `.xlsx`。

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

// 添加数据透视表，源数据为 A1:C10，定位在 E3，名称为 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 步骤 1：注册一个新的自定义数据透视表样式并获取其索引
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// 步骤 2：添加一个 WholeTable 元素，并在四边应用细的黑色边框
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);

// 步骤 3：添加一个 GrandTotalRow 元素，并应用粗体红色字体
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);

// 步骤 4：通过名称应用自定义样式（不要使用 PivotTableStyleType，它是用于内置预设样式的）
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **使用 FormatAll 将一个样式应用于数据透视表的每个单元格**

`PivotTable.FormatAll(Style)` 是一个快捷方法，可将单个 `Style` 对象应用于数据透视表的每个单元格，包括数据区域、行和列标题以及总计。之前通过 `PivotTableStyleType` 或 `PivotTableStyleName` 设置的内容将被覆盖。

{{% alert color="primary" %}}

`FormatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅当在整个数据透视表中需要统一且不依赖主题的外观时才使用它。

{{% /alert %}}

下面的示例创建一个具有黄色实心填充、加粗的深蓝色字体以及四周细黑色边框的 `Style`，然后使用 `FormatAll` 应用它并保存为 `.xlsx`。

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

// 添加数据透视表：源数据范围 A1:C10，目标单元格 E3，名称 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 创建一个样式，将强制应用于数据透视表的每个单元格
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

// 应用 FormatAll：将此单一样式强制应用于数据透视表的每个单元格，
// 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);

// 以现代 .xlsx 格式保存工作簿
workbook.save("output.xlsx");
```

## **我应该使用哪种样式 API？**

样式 API 的选择取决于您要保存为的文件格式。请使用下表作为快速参考。

| 目标文件格式 | 使用的 API | 备注 |
|---|---|---|
| `.xls`（旧式） | `PivotTable.AutoFormatType` | 取值来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType`（例如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。保存为现代格式时将被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `PivotTable.PivotTableStyleType` | 取值来自 `Aspose.Cells.PivotTableStyleType`（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 内置预设不够用时使用。通过 `TableStyleElement.SetElementStyle(...)` 进行配置。 |
| 任何格式（统一覆盖） | `PivotTable.FormatAll(Style)` | 快捷方法，覆盖整个数据透视表上的所有其他样式设置。 |

如有疑问，请保存为 `.xlsx`，并对内置主题使用 `PivotTableStyleType`，对自定义主题使用 `PivotTableStyleName`。

{{< app/cells/assistant language="javascript" >}}
