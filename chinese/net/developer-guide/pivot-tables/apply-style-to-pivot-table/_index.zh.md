---
title: 在 Aspose.Cells for .NET 中应用数据透视表样式
linktitle: 应用数据透视表样式
description: 了解如何在 Aspose.Cells for .NET 中将内置样式和自定义样式应用于数据透视表，涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells .NET pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 既支持应用旧版数据透视表自动格式（适用于 `.xls` 文件），也支持现代命名或自定义的数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。应调用的 API 取决于工作簿保存到的文件格式，而不是加载时的格式。

{{% /alert %}}

## **简介**

Aspose.Cells 为数据透视表提供两套并行的样式 API。它们之间的选择由工作簿保存到的文件格式决定，而不是由读取时的格式决定。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，在这种情况下将使用现代样式 API，而不是旧版 API。

对于旧版 `.xls` 输出，请使用 `PivotTable.AutoFormatType` 属性以及 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举。此 API 对应于经典 Excel 为数据透视表提供的自动格式选择器。

对于现代 `.xlsx`、`.xlsm` 和 `.xlsb` 输出，提供两种类型的样式 API：

- `PivotTable.PivotTableStyleType` 选择内置的命名样式之一（浅色和深色主题，包括 Excel 2017 中添加的样式）。这些预设是只读的。
- `PivotTable.PivotTableStyleName` 用于选择您通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` 自定义的样式。当您希望修改预设所提供的颜色、边框或字体时，必须使用自定义样式。

此外，`PivotTable.FormatAll(Style)` 是一个快捷方式，可以将单个 `Style` 对象应用于数据透视表的每个单元格，覆盖通过上述任一样式名称 API 设置的内容。当需要统一外观而不受底层主题影响时，这非常有用。

## **应用旧版 XLS 预设自动格式**

`PivotTable.AutoFormatType` 接受来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举的值。可用值包括 `Report1` 到 `Report10`、`Classic` 以及 `Table1` 到 `Table10`。

{{% alert color="primary" %}}

`AutoFormatType` 仅在工作簿保存为 `.xls` 时才会生效。当同一工作簿保存为 `.xlsx`、`.xlsm` 或 `.xlsb` 时，Excel 会忽略此属性并回退到 `PivotTableStyleType` 和 `PivotTableStyleName` 设置。

{{% /alert %}}

以下示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.Report5`，并将结果保存为 `.xls`。

{{% alert color="primary" %}}

**为什么没有列字段？** Report 系列自动格式（`Report1` 到 `Report10`、`Table1` 到 `Table10`）是在经典 Excel 中为**单维度数据透视表**设计的——只有行字段和值，没有为列字段标题提供内置样式。如果透视表需要列字段，请改用下方场景 2 中的现代 `PivotTableStyleType` 预设样式，它们专为现代 Excel 的二维布局而设计。

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 场景 1：应用旧的 XLS 预设自动格式
// 使用的 API：PivotTable.AutoFormatType
// 目标文件格式：.xls（旧版）
// 如需完整示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET

// 创建一个新的工作簿
Workbook workbook = new Workbook();

// 获取第一个工作表
Worksheet sheet = workbook.Worksheets[0];

// 填充源数据，包含表头行（Fruit、Year、Amount）
// 以及 9 行数据，涵盖 2020 和 2021 年的 grape、blueberry、kiwi、cherry
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");

sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);

sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);

sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);

sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);

sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);

sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);

sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);

sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);

sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);

// 在目标单元格 E3 添加一个名为 "Pivot1" 的数据透视表，使用源区域 A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// 分配字段：Fruit -> 行，Year -> 列，Amount -> 数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 应用旧的 XLS 预设自动格式 "Report5"
// 注意：此属性仅在另存为 .xls 时有效。
// 当另存为 .xlsx/.xlsm/.xlsb 时，Excel 会忽略 AutoFormatType，
// 并使用 PivotTableStyleType / PivotTableStyleName 所指定的样式。
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// 以旧版 .xls 格式保存工作簿
workbook.Save("output.xls");
```

## **应用现代命名预设数据透视表样式**

`PivotTable.PivotTableStyleType` 接受来自 `Aspose.Cells.PivotTableStyleType` 枚举的值。该枚举涵盖浅色主题 `PivotTableStyleLight1` 到 `PivotTableStyleLight28` 以及深色主题 `PivotTableStyleDark1` 到 `PivotTableStyleDark28`。Excel 2017 中添加的样式（第二波浅色和深色主题）也可以通过同一枚举访问。

对于任何现代文件格式，这是推荐的 API。与旧版自动格式不同，此处选择的样式能够被 Excel 准确呈现，并能在其他 Office 工具中往返保留。

以下示例使用相同的 Fruit/Year/Amount 数据，创建相同的数据透视表，应用 `PivotTableStyleDark1`，并将工作簿保存为 `.xlsx`。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 场景 2:使用 PivotTableStyleType 应用现代 Excel 2007+ 命名预设样式。
// 目标文件格式:.xlsx。PivotTableStyleType 枚举位于 Aspose.Cells 命名空间中
// (不在 Aspose.Cells.Pivot 中) —— 这就是为什么我们不需要任何额外的 using 语句。
// GitHub 参考:https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// 表头行:Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 行 Fruit / Year / Amount 数据
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// 在 E3 添加一个名为 "Pivot1" 的数据透视表,数据源为 A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// 分配数据透视字段:Fruit -> 行区域,Year -> 列区域,Amount -> 数据区域
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 应用现代 Excel 2007+ 命名预设数据透视样式。
// PivotTableStyleType 是适用于 .xlsx / .xlsm / .xlsb 文件的正确 API;AutoFormatType
// 在这些格式中会被 Excel 忽略。PivotTableStyleDark1 属于深色主题
// 系列(PivotTableStyleDark1..PivotTableStyleDark28),同一枚举还公开了
// 较新的 Excel 2017 浅色/深色主题(PivotTableStyleLight1..Light28 / Dark1..Dark28)。
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// 另存为现代 .xlsx 格式 —— 这是 PivotTableStyleType 真正发挥作用的格式。
workbook.Save("output.xlsx");
```

