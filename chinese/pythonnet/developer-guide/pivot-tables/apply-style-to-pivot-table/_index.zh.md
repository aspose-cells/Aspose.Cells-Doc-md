---
title: 为透视表应用样式
linktitle: 为透视表应用样式
description: 了解如何在 Aspose.Cells for Python via .NET 中为透视表应用内置和自定义样式,涵盖传统 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells Python via .NET pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持同时应用传统透视表自动格式(适用于 `.xls` 文件)和现代命名或自定义透视表样式(适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件)。您应调用的 API 取决于工作簿保存到的文件格式,而非读取时的格式。

{{% /alert %}}

## **简介**

Aspose.Cells 为透视表提供了两套并行的样式 API。它们之间的选择由工作簿保存到的文件格式决定,而非读取时的格式决定。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`,在这种情况下,应使用现代样式 API,而不是传统 API。

对于传统 `.xls` 输出,请使用 `PivotTable.auto_format_type` 属性以及 `aspose.cells.pivot.PivotTableAutoFormatType` 枚举。此 API 对应于经典 Excel 中为透视表提供的自动格式选择器。

对于现代 `.xlsx`、`.xlsm` 和 `.xlsb` 输出,有两种风格的样式 API 可用:

- `PivotTable.pivot_table_style_type` 用于选择内置命名样式之一(浅色和深色主题,包括 Excel 2017 中新增的样式)。这些预设样式为只读。
- `PivotTable.pivot_table_style_name` 用于选择您通过 `workbook.worksheets.table_styles.add_pivot_table_style(...)` 自行定义的自定义样式。当您希望修改预设样式之外的颜色、边框或字体时,必须使用自定义样式。

此外,`PivotTable.format_all(Style)` 是一个快捷方式,它将单个 `Style` 对象应用于透视表的每个单元格,覆盖通过上述任一样式名称 API 所设置的内容。当无论底层主题如何都需要统一外观时,这非常有用。

## **应用传统 XLS 预设自动格式**

`PivotTable.auto_format_type` 接受来自 `aspose.cells.pivot.PivotTableAutoFormatType` 枚举的值。可用值为 `REPORT_1` 到 `REPORT_10`、`CLASSIC` 以及 `TABLE_1` 到 `TABLE_10`。

{{% alert color="primary" %}}

`auto_format_type` 仅在工作簿保存为 `.xls` 时才会生效。当同一工作簿保存为 `.xlsx`、`.xlsm` 或 `.xlsb` 时,Excel 会忽略此属性,并回退到 `pivot_table_style_type` 和 `pivot_table_style_name` 设置。

{{% /alert %}}

以下示例加载一个新工作簿,填充 Fruit/Year/Amount 示例数据,添加一个透视表,应用 `PivotTableAutoFormatType.REPORT_5`,并将结果保存为 `.xls`。

```python
import aspose.cells as ac

# 场景 1：应用旧版 XLS 预设自动格式
# 使用的 API：PivotTable.AutoFormatType
# 目标文件格式：.xls（旧版）
# 有关完整的示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET

# 创建一个新的工作簿
workbook = ac.Workbook()

# 获取第一个工作表
sheet = workbook.worksheets[0]

# 使用标题行（Fruit、Year、Amount）填充源数据
# 以及 9 行数据行，涵盖 2020 年和 2021 年的葡萄、蓝莓、猕猴桃和樱桃
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

# 在目标单元格 E3 处添加一个数据透视表，命名为 "Pivot1"，使用源范围 A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# 分配字段：Fruit -> 行，Year -> 列，Amount -> 数据
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 应用旧版 XLS 预设自动格式 "Report5"
# 注意：此属性仅在保存为 .xls 时才有意义。
# 当保存为 .xlsx/.xlsm/.xlsb 时，Excel 会忽略 AutoFormatType
# 并使用 PivotTableStyleType / PivotTableStyleName 指定的内容。
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# 以旧版 .xls 格式保存工作簿
workbook.save("output.xls")
```

## **应用现代命名预设透视表样式**

`PivotTable.pivot_table_style_type` 接受来自 `aspose.cells.PivotTableStyleType` 枚举的值。该枚举涵盖浅色主题 `PIVOT_TABLE_STYLE_LIGHT_1` 到 `PIVOT_TABLE_STYLE_LIGHT_28` 以及深色主题 `PIVOT_TABLE_STYLE_DARK_1` 到 `PIVOT_TABLE_STYLE_DARK_28`。Excel 2017 中新增的样式(第二批浅色和深色主题)也可通过同一枚举访问。

对于任何现代文件格式,这是推荐的 API。与传统自动格式不同,此处选择的样式可被 Excel 忠实地呈现,并在通过其他 Office 工具往返保存时得以保留。

以下示例使用相同的 Fruit/Year/Amount 数据,创建相同的透视表,应用 `PIVOT_TABLE_STYLE_DARK_1`,并将工作簿保存为 `.xlsx`。

```python
import aspose.cells as ac

