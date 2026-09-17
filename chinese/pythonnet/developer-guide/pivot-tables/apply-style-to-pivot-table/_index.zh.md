---
title: 在 Aspose.Cells for Python via .NET 中为数据透视表应用样式
linktitle: 在 Aspose.Cells for Python via .NET 中为数据透视表应用样式
description: 了解如何在 Aspose.Cells for Python via .NET 中为数据透视表应用内置和自定义样式，涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells Python via .NET 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 同时支持应用旧版的数据透视自动格式（适用于 `.xls` 文件）和现代的命名或自定义数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。应调用的 API 取决于工作簿保存为的文件格式，而不是加载时的格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供了两套并行的样式 API。它们之间的选择取决于工作簿保存为的文件格式，而不是读取时的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，在这种情况下应使用现代样式 API，而不是旧版样式 API。
- `PivotTable.pivot_table_style_type` 用于选择内置命名样式之一（浅色和深色主题，包括 Excel 2017 中新增的样式）。这些预设样式为只读。
- `PivotTable.pivot_table_style_name` 用于选择您通过 `workbook.worksheets.table_styles.add_pivot_table_style(...)` 自定义定义的样式。当您希望修改预设样式之外的颜色、边框或字体时，必须使用自定义样式。
此外，`PivotTable.format_all(Style)` 是一个快捷方式，它将单个 `Style` 对象应用于数据透视表的每个单元格，覆盖通过上述任一样式名称 API 设置的所有内容。当需要统一外观而不受基础主题影响时，此方法非常有用。

## **应用旧版 XLS 预设自动格式**
`PivotTable.auto_format_type` 接受 `aspose.cells.pivot.PivotTableAutoFormatType` 枚举中的一个值。可用值包括 `REPORT_1` 至 `REPORT_10`、`CLASSIC`，以及 `TABLE_1` 至 `TABLE_10`。
以下示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.REPORT_5`，并将结果保存为 `.xls` 文件。

{{% alert color="primary" %}}
**为什么没有列字段？** Report 系列自动格式（`Report1` 至 `Report10`、`Table1` 至 `Table10`）是经典 Excel 中为仅含行字段和值的**单维度**数据透视表设计的——它们没有为列字段标题提供内置样式。如果您的数据透视表需要列字段，请改用[场景 2](#apply-a-modern-named-preset-pivot-table-style)中的现代 `PivotTableStyleType` 预设样式，这些样式专为现代 Excel 使用的二维布局而设计。
{{% /alert %}}

```python
import aspose.cells as ac
# 场景 1：应用传统的 XLS 预设自动格式
# 使用的 API：PivotTable.AutoFormatType
# 目标文件格式：.xls（传统格式）
# 如需完整的示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET
# 创建一个新工作簿
workbook = ac.Workbook()
# 获取第一个工作表
sheet = workbook.worksheets[0]
# 使用标题行（Fruit、Year、Amount）填充源数据
# 以及覆盖 2020 和 2021 年葡萄、蓝莓、猕猴桃、樱桃的 9 行数据
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")
sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)
sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)
sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)
sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)
sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)
sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)
sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)
sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)
sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)
# 在目标单元格 E3 处添加一个名为 "Pivot1" 的数据透视表，使用源范围 A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]
# 分配字段：Fruit -> 行，Amount -> 数据
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# 应用传统的 XLS 预设自动格式 "Report5"
# 注意：此属性仅在保存为 .xls 格式时有效。
# 当保存为 .xlsx/.xlsm/.xlsb 格式时，Excel 会忽略 AutoFormatType
# 并使用 PivotTableStyleType / PivotTableStyleName 所指定的样式。
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5
# 以传统的 .xls 格式保存工作簿
workbook.save("output.xls")
```

## **应用现代命名预设数据透视表样式**

## **定义并应用自定义数据透视表样式**
内置预设样式无法修改。每当您需要覆盖颜色、边框或字体时，都必须定义自定义数据透视样式。该工作流包含三个步骤：
1. 通过 `workbook.worksheets.table_styles.add_pivot_table_style(name)` 向工作簿的 `table_styles` 集合添加自定义样式。这将返回新创建样式的索引。
2. 通过 `table_style.table_style_elements.add(TableStyleElementType)` 添加元素（例如 `WHOLE_TABLE` 或 `GRAND_TOTAL_ROW`）来配置样式，然后通过 `table_style_element.set_element_style(Style)` 为每个元素分配一个 `Style`。
3. 将 `PivotTable.pivot_table_style_name` 设置为该样式的名称，将自定义样式应用于数据透视表。此处不要使用 `pivot_table_style_type`，因为该属性用于选择内置预设样式。

{{% alert color="primary" %}}
`pivot_table_style_name` 和 `pivot_table_style_type` 不能互换使用。对于内置预设样式使用 `pivot_table_style_type`，对于通过 `add_pivot_table_style` 定义的自定义样式使用 `pivot_table_style_name`。同时设置两者不会产生错误，但只有与预期来源匹配的那个会被渲染。
{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS` 和 `PAGE_FIELD_VALUES`。
以下示例定义一个自定义数据透视样式，在 `WHOLE_TABLE` 上使用细黑色边框，在 `GRAND_TOTAL_ROW` 上使用粗体红色字体，然后通过 `pivot_table_style_name` 应用它并保存为 `.xlsx` 文件。

