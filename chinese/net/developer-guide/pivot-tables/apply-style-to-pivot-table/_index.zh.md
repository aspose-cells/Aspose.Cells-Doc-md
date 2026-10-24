---
title: 在 Aspose.Cells for .NET 中将样式应用于数据透视表
linktitle: 在 Aspose.Cells for .NET 中将样式应用于数据透视表
description: 了解如何在 Aspose.Cells for .NET 中将内置样式和自定义样式应用于数据透视表，内容涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells for .NET 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持应用旧版数据透视表自动格式（适用于 `.xls` 文件），也支持应用现代命名或自定义数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。应调用的 API 取决于工作簿保存时采用的文件格式，而不是加载时采用的文件格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供两套并行的样式 API。选择哪一套取决于保存工作簿时采用的文件格式，而不是读取工作簿时采用的文件格式。通过 `.xls` 文件加载的工作簿可以另存为 `.xlsx`，此时将应用现代样式 API，而不是旧版 API。
- `PivotTable.PivotTableStyleType` 用于选择一种内置命名样式，包括浅色和深色主题，以及 Excel 2017 中新增的样式。这些预设样式为只读。
- `PivotTable.PivotTableStyleName` 用于选择通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` 自行定义的自定义样式。每当需要修改预设样式未涵盖的颜色、边框或字体时，都必须使用自定义样式。
此外，`PivotTable.FormatAll(Style)` 是一个快捷方法，可将单个 `Style` 对象应用于数据透视表中的每个单元格，并覆盖通过上述任一样式名称 API 设置的样式。如果需要整个数据透视表呈现统一外观，而不受底层主题影响，此方法非常有用。

## **应用旧版 XLS 预设自动格式**
`PivotTable.AutoFormatType` 接受 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举中的值。可用值包括 `Report1` 至 `Report10`、`Classic` 以及 `Table1` 至 `Table10`。
以下示例加载一个新建的工作簿，填充 `Fruit/Year/Amount` 示例数据，添加数据透视表，应用 `PivotTableAutoFormatType.Report5`，然后将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为什么没有列字段？** Report 系列自动格式（`Report1` 至 `Report10` 以及 `Table1` 至 `Table10`）最初是为经典版 Excel 中仅包含行字段和值的**单维数据透视表**设计的，因此并未提供针对列字段标题的内置样式。如果数据透视表需要列字段，请改用[场景 2](#apply-a-modern-named-preset-pivot-table-style)中介绍的现代 `PivotTableStyleType` 预设样式，这些样式专为现代 Excel 所使用的二维布局而设计。
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 场景 1：应用旧版 XLS 预设自动格式
// 使用的 API：PivotTable.AutoFormatType
// 目标文件格式：.xls（旧版）
// 如需完整示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET
// 创建新工作簿
Workbook workbook = new Workbook();
// 获取第一个工作表
Worksheet sheet = workbook.Worksheets[0];
// 填充源数据，包括标题行（Fruit、Year、Amount）
// 以及涵盖 2020 年和 2021 年 grape、blueberry、kiwi、cherry 的 9 行数据
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
// 使用源范围 A1:C10，在目标单元格 E3 添加一个名为 "Pivot1" 的数据透视表
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];
// 分配字段：Fruit -> 行，Amount -> 数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// 应用旧版 XLS 预设自动格式 "Report5"
// 注意：仅在保存为 .xls 时此属性才有意义。
// 保存为 .xlsx/.xlsm/.xlsb 时，Excel 会忽略 AutoFormatType
// 并使用 PivotTableStyleType / PivotTableStyleName 指定的样式。
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// 将工作簿保存为旧版 .xls 格式
workbook.Save("output.xls");
```

## **应用现代命名预设数据透视表样式**