# 场景 2: 使用 PivotTableStyleType 应用现代 Excel 2007+ 命名预设样式。
# 目标文件格式: .xlsx。PivotTableStyleType 枚举位于 Aspose.Cells 命名空间中
# (不在 Aspose.Cells.Pivot 中) — 这就是为什么我们不需要任何额外的 using 声明。
# GitHub 参考: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 表头行: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 行 Fruit / Year / Amount 数据
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# 在 E3 位置添加一个名为 "Pivot1" 的数据透视表,数据源为 A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# 分配透视字段: Fruit -> 行区域, Year -> 列区域, Amount -> 数据区域
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# 应用现代 Excel 2007+ 命名预设透视样式。
# PivotTableStyleType 是适用于 .xlsx / .xlsm / .xlsb 文件的正确 API; AutoFormatType
# 在这些格式中会被 Excel 忽略。PivotTableStyleDark1 属于深色主题系列
# (PivotTableStyleDark1..PivotTableStyleDark28),同一枚举还公开了
# 较新的 Excel 2017 浅色/深色主题 (PivotTableStyleLight1..Light28 / Dark1..Dark28)。
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# 保存为现代 .xlsx 格式 — 这是 PivotTableStyleType 有效的格式。
workbook.save("output.xlsx")
```

## **定义并应用自定义透视表样式**

无法修改内置预设样式。每当您需要覆盖颜色、边框或字体时,都必须定义自定义透视表样式。该工作流包含三个步骤:

1. 通过 `workbook.worksheets.table_styles.add_pivot_table_style(name)` 将自定义样式添加到工作簿的 `table_styles` 集合中。这将返回新创建样式的索引。
2. 通过 `table_style.table_style_elements.add(TableStyleElementType)` 添加元素(例如 `WHOLE_TABLE` 或 `GRAND_TOTAL_ROW`)来配置样式,然后通过 `table_style_element.set_element_style(Style)` 为每个元素分配一个 `Style`。
3. 通过将 `PivotTable.pivot_table_style_name` 设置为该样式的名称,将自定义样式应用于透视表。此处不要使用 `pivot_table_style_type`,因为该属性用于选择内置预设样式。

{{% alert color="primary" %}}

`pivot_table_style_name` 和 `pivot_table_style_type` 不可互换。对于内置预设样式,请使用 `pivot_table_style_type`;对于通过 `add_pivot_table_style` 定义的自定义样式,请使用 `pivot_table_style_name`。同时设置两者不会出错,但仅会呈现与预期来源匹配的那一个。

{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS` 和 `PAGE_FIELD_VALUES`。

以下示例定义了一个自定义透视表样式,为 `WHOLE_TABLE` 设置细黑色边框,为 `GRAND_TOTAL_ROW` 设置粗体红色字体,然后通过 `pivot_table_style_name` 应用它,并保存为 `.xlsx`。

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 填充源数据：表头行 + 9 行数据 (A1:C10)
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

# 步骤 2：添加 WholeTable 元素，并在四边应用细黑色边框
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

# 步骤 3：添加 GrandTotalRow 元素，并应用粗体红色字体
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# 步骤 4：通过名称应用自定义样式（不要使用 PivotTableStyleType，它是用于内置预设样式的）
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **使用 FormatAll 将一种样式应用于每个透视表单元格**

`PivotTable.format_all(Style)` 是一个快捷方式,它将单个 `Style` 对象应用于透视表的每个单元格,包括数据区域、行和列标题以及总计。之前通过 `pivot_table_style_type` 或 `pivot_table_style_name` 设置的所有内容都会被覆盖。

{{% alert color="primary" %}}

`format_all` 会覆盖 `pivot_table_style_type` 和 `pivot_table_style_name`。仅当需要跨整个透视表获得与主题无关的统一外观时才使用它。

{{% /alert %}}

以下示例创建一个具有黄色实心填充、粗体深蓝色字体以及四边细黑色边框的 `Style`,然后使用 `format_all` 应用它,并保存为 `.xlsx`。

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# 场景 4：使用 FormatAll 将单个样式应用于每个数据透视表单元格
# 使用的 API：PivotTable.FormatAll(Style)
# 目标格式：.xlsx
# GitHub 参考：参见 Aspose.Cells-for-.NET 仓库 — 数据透视表样式示例

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

# 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# 构建一个将强制应用于数据透视表每个单元格的样式
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

# 应用 FormatAll：将此单个样式强制应用于数据透视表的每个单元格，
# 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivot_table.format_all(style)

# 以现代 .xlsx 格式保存工作簿
workbook.save("output.xlsx")
```

## **应该使用哪种样式 API?**

样式 API 的选择取决于您要保存到的文件格式。请使用下表作为快速参考。

| 目标文件格式 | 使用的 API | 备注 |
|---|---|---|
| `.xls`(传统格式) | `PivotTable.auto_format_type` | 取自 `aspose.cells.pivot.PivotTableAutoFormatType` 的值(例如 `REPORT_1`–`REPORT_10`、`CLASSIC`、`TABLE_1`–`TABLE_10`)。保存为现代格式时会被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`(现代格式,内置样式) | `PivotTable.pivot_table_style_type` | 取自 `aspose.cells.PivotTableStyleType` 的值(浅色/深色主题,包括 Excel 2017 中新增的样式)。 |
| `.xlsx` / `.xlsm` / `.xlsb`(现代格式,自定义样式) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | 当内置预设样式不够用时使用。通过 `table_style_element.set_element_style(...)` 进行配置。 |
| 任何格式(统一覆盖) | `PivotTable.format_all(Style)` | 快捷方式,覆盖整个透视表的所有其他样式设置。 |

如有疑问,请保存为 `.xlsx`,并对内置主题使用 `pivot_table_style_type`,对自定义主题使用 `pivot_table_style_name`。

{{< app/cells/assistant language="python" >}}