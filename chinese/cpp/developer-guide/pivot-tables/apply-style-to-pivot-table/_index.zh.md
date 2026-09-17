---
title: 在 Aspose.Cells for C++ 中为数据透视表应用样式
linktitle: 在 Aspose.Cells for C++ 中为数据透视表应用样式
description: 学习如何在 Aspose.Cells for C++ 中为数据透视表应用内置和自定义样式，涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方法。
keywords: Aspose.Cells C++ 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持同时应用旧版数据透视表自动格式（针对 `.xls` 文件）和现代命名或自定义数据透视表样式（针对 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。应调用的 API 取决于工作簿保存为何种文件格式，而不是加载时的格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供了两套并行的样式 API。它们之间的选择取决于工作簿保存为何种文件格式，而不是读取时的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，这种情况下应使用现代样式 API，而不是旧版 API。
- `PivotTable.PivotTableStyleType` 用于选择内置命名样式之一（浅色和深色主题，包括 Excel 2017 中新增的样式）。这些预设是只读的。
- `PivotTable.PivotTableStyleName` 用于选择通过 `Worksheets.TableStyles.AddPivotTableStyle(...)` 自定义定义的样式。当需要修改预设之外的颜色、边框或字体时，必须使用自定义样式。
此外，`PivotTable.FormatAll(Style)` 是一个快捷方法，可以将单个 `Style` 对象应用到数据透视表的每个单元格，覆盖通过上述任一样式名称 API 设置的内容。当需要统一外观而不受基础主题影响时，这非常有用。

## **应用旧版 XLS 预设自动格式**
`PivotTable.AutoFormatType` 接受来自 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举的值。可用值包括 `Report1` 至 `Report10`、`Classic` 以及 `Table1` 至 `Table10`。
以下示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.Report5`，然后将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为什么没有列字段？** Report 系列自动格式（`Report1` 至 `Report10`、`Table1` 至 `Table10`）是为经典 Excel 中只有行字段和值的**单维数据透视表**设计的，它们没有为列字段标题提供内置样式。如果数据透视表需要列字段，请改用 [方案二](#apply-a-modern-named-preset-pivot-table-style) 中的现代 `PivotTableStyleType` 预设，它们是为现代 Excel 使用的二维布局设计的。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 创建新的工作簿
    Workbook workbook;
    // 获取第一个工作表
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // 使用表头行（Fruit、Year、Amount）填充源数据
    // 包含 9 行数据，覆盖 2020 年和 2021 年的葡萄、蓝莓、猕猴桃和樱桃
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");
    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);
    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);
    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);
    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);
    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);
    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);
    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);
    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);
    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);
    // 在目标单元格 E3 处添加名为“Pivot1”的数据透视表，使用源区域 A1:C10
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);
    // 分配字段：Fruit -> 行，Amount -> 数据
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // 应用旧版 XLS 预设自动格式“Report5”
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);
    // 以旧版 .xls 格式保存工作簿
    workbook.Save(u"output.xls");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **应用现代命名预设数据透视表样式**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);
    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);
    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);
    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);
    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);
    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **定义并应用自定义数据透视表样式**
内置预设无法修改。每当需要覆盖颜色、边框或字体时，必须定义自定义数据透视样式。该工作流分为三个步骤：
1. 通过 `Worksheets.TableStyles.AddPivotTableStyle(string name)` 向工作簿的 `TableStyles` 集合添加自定义样式。这将返回新创建样式的索引。
2. 通过 `TableStyle.TableStyleElements.Add(TableStyleElementType)` 添加元素（例如 `WholeTable` 或 `GrandTotalRow`），然后通过 `TableStyleElement.SetElementStyle(Style)` 为每个元素分配 `Style`。
3. 通过将 `PivotTable.PivotTableStyleName` 设置为样式的名称，将自定义样式应用于数据透视表。此处不要使用 `PivotTableStyleType`，因为该属性选择的是内置预设。

{{% alert color="primary" %}}
`PivotTableStyleName` 和 `PivotTableStyleType` 不能互换使用。内置预设使用 `PivotTableStyleType`，而通过 `AddPivotTableStyle` 定义的自定义样式使用 `PivotTableStyleName`。同时设置两者不会有问题，但只会渲染与预期来源匹配的那一个。
{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。
以下示例定义一个自定义数据透视样式，在 `WholeTable` 上使用细黑色边框，在 `GrandTotalRow` 上使用粗体红色字体，然后通过 `PivotTableStyleName` 应用该样式，并保存为 `.xlsx`。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // 填充源数据：表头行 + 9 行数据（A1:C10）
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);
    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);
    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);
    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);
    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);
    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);
    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);
    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);
    // 添加数据源为 A1:C10 的数据透视表，定位在 E3，名称为 "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // 步骤 1：注册一个新的自定义数据透视表样式并获取其索引
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);
    // 步骤 2：添加 WholeTable 元素，并在四边应用黑色细边框
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);
    // 步骤 3：添加 GrandTotalRow 元素，并应用粗体红色字体
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);
    // 步骤 4：通过名称应用自定义样式（不要使用 PivotTableStyleType，它用于内置预设）
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **使用 FormatAll 将一种样式应用于每个数据透视表单元格**
`PivotTable.FormatAll(Style)` 是一个快捷方法，可将单个 `Style` 对象应用到数据透视表的每个单元格，包括数据区域、行标题和列标题以及汇总。以前通过 `PivotTableStyleType` 或 `PivotTableStyleName` 设置的内容将被覆盖。

{{% alert color="primary" %}}
`FormatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅在整个数据透视表需要统一、与主题无关的外观时才使用它。
{{% /alert %}}

以下示例创建一个 `Style`，使用黄色实心填充、粗体深蓝色字体和四边细黑色边框，然后使用 `FormatAll` 应用，并将结果保存为 `.xlsx`。

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // 表头行
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // 数据行
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);
    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);
    // 添加数据透视表:源区域 A1:C10,目标单元格 E3,名称 "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // 分配数据透视表字段
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // 构建一个样式,将其强制应用到数据透视表的每个单元格
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    // 应用 FormatAll
    pivotTable.FormatAll(style);
    // 保存工作簿
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **应该使用哪种样式 API？**
样式 API 的选择取决于要保存的文件格式。请参考下表。
| 目标文件格式 | 使用的 API | 说明 |
|---|---|---|
| `.xls`（旧版） | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` 中的值（例如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。保存为现代格式时会被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代内置样式） | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` 中的值（浅色/深色主题，包括 Excel 2017 中新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代自定义样式） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | 在内置预设不够时使用。通过 `TableStyleElement.SetElementStyle(...)` 进行配置。 |
| 任何格式（统一覆盖） | `PivotTable.FormatAll(Style)` | 覆盖整个数据透视表所有其他样式设置的快捷方法。 |
如有疑问，请保存为 `.xlsx`，对内置主题使用 `PivotTableStyleType`，对自定义主题使用 `PivotTableStyleName`。

{{< app/cells/assistant language="cpp" >}}