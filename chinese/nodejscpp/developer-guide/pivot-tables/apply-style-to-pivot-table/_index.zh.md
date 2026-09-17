---
title: 在 Aspose.Cells for Node.js via C++ 中为数据透视表应用样式
linktitle: 在 Aspose.Cells for Node.js via C++ 中为数据透视表应用样式
description: 学习如何使用 Aspose.Cells for Node.js via C++ 为数据透视表应用内置和自定义样式,涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式,以及 FormatAll 快捷方式。
keywords: Aspose.Cells Node.js via C++ 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持应用旧版数据透视自动格式(适用于 `.xls` 文件)和现代命名或自定义数据透视表样式(适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件)。您应调用的 API 取决于工作簿保存为的文件格式,而非加载时的格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供两套并行的样式 API。两者之间的选择取决于工作簿保存为的文件格式,而非读取时的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`,在这种情况下适用现代样式 API,而非旧版样式 API。
- `PivotTable.PivotTableStyleType` 用于选择内置命名样式之一(包括浅色和深色主题,以及 Excel 2017 新增的样式)。这些预设样式为只读。
- `PivotTable.PivotTableStyleName` 用于选择通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` 自行定义的自定义样式。当您希望修改颜色、边框或字体,而预设样式无法满足需求时,必须使用自定义样式。
此外,`PivotTable.FormatAll(Style)` 是一个快捷方式,可将单个 `Style` 对象应用于数据透视表的每个单元格,覆盖通过上述任一样式名称 API 所设置的内容。当需要统一外观且不受底层主题影响时,此方法非常有用。

## **应用旧版 XLS 预设自动格式**
`PivotTable.AutoFormatType` 接受来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举的值。可用值包括 `Report1` 至 `Report10`、`Classic` 以及 `Table1` 至 `Table10`。
以下示例加载一个新工作簿,填充 Fruit/Year/Amount 示例数据,添加一个数据透视表,应用 `PivotTableAutoFormatType.Report5`,并将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为什么没有列字段?** Report 系列自动格式(`Report1` 至 `Report10`、`Table1` 至 `Table10`)在经典 Excel 中是针对仅包含行字段和值的**单维数据透视表**设计的——它们对列字段标题没有内置样式。如果您的数据透视表需要列字段,请改用 [场景 2](#apply-a-modern-named-preset-pivot-table-style) 中的现代 `PivotTableStyleType` 预设,这些预设专为现代 Excel 所使用的二维布局而设计。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// 场景 1: 应用旧版 XLS 预设自动格式
// 使用的 API: PivotTable.AutoFormatType
// 目标文件格式: .xls（旧版）
// 如需完整示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET
// 创建一个新的工作簿
const workbook = new AsposeCells.Workbook();
// 获取第一个工作表
const sheet = workbook.getWorksheets().get(0);
// 用包含表头行（Fruit、Year、Amount）的源数据填充
// 以及覆盖 2020 和 2021 年葡萄、蓝莓、猕猴桃、樱桃的 9 行数据
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
// 在目标单元格 E3 添加一个数据透视表，命名为 "Pivot1"，使用源区域 A1:C10
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);
// 分配字段：Fruit -> 行，Amount -> 数据
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// 应用旧版 XLS 预设自动格式 "Report5"
// 注意：此属性仅在保存为 .xls 时有效。
// 当保存为 .xlsx/.xlsm/.xlsb 时，Excel 会忽略 AutoFormatType
// 并使用 PivotTableStyleType / PivotTableStyleName 指定的样式。
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// 以旧版 .xls 格式保存工作簿
workbook.save("output.xls");
```

## **应用现代命名预设数据透视表样式**

## **定义并应用自定义数据透视表样式**
内置预设样式无法修改。每当您需要覆盖颜色、边框或字体时,都必须定义自定义数据透视样式。该工作流包含三个步骤:
1. 通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` 将自定义样式添加到工作簿的 `TableStyles` 集合中。此方法返回新创建样式的索引。
2. 通过 `TableStyle.TableStyleElements.Add(TableStyleElementType)` 添加元素(如 `WholeTable` 或 `GrandTotalRow`)来配置样式,然后通过 `TableStyleElement.SetElementStyle(Style)` 为每个元素分配一个 `Style`。
3. 将 `PivotTable.PivotTableStyleName` 设置为该样式的名称,从而将自定义样式应用于数据透视表。请勿在此处使用 `PivotTableStyleType`,因为该属性选择的是内置预设样式。

{{% alert color="primary" %}}
`PivotTableStyleName` 和 `PivotTableStyleType` 不能互换使用。请将 `PivotTableStyleType` 用于内置预设样式,将 `PivotTableStyleName` 用于您通过 `AddPivotTableStyle` 定义的自定义样式。同时设置两者无害,但仅会呈现与预期来源匹配的那一个。
{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。
以下示例定义一个自定义数据透视样式:在 `WholeTable` 上使用细黑色边框,在 `GrandTotalRow` 上使用粗体红色字体,然后通过 `PivotTableStyleName` 应用该样式,并保存为 `.xlsx`。

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
// 添加数据源为 A1:C10 的数据透视表，定位到 E3，命名为 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// 步骤 1：注册一个新的自定义数据透视表样式并获取其索引
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// 步骤 2：添加 WholeTable 元素，并在四个方向应用细黑色边框
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
// 步骤 3：添加 GrandTotalRow 元素，并应用粗体红色字体
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);
// 步骤 4：通过名称应用自定义样式（不要使用 PivotTableStyleType，那是用于内置预设样式的）
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **使用 FormatAll 将一种样式应用于数据透视表的每个单元格**
`PivotTable.FormatAll(Style)` 是一个快捷方式,可将单个 `Style` 对象应用于数据透视表的每个单元格,包括数据区域、行/列标题以及汇总。无论之前通过 `PivotTableStyleType` 或 `PivotTableStyleName` 设置了什么,都会被覆盖。

{{% alert color="primary" %}}
`FormatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅当整个数据透视表需要统一的、不受主题影响的外观时才使用它。
{{% /alert %}}

以下示例创建一个 `Style`,具有黄色实心填充、深蓝色粗体字体以及四边的细黑色边框,然后使用 `FormatAll` 应用该样式,并保存为 `.xlsx`。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// 填充源数据：表头行（第1行）+ 9行数据行（第2-10行）
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
// 应用 FormatAll：强制将此单个样式应用到数据透视表的每个单元格，
// 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);
// 以现代 .xlsx 格式保存工作簿
workbook.save("output.xlsx");
```

## **应使用哪种样式 API?**
样式 API 的选择取决于您要保存为的文件格式。请参考下表作为快速参考。
| 目标文件格式 | 使用的 API | 说明 |
|---|---|---|
| `.xls`(旧版) | `PivotTable.AutoFormatType` | 取自 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 的值(如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`)。保存为现代格式时会被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`(现代,内置样式) | `PivotTable.PivotTableStyleType` | 取自 `Aspose.Cells.PivotTableStyleType` 的值(浅色/深色主题,包括 Excel 2017 新增的样式)。 |
| `.xlsx` / `.xlsm` / `.xlsb`(现代,自定义样式) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 在内置预设样式不够用时使用。通过 `TableStyleElement.SetElementStyle(...)` 进行配置。 |
| 任意格式(统一覆盖) | `PivotTable.FormatAll(Style)` | 快捷方式,会覆盖整个数据透视表的所有其他样式设置。 |
如有疑问,请保存为 `.xlsx`,并对内置主题使用 `PivotTableStyleType`,对自定义主题使用 `PivotTableStyleName`。

{{< app/cells/assistant language="nodejs-cpp" >}}