```python
import aspose.cells as ac
import System.Drawing
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# 填充源数据：标题行 + 9 行数据 (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)
worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)
# 添加数据源为 A1:C10 的数据透视表，锚定在 E3，命名为 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# 步骤 1：注册一个新的自定义数据透视表样式并获取其索引
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]
# 步骤 2：添加 WholeTable 元素并在四边应用细黑色边框
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)
# 步骤 3：添加 GrandTotalRow 元素并应用粗体红色字体
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)
# 步骤 4：按名称应用自定义样式（不要使用 PivotTableStyleType，它用于内置预设样式）
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **使用 FormatAll 将同一样式应用于数据透视表的每个单元格**
`PivotTable.format_all(Style)` 是一个快捷方式，它将单个 `Style` 对象应用于数据透视表的每个单元格，包括数据区域、行和列标题以及总计。通过 `pivot_table_style_type` 或 `pivot_table_style_name` 先前设置的所有内容都将被覆盖。

{{% alert color="primary" %}}
`format_all` 会覆盖 `pivot_table_style_type` 和 `pivot_table_style_name`。仅当需要跨整个数据透视表应用统一且独立于主题的外观时才使用它。
{{% /alert %}}

以下示例创建一个 `Style`，使用黄色纯色填充、深蓝色粗体字体以及四边的细黑色边框，然后使用 `format_all` 应用它并保存为 `.xlsx` 文件。

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# 场景 4：使用 FormatAll 将单个 Style 应用于数据透视表的每个单元格
# 使用的 API：PivotTable.FormatAll(Style)
# 目标格式：.xlsx
# GitHub 参考：参见 Aspose.Cells-for-.NET 仓库 — 数据透视表样式设置示例
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# 填充源数据：表头行（第 1 行）+ 9 行数据（第 2-10 行）
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)
worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)
# 添加数据透视表：源区域 A1:C10，目标单元格 E3，名称 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# 分配数据透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# 创建一个将强制应用于数据透视表每个单元格的样式
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black
# 应用 FormatAll：将此单个样式强制应用到数据透视表的每个单元格，
# 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivot_table.format_all(style)
# 以现代 .xlsx 格式保存工作簿
workbook.save("output.xlsx")
```

## **我应该使用哪个样式 API？**
样式 API 的选择取决于您要保存为的目标文件格式。请参考下表以快速查阅。
| 目标文件格式 | 使用的 API | 备注 |
|---|---|---|
| `.xls`（旧版） | `PivotTable.auto_format_type` | 值来自 `aspose.cells.pivot.PivotTableAutoFormatType`（例如 `REPORT_1`–`REPORT_10`、`CLASSIC`、`TABLE_1`–`TABLE_10`）。保存为现代格式时将被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `PivotTable.pivot_table_style_type` | 值来自 `aspose.cells.PivotTableStyleType`（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | 当内置预设样式不够用时使用。通过 `table_style_element.set_element_style(...)` 进行配置。 |
| 任何格式（统一覆盖） | `PivotTable.format_all(Style)` | 覆盖整个数据透视表所有其他样式设置的快捷方式。 |
如有疑问，请保存为 `.xlsx` 并对内置主题使用 `pivot_table_style_type`，或对自定义主题使用 `pivot_table_style_name`。

{{< app/cells/assistant language="python-net" >}}