## **定义并应用自定义数据透视表样式**

无法修改内置预设。每当您需要覆盖颜色、边框或字体时，必须定义自定义数据透视表样式。工作流包括三个步骤：

1. 通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` 向工作簿的 `TableStyles` 集合添加自定义样式。这将返回新创建样式的索引。
2. 通过 `TableStyle.TableStyleElements.Add(TableStyleElementType)` 添加元素（例如 `WholeTable` 或 `GrandTotalRow`）来配置样式，然后通过 `TableStyleElement.SetElementStyle(Style)` 为每个元素分配 `Style`。
3. 通过将 `PivotTable.PivotTableStyleName` 设置为样式名称，将自定义样式应用于数据透视表。此处不要使用 `PivotTableStyleType`，因为该属性选择的是内置预设。

{{% alert color="primary" %}}

`PivotTableStyleName` 和 `PivotTableStyleType` 不能互换使用。对内置预设使用 `PivotTableStyleType`，对通过 `AddPivotTableStyle` 定义的自定义样式使用 `PivotTableStyleName`。同时设置两者没有害处，但只有与预期来源匹配的那一个会被呈现。

{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。

以下示例定义了一个自定义数据透视表样式，在 `WholeTable` 上使用细黑色边框，在 `GrandTotalRow` 上使用粗体红色字体，然后通过 `PivotTableStyleName` 应用该样式，并保存为 `.xlsx`。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// 填充源数据：表头行 + 9 行数据 (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

// 添加数据源为 A1:C10 的数据透视表，锚定在 E3，命名为 "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 第 1 步：注册一个新的自定义数据透视表样式并获取其索引
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];

// 第 2 步：添加 WholeTable 元素，并在四边应用细黑色边框
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);

// 第 3 步：添加 GrandTotalRow 元素，并应用粗体红色字体
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// 第 4 步：通过名称应用自定义样式（不是通过 PivotTableStyleType，那是用于内置预设的）
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **使用 FormatAll 将一个样式应用于每个数据透视表单元格**

`PivotTable.FormatAll(Style)` 是一个快捷方式，可以将单个 `Style` 对象应用于数据透视表的每个单元格，包括数据区域、行和列标题以及总计。通过 `PivotTableStyleType` 或 `PivotTableStyleName` 之前设置的任何内容都将被覆盖。

{{% alert color="primary" %}}

`FormatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅当在整个数据透视表中需要统一的、与主题无关的外观时才使用它。

{{% /alert %}}

以下示例创建一个具有黄色实心填充、粗体深蓝色字体以及四边细黑色边框的 `Style`，然后使用 `FormatAll` 应用它，并保存为 `.xlsx`。

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 场景4：使用FormatAll将单个Style应用于每个数据透视表单元格
// 使用的API：PivotTable.FormatAll(Style)
// 目标格式：.xlsx
// GitHub参考：请参阅Aspose.Cells-for-.NET存储库 — 数据透视表样式示例

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// 填充源数据：标题行（第1行）+ 9个数据行（第2-10行）
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);

// 添加数据透视表：源区域A1:C10，目标单元格E3，名称"Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 构建一个将强制应用于数据透视表每个单元格的Style
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;

// 应用FormatAll：将此单个样式强制应用于数据透视表的每个单元格，
// 覆盖之前设置的任何PivotTableStyleType / PivotTableStyleName
pivotTable.FormatAll(style);

// 以现代.xlsx格式保存工作簿
workbook.Save("output.xlsx");
```

## **我应该使用哪种样式 API？**

样式 API 的选择取决于要保存到的文件格式。请参考下表作为快速参考。

| 目标文件格式 | 使用的 API | 备注 |
|---|---|---|
| `.xls`（旧版） | `PivotTable.AutoFormatType` | 值来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType`（例如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。在保存为现代格式时被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `PivotTable.PivotTableStyleType` | 值来自 `Aspose.Cells.PivotTableStyleType`（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 在内置预设不够用时使用。通过 `TableStyleElement.SetElementStyle(...)` 进行配置。 |
| 任何格式（统一覆盖） | `PivotTable.FormatAll(Style)` | 快捷方式，可覆盖整个数据透视表中的所有其他样式设置。 |

如有疑问，请保存为 `.xlsx`，对内置主题使用 `PivotTableStyleType`，对自定义主题使用 `PivotTableStyleName`。

{{< app/cells/assistant language="csharp" >}}