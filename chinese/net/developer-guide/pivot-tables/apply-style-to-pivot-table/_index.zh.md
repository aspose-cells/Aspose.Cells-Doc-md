---
title: 在 Aspose.Cells for .NET 中为数据透视表应用样式
linktitle: 在 Aspose.Cells for .NET 中为数据透视表应用样式
description: 了解如何在 Aspose.Cells for .NET 中为数据透视表应用内置和自定义样式，内容涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells .NET 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 同时支持应用旧版的数据透视表自动格式（用于 `.xls` 文件）和现代的命名或自定义数据透视表样式（用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。应调用的 API 取决于工作簿要保存到的文件格式，而不是读取时的格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供两套并行的样式 API。它们之间的选择由工作簿要保存到的文件格式决定，而不是由读取的格式决定。从 `.xls` 文件加载的工作簿可以重新另存为 `.xlsx`，这种情况下应使用现代样式 API，而不是旧版 API。
- `PivotTable.PivotTableStyleType` 用于选择某个内置命名样式（包括浅色和深色主题，以及 Excel 2017 中新增的样式）。这些预设样式为只读。
- `PivotTable.PivotTableStyleName` 用于选择通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` 自定义定义的样式。当需要在预设样式之外修改颜色、边框或字体时，必须使用自定义样式。
此外，`PivotTable.FormatAll(Style)` 是一个快捷方式，可将单个 `Style` 对象应用到数据透视表的每个单元格，覆盖通过上述任一样式名称 API 设置的内容。当需要与底层主题无关的统一外观时，这一方法非常有用。

## **应用旧版 XLS 预设自动格式**
`PivotTable.AutoFormatType` 接受来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举的值。可用值包括 `Report1` 至 `Report10`、`Classic` 以及 `Table1` 至 `Table10`。
下面的示例加载一个新的工作簿，填入 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.Report5`，并将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为什么没有列字段？** Report 系列自动格式（`Report1` 至 `Report10`、`Table1` 至 `Table10`）是经典 Excel 中为**单维度数据透视表**设计的，仅包含行字段和值字段——它们没有为列字段标题提供内置样式。如果你的数据透视表需要列字段，请改用 [方案 2](#apply-a-modern-named-preset-pivot-table-style) 中的现代 `PivotTableStyleType` 预设样式，这些样式是为现代 Excel 的二维布局设计的。
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 场景 1：应用旧版 XLS 预设自动格式
// 使用的 API：PivotTable.AutoFormatType
// 目标文件格式：.xls（旧版）
// 有关完整示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET
// 创建一个新工作簿
Workbook workbook = new Workbook();
// 获取第一个工作表
Worksheet sheet = workbook.Worksheets[0];
// 用标题行（Fruit、Year、Amount）填充源数据
// 以及涵盖 2020 和 2021 年葡萄、蓝莓、猕猴桃、樱桃的 9 行数据
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
// 在目标单元格 E3 处添加一个名为 "Pivot1" 的数据透视表，使用源区域 A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];
// 分配字段：Fruit -> 行，Amount -> 数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// 应用旧版 XLS 预设自动格式 "Report5"
// 注意：此属性仅在保存为 .xls 文件时才有意义。
// 当保存为 .xlsx/.xlsm/.xlsb 格式时，Excel 会忽略 AutoFormatType
// 并使用 PivotTableStyleType / PivotTableStyleName 所指定的样式。
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// 以旧版 .xls 格式保存工作簿
workbook.Save("output.xls");
```

## **应用现代命名预设数据透视表样式**

## **定义并应用自定义数据透视表样式**
无法修改内置预设样式。当需要覆盖颜色、边框或字体时，必须定义自定义数据透视表样式。整个流程包含三个步骤：
1. 通过 `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` 将自定义样式添加到工作簿的 `TableStyles` 集合中。该方法返回新创建样式的索引。
2. 通过 `TableStyle.TableStyleElements.Add(TableStyleElementType)` 添加样式元素（如 `WholeTable` 或 `GrandTotalRow`），然后通过 `TableStyleElement.SetElementStyle(Style)` 为每个元素分配 `Style`。
3. 将 `PivotTable.PivotTableStyleName` 设置为该样式的名称，从而将自定义样式应用到数据透视表。此处不要使用 `PivotTableStyleType`，因为该属性用于选择内置预设样式。

{{% alert color="primary" %}}
`PivotTableStyleName` 和 `PivotTableStyleType` 不可互换。内置预设样式请使用 `PivotTableStyleType`，而通过 `AddPivotTableStyle` 定义的自定义样式请使用 `PivotTableStyleName`。同时设置两者不会出错，但只有与预期来源匹配的那一个会呈现。
{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。
下面的示例定义了一个自定义数据透视表样式，对 `WholeTable` 应用细黑色边框，对 `GrandTotalRow` 应用粗体红色字体，然后通过 `PivotTableStyleName` 应用该样式并保存为 `.xlsx`。

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
// 步骤 1：注册一个新的自定义数据透视表样式并获取其索引
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];
// 步骤 2：添加一个 WholeTable 元素，并在四边应用细的黑色边框
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
// 步骤 3：添加一个 GrandTotalRow 元素，并应用粗体红色字体
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);
// 步骤 4：通过名称应用自定义样式（不是通过 PivotTableStyleType，因为它用于内置预设）
pivotTable.PivotTableStyleName = "CustomPivotStyle";
workbook.Save("output.xlsx");
```

## **使用 FormatAll 将同一样式应用到数据透视表的每个单元格**
`PivotTable.FormatAll(Style)` 是一个快捷方式，可将单个 `Style` 对象应用到数据透视表的每个单元格，包括数据区域、行和列标题以及总计。无论之前通过 `PivotTableStyleType` 或 `PivotTableStyleName` 设置的内容，都将被覆盖。

{{% alert color="primary" %}}
`FormatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅当需要在整个数据透视表上获得与主题无关的统一外观时才使用它。
{{% /alert %}}

下面的示例创建了一个 `Style`，具有黄色实心填充、粗体深蓝色字体以及四周的细黑色边框，然后使用 `FormatAll` 应用该样式，并保存为 `.xlsx`。

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 场景 4：使用 FormatAll API 将单个 Style 应用于数据透视表的每个单元格
// 使用的 API：PivotTable.FormatAll(Style)
// 目标格式：.xlsx
// GitHub 参考：参见 Aspose.Cells-for-.NET 仓库 — 数据透视表样式示例
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// 填充源数据：标题行（第 1 行）+ 9 行数据（第 2-10 行）
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
// 构建一个将被强制应用于数据透视表每个单元格的 Style
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
// 应用 FormatAll：强制将此单个样式应用于数据透视表的每个单元格，
// 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.FormatAll(style);
// 以现代 .xlsx 格式保存工作簿
workbook.Save("output.xlsx");
```

## **应该使用哪种样式 API？**
样式 API 的选择取决于要保存到的文件格式。可参考下表快速查阅。
| 目标文件格式 | 使用的 API | 备注 |
|---|---|---|
| `.xls`（旧版） | `PivotTable.AutoFormatType` | 取值来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType`（例如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。保存为现代格式时会被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `PivotTable.PivotTableStyleType` | 取值来自 `Aspose.Cells.PivotTableStyleType`（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 在内置预设样式不够时使用。通过 `TableStyleElement.SetElementStyle(...)` 进行配置。 |
| 任意格式（统一覆盖） | `PivotTable.FormatAll(Style)` | 快捷方式，会覆盖整个数据透视表上的所有其他样式设置。 |
如有疑问，请保存为 `.xlsx`，内置主题使用 `PivotTableStyleType`，自定义主题使用 `PivotTableStyleName`。

## 相关文章
- [Add Pivot Table Row and Column Fields in Aspose.Cells for .NET](/cells/zh/net/pivot-table-add-row-and-column-fields/)
- [Manage Pivot Table Value Fields in Aspose.Cells for .NET](/cells/zh/net/manage-value-fields/)
- [Refreshing Pivot Tables in Aspose.Cells for .NET](/cells/zh/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}