`PivotTable.PivotTableStyleType` 用于选择 Excel 2007 为数据透视表引入的内置命名样式之一。`PivotTableStyleType` 枚举包含三个主题系列：浅色系列从 `PivotTableStyleLight1` 到 `PivotTableStyleLight28`，中等系列从 `PivotTableStyleMedium1` 到 `PivotTableStyleMedium28`，深色系列从 `PivotTableStyleDark1` 到 `PivotTableStyleDark28`。它还定义了 `None` 和 `Custom`。每个系列中编号较高的成员都是 Excel 2017 中新增的样式。
这些预设样式为只读。一旦需要更改预设样式未涵盖的颜色、边框或字体，就必须改为定义自定义数据透视表样式，如[场景 3](#define-and-apply-a-custom-pivot-table-style)所示。

{{% alert color="primary" %}}
**为什么使用现代预设样式，而不是报表系列自动格式？** `PivotTableAutoFormatType` 的 `Report1` 到 `Report10` 以及 `Table1` 到 `Table10` 值早于数据透视表列字段出现，因此不包含列字段标题的样式，Excel 会将这些标题呈现为无样式。`PivotTableStyleType` 预设样式专为现代 Excel 使用的二维布局而设计，可为行字段和列字段标题应用相同样式。
{{% /alert %}}

此场景复用场景 1 的 Fruit/Year/Amount 数据集，通过 `PivotFieldType.Column` 将 `Year` 添加到列区域，并将其与 `Fruit` 行字段并列，使用 `PivotTable.PivotTableStyleType` 应用深色主题预设样式 `PivotTableStyleDark1`，然后将结果另存为 `.xlsx`——这是 `PivotTableStyleType` 有实际意义的格式。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 场景 2：使用 PivotTableStyleType 应用现代 Excel 2007+ 命名预设样式。
// 目标文件格式：.xlsx。PivotTableStyleType 枚举位于 Aspose.Cells 命名空间中
// （而不是 Aspose.Cells.Pivot）-- 因此无需为它添加任何额外的 using 指令。
// GitHub 引用：https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// 表头行：Fruit / Year / Amount
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
// 在 E3 处添加一个名为 "Pivot1" 的数据透视表，数据源为 A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// 分配透视字段：Fruit -> Row 区域，Year -> Column 区域，Amount -> Data 区域
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// 应用现代 Excel 2007+ 命名预设数据透视样式。
// PivotTableStyleType 是 .xlsx / .xlsm / .xlsb 文件的正确 API；对于这些格式，Excel 会忽略
// AutoFormatType。PivotTableStyleDark1 属于深色主题
// 系列 (PivotTableStyleDark1..PivotTableStyleDark28)，同一枚举还公开了
// 较新的 Excel 2017 浅色/深色主题 (PivotTableStyleLight1..Light28 / Dark1..Dark28)。
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;
// 保存为现代 .xlsx 格式 -- PivotTableStyleType 仅对此格式有效。
workbook.Save("output.xlsx");
```
## **定义并应用自定义数据透视表样式**
内置预设样式无法修改。每当需要覆盖颜色、边框或字体时，都必须定义自定义数据透视表样式。工作流包含以下三个步骤：
1. 通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` 将自定义样式添加到工作簿的 `TableStyles` 集合中。该方法返回新建样式的索引。
2. 通过 `TableStyle.TableStyleElements.Add(TableStyleElementType)` 添加元素（如 `WholeTable` 或 `GrandTotalRow`）来配置样式，然后通过 `TableStyleElement.SetElementStyle(Style)` 为每个元素设置 `Style`。
3. 将 `PivotTable.PivotTableStyleName` 设置为该样式的名称，以将自定义样式应用于数据透视表。此处不要使用 `PivotTableStyleType`，因为该属性用于选择内置预设样式。

{{% alert color="primary" %}}
`PivotTableStyleName` 和 `PivotTableStyleType` 不能互换。对于内置预设样式，请使用 `PivotTableStyleType`；对于通过 `AddPivotTableStyle` 定义的自定义样式，请使用 `PivotTableStyleName`。同时设置两者不会造成问题，但实际呈现的仅是与预期来源相符的那一个。
可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。
以下示例定义一个自定义数据透视表样式，为 `WholeTable` 设置黑色细边框，为 `GrandTotalRow` 设置红色粗体字体，然后通过 `PivotTableStyleName` 应用该样式并保存为 `.xlsx`。
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// 填充源数据：标题行 + 9 个数据行 (A1:C10)
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
// 添加数据源为 A1:C10、锚定于 E3 且名为 "Pivot1" 的数据透视表
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// 第 1 步：注册新的自定义数据透视表样式并获取其索引
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];
// 第 2 步：添加 WholeTable 元素并为四个边应用黑色细边框
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
// 第 3 步：添加 GrandTotalRow 元素并应用红色粗体字体
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);
// 第 4 步：按名称应用自定义样式（不要使用 PivotTableStyleType，后者用于内置预设）
pivotTable.PivotTableStyleName = "CustomPivotStyle";
workbook.Save("output.xlsx");
```

## **使用 FormatAll 将一种样式应用于数据透视表中的每个单元格**
`PivotTable.FormatAll(Style)` 是一个快捷方法，可将单个 `Style` 对象应用于数据透视表中的每个单元格，包括数据区域、行标题、列标题和总计值。此前通过 `PivotTableStyleType` 或 `PivotTableStyleName` 设置的样式都将被覆盖。

{{% alert color="primary" %}}
`FormatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅当整个数据透视表都需要统一且与主题无关的外观时，才应使用此方法。
以下示例创建一个 `Style`，为其设置黄色实心填充、深蓝色粗体字体和四周黑色细边框，然后通过 `FormatAll` 应用该样式并保存为 `.xlsx`。
{{% /alert %}}

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 场景 4：使用 FormatAll 将单个 Style 应用到数据透视表的每个单元格
// 使用的 API：PivotTable.FormatAll(Style)
// 目标格式：.xlsx
// GitHub 参考：请参阅 Aspose.Cells-for-.NET 仓库 — 数据透视表样式示例
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// 填充源数据：表头行（第 1 行） + 9 行数据（第 2-10 行）
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
// 添加数据透视表：源区域 A1:C10，目标单元格 E3，名称 "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// 创建一个将强制应用于数据透视表每个单元格的 Style
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
// 应用 FormatAll：将此单个样式强制应用到数据透视表的每个单元格，
// 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.FormatAll(style);
// 以现代 .xlsx 格式保存工作簿
workbook.Save("output.xlsx");
```

## **应使用哪套样式 API？**
样式 API 的选择取决于保存时采用的文件格式。请参阅下表以快速了解对应关系。
| 目标文件格式 | 应使用的 API | 说明 |
|---|---|---|
| `.xls`（旧版） | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` 中提供的值（例如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。保存为现代格式时会被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代格式，内置样式） | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` 中提供的值（浅色和深色主题，包括 Excel 2017 中新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代格式，自定义样式） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 当内置预设样式无法满足需求时使用。通过 `TableStyleElement.SetElementStyle(...)` 配置样式。 |
| 任意格式（统一覆盖） | `PivotTable.FormatAll(Style)` | 覆盖整个数据透视表上所有其他样式设置的快捷方式。 |
如果不确定采用哪种方法，请保存为 `.xlsx`，并使用 `PivotTableStyleType` 应用内置主题，或使用 `PivotTableStyleName` 应用自定义主题。

## 相关文章
- [在 Aspose.Cells for .NET 中将行字段和列字段添加到数据透视表](/cells/zh/net/pivot-table-add-row-and-column-fields/)
- [管理 Aspose.Cells for .NET 数据透视表中的值字段](/cells/zh/net/manage-value-fields/)
- [刷新 Aspose.Cells for .NET 中的数据透视表](/cells/zh/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}